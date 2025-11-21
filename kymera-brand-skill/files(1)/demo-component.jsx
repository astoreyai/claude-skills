import React, { useState, useEffect } from 'react';

export default function KymeraBrandDemo() {
  const [activeTab, setActiveTab] = useState('overview');
  const [glowIntensity, setGlowIntensity] = useState(0.3);

  useEffect(() => {
    const interval = setInterval(() => {
      setGlowIntensity(prev => 0.3 + Math.sin(Date.now() / 2000) * 0.1);
    }, 50);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-br from-[#0A0E1A] via-[#121826] to-[#0A0E1A] text-gray-100 font-['Space_Mono',monospace] overflow-hidden">
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Space+Mono:wght@400;700&family=JetBrains+Mono:wght@400;600&display=swap');
        
        .glow-cyan {
          box-shadow: 0 0 20px rgba(0, 217, 255, ${glowIntensity}),
                      0 0 40px rgba(0, 217, 255, ${glowIntensity * 0.6}),
                      inset 0 0 20px rgba(0, 217, 255, ${glowIntensity * 0.3});
        }
        
        .glow-text {
          text-shadow: 0 0 10px rgba(0, 255, 255, 0.8),
                       0 0 20px rgba(0, 217, 255, 0.6);
        }
        
        .scan-line {
          background: linear-gradient(
            180deg,
            transparent 0%,
            rgba(0, 217, 255, 0.03) 50%,
            transparent 100%
          );
          animation: scan 4s linear infinite;
        }
        
        @keyframes scan {
          0% { transform: translateY(-100%); }
          100% { transform: translateY(100vh); }
        }
        
        .grid-overlay {
          background-image: 
            linear-gradient(rgba(0, 217, 255, 0.05) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 217, 255, 0.05) 1px, transparent 1px);
          background-size: 50px 50px;
        }
        
        .stagger-fade-in {
          animation: fadeIn 0.6s cubic-bezier(0.4, 0.0, 0.2, 1) backwards;
        }
        
        @keyframes fadeIn {
          from {
            opacity: 0;
            transform: translateY(20px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
      `}</style>

      {/* Animated scan line */}
      <div className="scan-line fixed inset-0 pointer-events-none w-full h-8 z-50" />
      
      {/* Grid overlay */}
      <div className="grid-overlay fixed inset-0 pointer-events-none opacity-30" />

      {/* Atmospheric glow spots */}
      <div className="fixed top-1/4 left-1/4 w-96 h-96 bg-cyan-500/10 rounded-full blur-3xl pointer-events-none" />
      <div className="fixed bottom-1/3 right-1/4 w-96 h-96 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none" />

      <div className="relative z-10 container mx-auto px-6 py-12">
        {/* Header */}
        <header className="mb-16 stagger-fade-in" style={{ animationDelay: '0.1s' }}>
          <div className="flex items-center gap-4 mb-4">
            <div className="w-2 h-12 bg-cyan-400 glow-cyan" />
            <h1 className="text-5xl font-['Orbitron',sans-serif] font-black tracking-wider text-cyan-400 glow-text uppercase">
              KYMERA SYSTEMS
            </h1>
          </div>
          <p className="text-gray-400 font-['JetBrains_Mono',monospace] text-sm ml-6 tracking-wide">
            // ALGORITHMIC TRADING INTELLIGENCE PLATFORM
          </p>
        </header>

        {/* Navigation Tabs */}
        <nav className="mb-12 stagger-fade-in" style={{ animationDelay: '0.2s' }}>
          <div className="flex gap-2 border-b border-cyan-900/30">
            {['overview', 'metrics', 'systems'].map((tab) => (
              <button
                key={tab}
                onClick={() => setActiveTab(tab)}
                className={`px-6 py-3 font-['JetBrains_Mono',monospace] text-sm uppercase tracking-widest transition-all duration-300
                  ${activeTab === tab 
                    ? 'bg-cyan-500/20 text-cyan-400 border-b-2 border-cyan-400 glow-cyan' 
                    : 'text-gray-500 hover:text-cyan-300 hover:bg-cyan-500/10'
                  }`}
              >
                {tab}
              </button>
            ))}
          </div>
        </nav>

        {/* Content Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Main Panel */}
          <div className="lg:col-span-2 stagger-fade-in" style={{ animationDelay: '0.3s' }}>
            <div className="bg-[#121826]/80 backdrop-blur-sm border border-cyan-900/30 rounded-lg p-8 glow-cyan">
              <h2 className="text-2xl font-['Orbitron',sans-serif] font-bold text-cyan-300 mb-6 tracking-wide">
                SABR20 MOMENTUM ANALYSIS
              </h2>
              
              <div className="space-y-6">
                {/* Timeframe Metrics */}
                {[
                  { timeframe: '15MIN', score: 78.4, trend: 'BULLISH', change: '+12.3%' },
                  { timeframe: '1HOUR', score: 65.2, trend: 'NEUTRAL', change: '+3.7%' },
                  { timeframe: '4HOUR', score: 82.1, trend: 'BULLISH', change: '+18.9%' }
                ].map((metric, idx) => (
                  <div 
                    key={metric.timeframe}
                    className="flex items-center justify-between p-4 bg-[#1A2332]/60 border border-cyan-900/20 rounded"
                    style={{ animationDelay: `${0.4 + idx * 0.1}s` }}
                  >
                    <div className="flex items-center gap-6">
                      <span className="font-['JetBrains_Mono',monospace] text-cyan-400 font-bold text-lg tracking-wider">
                        {metric.timeframe}
                      </span>
                      <div className="h-px w-12 bg-gradient-to-r from-cyan-500/50 to-transparent" />
                      <span className="font-['JetBrains_Mono',monospace] text-3xl font-bold text-white">
                        {metric.score}
                      </span>
                    </div>
                    <div className="flex items-center gap-4">
                      <span className={`font-['JetBrains_Mono',monospace] text-sm font-semibold px-3 py-1 rounded
                        ${metric.trend === 'BULLISH' ? 'bg-emerald-500/20 text-emerald-400' : 'bg-yellow-500/20 text-yellow-400'}`}>
                        {metric.trend}
                      </span>
                      <span className="font-['JetBrains_Mono',monospace] text-emerald-400 font-bold">
                        {metric.change}
                      </span>
                    </div>
                  </div>
                ))}
              </div>

              {/* Visual Indicator */}
              <div className="mt-8 p-4 bg-gradient-to-r from-cyan-950/30 to-transparent border-l-4 border-cyan-400">
                <p className="text-sm font-['JetBrains_Mono',monospace] text-gray-300">
                  <span className="text-cyan-400 font-bold">&gt;&gt;</span> SYSTEM STATUS: All momentum indicators converging on bullish reversal pattern. Multi-timeframe confirmation at 87.3% probability threshold.
                </p>
              </div>
            </div>
          </div>

          {/* Side Panel */}
          <div className="space-y-6">
            {/* System Status */}
            <div className="bg-[#121826]/80 backdrop-blur-sm border border-cyan-900/30 rounded-lg p-6 glow-cyan stagger-fade-in" style={{ animationDelay: '0.4s' }}>
              <h3 className="text-lg font-['Orbitron',sans-serif] font-bold text-cyan-300 mb-4 tracking-wide">
                SYSTEM STATUS
              </h3>
              <div className="space-y-3">
                {[
                  { label: 'MARKET DATA', status: 'ONLINE', value: '99.98%' },
                  { label: 'EXECUTION', status: 'ACTIVE', value: '12ms' },
                  { label: 'RISK ENGINE', status: 'OPTIMAL', value: '1.8x' }
                ].map((item, idx) => (
                  <div key={item.label} className="flex justify-between items-center text-sm">
                    <span className="font-['JetBrains_Mono',monospace] text-gray-400">
                      {item.label}
                    </span>
                    <div className="flex items-center gap-2">
                      <div className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
                      <span className="font-['JetBrains_Mono',monospace] text-emerald-400 font-semibold">
                        {item.value}
                      </span>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Quick Stats */}
            <div className="bg-[#121826]/80 backdrop-blur-sm border border-cyan-900/30 rounded-lg p-6 glow-cyan stagger-fade-in" style={{ animationDelay: '0.5s' }}>
              <h3 className="text-lg font-['Orbitron',sans-serif] font-bold text-cyan-300 mb-4 tracking-wide">
                PERFORMANCE
              </h3>
              <div className="space-y-4">
                <div>
                  <div className="flex justify-between text-sm mb-1">
                    <span className="font-['JetBrains_Mono',monospace] text-gray-400">WIN RATE</span>
                    <span className="font-['JetBrains_Mono',monospace] text-white font-bold">67.3%</span>
                  </div>
                  <div className="h-2 bg-[#1A2332] rounded-full overflow-hidden">
                    <div className="h-full w-[67.3%] bg-gradient-to-r from-emerald-500 to-cyan-400" />
                  </div>
                </div>
                <div>
                  <div className="flex justify-between text-sm mb-1">
                    <span className="font-['JetBrains_Mono',monospace] text-gray-400">SHARPE RATIO</span>
                    <span className="font-['JetBrains_Mono',monospace] text-white font-bold">2.84</span>
                  </div>
                  <div className="h-2 bg-[#1A2332] rounded-full overflow-hidden">
                    <div className="h-full w-[90%] bg-gradient-to-r from-cyan-500 to-blue-400" />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Footer */}
        <footer className="mt-16 pt-8 border-t border-cyan-900/20 stagger-fade-in" style={{ animationDelay: '0.6s' }}>
          <div className="flex justify-between items-center text-xs font-['JetBrains_Mono',monospace] text-gray-500">
            <span>KYMERA SYSTEMS LLC © 2025</span>
            <span>LAST UPDATE: {new Date().toLocaleString('en-US', { 
              hour: '2-digit', 
              minute: '2-digit', 
              second: '2-digit',
              hour12: false 
            })}</span>
          </div>
        </footer>
      </div>
    </div>
  );
}
