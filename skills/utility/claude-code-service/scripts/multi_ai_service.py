#!/usr/bin/env python3
"""
Multi-AI Service - Claude Code with Gemini and OpenAI CLI integration

Unified service that can route requests to Claude, Gemini, or OpenAI
based on configuration, load balancing, or user preference.
"""
import os
import sys
import json
import subprocess
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from enum import Enum
from typing import Optional, Dict, Any
import anthropic
import logging

app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AIProvider(Enum):
    CLAUDE = "claude"
    GEMINI = "gemini"
    OPENAI = "openai"

class MultiAIService:
    """
    Unified AI service supporting multiple providers
    """
    def __init__(self):
        # API keys from environment
        self.claude_key = os.getenv('ANTHROPIC_API_KEY')
        self.openai_key = os.getenv('OPENAI_API_KEY')
        self.gemini_key = os.getenv('GOOGLE_API_KEY')
        
        # Initialize clients
        self.claude_client = None
        if self.claude_key:
            self.claude_client = anthropic.Anthropic(api_key=self.claude_key)
        
        # Check CLI availability
        self.cli_available = {
            AIProvider.GEMINI: self._check_gemini_cli(),
            AIProvider.OPENAI: self._check_openai_cli()
        }
        
        logger.info(f"Claude API: {'✓' if self.claude_client else '✗'}")
        logger.info(f"Gemini CLI: {'✓' if self.cli_available[AIProvider.GEMINI] else '✗'}")
        logger.info(f"OpenAI CLI: {'✓' if self.cli_available[AIProvider.OPENAI] else '✗'}")
    
    def _check_gemini_cli(self) -> bool:
        """Check if Gemini CLI is available"""
        try:
            result = subprocess.run(
                ['gemini', '--version'],
                capture_output=True,
                timeout=5
            )
            return result.returncode == 0
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return False
    
    def _check_openai_cli(self) -> bool:
        """Check if OpenAI CLI is available"""
        try:
            result = subprocess.run(
                ['openai', '--version'],
                capture_output=True,
                timeout=5
            )
            return result.returncode == 0
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return False
    
    def chat_claude(self, message: str, context: Optional[str] = None) -> Dict[str, Any]:
        """Chat with Claude API"""
        if not self.claude_client:
            return {
                'error': 'Claude API not configured',
                'message': 'Set ANTHROPIC_API_KEY environment variable'
            }
        
        try:
            messages = []
            if context:
                messages.append({
                    "role": "user",
                    "content": context
                })
            
            messages.append({
                "role": "user",
                "content": message
            })
            
            response = self.claude_client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=4096,
                messages=messages
            )
            
            return {
                'provider': 'claude',
                'response': response.content[0].text,
                'model': 'claude-sonnet-4',
                'tokens': {
                    'input': response.usage.input_tokens,
                    'output': response.usage.output_tokens
                }
            }
        
        except Exception as e:
            logger.error(f"Claude API error: {e}")
            return {'error': str(e)}
    
    def chat_gemini(self, message: str, context: Optional[str] = None) -> Dict[str, Any]:
        """Chat with Gemini CLI"""
        if not self.cli_available[AIProvider.GEMINI]:
            return {
                'error': 'Gemini CLI not available',
                'message': 'Install with: pip install google-generativeai && gemini setup'
            }
        
        try:
            # Prepare prompt
            prompt = message
            if context:
                prompt = f"{context}\n\n{message}"
            
            # Call Gemini CLI
            result = subprocess.run(
                ['gemini', 'chat', prompt],
                capture_output=True,
                text=True,
                timeout=30,
                env={**os.environ, 'GOOGLE_API_KEY': self.gemini_key}
            )
            
            if result.returncode != 0:
                return {'error': result.stderr}
            
            return {
                'provider': 'gemini',
                'response': result.stdout.strip(),
                'model': 'gemini-pro'
            }
        
        except subprocess.TimeoutExpired:
            return {'error': 'Gemini request timed out'}
        except Exception as e:
            logger.error(f"Gemini CLI error: {e}")
            return {'error': str(e)}
    
    def chat_openai(self, message: str, context: Optional[str] = None) -> Dict[str, Any]:
        """Chat with OpenAI CLI"""
        if not self.cli_available[AIProvider.OPENAI]:
            return {
                'error': 'OpenAI CLI not available',
                'message': 'Install with: pip install openai && openai api key set'
            }
        
        try:
            # Prepare messages
            messages = []
            if context:
                messages.append({'role': 'system', 'content': context})
            messages.append({'role': 'user', 'content': message})
            
            messages_json = json.dumps(messages)
            
            # Call OpenAI CLI
            result = subprocess.run(
                ['openai', 'api', 'chat.completions.create', 
                 '-m', 'gpt-4', 
                 '--messages', messages_json],
                capture_output=True,
                text=True,
                timeout=30,
                env={**os.environ, 'OPENAI_API_KEY': self.openai_key}
            )
            
            if result.returncode != 0:
                return {'error': result.stderr}
            
            # Parse response
            response_data = json.loads(result.stdout)
            
            return {
                'provider': 'openai',
                'response': response_data['choices'][0]['message']['content'],
                'model': response_data['model'],
                'tokens': {
                    'input': response_data['usage']['prompt_tokens'],
                    'output': response_data['usage']['completion_tokens']
                }
            }
        
        except subprocess.TimeoutExpired:
            return {'error': 'OpenAI request timed out'}
        except json.JSONDecodeError as e:
            return {'error': f'Failed to parse OpenAI response: {e}'}
        except Exception as e:
            logger.error(f"OpenAI CLI error: {e}")
            return {'error': str(e)}
    
    def chat(self, message: str, provider: str = 'claude', context: Optional[str] = None) -> Dict[str, Any]:
        """
        Route chat request to appropriate provider
        
        Args:
            message: User message
            provider: AI provider ('claude', 'gemini', 'openai', 'auto')
            context: Optional context/system message
        """
        # Auto-select provider
        if provider == 'auto':
            if self.claude_client:
                provider = 'claude'
            elif self.cli_available[AIProvider.GEMINI]:
                provider = 'gemini'
            elif self.cli_available[AIProvider.OPENAI]:
                provider = 'openai'
            else:
                return {'error': 'No AI providers available'}
        
        # Route to provider
        if provider == 'claude':
            return self.chat_claude(message, context)
        elif provider == 'gemini':
            return self.chat_gemini(message, context)
        elif provider == 'openai':
            return self.chat_openai(message, context)
        else:
            return {'error': f'Unknown provider: {provider}'}
    
    def get_available_providers(self) -> Dict[str, bool]:
        """Get list of available providers"""
        return {
            'claude': self.claude_client is not None,
            'gemini': self.cli_available[AIProvider.GEMINI],
            'openai': self.cli_available[AIProvider.OPENAI]
        }

