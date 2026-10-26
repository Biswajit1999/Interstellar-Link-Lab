/* Interstellar Link Lab: deterministic visual model, no external libraries */
(() => {
 "use strict";
 const C=299792458, H=6.62607015e-34, LY=9.4607304725808e15, YEAR=365.25*86400;
 const byId=id=>document.getElementById(id);
 const nice=(v,unit="")=>{if(!Number.isFinite(v))return "—";if(v>=1e6)return (v/1e6).toFixed(2)+"M"+unit;if(v>=1e3)return (v/1000).toFixed(2)+"k"+unit;if(v>=10)return v.toFixed(1)+unit;if(v>=1)return v.toFixed(2)+unit;if(v>=.001)return v.toPrecision(3)+unit;return v.toExponential(2)+unit};
 const inputs=["power","dtx","drx","distance","wavelength","efficiency","pointing","order","signal","background"];
 let last={};
 function get(id){const v=Number(byId(id)?.value||0);return id==="order"?Math.pow(2,v):v}
 function format(id,v){if(id==="order")return String(Math.pow(2,v));if(id==="wavelength")return v+" nm";if(id==="distance")return v.toFixed(2)+" ly";if(id==="efficiency")return Math.round(v*100)+"%";if(id==="pointing")return v.toFixed(2)+" μrad";if(id==="power")return v+" W";if(id==="signal")return v.toFixed(2)+" photons";if(id==="background")return v.toFixed(2)+" photons";if(id==="dtx"||id==="drx")return v.toFixed(1)+" m";return String(v)}
 function simulateLink(){
  const p=get("power"),dt=get("dtx"),dr=get("drx"),dly=get("distance"),lam=get("wavelength")*1e-9,eta=get("efficiency"),sig=get("pointing")*1e-6;
  const R=dly*LY,z=Math.PI*dt*dr/(2*lam*R),capture=z*z/4-z**4/32;
  const ideal=p*lam/(H*C)*capture*eta;
  const radius=2*lam/(Math.PI*dt);  // equivalent Gaussian, not Airy jitter integral
  const jitterAvg=1/(1+4*(sig/radius)**2);
  const detected=ideal*jitterAvg;
  const oneWay=R/C/YEAR,roundTrip=2*oneWay;
  last={...last,photon_rate_s:detected,ideal_photon_rate_s:ideal,pointing_factor:jitterAvg,one_way_years:oneWay,round_trip_years:roundTrip};
  if(byId("rate"))byId("rate").textContent=nice(detected," /s");
  if(byId("oneway"))byId("oneway").textContent=nice(oneWay," y");
  if(byId("roundtrip"))byId("roundtrip").textContent=nice(roundTrip," y");
  if(byId("coupling"))byId("coupling").textContent=(jitterAvg*100).toFixed(1)+"%";
  if(byId("thousand"))byId("thousand").textContent=detected>0?nice(1000/detected," s"):"—";
  if(byId("capture"))byId("capture").textContent=capture.toExponential(3);
 }
 // Knuth sampler: bound mean <=25
 function rng(seed){let s=seed>>>0;return ()=>((s=(Math.imul(s,1664525)+1013904223)>>>0)/4294967296)}
 function poisson(mu,rand){const limit=Math.exp(-mu);let k=0,p=1;do{k++;p*=rand()}while(p>limit);return k-1}
 function monteCarlo(order,signal,background,points=800,seed=20261026){
  const rand=rng(seed);let errors=0,sample=[];
  for(let j=0;j<points;j++){
   const tx=Math.floor(rand()*order);const v=Array.from({length:order},(_,i)=>poisson(background+(i===tx?signal:0),rand));
   const m=Math.max(...v),which=v.map((x,i)=>x===m?i:-1).filter(x=>x>=0);
   const rx=which[Math.floor(rand()*which.length)];
   errors+=(rx!==tx); if(j===0)sample=v;
  }
  return {order,signal,background,seed,symbols:points,errors,ser:errors/points,sample};
 }
 function plot(data){
  const el=byId("slotChart");if(!el)return;
  const dpr=Math.min(2,window.devicePixelRatio||1),width=el.clientWidth||720,height=230;
  el.width=Math.round(width*dpr);el.height=Math.round(height*dpr);
  const ctx=el.getContext("2d");ctx.scale(dpr,dpr);ctx.clearRect(0,0,width,height);
  ctx.fillStyle="#081523";ctx.fillRect(0,0,width,height);
  const m=data.sample.length,high=Math.max(3,...data.sample)+1;
  ctx.strokeStyle="#32495f";ctx.lineWidth=1;
  for(let i=0;i<=4;i++){const y=30+i*(height-60)/4;ctx.beginPath();ctx.moveTo(45,y);ctx.lineTo(width-20,y);ctx.stroke();}
  for(let i=0;i<m;i++){
    const cell=(width-80)/m,bw=Math.max(3,cell*.56),bh=(data.sample[i]/high)*(height-70);
    ctx.fillStyle=data.sample[i]===Math.max(...data.sample)?"#76e7ec":"#477fac";
    ctx.fillRect(48+i*cell+(cell-bw)/2,height-39-bh,bw,bh);
    if(m<=16){ctx.fillStyle="#a8c2d4";ctx.font="12px system-ui";ctx.textAlign="center";ctx.fillText(String(i),48+i*cell+cell/2,height-15);}
  }
  ctx.textAlign="left";ctx.font="12px system-ui";ctx.fillStyle="#bdd6e8";ctx.fillText("Detected photon counts by PPM slot",47,21);
 }
 function refresh(){
  inputs.forEach(id=>{const x=byId(id),out=byId(id+"Out");if(x&&out)out.textContent=format(id,Number(x.value))});
  simulateLink();
  const result=monteCarlo(get("order"),get("signal"),get("background"));
  last={...last,ppm:result};
  if(byId("ser"))byId("ser").textContent=(100*result.ser).toFixed(2)+"%";
  if(byId("errors"))byId("errors").textContent=result.errors+" / "+result.symbols;
  plot(result);
 }
 inputs.forEach(id=>{byId(id)?.addEventListener("input",refresh)});
 byId("simulate")?.addEventListener("click",refresh);
 byId("export")?.addEventListener("click",()=>{
  const a=document.createElement("a");
  const blob=new Blob([JSON.stringify({schema:"interstellar-link-lab/v0.7",assumptions:"small receiver Airy approximation; Gaussian equivalent jitter; synthetic uncoded PPM",...last},null,2)],{type:"application/json"});
  a.href=URL.createObjectURL(blob);a.download="interstellar-link-simulation.json";a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1000);
 });
 const observer=("IntersectionObserver" in window)?new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add("visible");observer.unobserve(e.target)}})},{rootMargin:"0px 0px -40px 0px",threshold:.1}):null;
 document.querySelectorAll(".reveal").forEach(x=>observer?observer.observe(x):x.classList.add("visible"));
 const bar=byId("progress");
 const onScroll=()=>{if(!bar)return;const d=document.documentElement;bar.style.width=(100*window.scrollY/Math.max(1,d.scrollHeight-window.innerHeight)).toFixed(1)+"%"};
 window.addEventListener("scroll",onScroll,{passive:true});
 window.addEventListener("resize",()=>{if(last.ppm)plot(last.ppm)},{passive:true});
 refresh();onScroll();
})();
