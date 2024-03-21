#Hello
import replicate
output = replicate.run(
    "cjwbw/animagine-xl-3.1:6afe2e6b27dad2d6f480b59195c221884b6acc589ff4d05ff0e5fc058690fbb9",
    input={
        "width": 896,
        "height": 1152,
        "prompt": "1girl, cagliostro, granblue fantasy, violet eyes, standing, hand on own chin, looking at object, smile, closed mouth, table, beaker, glass tube, experiment apparatus, dark room, laboratory, upper body",
        "guidance_scale": 7,
        "style_selector": "(None)",
        "negative_prompt": "nsfw, lowres, (bad), text, error, fewer, extra, missing, worst quality, jpeg artifacts, low quality, watermark, unfinished, displeasing, oldest, early, chromatic aberration, signature, extra digits, artistic error, username, scan, [abstract]",
        "quality_selector": "Standard v3.1",
        "num_inference_steps": 28
    }
)
print(output)

