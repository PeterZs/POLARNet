import requests

API_URL = "https://api.polyhaven.com/assets?type=hdris"
HDR_LINK_TEMPLATE = "https://dl.polyhaven.org/file/ph-assets/HDRIs/hdr/4k/{}_4k.hdr"
output_file = "polyhaven_hdr_4k.hdr.txt"

print("📡 Fetching HDR asset metadata from Poly Haven...")
res = requests.get(API_URL)
res.raise_for_status()
assets = res.json()

hdr_urls = []
for asset_id in assets:
    # 拼接成下载链接
    hdr_url = HDR_LINK_TEMPLATE.format(asset_id)
    hdr_urls.append(hdr_url)

# 保存链接
with open(output_file, "w") as f:
    for url in hdr_urls:
        f.write(url + "\n")

print(f"✅ 共生成 {len(hdr_urls)} 个 HDR 资源链接，已保存至 {output_file}")