# Initialize service
ai_service = MultiAIService()

# Flask routes
@app.route('/')
def index():
    """Main page"""
    available = ai_service.get_available_providers()
    return render_template('index.html', providers=available)

@app.route('/api/chat', methods=['POST'])
def chat():
    """Chat endpoint"""
    data = request.json
    message = data.get('message', '')
    provider = data.get('provider', 'auto')
    context = data.get('context')
    
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    
    result = ai_service.chat(message, provider=provider, context=context)
    
    if 'error' in result:
        return jsonify(result), 500
    
    return jsonify(result)

@app.route('/api/providers')
def providers():
    """Get available providers"""
    return jsonify(ai_service.get_available_providers())

@app.route('/api/status')
def status():
    """Health check"""
    available = ai_service.get_available_providers()
    
    return jsonify({
        'status': 'running',
        'providers': available,
        'healthy': any(available.values())
    })

@app.route('/api/compare', methods=['POST'])
def compare():
    """Compare responses from multiple providers"""
    data = request.json
    message = data.get('message', '')
    providers = data.get('providers', ['claude', 'gemini', 'openai'])
    
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    
    results = {}
    for provider in providers:
        result = ai_service.chat(message, provider=provider)
        results[provider] = result
    
    return jsonify(results)

def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Multi-AI Service with Claude, Gemini, and OpenAI'
    )
    
    parser.add_argument(
        '--port',
        type=int,
        default=8080,
        help='Port to run server on'
    )
    
    parser.add_argument(
        '--host',
        default='0.0.0.0',
        help='Host to bind to'
    )
    
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Run in debug mode'
    )
    
    args = parser.parse_args()
    
    # Check available providers
    available = ai_service.get_available_providers()
    
    print("\n" + "="*60)
    print("Multi-AI Service Starting")
    print("="*60)
    print("\nAvailable Providers:")
    for provider, is_available in available.items():
        status = "✓" if is_available else "✗"
        print(f"  {status} {provider.upper()}")
    
    if not any(available.values()):
        print("\n❌ No AI providers available!")
        print("\nSetup instructions:")
        print("  Claude:  export ANTHROPIC_API_KEY=your-key")
        print("  Gemini:  pip install google-generativeai && gemini setup")
        print("  OpenAI:  pip install openai && openai api key set")
        sys.exit(1)
    
    print(f"\n🚀 Server starting on http://{args.host}:{args.port}")
    print("="*60 + "\n")
    
    app.run(host=args.host, port=args.port, debug=args.debug)

if __name__ == '__main__':
    main()
