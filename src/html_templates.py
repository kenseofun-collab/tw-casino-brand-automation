def generate_block_2(brand):
    return f"""
<div class="sy-block-2-wrapper">
  <style>
    .sy-block-2-wrapper {{ font-family: system-ui, -apple-system, sans-serif; width: 100%; margin: 0; background: linear-gradient(135deg, #241b45 0%, #171131 100%); border-radius: 16px; padding: 24px; color: #ffffff; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15); box-sizing: border-box; }}
    .sy-card-container {{ display: flex; align-items: stretch; gap: 20px; flex-wrap: wrap; }}
    .sy-logo-col {{ flex: 0 0 130px; display: flex; flex-direction: column; justify-content: center; align-items: center; background-color: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; padding: 10px; min-height: 130px; box-sizing: border-box; }}
    .sy-logo-img {{ max-width: 100%; max-height: 80px; object-fit: contain; border-radius: 6px; }}
    .sy-logo-fallback {{ font-size: 20px; font-weight: bold; color: #ffffff; text-align: center; background: linear-gradient(45deg, #ff416c, #ff4b2b); width: 100%; height: 80px; line-height: 80px; border-radius: 8px; display: none; }}
    .sy-rating-col {{ flex: 1 1 220px; background-color: #120e28; border-radius: 12px; padding: 16px; border: 1px solid rgba(255, 255, 255, 0.05); box-sizing: border-box; }}
    .sy-col-title {{ font-size: 15px; color: #a49fc6; font-weight: 600; margin-top: 0; margin-bottom: 12px; border-bottom: 1px solid rgba(255, 255, 255, 0.1); padding-bottom: 6px; }}
    .sy-rating-item {{ display: flex; justify-content: space-between; align-items: center; max-width: 180px; margin: 0 auto 8px auto; font-size: 12px; }}
    .sy-rating-label {{ color: #d1cbdc; }}
    .sy-stars-container {{ display: flex; gap: 2px; }}
    .sy-star {{ font-size: 15px; line-height: 1; display: inline-block; }}
    .sy-star.gold {{ color: #ffc107; }}
    .sy-star.gray {{ color: #555555; }}
    .sy-highlights-col {{ flex: 1.2 1 250px; box-sizing: border-box; padding: 4px; }}
    .sy-highlight-list {{ list-style: none; padding: 0; margin: 0; }}
    .sy-highlight-item {{ display: flex; align-items: flex-start; margin-bottom: 12px; font-size: 14.5px; color: #f1f0f5; }}
    .sy-check-icon {{ width: 18px; height: 18px; fill: #2ecc71; margin-right: 8px; flex-shrink: 0; margin-top: 2px; }}
    .sy-action-col {{ flex: 1.5 1 280px; display: flex; flex-direction: column; justify-content: space-between; gap: 12px; box-sizing: border-box; }}
    .sy-promo-banner-card {{ background-color: #2b2450; border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 10px; padding: 12px 16px; display: flex; align-items: center; justify-content: space-between; gap: 12px; }}
    .sy-gift-area {{ display: flex; align-items: center; gap: 10px; }}
    .sy-gift-icon {{ width: 28px; height: 28px; }}
    .sy-promo-text-wrap {{ display: flex; flex-direction: column; }}
    .sy-promo-subtitle {{ font-size: 11px; color: #b3aed2; }}
    .sy-promo-val {{ font-size: 15px; font-weight: 800; color: #ffffff; }}
    .sy-cta-button {{ background: linear-gradient(180deg, #f5b041 0%, #e67e22 100%); color: #ffffff !important; text-shadow: 0 1px 2px rgba(0,0,0,0.5); padding: 10px 16px; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 14.5px; border: none; cursor: pointer; transition: all 0.2s ease-in-out; box-shadow: 0 4px 10px rgba(245, 176, 65, 0.2); text-align: center; white-space: nowrap; }}
    .sy-cta-button:hover {{ background: linear-gradient(180deg, #f7b955 0%, #f39c12 100%); transform: translateY(-2px); box-shadow: 0 6px 15px rgba(245, 176, 65, 0.35); }}
    .sy-tags-row {{ display: flex; gap: 8px; flex-wrap: wrap; }}
    .sy-tag {{ background-color: #382e70; color: #d1cbdc; font-size: 12px; padding: 4px 10px; border-radius: 4px; border: 1px solid rgba(255, 255, 255, 0.05); }}
    @media (max-width: 768px) {{ .sy-card-container {{ flex-direction: column; gap: 16px; }} .sy-logo-col {{ flex: 1 1 auto; min-height: auto; padding: 16px; }} .sy-logo-img {{ max-height: 60px; }} .sy-rating-col, .sy-highlights-col, .sy-action-col {{ flex: 1 1 auto; }} .sy-promo-banner-card {{ padding: 12px; }} }}
  </style>

  <div class="sy-card-container">
    <div class="sy-logo-col">
      <img id="{brand['slug']}-logo-img" class="sy-logo-img" src="{brand['logo']}" alt="{brand['name']}" onerror="document.getElementById('{brand['slug']}-logo-img').style.display='none';document.getElementById('{brand['slug']}-logo-fallback').style.display='block';">
      <div id="{brand['slug']}-logo-fallback" class="sy-logo-fallback">{brand['name']}</div>
    </div>

    <div class="sy-rating-col">
      <h3 class="sy-col-title">品牌評分</h3>
      <div class="sy-rating-item"><span class="sy-rating-label">出入金透明度</span><div class="sy-stars-container"><span class="sy-star gold">★</span><span class="sy-star gold">★</span><span class="sy-star gold">★</span><span class="sy-star gold">★</span><span class="sy-star gold">★</span></div></div>
      <div class="sy-rating-item"><span class="sy-rating-label">新手入門體驗金</span><div class="sy-stars-container"><span class="sy-star gold">★</span><span class="sy-star gold">★</span><span class="sy-star gold">★</span><span class="sy-star gold">★</span><span class="sy-star gold">★</span></div></div>
      <div class="sy-rating-item"><span class="sy-rating-label">老玩家開玩優惠</span><div class="sy-stars-container"><span class="sy-star gold">★</span><span class="sy-star gold">★</span><span class="sy-star gold">★</span><span class="sy-star gold">★</span><span class="sy-star gray">★</span></div></div>
      <div class="sy-rating-item"><span class="sy-rating-label">客服與金流體驗</span><div class="sy-stars-container"><span class="sy-star gold">★</span><span class="sy-star gold">★</span><span class="sy-star gold">★</span><span class="sy-star gold">★</span><span class="sy-star gold">★</span></div></div>
    </div>

    <div class="sy-highlights-col">
      <h3 class="sy-col-title">亮點</h3>
      <ul class="sy-highlight-list">
        {''.join([f'<li class="sy-highlight-item"><svg class="sy-check-icon" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z" /></svg>{hl}</li>' for hl in brand['highlights']])}
      </ul>
    </div>

    <div class="sy-action-col">
      <div class="sy-promo-banner-card">
        <div class="sy-gift-area">
          <svg class="sy-gift-icon" viewBox="0 0 24 24"><path d="M12 22h8a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-8v15z" fill="#e74c3c" /><path d="M12 22H4a2 2 0 0 1-2-2V9a2 2 0 0 1 2-2h8v15z" fill="#c0392b" /><path d="M22 6.5A1.5 1.5 0 0 0 20.5 5H17c-.55 0-1 .45-1 1a3 3 0 0 0-6 0c0-.55-.45-1-1-1H3.5A1.5 1.5 0 0 0 2 6.5v1A1.5 1.5 0 0 0 3.5 9h17A1.5 1.5 0 0 0 22 7.5v-1z" fill="#f1c40f" /><path d="M10 6a1 1 0 0 1 1-1h1v2h-1a1 1 0 0 1-1-1zM14 6a1 1 0 0 0-1-1h-1v2h1a1 1 0 0 0 1-1z" fill="#d35400" /><rect x="11" y="7" width="2" height="15" fill="#f1c40f" /></svg>
          <div class="sy-promo-text-wrap">
            <span class="sy-promo-subtitle">{brand['promo_title']}</span>
            <span class="sy-promo-val">{brand['promo_val']}</span>
          </div>
        </div>
        <a class="sy-cta-button" href="{brand['link']}" target="_blank" rel="noopener noreferrer nofollow">前往{brand['name']}</a>
      </div>
      <div class="sy-tags-row">
        {''.join([f'<span class="sy-tag">{tag}</span>' for tag in brand['tags']])}
      </div>
    </div>
  </div>
</div>
"""

