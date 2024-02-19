from PIL import Image, ImageDraw
import cv2,codecs,json

lead = "Coin_leads/ac7d9e74-4030-4633-909e-eecd017b8dcc_coin"
# leadsid = "/root/Downloads/final_repo/Tyre_Health/Claim_ID/Coin_Leads/"+lead

def draw_img(claim_id):
    image = Image.open(claim_id + "/image.jpg")
    draw = ImageDraw.Draw(image)
    # load predicted mask into an object
    file_path = claim_id + "/mask_coord.json"
    obj_text = codecs.open(file_path, 'r', encoding='utf-8').read()
    b_new = json.loads(obj_text)
    points = b_new
    for point in points:
        draw.point(point, fill="red")
    # Save the image
    image.save(claim_id + "/image_detected.jpg")
    
draw_img(lead)
