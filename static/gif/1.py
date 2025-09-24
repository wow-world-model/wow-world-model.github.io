from moviepy.editor import VideoFileClip, ImageClip, concatenate_videoclips
import os

# 输入视频路径
input_videos = [
    "articulate65.mp4"
]

# 输出文件夹
output_folder = "./output"
os.makedirs(output_folder, exist_ok=True)

for path in input_videos:
    clip = VideoFileClip(path)
    
    # 获取最后一帧
    last_frame = clip.get_frame(clip.duration - 1/clip.fps)
    
    # 创建 1 秒静态帧
    freeze_clip = ImageClip(last_frame).set_duration(1).set_fps(clip.fps)
    
    # 合并原视频 + 静态帧
    final_clip = concatenate_videoclips([clip, freeze_clip])
    
    # 输出
    output_path = os.path.join(output_folder, os.path.basename(path))
    final_clip.write_videofile(output_path, codec="libx264", fps=clip.fps)

    clip.close()
    final_clip.close()

print("处理完成！")
