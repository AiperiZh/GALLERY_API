from typing import Dict

import cloudinary.uploader as cloud_uploader 

def upload_image_to_cloud(file) -> Dict[str, str]:
    res = cloud_uploader.upload(file) 
    return {
        "url": res.get("secure_url") or res.get("url"),
        "public_id": res["public_id"],
    }