def generate_block_1(brand):
    return f"""
<div class="sy-block-1-wrapper">
  <style>
    .sy-block-1-wrapper {{ font-family: system-ui, -apple-system, sans-serif; color: #333333; width: 100%; margin: 20px auto; line-height: 1.7; }}
    .sy-block-1-wrapper p {{ margin-top: 0; margin-bottom: 16px; font-size: 15px; color: #4a4a4a; }}
    .sy-block-1-wrapper ul, .sy-block-1-wrapper ol {{ margin-top: 0; margin-bottom: 16px; padding-left: 24px; }}
    .sy-block-1-wrapper li {{ margin-bottom: 8px; font-size: 15px; color: #4a4a4a; }}
    .sy-block-1-wrapper .sy-heading-2 {{ font-size: 20px; font-weight: 700; color: #ffffff; background: linear-gradient(135deg, #5c24e6 0%, #4019a1 100%); padding: 12px 20px; margin-top: 36px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); clear: both !important; display: block !important; overflow: hidden; }}
    .sy-block-1-wrapper .sy-heading-3 {{ font-size: 18px; font-weight: 700; color: #2c2c2c; margin-top: 30px; margin-bottom: 16px; border-bottom: 1px solid #e9ecef; padding-bottom: 6px; }}
    .sy-block-1-wrapper .sy-pros-cons-title {{ font-size: 18px; font-weight: 700; color: #2c2c2c; margin-bottom: 12px; padding-left: 10px; border-left: 4px solid; clear: both; }}
    .sy-pros-cons-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 30px; clear: both !important; display: grid !important; }}
    .sy-block-1-wrapper .sy-card {{ border-radius: 12px; padding: 20px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02); height: 100%; box-sizing: border-box; }}
    .sy-block-1-wrapper .sy-pros-card {{ background-color: #fafdfb; border: 1px solid #d4edda; border-top: 4px solid #2ecc71; }}
    .sy-block-1-wrapper .sy-cons-card {{ background-color: #fdfafa; border: 1px solid #f8d7da; border-top: 4px solid #e74c3c; }}
    .sy-block-1-wrapper .sy-card-list {{ margin: 0; padding-left: 20px; }}
    .sy-block-1-wrapper .sy-card-list li {{ margin-bottom: 10px; font-size: 14.5px; line-height: 1.6; }}
    .sy-block-1-wrapper .sy-info-layout {{ display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 24px; margin-bottom: 30px; background: #ffffff; border: 1px solid #e9ecef; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03); }}
    .sy-block-1-wrapper .sy-info-metadata {{ padding: 24px; display: flex; flex-direction: column; gap: 16px; background-color: #f8f9fa; }}
    .sy-block-1-wrapper .sy-info-row {{ display: flex; align-items: flex-start; gap: 14px; padding-bottom: 14px; border-bottom: 1px solid #f1f3f5; }}
    .sy-block-1-wrapper .sy-info-row:last-child {{ border-bottom: none; padding-bottom: 0; }}
    .sy-block-1-wrapper .sy-info-icon-wrapper {{ display: flex; align-items: center; justify-content: center; width: 38px; height: 38px; background-color: #f3efff; color: #5c24e6; border-radius: 8px; flex-shrink: 0; }}
    .sy-block-1-wrapper .sy-info-icon-wrapper svg {{ width: 18px; height: 18px; }}
    .sy-block-1-wrapper .sy-info-content {{ flex-grow: 1; }}
    .sy-block-1-wrapper .sy-info-label {{ font-size: 13px; color: #8e8e93; margin-bottom: 3px; font-weight: 500; }}
    .sy-block-1-wrapper .sy-info-text {{ font-size: 15px; color: #2c2c2c; font-weight: 600; line-height: 1.5; }}
    .sy-block-1-wrapper .sy-info-text.font-highlight {{ color: #5c24e6; font-size: 16px; }}
    .sy-block-1-wrapper .sy-info-rules {{ background-color: #faf9ff; border-left: 1px solid #eae6ff; padding: 24px; display: flex; flex-direction: column; justify-content: flex-start; }}
    .sy-block-1-wrapper .sy-rules-title {{ font-size: 16px; font-weight: 700; color: #1a1a1a; margin-top: 0; margin-bottom: 16px; display: flex; align-items: center; gap: 8px; }}
    .sy-block-1-wrapper .sy-rules-list {{ list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 14px; }}
    .sy-block-1-wrapper .sy-rules-list li {{ display: flex; align-items: flex-start; gap: 12px; margin-bottom: 0; }}
    .sy-block-1-wrapper .sy-rules-number {{ display: flex; align-items: center; justify-content: center; width: 22px; height: 22px; background-color: #5c24e6; color: #ffffff; font-size: 12px; font-weight: 700; border-radius: 50%; flex-shrink: 0; margin-top: 2px; }}
    .sy-block-1-wrapper .sy-rules-number-warning {{ display: flex; align-items: center; justify-content: center; width: 22px; height: 22px; background-color: #e74c3c; color: #ffffff; font-size: 12px; font-weight: 700; border-radius: 50%; flex-shrink: 0; margin-top: 2px; }}
    .sy-block-1-wrapper .sy-rules-detail {{ font-size: 14px; color: #4a4a4a; line-height: 1.5; }}
    .sy-block-1-wrapper .sy-rules-detail strong {{ color: #2c2c2c; }}
    .sy-block-1-wrapper .sy-section-card {{ background-color: #f8f9fa; border: 1px solid #e9ecef; border-radius: 12px; padding: 24px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02); margin-bottom: 30px; }}
    .sy-block-1-wrapper .sy-promo-list {{ margin: 0; padding-left: 20px; }}
    .sy-block-1-wrapper .sy-promo-list li {{ margin-bottom: 12px; font-size: 15px; color: #333333; }}
    .sy-block-1-wrapper .sy-promo-list li strong {{ color: #5c24e6; }}
    .sy-block-1-wrapper .sy-table-container {{ width: 100%; overflow-x: auto; margin-top: 15px; margin-bottom: 25px; border-radius: 8px; border: 1px solid #e9ecef; }}
    .sy-block-1-wrapper .sy-table {{ width: 100%; border-collapse: collapse; background-color: #ffffff; min-width: 600px; }}
    .sy-block-1-wrapper .sy-table th {{ background-color: #5c24e6; color: #ffffff; text-align: left; padding: 12px 16px; font-weight: bold; font-size: 15px; border: 1px solid #e9ecef; }}
    .sy-block-1-wrapper .sy-table td {{ padding: 12px 16px; border: 1px solid #e9ecef; font-size: 14px; color: #555555; line-height: 1.6; }}
    .sy-block-1-wrapper .sy-table tr:nth-child(even) {{ background-color: #f9f8ff; }}
    .sy-block-1-wrapper .sy-table td:first-child {{ font-weight: bold; color: #333333; width: 25%; background-color: #f5f3ff; }}
    .sy-block-1-wrapper .sy-table td:nth-child(2) {{ width: 38%; }}
    .sy-block-1-wrapper .sy-table td:nth-child(3) {{ width: 37%; }}
    @media (max-width: 768px) {{
      .sy-pros-cons-grid {{ grid-template-columns: 1fr !important; }}
      .sy-block-1-wrapper .sy-info-layout {{ grid-template-columns: 1fr !important; gap: 0; }}
      .sy-block-1-wrapper .sy-info-rules {{ border-left: none !important; border-top: 1px solid #eae6ff; }}
    }}
  </style>

  <div class="sy-pros-cons-grid">
    <div>
      <div class="sy-pros-cons-title" style="border-left-color: #2ecc71;">優點</div>
      <div class="sy-card sy-pros-card">
        <ul class="sy-card-list">
          {''.join([f'<li>{p}</li>' for p in brand['pros']])}
        </ul>
      </div>
    </div>
    <div>
      <div class="sy-pros-cons-title" style="border-left-color: #e74c3c;">缺點</div>
      <div class="sy-card sy-cons-card">
        <ul class="sy-card-list">
          {''.join([f'<li>{c}</li>' for c in brand['cons']])}
        </ul>
      </div>
    </div>
  </div>

  <div style="clear: both; height: 1px; width: 100%;"></div>
  <h2 class="sy-heading-2">{brand['name']}基本資料</h2>
  <div class="sy-info-layout">
    <div class="sy-info-metadata">
      <div class="sy-info-row">
        <div class="sy-info-icon-wrapper"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
        <div class="sy-info-content"><div class="sy-info-label">品牌名稱</div><div class="sy-info-text font-highlight">{brand['name']}</div></div>
      </div>
      <div class="sy-info-row">
        <div class="sy-info-icon-wrapper"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="9" y1="3" x2="9" y2="21"/><line x1="15" y1="3" x2="15" y2="21"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="3" y1="15" x2="21" y2="15"/></svg></div>
        <div class="sy-info-content"><div class="sy-info-label">遊戲版本</div><div class="sy-info-text">現金版（入金娛樂城）</div></div>
      </div>
      <div class="sy-info-row">
        <div class="sy-info-icon-wrapper"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"/><line x1="1" y1="10" x2="23" y2="10"/></svg></div>
        <div class="sy-info-content"><div class="sy-info-label">支援入金管道</div><div class="sy-info-text">{brand['deposit']}</div></div>
      </div>
      <div class="sy-info-row">
        <div class="sy-info-icon-wrapper"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></div>
        <div class="sy-info-content"><div class="sy-info-label">線上客服管道</div><div class="sy-info-text">LINE 官方客服（24小時）、官網線上浮動客服</div></div>
      </div>
    </div>
    <div class="sy-info-rules">
      <h3 class="sy-rules-title"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#5c24e6" stroke-width="2.5" style="width: 18px; height: 18px;"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>出入金規則簡述</h3>
      <ul class="sy-rules-list">
        {''.join([f'<li><span class="sy-rules-number">{i+1}</span><div class="sy-rules-detail">{r}</div></li>' for i, r in enumerate(brand['rules'])])}
      </ul>
    </div>
  </div>

  <h2 class="sy-heading-2" id="sy-promotions">{brand['name']}優惠</h2>
  <div class="sy-section-card">
    <ul class="sy-promo-list">
      {''.join([f'<li><strong>{p[0]}：</strong>{p[1]}</li>' for p in brand['promo_details']])}
    </ul>
  </div>

  <h2 class="sy-heading-2">{brand['name']}評價：{brand['review_title']}</h2>
  <p>{brand['review_desc1']}</p>
  <p>{brand['review_desc2']}</p>

</div>
"""
