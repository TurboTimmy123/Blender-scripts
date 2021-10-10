# Iterates through all actions in 1 sequence
# Useful when searching through 100's of animations from an externally imported animation

import bpy

def stop_at_last_frame(scene):
    # NOTE, due to frame-skipping/AV sync, -5 offset is required to trigger
    # Assuming no more than 5 frames are skipped during playback
    if scene.frame_current >= bpy.context.scene.frame_end - 5:
        list = []
        for a in bpy.data.actions:
            list.append(a.name)
        index = list.index(bpy.context.active_object.animation_data.action.name)
        print('Setting to', list[index+1])
        bpy.context.active_object.animation_data.action = bpy.data.actions.get(list[index+1])
        action_list = [action.frame_range for action in bpy.data.actions]
        
        print('Action length', action_list[index+1][-1])
        
        bpy.context.scene.frame_end = action_list[index+1][-1]
        bpy.context.scene.frame_current = 0

print('Clearing handler')
bpy.app.handlers.frame_change_post.clear()
bpy.app.handlers.frame_change_post.append(stop_at_last_frame)
print('Registered handler')