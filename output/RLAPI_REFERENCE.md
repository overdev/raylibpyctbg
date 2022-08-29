# raylib-py <sub>4.2</sub> cheat sheet

CONSTANTS | ENUMERATIONS | STRUCTURES | FUNCTIONS

---
## Enumerations

### ConfigFlags enumeration

Members
Name | Value | Description
-----|-------|------------
FLAG_VSYNC_HINT | 64 | Set to try enabling V-Sync on GPU
FLAG_FULLSCREEN_MODE | 2 | Set to run program in fullscreen
FLAG_WINDOW_RESIZABLE | 4 | Set to allow resizable window
FLAG_WINDOW_UNDECORATED | 8 | Set to disable window decoration (frame and buttons)
FLAG_WINDOW_HIDDEN | 128 | Set to hide window
FLAG_WINDOW_MINIMIZED | 512 | Set to minimize window (iconify)
FLAG_WINDOW_MAXIMIZED | 1024 | Set to maximize window (expanded to monitor)
FLAG_WINDOW_UNFOCUSED | 2048 | Set to window non focused
FLAG_WINDOW_TOPMOST | 4096 | Set to window always on top
FLAG_WINDOW_ALWAYS_RUN | 256 | Set to allow windows running while minimized
FLAG_WINDOW_TRANSPARENT | 16 | Set to allow transparent framebuffer
FLAG_WINDOW_HIGHDPI | 8192 | Set to support HighDPI
FLAG_WINDOW_MOUSE_PASSTHROUGH | 16384 | Set to support mouse passthrough, only supported when FLAG_WINDOW_UNDECORATED
FLAG_MSAA_4X_HINT | 32 | Set to try enabling MSAA 4X
FLAG_INTERLACED_HINT | 65536 | Set to try enabling interlaced video format (for V3D)

### TraceLogLevel enumeration

Members
Name | Value | Description
-----|-------|------------
LOG_ALL | 0 | Display all logs
LOG_TRACE | 1 | Trace logging, intended for internal use only
LOG_DEBUG | 2 | Debug logging, used for internal debugging, it should be disabled on release builds
LOG_INFO | 3 | Info logging, used for program execution info
LOG_WARNING | 4 | Warning logging, used on recoverable failures
LOG_ERROR | 5 | Error logging, used on unrecoverable failures
LOG_FATAL | 6 | Fatal logging, used to abort program: exit(EXIT_FAILURE)
LOG_NONE | 7 | Disable logging

### KeyboardKey enumeration

Members
Name | Value | Description
-----|-------|------------
KEY_NULL | 0 | Key: NULL, used for no key pressed
KEY_APOSTROPHE | 39 | Key: '
KEY_COMMA | 44 | Key: ,
KEY_MINUS | 45 | Key: -
KEY_PERIOD | 46 | Key: .
KEY_SLASH | 47 | Key: /
KEY_ZERO | 48 | Key: 0
KEY_ONE | 49 | Key: 1
KEY_TWO | 50 | Key: 2
KEY_THREE | 51 | Key: 3
KEY_FOUR | 52 | Key: 4
KEY_FIVE | 53 | Key: 5
KEY_SIX | 54 | Key: 6
KEY_SEVEN | 55 | Key: 7
KEY_EIGHT | 56 | Key: 8
KEY_NINE | 57 | Key: 9
KEY_SEMICOLON | 59 | Key: ;
KEY_EQUAL | 61 | Key: =
KEY_A | 65 | Key: A | a
KEY_B | 66 | Key: B | b
KEY_C | 67 | Key: C | c
KEY_D | 68 | Key: D | d
KEY_E | 69 | Key: E | e
KEY_F | 70 | Key: F | f
KEY_G | 71 | Key: G | g
KEY_H | 72 | Key: H | h
KEY_I | 73 | Key: I | i
KEY_J | 74 | Key: J | j
KEY_K | 75 | Key: K | k
KEY_L | 76 | Key: L | l
KEY_M | 77 | Key: M | m
KEY_N | 78 | Key: N | n
KEY_O | 79 | Key: O | o
KEY_P | 80 | Key: P | p
KEY_Q | 81 | Key: Q | q
KEY_R | 82 | Key: R | r
KEY_S | 83 | Key: S | s
KEY_T | 84 | Key: T | t
KEY_U | 85 | Key: U | u
KEY_V | 86 | Key: V | v
KEY_W | 87 | Key: W | w
KEY_X | 88 | Key: X | x
KEY_Y | 89 | Key: Y | y
KEY_Z | 90 | Key: Z | z
KEY_LEFT_BRACKET | 91 | Key: [
KEY_BACKSLASH | 92 | Key: '\'
KEY_RIGHT_BRACKET | 93 | Key: ]
KEY_GRAVE | 96 | Key: `
KEY_SPACE | 32 | Key: Space
KEY_ESCAPE | 256 | Key: Esc
KEY_ENTER | 257 | Key: Enter
KEY_TAB | 258 | Key: Tab
KEY_BACKSPACE | 259 | Key: Backspace
KEY_INSERT | 260 | Key: Ins
KEY_DELETE | 261 | Key: Del
KEY_RIGHT | 262 | Key: Cursor right
KEY_LEFT | 263 | Key: Cursor left
KEY_DOWN | 264 | Key: Cursor down
KEY_UP | 265 | Key: Cursor up
KEY_PAGE_UP | 266 | Key: Page up
KEY_PAGE_DOWN | 267 | Key: Page down
KEY_HOME | 268 | Key: Home
KEY_END | 269 | Key: End
KEY_CAPS_LOCK | 280 | Key: Caps lock
KEY_SCROLL_LOCK | 281 | Key: Scroll down
KEY_NUM_LOCK | 282 | Key: Num lock
KEY_PRINT_SCREEN | 283 | Key: Print screen
KEY_PAUSE | 284 | Key: Pause
KEY_F1 | 290 | Key: F1
KEY_F2 | 291 | Key: F2
KEY_F3 | 292 | Key: F3
KEY_F4 | 293 | Key: F4
KEY_F5 | 294 | Key: F5
KEY_F6 | 295 | Key: F6
KEY_F7 | 296 | Key: F7
KEY_F8 | 297 | Key: F8
KEY_F9 | 298 | Key: F9
KEY_F10 | 299 | Key: F10
KEY_F11 | 300 | Key: F11
KEY_F12 | 301 | Key: F12
KEY_LEFT_SHIFT | 340 | Key: Shift left
KEY_LEFT_CONTROL | 341 | Key: Control left
KEY_LEFT_ALT | 342 | Key: Alt left
KEY_LEFT_SUPER | 343 | Key: Super left
KEY_RIGHT_SHIFT | 344 | Key: Shift right
KEY_RIGHT_CONTROL | 345 | Key: Control right
KEY_RIGHT_ALT | 346 | Key: Alt right
KEY_RIGHT_SUPER | 347 | Key: Super right
KEY_KB_MENU | 348 | Key: KB menu
KEY_KP_0 | 320 | Key: Keypad 0
KEY_KP_1 | 321 | Key: Keypad 1
KEY_KP_2 | 322 | Key: Keypad 2
KEY_KP_3 | 323 | Key: Keypad 3
KEY_KP_4 | 324 | Key: Keypad 4
KEY_KP_5 | 325 | Key: Keypad 5
KEY_KP_6 | 326 | Key: Keypad 6
KEY_KP_7 | 327 | Key: Keypad 7
KEY_KP_8 | 328 | Key: Keypad 8
KEY_KP_9 | 329 | Key: Keypad 9
KEY_KP_DECIMAL | 330 | Key: Keypad .
KEY_KP_DIVIDE | 331 | Key: Keypad /
KEY_KP_MULTIPLY | 332 | Key: Keypad *
KEY_KP_SUBTRACT | 333 | Key: Keypad -
KEY_KP_ADD | 334 | Key: Keypad +
KEY_KP_ENTER | 335 | Key: Keypad Enter
KEY_KP_EQUAL | 336 | Key: Keypad =
KEY_BACK | 4 | Key: Android back button
KEY_MENU | 82 | Key: Android menu button
KEY_VOLUME_UP | 24 | Key: Android volume up button
KEY_VOLUME_DOWN | 25 | Key: Android volume down button

### MouseButton enumeration

Members
Name | Value | Description
-----|-------|------------
MOUSE_BUTTON_LEFT | 0 | Mouse button left
MOUSE_BUTTON_RIGHT | 1 | Mouse button right
MOUSE_BUTTON_MIDDLE | 2 | Mouse button middle (pressed wheel)
MOUSE_BUTTON_SIDE | 3 | Mouse button side (advanced mouse device)
MOUSE_BUTTON_EXTRA | 4 | Mouse button extra (advanced mouse device)
MOUSE_BUTTON_FORWARD | 5 | Mouse button fordward (advanced mouse device)
MOUSE_BUTTON_BACK | 6 | Mouse button back (advanced mouse device)

### MouseCursor enumeration

Members
Name | Value | Description
-----|-------|------------
MOUSE_CURSOR_DEFAULT | 0 | Default pointer shape
MOUSE_CURSOR_ARROW | 1 | Arrow shape
MOUSE_CURSOR_IBEAM | 2 | Text writing cursor shape
MOUSE_CURSOR_CROSSHAIR | 3 | Cross shape
MOUSE_CURSOR_POINTING_HAND | 4 | Pointing hand cursor
MOUSE_CURSOR_RESIZE_EW | 5 | Horizontal resize/move arrow shape
MOUSE_CURSOR_RESIZE_NS | 6 | Vertical resize/move arrow shape
MOUSE_CURSOR_RESIZE_NWSE | 7 | Top-left to bottom-right diagonal resize/move arrow shape
MOUSE_CURSOR_RESIZE_NESW | 8 | The top-right to bottom-left diagonal resize/move arrow shape
MOUSE_CURSOR_RESIZE_ALL | 9 | The omni-directional resize/move cursor shape
MOUSE_CURSOR_NOT_ALLOWED | 10 | The operation-not-allowed shape

### GamepadButton enumeration

Members
Name | Value | Description
-----|-------|------------
GAMEPAD_BUTTON_UNKNOWN | 0 | Unknown button, just for error checking
GAMEPAD_BUTTON_LEFT_FACE_UP | 1 | Gamepad left DPAD up button
GAMEPAD_BUTTON_LEFT_FACE_RIGHT | 2 | Gamepad left DPAD right button
GAMEPAD_BUTTON_LEFT_FACE_DOWN | 3 | Gamepad left DPAD down button
GAMEPAD_BUTTON_LEFT_FACE_LEFT | 4 | Gamepad left DPAD left button
GAMEPAD_BUTTON_RIGHT_FACE_UP | 5 | Gamepad right button up (i.e. PS3: Triangle, Xbox: Y)
GAMEPAD_BUTTON_RIGHT_FACE_RIGHT | 6 | Gamepad right button right (i.e. PS3: Square, Xbox: X)
GAMEPAD_BUTTON_RIGHT_FACE_DOWN | 7 | Gamepad right button down (i.e. PS3: Cross, Xbox: A)
GAMEPAD_BUTTON_RIGHT_FACE_LEFT | 8 | Gamepad right button left (i.e. PS3: Circle, Xbox: B)
GAMEPAD_BUTTON_LEFT_TRIGGER_1 | 9 | Gamepad top/back trigger left (first), it could be a trailing button
GAMEPAD_BUTTON_LEFT_TRIGGER_2 | 10 | Gamepad top/back trigger left (second), it could be a trailing button
GAMEPAD_BUTTON_RIGHT_TRIGGER_1 | 11 | Gamepad top/back trigger right (one), it could be a trailing button
GAMEPAD_BUTTON_RIGHT_TRIGGER_2 | 12 | Gamepad top/back trigger right (second), it could be a trailing button
GAMEPAD_BUTTON_MIDDLE_LEFT | 13 | Gamepad center buttons, left one (i.e. PS3: Select)
GAMEPAD_BUTTON_MIDDLE | 14 | Gamepad center buttons, middle one (i.e. PS3: PS, Xbox: XBOX)
GAMEPAD_BUTTON_MIDDLE_RIGHT | 15 | Gamepad center buttons, right one (i.e. PS3: Start)
GAMEPAD_BUTTON_LEFT_THUMB | 16 | Gamepad joystick pressed button left
GAMEPAD_BUTTON_RIGHT_THUMB | 17 | Gamepad joystick pressed button right

### GamepadAxis enumeration

Members
Name | Value | Description
-----|-------|------------
GAMEPAD_AXIS_LEFT_X | 0 | Gamepad left stick X axis
GAMEPAD_AXIS_LEFT_Y | 1 | Gamepad left stick Y axis
GAMEPAD_AXIS_RIGHT_X | 2 | Gamepad right stick X axis
GAMEPAD_AXIS_RIGHT_Y | 3 | Gamepad right stick Y axis
GAMEPAD_AXIS_LEFT_TRIGGER | 4 | Gamepad back trigger left, pressure level: [1..-1]
GAMEPAD_AXIS_RIGHT_TRIGGER | 5 | Gamepad back trigger right, pressure level: [1..-1]

### MaterialMapIndex enumeration

Members
Name | Value | Description
-----|-------|------------
MATERIAL_MAP_ALBEDO | 0 | Albedo material (same as: MATERIAL_MAP_DIFFUSE)
MATERIAL_MAP_METALNESS | 1 | Metalness material (same as: MATERIAL_MAP_SPECULAR)
MATERIAL_MAP_NORMAL | 2 | Normal material
MATERIAL_MAP_ROUGHNESS | 3 | Roughness material
MATERIAL_MAP_OCCLUSION | 4 | Ambient occlusion material
MATERIAL_MAP_EMISSION | 5 | Emission material
MATERIAL_MAP_HEIGHT | 6 | Heightmap material
MATERIAL_MAP_CUBEMAP | 7 | Cubemap material (NOTE: Uses GL_TEXTURE_CUBE_MAP)
MATERIAL_MAP_IRRADIANCE | 8 | Irradiance material (NOTE: Uses GL_TEXTURE_CUBE_MAP)
MATERIAL_MAP_PREFILTER | 9 | Prefilter material (NOTE: Uses GL_TEXTURE_CUBE_MAP)
MATERIAL_MAP_BRDF | 10 | Brdf material

### ShaderLocationIndex enumeration

Members
Name | Value | Description
-----|-------|------------
SHADER_LOC_VERTEX_POSITION | 0 | Shader location: vertex attribute: position
SHADER_LOC_VERTEX_TEXCOORD01 | 1 | Shader location: vertex attribute: texcoord01
SHADER_LOC_VERTEX_TEXCOORD02 | 2 | Shader location: vertex attribute: texcoord02
SHADER_LOC_VERTEX_NORMAL | 3 | Shader location: vertex attribute: normal
SHADER_LOC_VERTEX_TANGENT | 4 | Shader location: vertex attribute: tangent
SHADER_LOC_VERTEX_COLOR | 5 | Shader location: vertex attribute: color
SHADER_LOC_MATRIX_MVP | 6 | Shader location: matrix uniform: model-view-projection
SHADER_LOC_MATRIX_VIEW | 7 | Shader location: matrix uniform: view (camera transform)
SHADER_LOC_MATRIX_PROJECTION | 8 | Shader location: matrix uniform: projection
SHADER_LOC_MATRIX_MODEL | 9 | Shader location: matrix uniform: model (transform)
SHADER_LOC_MATRIX_NORMAL | 10 | Shader location: matrix uniform: normal
SHADER_LOC_VECTOR_VIEW | 11 | Shader location: vector uniform: view
SHADER_LOC_COLOR_DIFFUSE | 12 | Shader location: vector uniform: diffuse color
SHADER_LOC_COLOR_SPECULAR | 13 | Shader location: vector uniform: specular color
SHADER_LOC_COLOR_AMBIENT | 14 | Shader location: vector uniform: ambient color
SHADER_LOC_MAP_ALBEDO | 15 | Shader location: sampler2d texture: albedo (same as: SHADER_LOC_MAP_DIFFUSE)
SHADER_LOC_MAP_METALNESS | 16 | Shader location: sampler2d texture: metalness (same as: SHADER_LOC_MAP_SPECULAR)
SHADER_LOC_MAP_NORMAL | 17 | Shader location: sampler2d texture: normal
SHADER_LOC_MAP_ROUGHNESS | 18 | Shader location: sampler2d texture: roughness
SHADER_LOC_MAP_OCCLUSION | 19 | Shader location: sampler2d texture: occlusion
SHADER_LOC_MAP_EMISSION | 20 | Shader location: sampler2d texture: emission
SHADER_LOC_MAP_HEIGHT | 21 | Shader location: sampler2d texture: height
SHADER_LOC_MAP_CUBEMAP | 22 | Shader location: samplerCube texture: cubemap
SHADER_LOC_MAP_IRRADIANCE | 23 | Shader location: samplerCube texture: irradiance
SHADER_LOC_MAP_PREFILTER | 24 | Shader location: samplerCube texture: prefilter
SHADER_LOC_MAP_BRDF | 25 | Shader location: sampler2d texture: brdf

### ShaderUniformDataType enumeration

Members
Name | Value | Description
-----|-------|------------
SHADER_UNIFORM_FLOAT | 0 | Shader uniform type: float
SHADER_UNIFORM_VEC2 | 1 | Shader uniform type: vec2 (2 float)
SHADER_UNIFORM_VEC3 | 2 | Shader uniform type: vec3 (3 float)
SHADER_UNIFORM_VEC4 | 3 | Shader uniform type: vec4 (4 float)
SHADER_UNIFORM_INT | 4 | Shader uniform type: int
SHADER_UNIFORM_IVEC2 | 5 | Shader uniform type: ivec2 (2 int)
SHADER_UNIFORM_IVEC3 | 6 | Shader uniform type: ivec3 (3 int)
SHADER_UNIFORM_IVEC4 | 7 | Shader uniform type: ivec4 (4 int)
SHADER_UNIFORM_SAMPLER2D | 8 | Shader uniform type: sampler2d

### ShaderAttributeDataType enumeration

Members
Name | Value | Description
-----|-------|------------
SHADER_ATTRIB_FLOAT | 0 | Shader attribute type: float
SHADER_ATTRIB_VEC2 | 1 | Shader attribute type: vec2 (2 float)
SHADER_ATTRIB_VEC3 | 2 | Shader attribute type: vec3 (3 float)
SHADER_ATTRIB_VEC4 | 3 | Shader attribute type: vec4 (4 float)

### PixelFormat enumeration

Members
Name | Value | Description
-----|-------|------------
PIXELFORMAT_UNCOMPRESSED_GRAYSCALE | 1 | 8 bit per pixel (no alpha)
PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA | 2 | 8*2 bpp (2 channels)
PIXELFORMAT_UNCOMPRESSED_R5G6B5 | 3 | 16 bpp
PIXELFORMAT_UNCOMPRESSED_R8G8B8 | 4 | 24 bpp
PIXELFORMAT_UNCOMPRESSED_R5G5B5A1 | 5 | 16 bpp (1 bit alpha)
PIXELFORMAT_UNCOMPRESSED_R4G4B4A4 | 6 | 16 bpp (4 bit alpha)
PIXELFORMAT_UNCOMPRESSED_R8G8B8A8 | 7 | 32 bpp
PIXELFORMAT_UNCOMPRESSED_R32 | 8 | 32 bpp (1 channel - float)
PIXELFORMAT_UNCOMPRESSED_R32G32B32 | 9 | 32*3 bpp (3 channels - float)
PIXELFORMAT_UNCOMPRESSED_R32G32B32A32 | 10 | 32*4 bpp (4 channels - float)
PIXELFORMAT_COMPRESSED_DXT1_RGB | 11 | 4 bpp (no alpha)
PIXELFORMAT_COMPRESSED_DXT1_RGBA | 12 | 4 bpp (1 bit alpha)
PIXELFORMAT_COMPRESSED_DXT3_RGBA | 13 | 8 bpp
PIXELFORMAT_COMPRESSED_DXT5_RGBA | 14 | 8 bpp
PIXELFORMAT_COMPRESSED_ETC1_RGB | 15 | 4 bpp
PIXELFORMAT_COMPRESSED_ETC2_RGB | 16 | 4 bpp
PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA | 17 | 8 bpp
PIXELFORMAT_COMPRESSED_PVRT_RGB | 18 | 4 bpp
PIXELFORMAT_COMPRESSED_PVRT_RGBA | 19 | 4 bpp
PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA | 20 | 8 bpp
PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA | 21 | 2 bpp

### TextureFilter enumeration

Members
Name | Value | Description
-----|-------|------------
TEXTURE_FILTER_POINT | 0 | No filter, just pixel approximation
TEXTURE_FILTER_BILINEAR | 1 | Linear filtering
TEXTURE_FILTER_TRILINEAR | 2 | Trilinear filtering (linear with mipmaps)
TEXTURE_FILTER_ANISOTROPIC_4X | 3 | Anisotropic filtering 4x
TEXTURE_FILTER_ANISOTROPIC_8X | 4 | Anisotropic filtering 8x
TEXTURE_FILTER_ANISOTROPIC_16X | 5 | Anisotropic filtering 16x

### TextureWrap enumeration

Members
Name | Value | Description
-----|-------|------------
TEXTURE_WRAP_REPEAT | 0 | Repeats texture in tiled mode
TEXTURE_WRAP_CLAMP | 1 | Clamps texture to edge pixel in tiled mode
TEXTURE_WRAP_MIRROR_REPEAT | 2 | Mirrors and repeats the texture in tiled mode
TEXTURE_WRAP_MIRROR_CLAMP | 3 | Mirrors and clamps to border the texture in tiled mode

### CubemapLayout enumeration

Members
Name | Value | Description
-----|-------|------------
CUBEMAP_LAYOUT_AUTO_DETECT | 0 | Automatically detect layout type
CUBEMAP_LAYOUT_LINE_VERTICAL | 1 | Layout is defined by a vertical line with faces
CUBEMAP_LAYOUT_LINE_HORIZONTAL | 2 | Layout is defined by an horizontal line with faces
CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR | 3 | Layout is defined by a 3x4 cross with cubemap faces
CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE | 4 | Layout is defined by a 4x3 cross with cubemap faces
CUBEMAP_LAYOUT_PANORAMA | 5 | Layout is defined by a panorama image (equirectangular map)

### FontType enumeration

Members
Name | Value | Description
-----|-------|------------
FONT_DEFAULT | 0 | Default font generation, anti-aliased
FONT_BITMAP | 1 | Bitmap font generation, no anti-aliasing
FONT_SDF | 2 | SDF font generation, requires external shader

### BlendMode enumeration

Members
Name | Value | Description
-----|-------|------------
BLEND_ALPHA | 0 | Blend textures considering alpha (default)
BLEND_ADDITIVE | 1 | Blend textures adding colors
BLEND_MULTIPLIED | 2 | Blend textures multiplying colors
BLEND_ADD_COLORS | 3 | Blend textures adding colors (alternative)
BLEND_SUBTRACT_COLORS | 4 | Blend textures subtracting colors (alternative)
BLEND_ALPHA_PREMULTIPLY | 5 | Blend premultiplied textures considering alpha
BLEND_CUSTOM | 6 | Blend textures using custom src/dst factors (use rlSetBlendMode())

### Gesture enumeration

Members
Name | Value | Description
-----|-------|------------
GESTURE_NONE | 0 | No gesture
GESTURE_TAP | 1 | Tap gesture
GESTURE_DOUBLETAP | 2 | Double tap gesture
GESTURE_HOLD | 4 | Hold gesture
GESTURE_DRAG | 8 | Drag gesture
GESTURE_SWIPE_RIGHT | 16 | Swipe right gesture
GESTURE_SWIPE_LEFT | 32 | Swipe left gesture
GESTURE_SWIPE_UP | 64 | Swipe up gesture
GESTURE_SWIPE_DOWN | 128 | Swipe down gesture
GESTURE_PINCH_IN | 256 | Pinch in gesture
GESTURE_PINCH_OUT | 512 | Pinch out gesture

### CameraMode enumeration

Members
Name | Value | Description
-----|-------|------------
CAMERA_CUSTOM | 0 | Custom camera
CAMERA_FREE | 1 | Free camera
CAMERA_ORBITAL | 2 | Orbital camera
CAMERA_FIRST_PERSON | 3 | First person camera
CAMERA_THIRD_PERSON | 4 | Third person camera

### CameraProjection enumeration

Members
Name | Value | Description
-----|-------|------------
CAMERA_PERSPECTIVE | 0 | Perspective projection
CAMERA_ORTHOGRAPHIC | 1 | Orthographic projection

### NPatchLayout enumeration

Members
Name | Value | Description
-----|-------|------------
NPATCH_NINE_PATCH | 0 | Npatch layout: 3x3 tiles
NPATCH_THREE_PATCH_VERTICAL | 1 | Npatch layout: 1x3 tiles
NPATCH_THREE_PATCH_HORIZONTAL | 2 | Npatch layout: 3x1 tiles


---
## Structures

### Vector2 structure
Vector2, 2 components

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
x | float | todo | todo
y | float | todo | todo


Classmethods:
Classmethod name | Bound API
-----------|---------
`Vector2.one()` | `vector2one()`


Methods:
Method name | Bound API
-----------|---------
`self.length()` | `vector2length()`
`self.length_sqr()` | `vector2length_sqr()`
`self.dot_product()` | `vector2dot_product()`
`self.distance()` | `vector2distance()`
`self.distance_sqr()` | `vector2distance_sqr()`
`self.angle()` | `vector2angle()`
`self.normalize()` | `vector2normalize()`
`self.transform()` | `vector2transform()`
`self.lerp()` | `vector2lerp()`
`self.reflect()` | `vector2reflect()`
`self.rotate()` | `vector2rotate()`
`self.move_towards()` | `vector2move_towards()`
`self.clamp()` | `vector2clamp()`
`self.clamp_value()` | `vector2clamp_value()`


Staticmethods:
_None._
### Vector3 structure
Vector3, 3 components

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
x | float | todo | todo
y | float | todo | todo
z | float | todo | todo


Classmethods:
Classmethod name | Bound API
-----------|---------
`Vector3.one()` | `vector3one()`


Methods:
Method name | Bound API
-----------|---------
`self.cross_product()` | `vector3cross_product()`
`self.perpendicular()` | `vector3perpendicular()`
`self.length()` | `vector3length()`
`self.length_sqr()` | `vector3length_sqr()`
`self.dot_product()` | `vector3dot_product()`
`self.distance()` | `vector3distance()`
`self.distance_sqr()` | `vector3distance_sqr()`
`self.angle()` | `vector3angle()`
`self.normalize()` | `vector3normalize()`
`self.ortho_normalize()` | `vector3ortho_normalize()`
`self.transform()` | `vector3transform()`
`self.rotate_by_quaternion()` | `vector3rotate_by_quaternion()`
`self.rotate_by_axis_angle()` | `vector3rotate_by_axis_angle()`
`self.lerp()` | `vector3lerp()`
`self.reflect()` | `vector3reflect()`
`self.min()` | `vector3min()`
`self.max()` | `vector3max()`
`self.barycenter()` | `vector3barycenter()`
`self.unproject()` | `vector3unproject()`
`self.to_float_v()` | `vector3to_float_v()`
`self.clamp()` | `vector3clamp()`
`self.clamp_value()` | `vector3clamp_value()`
`self.refract()` | `vector3refract()`


Staticmethods:
_None._
### Vector4 structure
Vector4, 4 components

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
x | float | todo | todo
y | float | todo | todo
z | float | todo | todo
w | float | todo | todo


Classmethods:
_None._

Methods:
_None._

Staticmethods:
_None._
### Matrix structure
Matrix, 4x4 components, column major, OpenGL style, right handed

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
m0 | float | todo | todo
m4 | float | todo | todo
m8 | float | todo | todo
m12 | float | todo | todo
m1 | float | todo | todo
m5 | float | todo | todo
m9 | float | todo | todo
m13 | float | todo | todo
m2 | float | todo | todo
m6 | float | todo | todo
m10 | float | todo | todo
m14 | float | todo | todo
m3 | float | todo | todo
m7 | float | todo | todo
m11 | float | todo | todo
m15 | float | todo | todo


Classmethods:
Classmethod name | Bound API
-----------|---------
`Matrix.identity()` | `matrix_identity()`
`Matrix.translate()` | `matrix_translate()`
`Matrix.rotate()` | `matrix_rotate()`
`Matrix.rotate_x()` | `matrix_rotate_x()`
`Matrix.rotate_y()` | `matrix_rotate_y()`
`Matrix.rotate_z()` | `matrix_rotate_z()`
`Matrix.rotate_xyz()` | `matrix_rotate_xyz()`
`Matrix.rotate_zyx()` | `matrix_rotate_zyx()`
`Matrix.scale()` | `matrix_scale()`
`Matrix.frustum()` | `matrix_frustum()`
`Matrix.perspective()` | `matrix_perspective()`
`Matrix.ortho()` | `matrix_ortho()`
`Matrix.look_at()` | `matrix_look_at()`


Methods:
Method name | Bound API
-----------|---------
`self.determinant()` | `matrix_determinant()`
`self.trace()` | `matrix_trace()`
`self.transpose()` | `matrix_transpose()`
`self.invert()` | `matrix_invert()`


Staticmethods:
_None._
### Color structure
Color, 4 components, R8G8B8A8 (32bit)

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
r | int | todo | todo
g | int | todo | todo
b | int | todo | todo
a | int | todo | todo


Classmethods:
_None._

Methods:
Method name | Bound API
-----------|---------
`self.fade()` | `fade()`
`self.to_int()` | `color_to_int()`
`self.to_hsv()` | `color_to_hsv()`
`self.from_hsv()` | `color_from_hsv()`
`self.alpha()` | `color_alpha()`
`self.alpha_blend()` | `color_alpha_blend()`


Staticmethods:
_None._
### Rectangle structure
Rectangle, 4 components

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
x | float | todo | todo
y | float | todo | todo
width | float | todo | todo
height | float | todo | todo


Classmethods:
_None._

Methods:
_None._

Staticmethods:
_None._
### Image structure
Image, pixel data stored in CPU memory (RAM)

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
data | bytes | todo | todo
width | int | todo | todo
height | int | todo | todo
mipmaps | int | todo | todo
format | int | todo | todo


Classmethods:
Classmethod name | Bound API
-----------|---------
`Image.load()` | `load_image()`
`Image.load_raw()` | `load_image_raw()`
`Image.load_anim()` | `load_image_anim()`
`Image.load_from_memory()` | `load_image_from_memory()`
`Image.load_from_texture()` | `load_image_from_texture()`
`Image.load_from_screen()` | `load_image_from_screen()`
`Image.gen_color()` | `gen_image_color()`
`Image.gen_gradient_h()` | `gen_image_gradient_h()`
`Image.gen_gradient_v()` | `gen_image_gradient_v()`
`Image.gen_gradient_radial()` | `gen_image_gradient_radial()`
`Image.gen_checked()` | `gen_image_checked()`
`Image.gen_white_noise()` | `gen_image_white_noise()`
`Image.gen_cellular()` | `gen_image_cellular()`
`Image.from_image()` | `image_from_image()`
`Image.text()` | `image_text()`
`Image.text_ex()` | `image_text_ex()`


Methods:
Method name | Bound API
-----------|---------
`self.unload()` | `unload_image()`
`self.export()` | `export_image()`
`self.export_as_code()` | `export_image_as_code()`
`self.copy()` | `image_copy()`
`self.format()` | `image_format()`
`self.to_pot()` | `image_to_pot()`
`self.crop()` | `image_crop()`
`self.alpha_crop()` | `image_alpha_crop()`
`self.alpha_clear()` | `image_alpha_clear()`
`self.alpha_mask()` | `image_alpha_mask()`
`self.alpha_premultiply()` | `image_alpha_premultiply()`
`self.resize()` | `image_resize()`
`self.resize_nn()` | `image_resize_nn()`
`self.resize_canvas()` | `image_resize_canvas()`
`self.mipmaps()` | `image_mipmaps()`
`self.dither()` | `image_dither()`
`self.flip_vertical()` | `image_flip_vertical()`
`self.flip_horizontal()` | `image_flip_horizontal()`
`self.rotate_cw()` | `image_rotate_cw()`
`self.rotate_ccw()` | `image_rotate_ccw()`
`self.color_tint()` | `image_color_tint()`
`self.color_invert()` | `image_color_invert()`
`self.color_grayscale()` | `image_color_grayscale()`
`self.color_contrast()` | `image_color_contrast()`
`self.color_brightness()` | `image_color_brightness()`
`self.color_replace()` | `image_color_replace()`
`self.clear_background()` | `image_clear_background()`
`self.draw_pixel()` | `image_draw_pixel()`
`self.draw_pixel_v()` | `image_draw_pixel_v()`
`self.draw_line()` | `image_draw_line()`
`self.draw_line_v()` | `image_draw_line_v()`
`self.draw_circle()` | `image_draw_circle()`
`self.draw_circle_v()` | `image_draw_circle_v()`
`self.draw_rectangle()` | `image_draw_rectangle()`
`self.draw_rectangle_v()` | `image_draw_rectangle_v()`
`self.draw_rectangle_rec()` | `image_draw_rectangle_rec()`
`self.draw_rectangle_lines()` | `image_draw_rectangle_lines()`
`self.draw()` | `image_draw()`
`self.draw_text()` | `image_draw_text()`
`self.draw_text_ex()` | `image_draw_text_ex()`
`self.load_colors()` | `load_image_colors()`
`self.load_palette()` | `load_image_palette()`
`self.get_alpha_border()` | `get_image_alpha_border()`
`self.get_color()` | `get_image_color()`
`Image.unload_colors()` | `unload_image_colors()`
`Image.unload_palette()` | `unload_image_palette()`


Staticmethods:
Method name | Bound API
-----------|---------

### Texture structure
Texture, tex data stored in GPU memory (VRAM)

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
id | int | todo | todo
width | int | todo | todo
height | int | todo | todo
mipmaps | int | todo | todo
format | int | todo | todo


Classmethods:
_None._

Methods:
_None._

Staticmethods:
_None._
### RenderTexture structure
RenderTexture, fbo for texture rendering

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
id | int | todo | todo
texture | Texture | todo | todo
depth | Texture | todo | todo


Classmethods:
_None._

Methods:
_None._

Staticmethods:
_None._
### NPatchInfo structure
NPatchInfo, n-patch layout info

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
source | Rectangle | todo | todo
left | int | todo | todo
top | int | todo | todo
right | int | todo | todo
bottom | int | todo | todo
layout | int | todo | todo


Classmethods:
_None._

Methods:
_None._

Staticmethods:
_None._
### GlyphInfo structure
GlyphInfo, font characters glyphs info

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
value | int | todo | todo
offsetX | int | todo | todo
offsetY | int | todo | todo
advanceX | int | todo | todo
image | Image | todo | todo


Classmethods:
_None._

Methods:
_None._

Staticmethods:
_None._
### Font structure
Font, font texture and GlyphInfo array data

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
baseSize | int | todo | todo
glyphCount | int | todo | todo
glyphPadding | int | todo | todo
texture | Texture2D | todo | todo
recs | RectanglePtr | todo | todo
glyphs | GlyphInfoPtr | todo | todo


Classmethods:
Classmethod name | Bound API
-----------|---------
`Font.load()` | `load_font()`
`Font.load_ex()` | `load_font_ex()`
`Font.load_from_image()` | `load_font_from_image()`
`Font.load_from_memory()` | `load_font_from_memory()`


Methods:
Method name | Bound API
-----------|---------
`self.unload()` | `unload_font()`
`self.draw_text_ex()` | `draw_text_ex()`
`self.draw_text_pro()` | `draw_text_pro()`
`self.draw_text_codepoint()` | `draw_text_codepoint()`
`self.draw_text_codepoints()` | `draw_text_codepoints()`
`self.measure_text_ex()` | `measure_text_ex()`
`self.get_glyph_index()` | `get_glyph_index()`
`self.get_glyph_info()` | `get_glyph_info()`
`self.get_glyph_atlas_rec()` | `get_glyph_atlas_rec()`
`Font.load_data()` | `load_font_data()`
`Font.unload_data()` | `unload_font_data()`


Staticmethods:
Method name | Bound API
-----------|---------

### Camera3D structure
Camera, defines position/orientation in 3d space

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
position | Vector3 | todo | todo
target | Vector3 | todo | todo
up | Vector3 | todo | todo
fovy | float | todo | todo
projection | int | todo | todo


Classmethods:
_None._

Methods:
Method name | Bound API
-----------|---------
`self.set_mode()` | `set_camera_mode()`


Staticmethods:
_None._
### Camera2D structure
Camera2D, defines position/orientation in 2d space

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
offset | Vector2 | todo | todo
target | Vector2 | todo | todo
rotation | float | todo | todo
zoom | float | todo | todo


Classmethods:
_None._

Methods:
_None._

Staticmethods:
_None._
### Mesh structure
Mesh, vertex data and vao/vbo

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
vertexCount | int | todo | todo
triangleCount | int | todo | todo
vertices | Sequence[float] | todo | todo
texcoords | Sequence[float] | todo | todo
texcoords2 | Sequence[float] | todo | todo
normals | Sequence[float] | todo | todo
tangents | Sequence[float] | todo | todo
colors | bytes | todo | todo
indices | Sequence[int] | todo | todo
animVertices | Sequence[float] | todo | todo
animNormals | Sequence[float] | todo | todo
boneIds | bytes | todo | todo
boneWeights | Sequence[float] | todo | todo
vaoId | int | todo | todo
vboId | Sequence[int] | todo | todo


Classmethods:
Classmethod name | Bound API
-----------|---------
`Mesh.gen_poly()` | `gen_mesh_poly()`
`Mesh.gen_plane()` | `gen_mesh_plane()`
`Mesh.gen_cube()` | `gen_mesh_cube()`
`Mesh.gen_sphere()` | `gen_mesh_sphere()`
`Mesh.gen_hemi_sphere()` | `gen_mesh_hemi_sphere()`
`Mesh.gen_cylinder()` | `gen_mesh_cylinder()`
`Mesh.gen_cone()` | `gen_mesh_cone()`
`Mesh.gen_torus()` | `gen_mesh_torus()`
`Mesh.gen_knot()` | `gen_mesh_knot()`
`Mesh.gen_heightmap()` | `gen_mesh_heightmap()`
`Mesh.gen_cubicmap()` | `gen_mesh_cubicmap()`


Methods:
Method name | Bound API
-----------|---------
`self.upload()` | `upload_mesh()`
`self.update_buffer()` | `update_mesh_buffer()`
`self.unload()` | `unload_mesh()`
`self.draw()` | `draw_mesh()`
`self.draw_instanced()` | `draw_mesh_instanced()`
`self.export()` | `export_mesh()`
`self.get_bounding_box()` | `get_mesh_bounding_box()`
`self.gen_tangents()` | `gen_mesh_tangents()`


Staticmethods:
_None._
### Shader structure
Shader

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
id | int | todo | todo
locs | Sequence[int] | todo | todo


Classmethods:
Classmethod name | Bound API
-----------|---------
`Shader.load()` | `load_shader()`
`Shader.load_from_memory()` | `load_shader_from_memory()`


Methods:
Method name | Bound API
-----------|---------
`self.get_location()` | `get_shader_location()`
`self.get_location_attrib()` | `get_shader_location_attrib()`
`self.set_value()` | `set_shader_value()`
`self.set_value_v()` | `set_shader_value_v()`
`self.set_value_matrix()` | `set_shader_value_matrix()`
`self.set_value_texture()` | `set_shader_value_texture()`
`self.unload()` | `unload_shader()`


Staticmethods:
_None._
### MaterialMap structure
MaterialMap

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
texture | Texture2D | todo | todo
color | Color | todo | todo
value | float | todo | todo


Classmethods:
_None._

Methods:
_None._

Staticmethods:
_None._
### Material structure
Material, includes shader and maps

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
shader | Shader | todo | todo
maps | MaterialMapPtr | todo | todo
params | Sequence[float] | todo | todo


Classmethods:
Classmethod name | Bound API
-----------|---------
`Material.load_materials()` | `load_materials()`
`Material.load_default()` | `load_material_default()`


Methods:
Method name | Bound API
-----------|---------
`self.unload()` | `unload_material()`
`self.set_texture()` | `set_material_texture()`


Staticmethods:
_None._
### Transform structure
Transform, vectex transformation data

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
translation | Vector3 | todo | todo
rotation | Quaternion | todo | todo
scale | Vector3 | todo | todo


Classmethods:
_None._

Methods:
_None._

Staticmethods:
_None._
### BoneInfo structure
Bone, skeletal animation bone

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
name | Sequence[bytes] | todo | todo
parent | int | todo | todo


Classmethods:
_None._

Methods:
_None._

Staticmethods:
_None._
### Model structure
Model, meshes, materials and animation data

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
transform | Matrix | todo | todo
meshCount | int | todo | todo
materialCount | int | todo | todo
meshes | MeshPtr | todo | todo
materials | MaterialPtr | todo | todo
meshMaterial | Sequence[int] | todo | todo
boneCount | int | todo | todo
bones | BoneInfoPtr | todo | todo
bindPose | TransformPtr | todo | todo


Classmethods:
Classmethod name | Bound API
-----------|---------
`Model.load()` | `load_model()`
`Model.load_from_mesh()` | `load_model_from_mesh()`


Methods:
Method name | Bound API
-----------|---------
`self.is_animation_valid()` | `is_model_animation_valid()`
`self.update_animation()` | `update_model_animation()`
`self.set_mesh_material()` | `set_model_mesh_material()`
`self.unload()` | `unload_model()`
`self.unload_keep_meshes()` | `unload_model_keep_meshes()`
`self.get_bounding_box()` | `get_model_bounding_box()`
`self.draw()` | `draw_model()`
`self.draw_ex()` | `draw_model_ex()`
`self.draw_wires()` | `draw_model_wires()`
`self.draw_wires_ex()` | `draw_model_wires_ex()`


Staticmethods:
_None._
### ModelAnimation structure
ModelAnimation

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
boneCount | int | todo | todo
frameCount | int | todo | todo
bones | BoneInfoPtr | todo | todo
framePoses | Sequence[TransformPtr] | todo | todo


Classmethods:
_None._

Methods:
_None._

Staticmethods:
_None._
### Ray structure
Ray, ray for raycasting

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
position | Vector3 | todo | todo
direction | Vector3 | todo | todo


Classmethods:
_None._

Methods:
_None._

Staticmethods:
_None._
### RayCollision structure
RayCollision, ray hit information

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
hit | bool | todo | todo
distance | float | todo | todo
point | Vector3 | todo | todo
normal | Vector3 | todo | todo


Classmethods:
_None._

Methods:
_None._

Staticmethods:
_None._
### BoundingBox structure
BoundingBox

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
min | Vector3 | todo | todo
max | Vector3 | todo | todo


Classmethods:
_None._

Methods:
_None._

Staticmethods:
_None._
### Wave structure
Wave, audio wave data

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
frameCount | int | todo | todo
sampleRate | int | todo | todo
sampleSize | int | todo | todo
channels | int | todo | todo
data | bytes | todo | todo


Classmethods:
Classmethod name | Bound API
-----------|---------
`Wave.load()` | `load_wave()`
`Wave.load_from_memory()` | `load_wave_from_memory()`


Methods:
Method name | Bound API
-----------|---------
`self.copy()` | `wave_copy()`
`self.crop()` | `wave_crop()`
`self.format()` | `wave_format()`
`self.format()` | `load_wave_samples()`
`self.export()` | `export_wave()`
`self.export_as_code()` | `export_wave_as_code()`
`self.unload()` | `unload_wave()`
`self.unload_samples()` | `unload_wave_samples()`


Staticmethods:
_None._
### AudioStream structure
AudioStream, custom audio stream

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
buffer | bytes | todo | todo
processor | bytes | todo | todo
sampleRate | int | todo | todo
sampleSize | int | todo | todo
channels | int | todo | todo


Classmethods:
Classmethod name | Bound API
-----------|---------
`AudioStream.load()` | `load_audio_stream()`


Methods:
Method name | Bound API
-----------|---------
`self.unload()` | `unload_audio_stream()`
`self.update()` | `update_audio_stream()`
`self.is_processed()` | `is_audio_stream_processed()`
`self.play()` | `play_audio_stream()`
`self.pause()` | `pause_audio_stream()`
`self.resume()` | `resume_audio_stream()`
`self.is_playing()` | `is_audio_stream_playing()`
`self.stop()` | `stop_audio_stream()`
`self.set_volume()` | `set_audio_stream_volume()`
`self.set_pitch()` | `set_audio_stream_pitch()`
`self.set_pan()` | `set_audio_stream_pan()`
`self.set_buffer_size_default()` | `set_audio_stream_buffer_size_default()`
`self.set_callback()` | `set_audio_stream_callback()`
`self.attach_processor()` | `attach_audio_stream_processor()`
`self.detach_processor()` | `detach_audio_stream_processor()`


Staticmethods:
_None._
### Sound structure
Sound

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
stream | AudioStream | todo | todo
frameCount | int | todo | todo


Classmethods:
Classmethod name | Bound API
-----------|---------
`Sound.load()` | `load_sound()`
`Sound.load_from_wave()` | `load_sound_from_wave()`


Methods:
Method name | Bound API
-----------|---------
`self.play()` | `play_sound()`
`self.stop()` | `stop_sound()`
`self.pause()` | `pause_sound()`
`self.resume()` | `resume_sound()`
`self.play_multi()` | `play_sound_multi()`
`self.is_playing()` | `is_sound_playing()`
`self.set_volume()` | `set_sound_volume()`
`self.set_pitch()` | `set_sound_pitch()`
`self.set_pan()` | `set_sound_pan()`
`self.unload()` | `unload_sound()`
`self.update()` | `update_sound()`
`Sound.get_sounds_playing()` | `get_sounds_playing()`
`Sound.stop_multi()` | `stop_sound_multi()`


Staticmethods:
Method name | Bound API
-----------|---------

### Music structure
Music, audio stream, anything longer than ~10 seconds should be streamed

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
stream | AudioStream | todo | todo
frameCount | int | todo | todo
looping | bool | todo | todo
ctxType | int | todo | todo
ctxData | bytes | todo | todo


Classmethods:
_None._

Methods:
Method name | Bound API
-----------|---------
`self.play()` | `play_music_stream()`
`self.is_playing()` | `is_music_stream_playing()`
`self.update()` | `update_music_stream()`
`self.stop()` | `stop_music_stream()`
`self.pause()` | `pause_music_stream()`
`self.resume()` | `resume_music_stream()`
`self.seek()` | `seek_music_stream()`
`self.set_volume()` | `set_music_volume()`
`self.set_pitch()` | `set_music_pitch()`
`self.set_pan()` | `set_music_pan()`
`self.get_time_length()` | `get_music_time_length()`
`self.get_time_played()` | `get_music_time_played()`
`Music.load()` | `load_music_stream()`
`Music.load_from_memory()` | `load_music_stream_from_memory()`


Staticmethods:
Method name | Bound API
-----------|---------

### VrDeviceInfo structure
VrDeviceInfo, Head-Mounted-Display device parameters

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
hResolution | int | todo | todo
vResolution | int | todo | todo
hScreenSize | float | todo | todo
vScreenSize | float | todo | todo
vScreenCenter | float | todo | todo
eyeToScreenDistance | float | todo | todo
lensSeparationDistance | float | todo | todo
interpupillaryDistance | float | todo | todo
lensDistortionValues | Sequence[float] | todo | todo
chromaAbCorrection | Sequence[float] | todo | todo


Classmethods:
_None._

Methods:
_None._

Staticmethods:
_None._
### VrStereoConfig structure
VrStereoConfig, VR stereo rendering configuration for simulator

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
projection | Sequence[Matrix] | todo | todo
viewOffset | Sequence[Matrix] | todo | todo
leftLensCenter | Sequence[float] | todo | todo
rightLensCenter | Sequence[float] | todo | todo
leftScreenCenter | Sequence[float] | todo | todo
rightScreenCenter | Sequence[float] | todo | todo
scale | Sequence[float] | todo | todo
scaleIn | Sequence[float] | todo | todo


Classmethods:
_None._

Methods:
_None._

Staticmethods:
_None._
### FilePathList structure
File path list

Fields:
Name | Type (Python) | Type (CTypes) | Type (C)
-----|---------------|---------------|---------
capacity | int | todo | todo
count | int | todo | todo
paths | Sequence[bytes] | todo | todo


Classmethods:
_None._

Methods:
_None._

Staticmethods:
_None._

---
## Functions

### init_window
Initialize window and OpenGL context

Python signature:
```python
def init_window(width: int, height: int, title: bytes) -> None
```

C API:
```c
None InitWindow(int width, int height, const char *title)
```

### window_should_close
Check if KEY_ESCAPE pressed or Close icon pressed

Python signature:
```python
def window_should_close() -> bool
```

C API:
```c
Bool WindowShouldClose()
```

### close_window
Close window and unload OpenGL context

Python signature:
```python
def close_window() -> None
```

C API:
```c
None CloseWindow()
```

### is_window_ready
Check if window has been initialized successfully

Python signature:
```python
def is_window_ready() -> bool
```

C API:
```c
Bool IsWindowReady()
```

### is_window_fullscreen
Check if window is currently fullscreen

Python signature:
```python
def is_window_fullscreen() -> bool
```

C API:
```c
Bool IsWindowFullscreen()
```

### is_window_hidden
Check if window is currently hidden (only PLATFORM_DESKTOP)

Python signature:
```python
def is_window_hidden() -> bool
```

C API:
```c
Bool IsWindowHidden()
```

### is_window_minimized
Check if window is currently minimized (only PLATFORM_DESKTOP)

Python signature:
```python
def is_window_minimized() -> bool
```

C API:
```c
Bool IsWindowMinimized()
```

### is_window_maximized
Check if window is currently maximized (only PLATFORM_DESKTOP)

Python signature:
```python
def is_window_maximized() -> bool
```

C API:
```c
Bool IsWindowMaximized()
```

### is_window_focused
Check if window is currently focused (only PLATFORM_DESKTOP)

Python signature:
```python
def is_window_focused() -> bool
```

C API:
```c
Bool IsWindowFocused()
```

### is_window_resized
Check if window has been resized last frame

Python signature:
```python
def is_window_resized() -> bool
```

C API:
```c
Bool IsWindowResized()
```

### is_window_state
Check if one specific window flag is enabled

Python signature:
```python
def is_window_state(flag: int) -> bool
```

C API:
```c
Bool IsWindowState(unsigned int flag)
```

### set_window_state
Set window configuration state using flags (only PLATFORM_DESKTOP)

Python signature:
```python
def set_window_state(flags: int) -> None
```

C API:
```c
None SetWindowState(unsigned int flags)
```

### clear_window_state
Clear window configuration state flags

Python signature:
```python
def clear_window_state(flags: int) -> None
```

C API:
```c
None ClearWindowState(unsigned int flags)
```

### toggle_fullscreen
Toggle window state: fullscreen/windowed (only PLATFORM_DESKTOP)

Python signature:
```python
def toggle_fullscreen() -> None
```

C API:
```c
None ToggleFullscreen()
```

### maximize_window
Set window state: maximized, if resizable (only PLATFORM_DESKTOP)

Python signature:
```python
def maximize_window() -> None
```

C API:
```c
None MaximizeWindow()
```

### minimize_window
Set window state: minimized, if resizable (only PLATFORM_DESKTOP)

Python signature:
```python
def minimize_window() -> None
```

C API:
```c
None MinimizeWindow()
```

### restore_window
Set window state: not minimized/maximized (only PLATFORM_DESKTOP)

Python signature:
```python
def restore_window() -> None
```

C API:
```c
None RestoreWindow()
```

### set_window_icon
Set icon for window (only PLATFORM_DESKTOP)

Python signature:
```python
def set_window_icon(image: Image) -> None
```

C API:
```c
None SetWindowIcon(Image image)
```

### set_window_title
Set title for window (only PLATFORM_DESKTOP)

Python signature:
```python
def set_window_title(title: bytes) -> None
```

C API:
```c
None SetWindowTitle(const char *title)
```

### set_window_position
Set window position on screen (only PLATFORM_DESKTOP)

Python signature:
```python
def set_window_position(x: int, y: int) -> None
```

C API:
```c
None SetWindowPosition(int x, int y)
```

### set_window_monitor
Set monitor for the current window (fullscreen mode)

Python signature:
```python
def set_window_monitor(monitor: int) -> None
```

C API:
```c
None SetWindowMonitor(int monitor)
```

### set_window_min_size
Set window minimum dimensions (for FLAG_WINDOW_RESIZABLE)

Python signature:
```python
def set_window_min_size(width: int, height: int) -> None
```

C API:
```c
None SetWindowMinSize(int width, int height)
```

### set_window_size
Set window dimensions

Python signature:
```python
def set_window_size(width: int, height: int) -> None
```

C API:
```c
None SetWindowSize(int width, int height)
```

### set_window_opacity
Set window opacity [0.0f..1.0f] (only PLATFORM_DESKTOP)

Python signature:
```python
def set_window_opacity(opacity: float) -> None
```

C API:
```c
None SetWindowOpacity(float opacity)
```

### get_window_handle
Get native window handle

Python signature:
```python
def get_window_handle() -> bytes
```

C API:
```c
VoidPtr GetWindowHandle()
```

### get_screen_width
Get current screen width

Python signature:
```python
def get_screen_width() -> int
```

C API:
```c
Int GetScreenWidth()
```

### get_screen_height
Get current screen height

Python signature:
```python
def get_screen_height() -> int
```

C API:
```c
Int GetScreenHeight()
```

### get_render_width
Get current render width (it considers HiDPI)

Python signature:
```python
def get_render_width() -> int
```

C API:
```c
Int GetRenderWidth()
```

### get_render_height
Get current render height (it considers HiDPI)

Python signature:
```python
def get_render_height() -> int
```

C API:
```c
Int GetRenderHeight()
```

### get_monitor_count
Get number of connected monitors

Python signature:
```python
def get_monitor_count() -> int
```

C API:
```c
Int GetMonitorCount()
```

### get_current_monitor
Get current connected monitor

Python signature:
```python
def get_current_monitor() -> int
```

C API:
```c
Int GetCurrentMonitor()
```

### get_monitor_position
Get specified monitor position

Python signature:
```python
def get_monitor_position(monitor: int) -> Vector2
```

C API:
```c
Vector2 GetMonitorPosition(int monitor)
```

### get_monitor_width
Get specified monitor width (current video mode used by monitor)

Python signature:
```python
def get_monitor_width(monitor: int) -> int
```

C API:
```c
Int GetMonitorWidth(int monitor)
```

### get_monitor_height
Get specified monitor height (current video mode used by monitor)

Python signature:
```python
def get_monitor_height(monitor: int) -> int
```

C API:
```c
Int GetMonitorHeight(int monitor)
```

### get_monitor_physical_width
Get specified monitor physical width in millimetres

Python signature:
```python
def get_monitor_physical_width(monitor: int) -> int
```

C API:
```c
Int GetMonitorPhysicalWidth(int monitor)
```

### get_monitor_physical_height
Get specified monitor physical height in millimetres

Python signature:
```python
def get_monitor_physical_height(monitor: int) -> int
```

C API:
```c
Int GetMonitorPhysicalHeight(int monitor)
```

### get_monitor_refresh_rate
Get specified monitor refresh rate

Python signature:
```python
def get_monitor_refresh_rate(monitor: int) -> int
```

C API:
```c
Int GetMonitorRefreshRate(int monitor)
```

### get_window_position
Get window position XY on monitor

Python signature:
```python
def get_window_position() -> Vector2
```

C API:
```c
Vector2 GetWindowPosition()
```

### get_window_scale_dpi
Get window scale DPI factor

Python signature:
```python
def get_window_scale_dpi() -> Vector2
```

C API:
```c
Vector2 GetWindowScaleDPI()
```

### get_monitor_name
Get the human-readable, UTF-8 encoded name of the primary monitor

Python signature:
```python
def get_monitor_name(monitor: int) -> bytes
```

C API:
```c
CharPtr GetMonitorName(int monitor)
```

### set_clipboard_text
Set clipboard text content

Python signature:
```python
def set_clipboard_text(text: bytes) -> None
```

C API:
```c
None SetClipboardText(const char *text)
```

### get_clipboard_text
Get clipboard text content

Python signature:
```python
def get_clipboard_text() -> bytes
```

C API:
```c
CharPtr GetClipboardText()
```

### enable_event_waiting
Enable waiting for events on EndDrawing(), no automatic event polling

Python signature:
```python
def enable_event_waiting() -> None
```

C API:
```c
None EnableEventWaiting()
```

### disable_event_waiting
Disable waiting for events on EndDrawing(), automatic events polling

Python signature:
```python
def disable_event_waiting() -> None
```

C API:
```c
None DisableEventWaiting()
```

### swap_screen_buffer
Swap back buffer with front buffer (screen drawing)

Python signature:
```python
def swap_screen_buffer() -> None
```

C API:
```c
None SwapScreenBuffer()
```

### poll_input_events
Register all input events

Python signature:
```python
def poll_input_events() -> None
```

C API:
```c
None PollInputEvents()
```

### wait_time
Wait for some time (halt program execution)

Python signature:
```python
def wait_time(seconds: float) -> None
```

C API:
```c
None WaitTime(double seconds)
```

### show_cursor
Shows cursor

Python signature:
```python
def show_cursor() -> None
```

C API:
```c
None ShowCursor()
```

### hide_cursor
Hides cursor

Python signature:
```python
def hide_cursor() -> None
```

C API:
```c
None HideCursor()
```

### is_cursor_hidden
Check if cursor is not visible

Python signature:
```python
def is_cursor_hidden() -> bool
```

C API:
```c
Bool IsCursorHidden()
```

### enable_cursor
Enables cursor (unlock cursor)

Python signature:
```python
def enable_cursor() -> None
```

C API:
```c
None EnableCursor()
```

### disable_cursor
Disables cursor (lock cursor)

Python signature:
```python
def disable_cursor() -> None
```

C API:
```c
None DisableCursor()
```

### is_cursor_on_screen
Check if cursor is on the screen

Python signature:
```python
def is_cursor_on_screen() -> bool
```

C API:
```c
Bool IsCursorOnScreen()
```

### clear_background
Set background color (framebuffer clear color)

Python signature:
```python
def clear_background(color: Color) -> None
```

C API:
```c
None ClearBackground(Color color)
```

### begin_drawing
Setup canvas (framebuffer) to start drawing

Python signature:
```python
def begin_drawing() -> None
```

C API:
```c
None BeginDrawing()
```

### end_drawing
End canvas drawing and swap buffers (double buffering)

Python signature:
```python
def end_drawing() -> None
```

C API:
```c
None EndDrawing()
```

### begin_mode2d
Begin 2D mode with custom camera (2D)

Python signature:
```python
def begin_mode2d(camera: Camera2D) -> None
```

C API:
```c
None BeginMode2D(Camera2D camera)
```

### end_mode2d
Ends 2D mode with custom camera

Python signature:
```python
def end_mode2d() -> None
```

C API:
```c
None EndMode2D()
```

### begin_mode3d
Begin 3D mode with custom camera (3D)

Python signature:
```python
def begin_mode3d(camera: Camera3D) -> None
```

C API:
```c
None BeginMode3D(Camera3D camera)
```

### end_mode3d
Ends 3D mode and returns to default 2D orthographic mode

Python signature:
```python
def end_mode3d() -> None
```

C API:
```c
None EndMode3D()
```

### begin_texture_mode
Begin drawing to render texture

Python signature:
```python
def begin_texture_mode(target: RenderTexture2D) -> None
```

C API:
```c
None BeginTextureMode(RenderTexture2D target)
```

### end_texture_mode
Ends drawing to render texture

Python signature:
```python
def end_texture_mode() -> None
```

C API:
```c
None EndTextureMode()
```

### begin_shader_mode
Begin custom shader drawing

Python signature:
```python
def begin_shader_mode(shader: Shader) -> None
```

C API:
```c
None BeginShaderMode(Shader shader)
```

### end_shader_mode
End custom shader drawing (use default shader)

Python signature:
```python
def end_shader_mode() -> None
```

C API:
```c
None EndShaderMode()
```

### begin_blend_mode
Begin blending mode (alpha, additive, multiplied, subtract, custom)

Python signature:
```python
def begin_blend_mode(mode: int) -> None
```

C API:
```c
None BeginBlendMode(int mode)
```

### end_blend_mode
End blending mode (reset to default: alpha blending)

Python signature:
```python
def end_blend_mode() -> None
```

C API:
```c
None EndBlendMode()
```

### begin_scissor_mode
Begin scissor mode (define screen area for following drawing)

Python signature:
```python
def begin_scissor_mode(x: int, y: int, width: int, height: int) -> None
```

C API:
```c
None BeginScissorMode(int x, int y, int width, int height)
```

### end_scissor_mode
End scissor mode

Python signature:
```python
def end_scissor_mode() -> None
```

C API:
```c
None EndScissorMode()
```

### begin_vr_stereo_mode
Begin stereo rendering (requires VR simulator)

Python signature:
```python
def begin_vr_stereo_mode(config: VrStereoConfig) -> None
```

C API:
```c
None BeginVrStereoMode(VrStereoConfig config)
```

### end_vr_stereo_mode
End stereo rendering (requires VR simulator)

Python signature:
```python
def end_vr_stereo_mode() -> None
```

C API:
```c
None EndVrStereoMode()
```

### load_vr_stereo_config
Load VR stereo config for VR simulator device parameters

Python signature:
```python
def load_vr_stereo_config(device: VrDeviceInfo) -> VrStereoConfig
```

C API:
```c
VrStereoConfig LoadVrStereoConfig(VrDeviceInfo device)
```

### unload_vr_stereo_config
Unload VR stereo config

Python signature:
```python
def unload_vr_stereo_config(config: VrStereoConfig) -> None
```

C API:
```c
None UnloadVrStereoConfig(VrStereoConfig config)
```

### load_shader
Load shader from files and bind default locations

Python signature:
```python
def load_shader(vs_file_name: bytes, fs_file_name: bytes) -> Shader
```

C API:
```c
Shader LoadShader(const char *vsFileName, const char *fsFileName)
```

### load_shader_from_memory
Load shader from code strings and bind default locations

Python signature:
```python
def load_shader_from_memory(vs_code: bytes, fs_code: bytes) -> Shader
```

C API:
```c
Shader LoadShaderFromMemory(const char *vsCode, const char *fsCode)
```

### get_shader_location
Get shader uniform location

Python signature:
```python
def get_shader_location(shader: Shader, uniform_name: bytes) -> int
```

C API:
```c
Int GetShaderLocation(Shader shader, const char *uniformName)
```

### get_shader_location_attrib
Get shader attribute location

Python signature:
```python
def get_shader_location_attrib(shader: Shader, attrib_name: bytes) -> int
```

C API:
```c
Int GetShaderLocationAttrib(Shader shader, const char *attribName)
```

### set_shader_value
Set shader uniform value

Python signature:
```python
def set_shader_value(shader: Shader, loc_index: int, value: bytes, uniform_type: int) -> None
```

C API:
```c
None SetShaderValue(Shader shader, int locIndex, const void *value, int uniformType)
```

### set_shader_value_v
Set shader uniform value vector

Python signature:
```python
def set_shader_value_v(shader: Shader, loc_index: int, value: bytes, uniform_type: int, count: int) -> None
```

C API:
```c
None SetShaderValueV(Shader shader, int locIndex, const void *value, int uniformType, int count)
```

### set_shader_value_matrix
Set shader uniform value (matrix 4x4)

Python signature:
```python
def set_shader_value_matrix(shader: Shader, loc_index: int, mat: Matrix) -> None
```

C API:
```c
None SetShaderValueMatrix(Shader shader, int locIndex, Matrix mat)
```

### set_shader_value_texture
Set shader uniform value for texture (sampler2d)

Python signature:
```python
def set_shader_value_texture(shader: Shader, loc_index: int, texture: Texture2D) -> None
```

C API:
```c
None SetShaderValueTexture(Shader shader, int locIndex, Texture2D texture)
```

### unload_shader
Unload shader from GPU memory (VRAM)

Python signature:
```python
def unload_shader(shader: Shader) -> None
```

C API:
```c
None UnloadShader(Shader shader)
```

### get_mouse_ray
Get a ray trace from mouse position

Python signature:
```python
def get_mouse_ray(mouse_position: Vector2, camera: Camera) -> Ray
```

C API:
```c
Ray GetMouseRay(Vector2 mousePosition, Camera camera)
```

### get_camera_matrix
Get camera transform matrix (view matrix)

Python signature:
```python
def get_camera_matrix(camera: Camera) -> Matrix
```

C API:
```c
Matrix GetCameraMatrix(Camera camera)
```

### get_camera_matrix2d
Get camera 2d transform matrix

Python signature:
```python
def get_camera_matrix2d(camera: Camera2D) -> Matrix
```

C API:
```c
Matrix GetCameraMatrix2D(Camera2D camera)
```

### get_world_to_screen
Get the screen space position for a 3d world space position

Python signature:
```python
def get_world_to_screen(position: Vector3, camera: Camera) -> Vector2
```

C API:
```c
Vector2 GetWorldToScreen(Vector3 position, Camera camera)
```

### get_screen_to_world2d
Get the world space position for a 2d camera screen space position

Python signature:
```python
def get_screen_to_world2d(position: Vector2, camera: Camera2D) -> Vector2
```

C API:
```c
Vector2 GetScreenToWorld2D(Vector2 position, Camera2D camera)
```

### get_world_to_screen_ex
Get size position for a 3d world space position

Python signature:
```python
def get_world_to_screen_ex(position: Vector3, camera: Camera, width: int, height: int) -> Vector2
```

C API:
```c
Vector2 GetWorldToScreenEx(Vector3 position, Camera camera, int width, int height)
```

### get_world_to_screen2d
Get the screen space position for a 2d camera world space position

Python signature:
```python
def get_world_to_screen2d(position: Vector2, camera: Camera2D) -> Vector2
```

C API:
```c
Vector2 GetWorldToScreen2D(Vector2 position, Camera2D camera)
```

### set_target_fps
Set target FPS (maximum)

Python signature:
```python
def set_target_fps(fps: int) -> None
```

C API:
```c
None SetTargetFPS(int fps)
```

### get_fps
Get current FPS

Python signature:
```python
def get_fps() -> int
```

C API:
```c
Int GetFPS()
```

### get_frame_time
Get time in seconds for last frame drawn (delta time)

Python signature:
```python
def get_frame_time() -> float
```

C API:
```c
Float GetFrameTime()
```

### get_time
Get elapsed time in seconds since InitWindow()

Python signature:
```python
def get_time() -> float
```

C API:
```c
Double GetTime()
```

### get_random_value
Get a random value between min and max (both included)

Python signature:
```python
def get_random_value(min: int, max: int) -> int
```

C API:
```c
Int GetRandomValue(int min, int max)
```

### set_random_seed
Set the seed for the random number generator

Python signature:
```python
def set_random_seed(seed: int) -> None
```

C API:
```c
None SetRandomSeed(unsigned int seed)
```

### take_screenshot
Takes a screenshot of current screen (filename extension defines format)

Python signature:
```python
def take_screenshot(file_name: bytes) -> None
```

C API:
```c
None TakeScreenshot(const char *fileName)
```

### set_config_flags
Setup init configuration flags (view FLAGS)

Python signature:
```python
def set_config_flags(flags: int) -> None
```

C API:
```c
None SetConfigFlags(unsigned int flags)
```

### trace_log
Show trace log messages (LOG_DEBUG, LOG_INFO, LOG_WARNING, LOG_ERROR...)

Python signature:
```python
def trace_log(log_level: int, text: bytes, *args: bytes) -> None
```

C API:
```c
None TraceLog(int logLevel, const char *text, ... args)
```

### set_trace_log_level
Set the current threshold (minimum) log level

Python signature:
```python
def set_trace_log_level(log_level: int) -> None
```

C API:
```c
None SetTraceLogLevel(int logLevel)
```

### mem_alloc
Internal memory allocator

Python signature:
```python
def mem_alloc(size: int) -> bytes
```

C API:
```c
VoidPtr MemAlloc(int size)
```

### mem_realloc
Internal memory reallocator

Python signature:
```python
def mem_realloc(ptr: bytes, size: int) -> bytes
```

C API:
```c
VoidPtr MemRealloc(void *ptr, int size)
```

### mem_free
Internal memory free

Python signature:
```python
def mem_free(ptr: bytes) -> None
```

C API:
```c
None MemFree(void *ptr)
```

### open_url
Open URL with default system browser (if available)

Python signature:
```python
def open_url(url: bytes) -> None
```

C API:
```c
None OpenURL(const char *url)
```

### set_trace_log_callback
Set custom trace log

Python signature:
```python
def set_trace_log_callback(callback: TraceLogCallback) -> None
```

C API:
```c
None SetTraceLogCallback(TraceLogCallback callback)
```

### set_load_file_data_callback
Set custom file binary data loader

Python signature:
```python
def set_load_file_data_callback(callback: LoadFileDataCallback) -> None
```

C API:
```c
None SetLoadFileDataCallback(LoadFileDataCallback callback)
```

### set_save_file_data_callback
Set custom file binary data saver

Python signature:
```python
def set_save_file_data_callback(callback: SaveFileDataCallback) -> None
```

C API:
```c
None SetSaveFileDataCallback(SaveFileDataCallback callback)
```

### set_load_file_text_callback
Set custom file text data loader

Python signature:
```python
def set_load_file_text_callback(callback: LoadFileTextCallback) -> None
```

C API:
```c
None SetLoadFileTextCallback(LoadFileTextCallback callback)
```

### set_save_file_text_callback
Set custom file text data saver

Python signature:
```python
def set_save_file_text_callback(callback: SaveFileTextCallback) -> None
```

C API:
```c
None SetSaveFileTextCallback(SaveFileTextCallback callback)
```

### load_file_data
Load file data as byte array (read)

Python signature:
```python
def load_file_data(file_name: bytes, bytes_read: Sequence[int]) -> bytes
```

C API:
```c
UBytePtr LoadFileData(const char *fileName, unsigned int *bytesRead)
```

### unload_file_data
Unload file data allocated by LoadFileData()

Python signature:
```python
def unload_file_data(data: bytes) -> None
```

C API:
```c
None UnloadFileData(unsigned char *data)
```

### save_file_data
Save data to file from byte array (write), returns true on success

Python signature:
```python
def save_file_data(file_name: bytes, data: bytes, bytes_to_write: int) -> bool
```

C API:
```c
Bool SaveFileData(const char *fileName, void *data, unsigned int bytesToWrite)
```

### export_data_as_code
Export data to code (.h), returns true on success

Python signature:
```python
def export_data_as_code(data: bytes, size: int, file_name: bytes) -> bool
```

C API:
```c
Bool ExportDataAsCode(const char *data, unsigned int size, const char *fileName)
```

### load_file_text
Load text data from file (read), returns a '\0' terminated string

Python signature:
```python
def load_file_text(file_name: bytes) -> bytes
```

C API:
```c
CharPtr LoadFileText(const char *fileName)
```

### unload_file_text
Unload file text data allocated by LoadFileText()

Python signature:
```python
def unload_file_text(text: bytes) -> None
```

C API:
```c
None UnloadFileText(char *text)
```

### save_file_text
Save text data to file (write), string must be '\0' terminated, returns true on success

Python signature:
```python
def save_file_text(file_name: bytes, text: bytes) -> bool
```

C API:
```c
Bool SaveFileText(const char *fileName, char *text)
```

### file_exists
Check if file exists

Python signature:
```python
def file_exists(file_name: bytes) -> bool
```

C API:
```c
Bool FileExists(const char *fileName)
```

### directory_exists
Check if a directory path exists

Python signature:
```python
def directory_exists(dir_path: bytes) -> bool
```

C API:
```c
Bool DirectoryExists(const char *dirPath)
```

### is_file_extension
Check file extension (including point: .png, .wav)

Python signature:
```python
def is_file_extension(file_name: bytes, ext: bytes) -> bool
```

C API:
```c
Bool IsFileExtension(const char *fileName, const char *ext)
```

### get_file_length
Get file length in bytes (NOTE: GetFileSize() conflicts with windows.h)

Python signature:
```python
def get_file_length(file_name: bytes) -> int
```

C API:
```c
Int GetFileLength(const char *fileName)
```

### get_file_extension
Get pointer to extension for a filename string (includes dot: '.png')

Python signature:
```python
def get_file_extension(file_name: bytes) -> bytes
```

C API:
```c
CharPtr GetFileExtension(const char *fileName)
```

### get_file_name
Get pointer to filename for a path string

Python signature:
```python
def get_file_name(file_path: bytes) -> bytes
```

C API:
```c
CharPtr GetFileName(const char *filePath)
```

### get_file_name_without_ext
Get filename string without extension (uses static string)

Python signature:
```python
def get_file_name_without_ext(file_path: bytes) -> bytes
```

C API:
```c
CharPtr GetFileNameWithoutExt(const char *filePath)
```

### get_directory_path
Get full path for a given fileName with path (uses static string)

Python signature:
```python
def get_directory_path(file_path: bytes) -> bytes
```

C API:
```c
CharPtr GetDirectoryPath(const char *filePath)
```

### get_prev_directory_path
Get previous directory path for a given path (uses static string)

Python signature:
```python
def get_prev_directory_path(dir_path: bytes) -> bytes
```

C API:
```c
CharPtr GetPrevDirectoryPath(const char *dirPath)
```

### get_working_directory
Get current working directory (uses static string)

Python signature:
```python
def get_working_directory() -> bytes
```

C API:
```c
CharPtr GetWorkingDirectory()
```

### get_application_directory
Get the directory if the running application (uses static string)

Python signature:
```python
def get_application_directory() -> bytes
```

C API:
```c
CharPtr GetApplicationDirectory()
```

### change_directory
Change working directory, return true on success

Python signature:
```python
def change_directory(dir: bytes) -> bool
```

C API:
```c
Bool ChangeDirectory(const char *dir)
```

### is_path_file
Check if a given path is a file or a directory

Python signature:
```python
def is_path_file(path: bytes) -> bool
```

C API:
```c
Bool IsPathFile(const char *path)
```

### load_directory_files
Load directory filepaths

Python signature:
```python
def load_directory_files(dir_path: bytes) -> FilePathList
```

C API:
```c
FilePathList LoadDirectoryFiles(const char *dirPath)
```

### load_directory_files_ex
Load directory filepaths with extension filtering and recursive directory scan

Python signature:
```python
def load_directory_files_ex(base_path: bytes, filter: bytes, scan_subdirs: bool) -> FilePathList
```

C API:
```c
FilePathList LoadDirectoryFilesEx(const char *basePath, const char *filter, bool scanSubdirs)
```

### unload_directory_files
Unload filepaths

Python signature:
```python
def unload_directory_files(files: FilePathList) -> None
```

C API:
```c
None UnloadDirectoryFiles(FilePathList files)
```

### is_file_dropped
Check if a file has been dropped into window

Python signature:
```python
def is_file_dropped() -> bool
```

C API:
```c
Bool IsFileDropped()
```

### load_dropped_files
Load dropped filepaths

Python signature:
```python
def load_dropped_files() -> FilePathList
```

C API:
```c
FilePathList LoadDroppedFiles()
```

### unload_dropped_files
Unload dropped filepaths

Python signature:
```python
def unload_dropped_files(files: FilePathList) -> None
```

C API:
```c
None UnloadDroppedFiles(FilePathList files)
```

### get_file_mod_time
Get file modification time (last write time)

Python signature:
```python
def get_file_mod_time(file_name: bytes) -> int
```

C API:
```c
Long GetFileModTime(const char *fileName)
```

### compress_data
Compress data (DEFLATE algorithm), memory must be MemFree()

Python signature:
```python
def compress_data(data: bytes, data_size: int, comp_data_size: Sequence[int]) -> bytes
```

C API:
```c
UBytePtr CompressData(const unsigned char *data, int dataSize, int *compDataSize)
```

### decompress_data
Decompress data (DEFLATE algorithm), memory must be MemFree()

Python signature:
```python
def decompress_data(comp_data: bytes, comp_data_size: int, data_size: Sequence[int]) -> bytes
```

C API:
```c
UBytePtr DecompressData(const unsigned char *compData, int compDataSize, int *dataSize)
```

### encode_data_base64
Encode data to Base64 string, memory must be MemFree()

Python signature:
```python
def encode_data_base64(data: bytes, data_size: int, output_size: Sequence[int]) -> bytes
```

C API:
```c
CharPtr EncodeDataBase64(const unsigned char *data, int dataSize, int *outputSize)
```

### decode_data_base64
Decode Base64 string data, memory must be MemFree()

Python signature:
```python
def decode_data_base64(data: bytes, output_size: Sequence[int]) -> bytes
```

C API:
```c
UBytePtr DecodeDataBase64(const unsigned char *data, int *outputSize)
```

### is_key_pressed
Check if a key has been pressed once

Python signature:
```python
def is_key_pressed(key: int) -> bool
```

C API:
```c
Bool IsKeyPressed(int key)
```

### is_key_down
Check if a key is being pressed

Python signature:
```python
def is_key_down(key: int) -> bool
```

C API:
```c
Bool IsKeyDown(int key)
```

### is_key_released
Check if a key has been released once

Python signature:
```python
def is_key_released(key: int) -> bool
```

C API:
```c
Bool IsKeyReleased(int key)
```

### is_key_up
Check if a key is NOT being pressed

Python signature:
```python
def is_key_up(key: int) -> bool
```

C API:
```c
Bool IsKeyUp(int key)
```

### set_exit_key
Set a custom key to exit program (default is ESC)

Python signature:
```python
def set_exit_key(key: int) -> None
```

C API:
```c
None SetExitKey(int key)
```

### get_key_pressed
Get key pressed (keycode), call it multiple times for keys queued, returns 0 when the queue is empty

Python signature:
```python
def get_key_pressed() -> int
```

C API:
```c
Int GetKeyPressed()
```

### get_char_pressed
Get char pressed (unicode), call it multiple times for chars queued, returns 0 when the queue is empty

Python signature:
```python
def get_char_pressed() -> int
```

C API:
```c
Int GetCharPressed()
```

### is_gamepad_available
Check if a gamepad is available

Python signature:
```python
def is_gamepad_available(gamepad: int) -> bool
```

C API:
```c
Bool IsGamepadAvailable(int gamepad)
```

### get_gamepad_name
Get gamepad internal name id

Python signature:
```python
def get_gamepad_name(gamepad: int) -> bytes
```

C API:
```c
CharPtr GetGamepadName(int gamepad)
```

### is_gamepad_button_pressed
Check if a gamepad button has been pressed once

Python signature:
```python
def is_gamepad_button_pressed(gamepad: int, button: int) -> bool
```

C API:
```c
Bool IsGamepadButtonPressed(int gamepad, int button)
```

### is_gamepad_button_down
Check if a gamepad button is being pressed

Python signature:
```python
def is_gamepad_button_down(gamepad: int, button: int) -> bool
```

C API:
```c
Bool IsGamepadButtonDown(int gamepad, int button)
```

### is_gamepad_button_released
Check if a gamepad button has been released once

Python signature:
```python
def is_gamepad_button_released(gamepad: int, button: int) -> bool
```

C API:
```c
Bool IsGamepadButtonReleased(int gamepad, int button)
```

### is_gamepad_button_up
Check if a gamepad button is NOT being pressed

Python signature:
```python
def is_gamepad_button_up(gamepad: int, button: int) -> bool
```

C API:
```c
Bool IsGamepadButtonUp(int gamepad, int button)
```

### get_gamepad_button_pressed
Get the last gamepad button pressed

Python signature:
```python
def get_gamepad_button_pressed() -> int
```

C API:
```c
Int GetGamepadButtonPressed()
```

### get_gamepad_axis_count
Get gamepad axis count for a gamepad

Python signature:
```python
def get_gamepad_axis_count(gamepad: int) -> int
```

C API:
```c
Int GetGamepadAxisCount(int gamepad)
```

### get_gamepad_axis_movement
Get axis movement value for a gamepad axis

Python signature:
```python
def get_gamepad_axis_movement(gamepad: int, axis: int) -> float
```

C API:
```c
Float GetGamepadAxisMovement(int gamepad, int axis)
```

### set_gamepad_mappings
Set internal gamepad mappings (SDL_GameControllerDB)

Python signature:
```python
def set_gamepad_mappings(mappings: bytes) -> int
```

C API:
```c
Int SetGamepadMappings(const char *mappings)
```

### is_mouse_button_pressed
Check if a mouse button has been pressed once

Python signature:
```python
def is_mouse_button_pressed(button: int) -> bool
```

C API:
```c
Bool IsMouseButtonPressed(int button)
```

### is_mouse_button_down
Check if a mouse button is being pressed

Python signature:
```python
def is_mouse_button_down(button: int) -> bool
```

C API:
```c
Bool IsMouseButtonDown(int button)
```

### is_mouse_button_released
Check if a mouse button has been released once

Python signature:
```python
def is_mouse_button_released(button: int) -> bool
```

C API:
```c
Bool IsMouseButtonReleased(int button)
```

### is_mouse_button_up
Check if a mouse button is NOT being pressed

Python signature:
```python
def is_mouse_button_up(button: int) -> bool
```

C API:
```c
Bool IsMouseButtonUp(int button)
```

### get_mouse_x
Get mouse position X

Python signature:
```python
def get_mouse_x() -> int
```

C API:
```c
Int GetMouseX()
```

### get_mouse_y
Get mouse position Y

Python signature:
```python
def get_mouse_y() -> int
```

C API:
```c
Int GetMouseY()
```

### get_mouse_position
Get mouse position XY

Python signature:
```python
def get_mouse_position() -> Vector2
```

C API:
```c
Vector2 GetMousePosition()
```

### get_mouse_delta
Get mouse delta between frames

Python signature:
```python
def get_mouse_delta() -> Vector2
```

C API:
```c
Vector2 GetMouseDelta()
```

### set_mouse_position
Set mouse position XY

Python signature:
```python
def set_mouse_position(x: int, y: int) -> None
```

C API:
```c
None SetMousePosition(int x, int y)
```

### set_mouse_offset
Set mouse offset

Python signature:
```python
def set_mouse_offset(offset_x: int, offset_y: int) -> None
```

C API:
```c
None SetMouseOffset(int offsetX, int offsetY)
```

### set_mouse_scale
Set mouse scaling

Python signature:
```python
def set_mouse_scale(scale_x: float, scale_y: float) -> None
```

C API:
```c
None SetMouseScale(float scaleX, float scaleY)
```

### get_mouse_wheel_move
Get mouse wheel movement for X or Y, whichever is larger

Python signature:
```python
def get_mouse_wheel_move() -> float
```

C API:
```c
Float GetMouseWheelMove()
```

### get_mouse_wheel_move_v
Get mouse wheel movement for both X and Y

Python signature:
```python
def get_mouse_wheel_move_v() -> Vector2
```

C API:
```c
Vector2 GetMouseWheelMoveV()
```

### set_mouse_cursor
Set mouse cursor

Python signature:
```python
def set_mouse_cursor(cursor: int) -> None
```

C API:
```c
None SetMouseCursor(int cursor)
```

### get_touch_x
Get touch position X for touch point 0 (relative to screen size)

Python signature:
```python
def get_touch_x() -> int
```

C API:
```c
Int GetTouchX()
```

### get_touch_y
Get touch position Y for touch point 0 (relative to screen size)

Python signature:
```python
def get_touch_y() -> int
```

C API:
```c
Int GetTouchY()
```

### get_touch_position
Get touch position XY for a touch point index (relative to screen size)

Python signature:
```python
def get_touch_position(index: int) -> Vector2
```

C API:
```c
Vector2 GetTouchPosition(int index)
```

### get_touch_point_id
Get touch point identifier for given index

Python signature:
```python
def get_touch_point_id(index: int) -> int
```

C API:
```c
Int GetTouchPointId(int index)
```

### get_touch_point_count
Get number of touch points

Python signature:
```python
def get_touch_point_count() -> int
```

C API:
```c
Int GetTouchPointCount()
```

### set_gestures_enabled
Enable a set of gestures using flags

Python signature:
```python
def set_gestures_enabled(flags: int) -> None
```

C API:
```c
None SetGesturesEnabled(unsigned int flags)
```

### is_gesture_detected
Check if a gesture have been detected

Python signature:
```python
def is_gesture_detected(gesture: int) -> bool
```

C API:
```c
Bool IsGestureDetected(int gesture)
```

### get_gesture_detected
Get latest detected gesture

Python signature:
```python
def get_gesture_detected() -> int
```

C API:
```c
Int GetGestureDetected()
```

### get_gesture_hold_duration
Get gesture hold time in milliseconds

Python signature:
```python
def get_gesture_hold_duration() -> float
```

C API:
```c
Float GetGestureHoldDuration()
```

### get_gesture_drag_vector
Get gesture drag vector

Python signature:
```python
def get_gesture_drag_vector() -> Vector2
```

C API:
```c
Vector2 GetGestureDragVector()
```

### get_gesture_drag_angle
Get gesture drag angle

Python signature:
```python
def get_gesture_drag_angle() -> float
```

C API:
```c
Float GetGestureDragAngle()
```

### get_gesture_pinch_vector
Get gesture pinch delta

Python signature:
```python
def get_gesture_pinch_vector() -> Vector2
```

C API:
```c
Vector2 GetGesturePinchVector()
```

### get_gesture_pinch_angle
Get gesture pinch angle

Python signature:
```python
def get_gesture_pinch_angle() -> float
```

C API:
```c
Float GetGesturePinchAngle()
```

### set_camera_mode
Set camera mode (multiple camera modes available)

Python signature:
```python
def set_camera_mode(camera: Camera, mode: int) -> None
```

C API:
```c
None SetCameraMode(Camera camera, int mode)
```

### update_camera
Update camera position for selected mode

Python signature:
```python
def update_camera(camera: CameraPtr) -> None
```

C API:
```c
None UpdateCamera(Camera *camera)
```

### set_camera_pan_control
Set camera pan key to combine with mouse movement (free camera)

Python signature:
```python
def set_camera_pan_control(key_pan: int) -> None
```

C API:
```c
None SetCameraPanControl(int keyPan)
```

### set_camera_alt_control
Set camera alt key to combine with mouse movement (free camera)

Python signature:
```python
def set_camera_alt_control(key_alt: int) -> None
```

C API:
```c
None SetCameraAltControl(int keyAlt)
```

### set_camera_smooth_zoom_control
Set camera smooth zoom key to combine with mouse (free camera)

Python signature:
```python
def set_camera_smooth_zoom_control(key_smooth_zoom: int) -> None
```

C API:
```c
None SetCameraSmoothZoomControl(int keySmoothZoom)
```

### set_camera_move_controls
Set camera move controls (1st person and 3rd person cameras)

Python signature:
```python
def set_camera_move_controls(key_front: int, key_back: int, key_right: int, key_left: int, key_up: int, key_down: int) -> None
```

C API:
```c
None SetCameraMoveControls(int keyFront, int keyBack, int keyRight, int keyLeft, int keyUp, int keyDown)
```

### set_shapes_texture
Set texture and rectangle to be used on shapes drawing

Python signature:
```python
def set_shapes_texture(texture: Texture2D, source: Rectangle) -> None
```

C API:
```c
None SetShapesTexture(Texture2D texture, Rectangle source)
```

### draw_pixel
Draw a pixel

Python signature:
```python
def draw_pixel(pos_x: int, pos_y: int, color: Color) -> None
```

C API:
```c
None DrawPixel(int posX, int posY, Color color)
```

### draw_pixel_v
Draw a pixel (Vector version)

Python signature:
```python
def draw_pixel_v(position: Vector2, color: Color) -> None
```

C API:
```c
None DrawPixelV(Vector2 position, Color color)
```

### draw_line
Draw a line

Python signature:
```python
def draw_line(start_pos_x: int, start_pos_y: int, end_pos_x: int, end_pos_y: int, color: Color) -> None
```

C API:
```c
None DrawLine(int startPosX, int startPosY, int endPosX, int endPosY, Color color)
```

### draw_line_v
Draw a line (Vector version)

Python signature:
```python
def draw_line_v(start_pos: Vector2, end_pos: Vector2, color: Color) -> None
```

C API:
```c
None DrawLineV(Vector2 startPos, Vector2 endPos, Color color)
```

### draw_line_ex
Draw a line defining thickness

Python signature:
```python
def draw_line_ex(start_pos: Vector2, end_pos: Vector2, thick: float, color: Color) -> None
```

C API:
```c
None DrawLineEx(Vector2 startPos, Vector2 endPos, float thick, Color color)
```

### draw_line_bezier
Draw a line using cubic-bezier curves in-out

Python signature:
```python
def draw_line_bezier(start_pos: Vector2, end_pos: Vector2, thick: float, color: Color) -> None
```

C API:
```c
None DrawLineBezier(Vector2 startPos, Vector2 endPos, float thick, Color color)
```

### draw_line_bezier_quad
Draw line using quadratic bezier curves with a control point

Python signature:
```python
def draw_line_bezier_quad(start_pos: Vector2, end_pos: Vector2, control_pos: Vector2, thick: float, color: Color) -> None
```

C API:
```c
None DrawLineBezierQuad(Vector2 startPos, Vector2 endPos, Vector2 controlPos, float thick, Color color)
```

### draw_line_bezier_cubic
Draw line using cubic bezier curves with 2 control points

Python signature:
```python
def draw_line_bezier_cubic(start_pos: Vector2, end_pos: Vector2, start_control_pos: Vector2, end_control_pos: Vector2, thick: float, color: Color) -> None
```

C API:
```c
None DrawLineBezierCubic(Vector2 startPos, Vector2 endPos, Vector2 startControlPos, Vector2 endControlPos, float thick, Color color)
```

### draw_line_strip
Draw lines sequence

Python signature:
```python
def draw_line_strip(points: Vector2Ptr, point_count: int, color: Color) -> None
```

C API:
```c
None DrawLineStrip(Vector2 *points, int pointCount, Color color)
```

### draw_circle
Draw a color-filled circle

Python signature:
```python
def draw_circle(center_x: int, center_y: int, radius: float, color: Color) -> None
```

C API:
```c
None DrawCircle(int centerX, int centerY, float radius, Color color)
```

### draw_circle_sector
Draw a piece of a circle

Python signature:
```python
def draw_circle_sector(center: Vector2, radius: float, start_angle: float, end_angle: float, segments: int, color: Color) -> None
```

C API:
```c
None DrawCircleSector(Vector2 center, float radius, float startAngle, float endAngle, int segments, Color color)
```

### draw_circle_sector_lines
Draw circle sector outline

Python signature:
```python
def draw_circle_sector_lines(center: Vector2, radius: float, start_angle: float, end_angle: float, segments: int, color: Color) -> None
```

C API:
```c
None DrawCircleSectorLines(Vector2 center, float radius, float startAngle, float endAngle, int segments, Color color)
```

### draw_circle_gradient
Draw a gradient-filled circle

Python signature:
```python
def draw_circle_gradient(center_x: int, center_y: int, radius: float, color1: Color, color2: Color) -> None
```

C API:
```c
None DrawCircleGradient(int centerX, int centerY, float radius, Color color1, Color color2)
```

### draw_circle_v
Draw a color-filled circle (Vector version)

Python signature:
```python
def draw_circle_v(center: Vector2, radius: float, color: Color) -> None
```

C API:
```c
None DrawCircleV(Vector2 center, float radius, Color color)
```

### draw_circle_lines
Draw circle outline

Python signature:
```python
def draw_circle_lines(center_x: int, center_y: int, radius: float, color: Color) -> None
```

C API:
```c
None DrawCircleLines(int centerX, int centerY, float radius, Color color)
```

### draw_ellipse
Draw ellipse

Python signature:
```python
def draw_ellipse(center_x: int, center_y: int, radius_h: float, radius_v: float, color: Color) -> None
```

C API:
```c
None DrawEllipse(int centerX, int centerY, float radiusH, float radiusV, Color color)
```

### draw_ellipse_lines
Draw ellipse outline

Python signature:
```python
def draw_ellipse_lines(center_x: int, center_y: int, radius_h: float, radius_v: float, color: Color) -> None
```

C API:
```c
None DrawEllipseLines(int centerX, int centerY, float radiusH, float radiusV, Color color)
```

### draw_ring
Draw ring

Python signature:
```python
def draw_ring(center: Vector2, inner_radius: float, outer_radius: float, start_angle: float, end_angle: float, segments: int, color: Color) -> None
```

C API:
```c
None DrawRing(Vector2 center, float innerRadius, float outerRadius, float startAngle, float endAngle, int segments, Color color)
```

### draw_ring_lines
Draw ring outline

Python signature:
```python
def draw_ring_lines(center: Vector2, inner_radius: float, outer_radius: float, start_angle: float, end_angle: float, segments: int, color: Color) -> None
```

C API:
```c
None DrawRingLines(Vector2 center, float innerRadius, float outerRadius, float startAngle, float endAngle, int segments, Color color)
```

### draw_rectangle
Draw a color-filled rectangle

Python signature:
```python
def draw_rectangle(pos_x: int, pos_y: int, width: int, height: int, color: Color) -> None
```

C API:
```c
None DrawRectangle(int posX, int posY, int width, int height, Color color)
```

### draw_rectangle_v
Draw a color-filled rectangle (Vector version)

Python signature:
```python
def draw_rectangle_v(position: Vector2, size: Vector2, color: Color) -> None
```

C API:
```c
None DrawRectangleV(Vector2 position, Vector2 size, Color color)
```

### draw_rectangle_rec
Draw a color-filled rectangle

Python signature:
```python
def draw_rectangle_rec(rec: Rectangle, color: Color) -> None
```

C API:
```c
None DrawRectangleRec(Rectangle rec, Color color)
```

### draw_rectangle_pro
Draw a color-filled rectangle with pro parameters

Python signature:
```python
def draw_rectangle_pro(rec: Rectangle, origin: Vector2, rotation: float, color: Color) -> None
```

C API:
```c
None DrawRectanglePro(Rectangle rec, Vector2 origin, float rotation, Color color)
```

### draw_rectangle_gradient_v
Draw a vertical-gradient-filled rectangle

Python signature:
```python
def draw_rectangle_gradient_v(pos_x: int, pos_y: int, width: int, height: int, color1: Color, color2: Color) -> None
```

C API:
```c
None DrawRectangleGradientV(int posX, int posY, int width, int height, Color color1, Color color2)
```

### draw_rectangle_gradient_h
Draw a horizontal-gradient-filled rectangle

Python signature:
```python
def draw_rectangle_gradient_h(pos_x: int, pos_y: int, width: int, height: int, color1: Color, color2: Color) -> None
```

C API:
```c
None DrawRectangleGradientH(int posX, int posY, int width, int height, Color color1, Color color2)
```

### draw_rectangle_gradient_ex
Draw a gradient-filled rectangle with custom vertex colors

Python signature:
```python
def draw_rectangle_gradient_ex(rec: Rectangle, col1: Color, col2: Color, col3: Color, col4: Color) -> None
```

C API:
```c
None DrawRectangleGradientEx(Rectangle rec, Color col1, Color col2, Color col3, Color col4)
```

### draw_rectangle_lines
Draw rectangle outline

Python signature:
```python
def draw_rectangle_lines(pos_x: int, pos_y: int, width: int, height: int, color: Color) -> None
```

C API:
```c
None DrawRectangleLines(int posX, int posY, int width, int height, Color color)
```

### draw_rectangle_lines_ex
Draw rectangle outline with extended parameters

Python signature:
```python
def draw_rectangle_lines_ex(rec: Rectangle, line_thick: float, color: Color) -> None
```

C API:
```c
None DrawRectangleLinesEx(Rectangle rec, float lineThick, Color color)
```

### draw_rectangle_rounded
Draw rectangle with rounded edges

Python signature:
```python
def draw_rectangle_rounded(rec: Rectangle, roundness: float, segments: int, color: Color) -> None
```

C API:
```c
None DrawRectangleRounded(Rectangle rec, float roundness, int segments, Color color)
```

### draw_rectangle_rounded_lines
Draw rectangle with rounded edges outline

Python signature:
```python
def draw_rectangle_rounded_lines(rec: Rectangle, roundness: float, segments: int, line_thick: float, color: Color) -> None
```

C API:
```c
None DrawRectangleRoundedLines(Rectangle rec, float roundness, int segments, float lineThick, Color color)
```

### draw_triangle
Draw a color-filled triangle (vertex in counter-clockwise order!)

Python signature:
```python
def draw_triangle(v1: Vector2, v2: Vector2, v3: Vector2, color: Color) -> None
```

C API:
```c
None DrawTriangle(Vector2 v1, Vector2 v2, Vector2 v3, Color color)
```

### draw_triangle_lines
Draw triangle outline (vertex in counter-clockwise order!)

Python signature:
```python
def draw_triangle_lines(v1: Vector2, v2: Vector2, v3: Vector2, color: Color) -> None
```

C API:
```c
None DrawTriangleLines(Vector2 v1, Vector2 v2, Vector2 v3, Color color)
```

### draw_triangle_fan
Draw a triangle fan defined by points (first vertex is the center)

Python signature:
```python
def draw_triangle_fan(points: Vector2Ptr, point_count: int, color: Color) -> None
```

C API:
```c
None DrawTriangleFan(Vector2 *points, int pointCount, Color color)
```

### draw_triangle_strip
Draw a triangle strip defined by points

Python signature:
```python
def draw_triangle_strip(points: Vector2Ptr, point_count: int, color: Color) -> None
```

C API:
```c
None DrawTriangleStrip(Vector2 *points, int pointCount, Color color)
```

### draw_poly
Draw a regular polygon (Vector version)

Python signature:
```python
def draw_poly(center: Vector2, sides: int, radius: float, rotation: float, color: Color) -> None
```

C API:
```c
None DrawPoly(Vector2 center, int sides, float radius, float rotation, Color color)
```

### draw_poly_lines
Draw a polygon outline of n sides

Python signature:
```python
def draw_poly_lines(center: Vector2, sides: int, radius: float, rotation: float, color: Color) -> None
```

C API:
```c
None DrawPolyLines(Vector2 center, int sides, float radius, float rotation, Color color)
```

### draw_poly_lines_ex
Draw a polygon outline of n sides with extended parameters

Python signature:
```python
def draw_poly_lines_ex(center: Vector2, sides: int, radius: float, rotation: float, line_thick: float, color: Color) -> None
```

C API:
```c
None DrawPolyLinesEx(Vector2 center, int sides, float radius, float rotation, float lineThick, Color color)
```

### check_collision_recs
Check collision between two rectangles

Python signature:
```python
def check_collision_recs(rec1: Rectangle, rec2: Rectangle) -> bool
```

C API:
```c
Bool CheckCollisionRecs(Rectangle rec1, Rectangle rec2)
```

### check_collision_circles
Check collision between two circles

Python signature:
```python
def check_collision_circles(center1: Vector2, radius1: float, center2: Vector2, radius2: float) -> bool
```

C API:
```c
Bool CheckCollisionCircles(Vector2 center1, float radius1, Vector2 center2, float radius2)
```

### check_collision_circle_rec
Check collision between circle and rectangle

Python signature:
```python
def check_collision_circle_rec(center: Vector2, radius: float, rec: Rectangle) -> bool
```

C API:
```c
Bool CheckCollisionCircleRec(Vector2 center, float radius, Rectangle rec)
```

### check_collision_point_rec
Check if point is inside rectangle

Python signature:
```python
def check_collision_point_rec(point: Vector2, rec: Rectangle) -> bool
```

C API:
```c
Bool CheckCollisionPointRec(Vector2 point, Rectangle rec)
```

### check_collision_point_circle
Check if point is inside circle

Python signature:
```python
def check_collision_point_circle(point: Vector2, center: Vector2, radius: float) -> bool
```

C API:
```c
Bool CheckCollisionPointCircle(Vector2 point, Vector2 center, float radius)
```

### check_collision_point_triangle
Check if point is inside a triangle

Python signature:
```python
def check_collision_point_triangle(point: Vector2, p1: Vector2, p2: Vector2, p3: Vector2) -> bool
```

C API:
```c
Bool CheckCollisionPointTriangle(Vector2 point, Vector2 p1, Vector2 p2, Vector2 p3)
```

### check_collision_lines
Check the collision between two lines defined by two points each, returns collision point by reference

Python signature:
```python
def check_collision_lines(start_pos1: Vector2, end_pos1: Vector2, start_pos2: Vector2, end_pos2: Vector2, collision_point: Vector2Ptr) -> bool
```

C API:
```c
Bool CheckCollisionLines(Vector2 startPos1, Vector2 endPos1, Vector2 startPos2, Vector2 endPos2, Vector2 *collisionPoint)
```

### check_collision_point_line
Check if point belongs to line created between two points [p1] and [p2] with defined margin in pixels [threshold]

Python signature:
```python
def check_collision_point_line(point: Vector2, p1: Vector2, p2: Vector2, threshold: int) -> bool
```

C API:
```c
Bool CheckCollisionPointLine(Vector2 point, Vector2 p1, Vector2 p2, int threshold)
```

### get_collision_rec
Get collision rectangle for two rectangles collision

Python signature:
```python
def get_collision_rec(rec1: Rectangle, rec2: Rectangle) -> Rectangle
```

C API:
```c
Rectangle GetCollisionRec(Rectangle rec1, Rectangle rec2)
```

### load_image
Load image from file into CPU memory (RAM)

Python signature:
```python
def load_image(file_name: bytes) -> Image
```

C API:
```c
Image LoadImage(const char *fileName)
```

### load_image_raw
Load image from RAW file data

Python signature:
```python
def load_image_raw(file_name: bytes, width: int, height: int, format: int, header_size: int) -> Image
```

C API:
```c
Image LoadImageRaw(const char *fileName, int width, int height, int format, int headerSize)
```

### load_image_anim
Load image sequence from file (frames appended to image.data)

Python signature:
```python
def load_image_anim(file_name: bytes, frames: Sequence[int]) -> Image
```

C API:
```c
Image LoadImageAnim(const char *fileName, int *frames)
```

### load_image_from_memory
Load image from memory buffer, fileType refers to extension: i.e. '.png'

Python signature:
```python
def load_image_from_memory(file_type: bytes, file_data: bytes, data_size: int) -> Image
```

C API:
```c
Image LoadImageFromMemory(const char *fileType, const unsigned char *fileData, int dataSize)
```

### load_image_from_texture
Load image from GPU texture data

Python signature:
```python
def load_image_from_texture(texture: Texture2D) -> Image
```

C API:
```c
Image LoadImageFromTexture(Texture2D texture)
```

### load_image_from_screen
Load image from screen buffer and (screenshot)

Python signature:
```python
def load_image_from_screen() -> Image
```

C API:
```c
Image LoadImageFromScreen()
```

### unload_image
Unload image from CPU memory (RAM)

Python signature:
```python
def unload_image(image: Image) -> None
```

C API:
```c
None UnloadImage(Image image)
```

### export_image
Export image data to file, returns true on success

Python signature:
```python
def export_image(image: Image, file_name: bytes) -> bool
```

C API:
```c
Bool ExportImage(Image image, const char *fileName)
```

### export_image_as_code
Export image as code file defining an array of bytes, returns true on success

Python signature:
```python
def export_image_as_code(image: Image, file_name: bytes) -> bool
```

C API:
```c
Bool ExportImageAsCode(Image image, const char *fileName)
```

### gen_image_color
Generate image: plain color

Python signature:
```python
def gen_image_color(width: int, height: int, color: Color) -> Image
```

C API:
```c
Image GenImageColor(int width, int height, Color color)
```

### gen_image_gradient_v
Generate image: vertical gradient

Python signature:
```python
def gen_image_gradient_v(width: int, height: int, top: Color, bottom: Color) -> Image
```

C API:
```c
Image GenImageGradientV(int width, int height, Color top, Color bottom)
```

### gen_image_gradient_h
Generate image: horizontal gradient

Python signature:
```python
def gen_image_gradient_h(width: int, height: int, left: Color, right: Color) -> Image
```

C API:
```c
Image GenImageGradientH(int width, int height, Color left, Color right)
```

### gen_image_gradient_radial
Generate image: radial gradient

Python signature:
```python
def gen_image_gradient_radial(width: int, height: int, density: float, inner: Color, outer: Color) -> Image
```

C API:
```c
Image GenImageGradientRadial(int width, int height, float density, Color inner, Color outer)
```

### gen_image_checked
Generate image: checked

Python signature:
```python
def gen_image_checked(width: int, height: int, checks_x: int, checks_y: int, col1: Color, col2: Color) -> Image
```

C API:
```c
Image GenImageChecked(int width, int height, int checksX, int checksY, Color col1, Color col2)
```

### gen_image_white_noise
Generate image: white noise

Python signature:
```python
def gen_image_white_noise(width: int, height: int, factor: float) -> Image
```

C API:
```c
Image GenImageWhiteNoise(int width, int height, float factor)
```

### gen_image_cellular
Generate image: cellular algorithm, bigger tileSize means bigger cells

Python signature:
```python
def gen_image_cellular(width: int, height: int, tile_size: int) -> Image
```

C API:
```c
Image GenImageCellular(int width, int height, int tileSize)
```

### image_copy
Create an image duplicate (useful for transformations)

Python signature:
```python
def image_copy(image: Image) -> Image
```

C API:
```c
Image ImageCopy(Image image)
```

### image_from_image
Create an image from another image piece

Python signature:
```python
def image_from_image(image: Image, rec: Rectangle) -> Image
```

C API:
```c
Image ImageFromImage(Image image, Rectangle rec)
```

### image_text
Create an image from text (default font)

Python signature:
```python
def image_text(text: bytes, font_size: int, color: Color) -> Image
```

C API:
```c
Image ImageText(const char *text, int fontSize, Color color)
```

### image_text_ex
Create an image from text (custom sprite font)

Python signature:
```python
def image_text_ex(font: Font, text: bytes, font_size: float, spacing: float, tint: Color) -> Image
```

C API:
```c
Image ImageTextEx(Font font, const char *text, float fontSize, float spacing, Color tint)
```

### image_format
Convert image data to desired format

Python signature:
```python
def image_format(image: ImagePtr, new_format: int) -> None
```

C API:
```c
None ImageFormat(Image *image, int newFormat)
```

### image_to_pot
Convert image to POT (power-of-two)

Python signature:
```python
def image_to_pot(image: ImagePtr, fill: Color) -> None
```

C API:
```c
None ImageToPOT(Image *image, Color fill)
```

### image_crop
Crop an image to a defined rectangle

Python signature:
```python
def image_crop(image: ImagePtr, crop: Rectangle) -> None
```

C API:
```c
None ImageCrop(Image *image, Rectangle crop)
```

### image_alpha_crop
Crop image depending on alpha value

Python signature:
```python
def image_alpha_crop(image: ImagePtr, threshold: float) -> None
```

C API:
```c
None ImageAlphaCrop(Image *image, float threshold)
```

### image_alpha_clear
Clear alpha channel to desired color

Python signature:
```python
def image_alpha_clear(image: ImagePtr, color: Color, threshold: float) -> None
```

C API:
```c
None ImageAlphaClear(Image *image, Color color, float threshold)
```

### image_alpha_mask
Apply alpha mask to image

Python signature:
```python
def image_alpha_mask(image: ImagePtr, alpha_mask: Image) -> None
```

C API:
```c
None ImageAlphaMask(Image *image, Image alphaMask)
```

### image_alpha_premultiply
Premultiply alpha channel

Python signature:
```python
def image_alpha_premultiply(image: ImagePtr) -> None
```

C API:
```c
None ImageAlphaPremultiply(Image *image)
```

### image_resize
Resize image (Bicubic scaling algorithm)

Python signature:
```python
def image_resize(image: ImagePtr, new_width: int, new_height: int) -> None
```

C API:
```c
None ImageResize(Image *image, int newWidth, int newHeight)
```

### image_resize_nn
Resize image (Nearest-Neighbor scaling algorithm)

Python signature:
```python
def image_resize_nn(image: ImagePtr, new_width: int, new_height: int) -> None
```

C API:
```c
None ImageResizeNN(Image *image, int newWidth, int newHeight)
```

### image_resize_canvas
Resize canvas and fill with color

Python signature:
```python
def image_resize_canvas(image: ImagePtr, new_width: int, new_height: int, offset_x: int, offset_y: int, fill: Color) -> None
```

C API:
```c
None ImageResizeCanvas(Image *image, int newWidth, int newHeight, int offsetX, int offsetY, Color fill)
```

### image_mipmaps
Compute all mipmap levels for a provided image

Python signature:
```python
def image_mipmaps(image: ImagePtr) -> None
```

C API:
```c
None ImageMipmaps(Image *image)
```

### image_dither
Dither image data to 16bpp or lower (Floyd-Steinberg dithering)

Python signature:
```python
def image_dither(image: ImagePtr, r_bpp: int, g_bpp: int, b_bpp: int, a_bpp: int) -> None
```

C API:
```c
None ImageDither(Image *image, int rBpp, int gBpp, int bBpp, int aBpp)
```

### image_flip_vertical
Flip image vertically

Python signature:
```python
def image_flip_vertical(image: ImagePtr) -> None
```

C API:
```c
None ImageFlipVertical(Image *image)
```

### image_flip_horizontal
Flip image horizontally

Python signature:
```python
def image_flip_horizontal(image: ImagePtr) -> None
```

C API:
```c
None ImageFlipHorizontal(Image *image)
```

### image_rotate_cw
Rotate image clockwise 90deg

Python signature:
```python
def image_rotate_cw(image: ImagePtr) -> None
```

C API:
```c
None ImageRotateCW(Image *image)
```

### image_rotate_ccw
Rotate image counter-clockwise 90deg

Python signature:
```python
def image_rotate_ccw(image: ImagePtr) -> None
```

C API:
```c
None ImageRotateCCW(Image *image)
```

### image_color_tint
Modify image color: tint

Python signature:
```python
def image_color_tint(image: ImagePtr, color: Color) -> None
```

C API:
```c
None ImageColorTint(Image *image, Color color)
```

### image_color_invert
Modify image color: invert

Python signature:
```python
def image_color_invert(image: ImagePtr) -> None
```

C API:
```c
None ImageColorInvert(Image *image)
```

### image_color_grayscale
Modify image color: grayscale

Python signature:
```python
def image_color_grayscale(image: ImagePtr) -> None
```

C API:
```c
None ImageColorGrayscale(Image *image)
```

### image_color_contrast
Modify image color: contrast (-100 to 100)

Python signature:
```python
def image_color_contrast(image: ImagePtr, contrast: float) -> None
```

C API:
```c
None ImageColorContrast(Image *image, float contrast)
```

### image_color_brightness
Modify image color: brightness (-255 to 255)

Python signature:
```python
def image_color_brightness(image: ImagePtr, brightness: int) -> None
```

C API:
```c
None ImageColorBrightness(Image *image, int brightness)
```

### image_color_replace
Modify image color: replace color

Python signature:
```python
def image_color_replace(image: ImagePtr, color: Color, replace: Color) -> None
```

C API:
```c
None ImageColorReplace(Image *image, Color color, Color replace)
```

### load_image_colors
Load color data from image as a Color array (RGBA - 32bit)

Python signature:
```python
def load_image_colors(image: Image) -> ColorPtr
```

C API:
```c
ColorPtr LoadImageColors(Image image)
```

### load_image_palette
Load colors palette from image as a Color array (RGBA - 32bit)

Python signature:
```python
def load_image_palette(image: Image, max_palette_size: int, color_count: Sequence[int]) -> ColorPtr
```

C API:
```c
ColorPtr LoadImagePalette(Image image, int maxPaletteSize, int *colorCount)
```

### unload_image_colors
Unload color data loaded with LoadImageColors()

Python signature:
```python
def unload_image_colors(colors: ColorPtr) -> None
```

C API:
```c
None UnloadImageColors(Color *colors)
```

### unload_image_palette
Unload colors palette loaded with LoadImagePalette()

Python signature:
```python
def unload_image_palette(colors: ColorPtr) -> None
```

C API:
```c
None UnloadImagePalette(Color *colors)
```

### get_image_alpha_border
Get image alpha border rectangle

Python signature:
```python
def get_image_alpha_border(image: Image, threshold: float) -> Rectangle
```

C API:
```c
Rectangle GetImageAlphaBorder(Image image, float threshold)
```

### get_image_color
Get image pixel color at (x, y) position

Python signature:
```python
def get_image_color(image: Image, x: int, y: int) -> Color
```

C API:
```c
Color GetImageColor(Image image, int x, int y)
```

### image_clear_background
Clear image background with given color

Python signature:
```python
def image_clear_background(dst: ImagePtr, color: Color) -> None
```

C API:
```c
None ImageClearBackground(Image *dst, Color color)
```

### image_draw_pixel
Draw pixel within an image

Python signature:
```python
def image_draw_pixel(dst: ImagePtr, pos_x: int, pos_y: int, color: Color) -> None
```

C API:
```c
None ImageDrawPixel(Image *dst, int posX, int posY, Color color)
```

### image_draw_pixel_v
Draw pixel within an image (Vector version)

Python signature:
```python
def image_draw_pixel_v(dst: ImagePtr, position: Vector2, color: Color) -> None
```

C API:
```c
None ImageDrawPixelV(Image *dst, Vector2 position, Color color)
```

### image_draw_line
Draw line within an image

Python signature:
```python
def image_draw_line(dst: ImagePtr, start_pos_x: int, start_pos_y: int, end_pos_x: int, end_pos_y: int, color: Color) -> None
```

C API:
```c
None ImageDrawLine(Image *dst, int startPosX, int startPosY, int endPosX, int endPosY, Color color)
```

### image_draw_line_v
Draw line within an image (Vector version)

Python signature:
```python
def image_draw_line_v(dst: ImagePtr, start: Vector2, end: Vector2, color: Color) -> None
```

C API:
```c
None ImageDrawLineV(Image *dst, Vector2 start, Vector2 end, Color color)
```

### image_draw_circle
Draw circle within an image

Python signature:
```python
def image_draw_circle(dst: ImagePtr, center_x: int, center_y: int, radius: int, color: Color) -> None
```

C API:
```c
None ImageDrawCircle(Image *dst, int centerX, int centerY, int radius, Color color)
```

### image_draw_circle_v
Draw circle within an image (Vector version)

Python signature:
```python
def image_draw_circle_v(dst: ImagePtr, center: Vector2, radius: int, color: Color) -> None
```

C API:
```c
None ImageDrawCircleV(Image *dst, Vector2 center, int radius, Color color)
```

### image_draw_rectangle
Draw rectangle within an image

Python signature:
```python
def image_draw_rectangle(dst: ImagePtr, pos_x: int, pos_y: int, width: int, height: int, color: Color) -> None
```

C API:
```c
None ImageDrawRectangle(Image *dst, int posX, int posY, int width, int height, Color color)
```

### image_draw_rectangle_v
Draw rectangle within an image (Vector version)

Python signature:
```python
def image_draw_rectangle_v(dst: ImagePtr, position: Vector2, size: Vector2, color: Color) -> None
```

C API:
```c
None ImageDrawRectangleV(Image *dst, Vector2 position, Vector2 size, Color color)
```

### image_draw_rectangle_rec
Draw rectangle within an image

Python signature:
```python
def image_draw_rectangle_rec(dst: ImagePtr, rec: Rectangle, color: Color) -> None
```

C API:
```c
None ImageDrawRectangleRec(Image *dst, Rectangle rec, Color color)
```

### image_draw_rectangle_lines
Draw rectangle lines within an image

Python signature:
```python
def image_draw_rectangle_lines(dst: ImagePtr, rec: Rectangle, thick: int, color: Color) -> None
```

C API:
```c
None ImageDrawRectangleLines(Image *dst, Rectangle rec, int thick, Color color)
```

### image_draw
Draw a source image within a destination image (tint applied to source)

Python signature:
```python
def image_draw(dst: ImagePtr, src: Image, src_rec: Rectangle, dst_rec: Rectangle, tint: Color) -> None
```

C API:
```c
None ImageDraw(Image *dst, Image src, Rectangle srcRec, Rectangle dstRec, Color tint)
```

### image_draw_text
Draw text (using default font) within an image (destination)

Python signature:
```python
def image_draw_text(dst: ImagePtr, text: bytes, pos_x: int, pos_y: int, font_size: int, color: Color) -> None
```

C API:
```c
None ImageDrawText(Image *dst, const char *text, int posX, int posY, int fontSize, Color color)
```

### image_draw_text_ex
Draw text (custom sprite font) within an image (destination)

Python signature:
```python
def image_draw_text_ex(dst: ImagePtr, font: Font, text: bytes, position: Vector2, font_size: float, spacing: float, tint: Color) -> None
```

C API:
```c
None ImageDrawTextEx(Image *dst, Font font, const char *text, Vector2 position, float fontSize, float spacing, Color tint)
```

### load_texture
Load texture from file into GPU memory (VRAM)

Python signature:
```python
def load_texture(file_name: bytes) -> Texture2D
```

C API:
```c
Texture2D LoadTexture(const char *fileName)
```

### load_texture_from_image
Load texture from image data

Python signature:
```python
def load_texture_from_image(image: Image) -> Texture2D
```

C API:
```c
Texture2D LoadTextureFromImage(Image image)
```

### load_texture_cubemap
Load cubemap from image, multiple image cubemap layouts supported

Python signature:
```python
def load_texture_cubemap(image: Image, layout: int) -> TextureCubemap
```

C API:
```c
TextureCubemap LoadTextureCubemap(Image image, int layout)
```

### load_render_texture
Load texture for rendering (framebuffer)

Python signature:
```python
def load_render_texture(width: int, height: int) -> RenderTexture2D
```

C API:
```c
RenderTexture2D LoadRenderTexture(int width, int height)
```

### unload_texture
Unload texture from GPU memory (VRAM)

Python signature:
```python
def unload_texture(texture: Texture2D) -> None
```

C API:
```c
None UnloadTexture(Texture2D texture)
```

### unload_render_texture
Unload render texture from GPU memory (VRAM)

Python signature:
```python
def unload_render_texture(target: RenderTexture2D) -> None
```

C API:
```c
None UnloadRenderTexture(RenderTexture2D target)
```

### update_texture
Update GPU texture with new data

Python signature:
```python
def update_texture(texture: Texture2D, pixels: bytes) -> None
```

C API:
```c
None UpdateTexture(Texture2D texture, const void *pixels)
```

### update_texture_rec
Update GPU texture rectangle with new data

Python signature:
```python
def update_texture_rec(texture: Texture2D, rec: Rectangle, pixels: bytes) -> None
```

C API:
```c
None UpdateTextureRec(Texture2D texture, Rectangle rec, const void *pixels)
```

### gen_texture_mipmaps
Generate GPU mipmaps for a texture

Python signature:
```python
def gen_texture_mipmaps(texture: Texture2DPtr) -> None
```

C API:
```c
None GenTextureMipmaps(Texture2D *texture)
```

### set_texture_filter
Set texture scaling filter mode

Python signature:
```python
def set_texture_filter(texture: Texture2D, filter: int) -> None
```

C API:
```c
None SetTextureFilter(Texture2D texture, int filter)
```

### set_texture_wrap
Set texture wrapping mode

Python signature:
```python
def set_texture_wrap(texture: Texture2D, wrap: int) -> None
```

C API:
```c
None SetTextureWrap(Texture2D texture, int wrap)
```

### draw_texture
Draw a Texture2D

Python signature:
```python
def draw_texture(texture: Texture2D, pos_x: int, pos_y: int, tint: Color) -> None
```

C API:
```c
None DrawTexture(Texture2D texture, int posX, int posY, Color tint)
```

### draw_texture_v
Draw a Texture2D with position defined as Vector2

Python signature:
```python
def draw_texture_v(texture: Texture2D, position: Vector2, tint: Color) -> None
```

C API:
```c
None DrawTextureV(Texture2D texture, Vector2 position, Color tint)
```

### draw_texture_ex
Draw a Texture2D with extended parameters

Python signature:
```python
def draw_texture_ex(texture: Texture2D, position: Vector2, rotation: float, scale: float, tint: Color) -> None
```

C API:
```c
None DrawTextureEx(Texture2D texture, Vector2 position, float rotation, float scale, Color tint)
```

### draw_texture_rec
Draw a part of a texture defined by a rectangle

Python signature:
```python
def draw_texture_rec(texture: Texture2D, source: Rectangle, position: Vector2, tint: Color) -> None
```

C API:
```c
None DrawTextureRec(Texture2D texture, Rectangle source, Vector2 position, Color tint)
```

### draw_texture_quad
Draw texture quad with tiling and offset parameters

Python signature:
```python
def draw_texture_quad(texture: Texture2D, tiling: Vector2, offset: Vector2, quad: Rectangle, tint: Color) -> None
```

C API:
```c
None DrawTextureQuad(Texture2D texture, Vector2 tiling, Vector2 offset, Rectangle quad, Color tint)
```

### draw_texture_tiled
Draw part of a texture (defined by a rectangle) with rotation and scale tiled into dest.

Python signature:
```python
def draw_texture_tiled(texture: Texture2D, source: Rectangle, dest: Rectangle, origin: Vector2, rotation: float, scale: float, tint: Color) -> None
```

C API:
```c
None DrawTextureTiled(Texture2D texture, Rectangle source, Rectangle dest, Vector2 origin, float rotation, float scale, Color tint)
```

### draw_texture_pro
Draw a part of a texture defined by a rectangle with 'pro' parameters

Python signature:
```python
def draw_texture_pro(texture: Texture2D, source: Rectangle, dest: Rectangle, origin: Vector2, rotation: float, tint: Color) -> None
```

C API:
```c
None DrawTexturePro(Texture2D texture, Rectangle source, Rectangle dest, Vector2 origin, float rotation, Color tint)
```

### draw_texture_npatch
Draws a texture (or part of it) that stretches or shrinks nicely

Python signature:
```python
def draw_texture_npatch(texture: Texture2D, n_patch_info: NPatchInfo, dest: Rectangle, origin: Vector2, rotation: float, tint: Color) -> None
```

C API:
```c
None DrawTextureNPatch(Texture2D texture, NPatchInfo nPatchInfo, Rectangle dest, Vector2 origin, float rotation, Color tint)
```

### draw_texture_poly
Draw a textured polygon

Python signature:
```python
def draw_texture_poly(texture: Texture2D, center: Vector2, points: Vector2Ptr, texcoords: Vector2Ptr, point_count: int, tint: Color) -> None
```

C API:
```c
None DrawTexturePoly(Texture2D texture, Vector2 center, Vector2 *points, Vector2 *texcoords, int pointCount, Color tint)
```

### fade
Get color with alpha applied, alpha goes from 0.0f to 1.0f

Python signature:
```python
def fade(color: Color, alpha: float) -> Color
```

C API:
```c
Color Fade(Color color, float alpha)
```

### color_to_int
Get hexadecimal value for a Color

Python signature:
```python
def color_to_int(color: Color) -> int
```

C API:
```c
Int ColorToInt(Color color)
```

### color_normalize
Get Color normalized as float [0..1]

Python signature:
```python
def color_normalize(color: Color) -> Vector4
```

C API:
```c
Vector4 ColorNormalize(Color color)
```

### color_from_normalized
Get Color from normalized values [0..1]

Python signature:
```python
def color_from_normalized(normalized: Vector4) -> Color
```

C API:
```c
Color ColorFromNormalized(Vector4 normalized)
```

### color_to_hsv
Get HSV values for a Color, hue [0..360], saturation/value [0..1]

Python signature:
```python
def color_to_hsv(color: Color) -> Vector3
```

C API:
```c
Vector3 ColorToHSV(Color color)
```

### color_from_hsv
Get a Color from HSV values, hue [0..360], saturation/value [0..1]

Python signature:
```python
def color_from_hsv(hue: float, saturation: float, value: float) -> Color
```

C API:
```c
Color ColorFromHSV(float hue, float saturation, float value)
```

### color_alpha
Get color with alpha applied, alpha goes from 0.0f to 1.0f

Python signature:
```python
def color_alpha(color: Color, alpha: float) -> Color
```

C API:
```c
Color ColorAlpha(Color color, float alpha)
```

### color_alpha_blend
Get src alpha-blended into dst color with tint

Python signature:
```python
def color_alpha_blend(dst: Color, src: Color, tint: Color) -> Color
```

C API:
```c
Color ColorAlphaBlend(Color dst, Color src, Color tint)
```

### get_color
Get Color structure from hexadecimal value

Python signature:
```python
def get_color(hex_value: int) -> Color
```

C API:
```c
Color GetColor(unsigned int hexValue)
```

### get_pixel_color
Get Color from a source pixel pointer of certain format

Python signature:
```python
def get_pixel_color(src_ptr: bytes, format: int) -> Color
```

C API:
```c
Color GetPixelColor(void *srcPtr, int format)
```

### set_pixel_color
Set color formatted into destination pixel pointer

Python signature:
```python
def set_pixel_color(dst_ptr: bytes, color: Color, format: int) -> None
```

C API:
```c
None SetPixelColor(void *dstPtr, Color color, int format)
```

### get_pixel_data_size
Get pixel data size in bytes for certain format

Python signature:
```python
def get_pixel_data_size(width: int, height: int, format: int) -> int
```

C API:
```c
Int GetPixelDataSize(int width, int height, int format)
```

### get_font_default
Get the default Font

Python signature:
```python
def get_font_default() -> Font
```

C API:
```c
Font GetFontDefault()
```

### load_font
Load font from file into GPU memory (VRAM)

Python signature:
```python
def load_font(file_name: bytes) -> Font
```

C API:
```c
Font LoadFont(const char *fileName)
```

### load_font_ex
Load font from file with extended parameters, use NULL for fontChars and 0 for glyphCount to load the default character set

Python signature:
```python
def load_font_ex(file_name: bytes, font_size: int, font_chars: Sequence[int], glyph_count: int) -> Font
```

C API:
```c
Font LoadFontEx(const char *fileName, int fontSize, int *fontChars, int glyphCount)
```

### load_font_from_image
Load font from Image (XNA style)

Python signature:
```python
def load_font_from_image(image: Image, key: Color, first_char: int) -> Font
```

C API:
```c
Font LoadFontFromImage(Image image, Color key, int firstChar)
```

### load_font_from_memory
Load font from memory buffer, fileType refers to extension: i.e. '.ttf'

Python signature:
```python
def load_font_from_memory(file_type: bytes, file_data: bytes, data_size: int, font_size: int, font_chars: Sequence[int], glyph_count: int) -> Font
```

C API:
```c
Font LoadFontFromMemory(const char *fileType, const unsigned char *fileData, int dataSize, int fontSize, int *fontChars, int glyphCount)
```

### load_font_data
Load font data for further use

Python signature:
```python
def load_font_data(file_data: bytes, data_size: int, font_size: int, font_chars: Sequence[int], glyph_count: int, type: int) -> GlyphInfoPtr
```

C API:
```c
GlyphInfoPtr LoadFontData(const unsigned char *fileData, int dataSize, int fontSize, int *fontChars, int glyphCount, int type)
```

### gen_image_font_atlas
Generate image font atlas using chars info

Python signature:
```python
def gen_image_font_atlas(chars: GlyphInfoPtr, recs: Sequence[RectanglePtr], glyph_count: int, font_size: int, padding: int, pack_method: int) -> Image
```

C API:
```c
Image GenImageFontAtlas(const GlyphInfo *chars, Rectangle **recs, int glyphCount, int fontSize, int padding, int packMethod)
```

### unload_font_data
Unload font chars info data (RAM)

Python signature:
```python
def unload_font_data(chars: GlyphInfoPtr, glyph_count: int) -> None
```

C API:
```c
None UnloadFontData(GlyphInfo *chars, int glyphCount)
```

### unload_font
Unload font from GPU memory (VRAM)

Python signature:
```python
def unload_font(font: Font) -> None
```

C API:
```c
None UnloadFont(Font font)
```

### export_font_as_code
Export font as code file, returns true on success

Python signature:
```python
def export_font_as_code(font: Font, file_name: bytes) -> bool
```

C API:
```c
Bool ExportFontAsCode(Font font, const char *fileName)
```

### draw_fps
Draw current FPS

Python signature:
```python
def draw_fps(pos_x: int, pos_y: int) -> None
```

C API:
```c
None DrawFPS(int posX, int posY)
```

### draw_text
Draw text (using default font)

Python signature:
```python
def draw_text(text: bytes, pos_x: int, pos_y: int, font_size: int, color: Color) -> None
```

C API:
```c
None DrawText(const char *text, int posX, int posY, int fontSize, Color color)
```

### draw_text_ex
Draw text using font and additional parameters

Python signature:
```python
def draw_text_ex(font: Font, text: bytes, position: Vector2, font_size: float, spacing: float, tint: Color) -> None
```

C API:
```c
None DrawTextEx(Font font, const char *text, Vector2 position, float fontSize, float spacing, Color tint)
```

### draw_text_pro
Draw text using Font and pro parameters (rotation)

Python signature:
```python
def draw_text_pro(font: Font, text: bytes, position: Vector2, origin: Vector2, rotation: float, font_size: float, spacing: float, tint: Color) -> None
```

C API:
```c
None DrawTextPro(Font font, const char *text, Vector2 position, Vector2 origin, float rotation, float fontSize, float spacing, Color tint)
```

### draw_text_codepoint
Draw one character (codepoint)

Python signature:
```python
def draw_text_codepoint(font: Font, codepoint: int, position: Vector2, font_size: float, tint: Color) -> None
```

C API:
```c
None DrawTextCodepoint(Font font, int codepoint, Vector2 position, float fontSize, Color tint)
```

### draw_text_codepoints
Draw multiple character (codepoint)

Python signature:
```python
def draw_text_codepoints(font: Font, codepoints: Sequence[int], count: int, position: Vector2, font_size: float, spacing: float, tint: Color) -> None
```

C API:
```c
None DrawTextCodepoints(Font font, const int *codepoints, int count, Vector2 position, float fontSize, float spacing, Color tint)
```

### measure_text
Measure string width for default font

Python signature:
```python
def measure_text(text: bytes, font_size: int) -> int
```

C API:
```c
Int MeasureText(const char *text, int fontSize)
```

### measure_text_ex
Measure string size for Font

Python signature:
```python
def measure_text_ex(font: Font, text: bytes, font_size: float, spacing: float) -> Vector2
```

C API:
```c
Vector2 MeasureTextEx(Font font, const char *text, float fontSize, float spacing)
```

### get_glyph_index
Get glyph index position in font for a codepoint (unicode character), fallback to '?' if not found

Python signature:
```python
def get_glyph_index(font: Font, codepoint: int) -> int
```

C API:
```c
Int GetGlyphIndex(Font font, int codepoint)
```

### get_glyph_info
Get glyph font info data for a codepoint (unicode character), fallback to '?' if not found

Python signature:
```python
def get_glyph_info(font: Font, codepoint: int) -> GlyphInfo
```

C API:
```c
GlyphInfo GetGlyphInfo(Font font, int codepoint)
```

### get_glyph_atlas_rec
Get glyph rectangle in font atlas for a codepoint (unicode character), fallback to '?' if not found

Python signature:
```python
def get_glyph_atlas_rec(font: Font, codepoint: int) -> Rectangle
```

C API:
```c
Rectangle GetGlyphAtlasRec(Font font, int codepoint)
```

### load_codepoints
Load all codepoints from a UTF-8 text string, codepoints count returned by parameter

Python signature:
```python
def load_codepoints(text: bytes, count: Sequence[int]) -> Sequence[int]
```

C API:
```c
IntPtr LoadCodepoints(const char *text, int *count)
```

### unload_codepoints
Unload codepoints data from memory

Python signature:
```python
def unload_codepoints(codepoints: Sequence[int]) -> None
```

C API:
```c
None UnloadCodepoints(int *codepoints)
```

### get_codepoint_count
Get total number of codepoints in a UTF-8 encoded string

Python signature:
```python
def get_codepoint_count(text: bytes) -> int
```

C API:
```c
Int GetCodepointCount(const char *text)
```

### get_codepoint
Get next codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure

Python signature:
```python
def get_codepoint(text: bytes, bytes_processed: Sequence[int]) -> int
```

C API:
```c
Int GetCodepoint(const char *text, int *bytesProcessed)
```

### codepoint_to_utf8
Encode one codepoint into UTF-8 byte array (array length returned as parameter)

Python signature:
```python
def codepoint_to_utf8(codepoint: int, byte_size: Sequence[int]) -> bytes
```

C API:
```c
CharPtr CodepointToUTF8(int codepoint, int *byteSize)
```

### text_codepoints_to_utf8
Encode text as codepoints array into UTF-8 text string (WARNING: memory must be freed!)

Python signature:
```python
def text_codepoints_to_utf8(codepoints: Sequence[int], length: int) -> bytes
```

C API:
```c
CharPtr TextCodepointsToUTF8(const int *codepoints, int length)
```

### text_copy
Copy one string to another, returns bytes copied

Python signature:
```python
def text_copy(dst: bytes, src: bytes) -> int
```

C API:
```c
Int TextCopy(char *dst, const char *src)
```

### text_is_equal
Check if two text string are equal

Python signature:
```python
def text_is_equal(text1: bytes, text2: bytes) -> bool
```

C API:
```c
Bool TextIsEqual(const char *text1, const char *text2)
```

### text_length
Get text length, checks for '\0' ending

Python signature:
```python
def text_length(text: bytes) -> int
```

C API:
```c
UInt TextLength(const char *text)
```

### text_format
Text formatting with variables (sprintf() style)

Python signature:
```python
def text_format(text: bytes, *args: bytes) -> bytes
```

C API:
```c
CharPtr TextFormat(const char *text, ... args)
```

### text_subtext
Get a piece of a text string

Python signature:
```python
def text_subtext(text: bytes, position: int, length: int) -> bytes
```

C API:
```c
CharPtr TextSubtext(const char *text, int position, int length)
```

### text_replace
Replace text string (WARNING: memory must be freed!)

Python signature:
```python
def text_replace(text: bytes, replace: bytes, by: bytes) -> bytes
```

C API:
```c
CharPtr TextReplace(char *text, const char *replace, const char *by)
```

### text_insert
Insert text in a position (WARNING: memory must be freed!)

Python signature:
```python
def text_insert(text: bytes, insert: bytes, position: int) -> bytes
```

C API:
```c
CharPtr TextInsert(const char *text, const char *insert, int position)
```

### text_join
Join text strings with delimiter

Python signature:
```python
def text_join(text_list: Sequence[bytes], count: int, delimiter: bytes) -> bytes
```

C API:
```c
CharPtr TextJoin(const char **textList, int count, const char *delimiter)
```

### text_split
Split text into multiple strings

Python signature:
```python
def text_split(text: bytes, delimiter: int, count: Sequence[int]) -> Sequence[bytes]
```

C API:
```c
POINTER(CharPtr) TextSplit(const char *text, char delimiter, int *count)
```

### text_append
Append text at specific position and move cursor!

Python signature:
```python
def text_append(text: bytes, append: bytes, position: Sequence[int]) -> None
```

C API:
```c
None TextAppend(char *text, const char *append, int *position)
```

### text_find_index
Find first text occurrence within a string

Python signature:
```python
def text_find_index(text: bytes, find: bytes) -> int
```

C API:
```c
Int TextFindIndex(const char *text, const char *find)
```

### text_to_upper
Get upper case version of provided string

Python signature:
```python
def text_to_upper(text: bytes) -> bytes
```

C API:
```c
CharPtr TextToUpper(const char *text)
```

### text_to_lower
Get lower case version of provided string

Python signature:
```python
def text_to_lower(text: bytes) -> bytes
```

C API:
```c
CharPtr TextToLower(const char *text)
```

### text_to_pascal
Get Pascal case notation version of provided string

Python signature:
```python
def text_to_pascal(text: bytes) -> bytes
```

C API:
```c
CharPtr TextToPascal(const char *text)
```

### text_to_integer
Get integer value from text (negative values not supported)

Python signature:
```python
def text_to_integer(text: bytes) -> int
```

C API:
```c
Int TextToInteger(const char *text)
```

### draw_line3d
Draw a line in 3D world space

Python signature:
```python
def draw_line3d(start_pos: Vector3, end_pos: Vector3, color: Color) -> None
```

C API:
```c
None DrawLine3D(Vector3 startPos, Vector3 endPos, Color color)
```

### draw_point3d
Draw a point in 3D space, actually a small line

Python signature:
```python
def draw_point3d(position: Vector3, color: Color) -> None
```

C API:
```c
None DrawPoint3D(Vector3 position, Color color)
```

### draw_circle3d
Draw a circle in 3D world space

Python signature:
```python
def draw_circle3d(center: Vector3, radius: float, rotation_axis: Vector3, rotation_angle: float, color: Color) -> None
```

C API:
```c
None DrawCircle3D(Vector3 center, float radius, Vector3 rotationAxis, float rotationAngle, Color color)
```

### draw_triangle3d
Draw a color-filled triangle (vertex in counter-clockwise order!)

Python signature:
```python
def draw_triangle3d(v1: Vector3, v2: Vector3, v3: Vector3, color: Color) -> None
```

C API:
```c
None DrawTriangle3D(Vector3 v1, Vector3 v2, Vector3 v3, Color color)
```

### draw_triangle_strip3d
Draw a triangle strip defined by points

Python signature:
```python
def draw_triangle_strip3d(points: Vector3Ptr, point_count: int, color: Color) -> None
```

C API:
```c
None DrawTriangleStrip3D(Vector3 *points, int pointCount, Color color)
```

### draw_cube
Draw cube

Python signature:
```python
def draw_cube(position: Vector3, width: float, height: float, length: float, color: Color) -> None
```

C API:
```c
None DrawCube(Vector3 position, float width, float height, float length, Color color)
```

### draw_cube_v
Draw cube (Vector version)

Python signature:
```python
def draw_cube_v(position: Vector3, size: Vector3, color: Color) -> None
```

C API:
```c
None DrawCubeV(Vector3 position, Vector3 size, Color color)
```

### draw_cube_wires
Draw cube wires

Python signature:
```python
def draw_cube_wires(position: Vector3, width: float, height: float, length: float, color: Color) -> None
```

C API:
```c
None DrawCubeWires(Vector3 position, float width, float height, float length, Color color)
```

### draw_cube_wires_v
Draw cube wires (Vector version)

Python signature:
```python
def draw_cube_wires_v(position: Vector3, size: Vector3, color: Color) -> None
```

C API:
```c
None DrawCubeWiresV(Vector3 position, Vector3 size, Color color)
```

### draw_cube_texture
Draw cube textured

Python signature:
```python
def draw_cube_texture(texture: Texture2D, position: Vector3, width: float, height: float, length: float, color: Color) -> None
```

C API:
```c
None DrawCubeTexture(Texture2D texture, Vector3 position, float width, float height, float length, Color color)
```

### draw_cube_texture_rec
Draw cube with a region of a texture

Python signature:
```python
def draw_cube_texture_rec(texture: Texture2D, source: Rectangle, position: Vector3, width: float, height: float, length: float, color: Color) -> None
```

C API:
```c
None DrawCubeTextureRec(Texture2D texture, Rectangle source, Vector3 position, float width, float height, float length, Color color)
```

### draw_sphere
Draw sphere

Python signature:
```python
def draw_sphere(center_pos: Vector3, radius: float, color: Color) -> None
```

C API:
```c
None DrawSphere(Vector3 centerPos, float radius, Color color)
```

### draw_sphere_ex
Draw sphere with extended parameters

Python signature:
```python
def draw_sphere_ex(center_pos: Vector3, radius: float, rings: int, slices: int, color: Color) -> None
```

C API:
```c
None DrawSphereEx(Vector3 centerPos, float radius, int rings, int slices, Color color)
```

### draw_sphere_wires
Draw sphere wires

Python signature:
```python
def draw_sphere_wires(center_pos: Vector3, radius: float, rings: int, slices: int, color: Color) -> None
```

C API:
```c
None DrawSphereWires(Vector3 centerPos, float radius, int rings, int slices, Color color)
```

### draw_cylinder
Draw a cylinder/cone

Python signature:
```python
def draw_cylinder(position: Vector3, radius_top: float, radius_bottom: float, height: float, slices: int, color: Color) -> None
```

C API:
```c
None DrawCylinder(Vector3 position, float radiusTop, float radiusBottom, float height, int slices, Color color)
```

### draw_cylinder_ex
Draw a cylinder with base at startPos and top at endPos

Python signature:
```python
def draw_cylinder_ex(start_pos: Vector3, end_pos: Vector3, start_radius: float, end_radius: float, sides: int, color: Color) -> None
```

C API:
```c
None DrawCylinderEx(Vector3 startPos, Vector3 endPos, float startRadius, float endRadius, int sides, Color color)
```

### draw_cylinder_wires
Draw a cylinder/cone wires

Python signature:
```python
def draw_cylinder_wires(position: Vector3, radius_top: float, radius_bottom: float, height: float, slices: int, color: Color) -> None
```

C API:
```c
None DrawCylinderWires(Vector3 position, float radiusTop, float radiusBottom, float height, int slices, Color color)
```

### draw_cylinder_wires_ex
Draw a cylinder wires with base at startPos and top at endPos

Python signature:
```python
def draw_cylinder_wires_ex(start_pos: Vector3, end_pos: Vector3, start_radius: float, end_radius: float, sides: int, color: Color) -> None
```

C API:
```c
None DrawCylinderWiresEx(Vector3 startPos, Vector3 endPos, float startRadius, float endRadius, int sides, Color color)
```

### draw_plane
Draw a plane XZ

Python signature:
```python
def draw_plane(center_pos: Vector3, size: Vector2, color: Color) -> None
```

C API:
```c
None DrawPlane(Vector3 centerPos, Vector2 size, Color color)
```

### draw_ray
Draw a ray line

Python signature:
```python
def draw_ray(ray: Ray, color: Color) -> None
```

C API:
```c
None DrawRay(Ray ray, Color color)
```

### draw_grid
Draw a grid (centered at (0, 0, 0))

Python signature:
```python
def draw_grid(slices: int, spacing: float) -> None
```

C API:
```c
None DrawGrid(int slices, float spacing)
```

### load_model
Load model from files (meshes and materials)

Python signature:
```python
def load_model(file_name: bytes) -> Model
```

C API:
```c
Model LoadModel(const char *fileName)
```

### load_model_from_mesh
Load model from generated mesh (default material)

Python signature:
```python
def load_model_from_mesh(mesh: Mesh) -> Model
```

C API:
```c
Model LoadModelFromMesh(Mesh mesh)
```

### unload_model
Unload model (including meshes) from memory (RAM and/or VRAM)

Python signature:
```python
def unload_model(model: Model) -> None
```

C API:
```c
None UnloadModel(Model model)
```

### unload_model_keep_meshes
Unload model (but not meshes) from memory (RAM and/or VRAM)

Python signature:
```python
def unload_model_keep_meshes(model: Model) -> None
```

C API:
```c
None UnloadModelKeepMeshes(Model model)
```

### get_model_bounding_box
Compute model bounding box limits (considers all meshes)

Python signature:
```python
def get_model_bounding_box(model: Model) -> BoundingBox
```

C API:
```c
BoundingBox GetModelBoundingBox(Model model)
```

### draw_model
Draw a model (with texture if set)

Python signature:
```python
def draw_model(model: Model, position: Vector3, scale: float, tint: Color) -> None
```

C API:
```c
None DrawModel(Model model, Vector3 position, float scale, Color tint)
```

### draw_model_ex
Draw a model with extended parameters

Python signature:
```python
def draw_model_ex(model: Model, position: Vector3, rotation_axis: Vector3, rotation_angle: float, scale: Vector3, tint: Color) -> None
```

C API:
```c
None DrawModelEx(Model model, Vector3 position, Vector3 rotationAxis, float rotationAngle, Vector3 scale, Color tint)
```

### draw_model_wires
Draw a model wires (with texture if set)

Python signature:
```python
def draw_model_wires(model: Model, position: Vector3, scale: float, tint: Color) -> None
```

C API:
```c
None DrawModelWires(Model model, Vector3 position, float scale, Color tint)
```

### draw_model_wires_ex
Draw a model wires (with texture if set) with extended parameters

Python signature:
```python
def draw_model_wires_ex(model: Model, position: Vector3, rotation_axis: Vector3, rotation_angle: float, scale: Vector3, tint: Color) -> None
```

C API:
```c
None DrawModelWiresEx(Model model, Vector3 position, Vector3 rotationAxis, float rotationAngle, Vector3 scale, Color tint)
```

### draw_bounding_box
Draw bounding box (wires)

Python signature:
```python
def draw_bounding_box(box: BoundingBox, color: Color) -> None
```

C API:
```c
None DrawBoundingBox(BoundingBox box, Color color)
```

### draw_billboard
Draw a billboard texture

Python signature:
```python
def draw_billboard(camera: Camera, texture: Texture2D, position: Vector3, size: float, tint: Color) -> None
```

C API:
```c
None DrawBillboard(Camera camera, Texture2D texture, Vector3 position, float size, Color tint)
```

### draw_billboard_rec
Draw a billboard texture defined by source

Python signature:
```python
def draw_billboard_rec(camera: Camera, texture: Texture2D, source: Rectangle, position: Vector3, size: Vector2, tint: Color) -> None
```

C API:
```c
None DrawBillboardRec(Camera camera, Texture2D texture, Rectangle source, Vector3 position, Vector2 size, Color tint)
```

### draw_billboard_pro
Draw a billboard texture defined by source and rotation

Python signature:
```python
def draw_billboard_pro(camera: Camera, texture: Texture2D, source: Rectangle, position: Vector3, up: Vector3, size: Vector2, origin: Vector2, rotation: float, tint: Color) -> None
```

C API:
```c
None DrawBillboardPro(Camera camera, Texture2D texture, Rectangle source, Vector3 position, Vector3 up, Vector2 size, Vector2 origin, float rotation, Color tint)
```

### upload_mesh
Upload mesh vertex data in GPU and provide VAO/VBO ids

Python signature:
```python
def upload_mesh(mesh: MeshPtr, dynamic: bool) -> None
```

C API:
```c
None UploadMesh(Mesh *mesh, bool dynamic)
```

### update_mesh_buffer
Update mesh vertex data in GPU for a specific buffer index

Python signature:
```python
def update_mesh_buffer(mesh: Mesh, index: int, data: bytes, data_size: int, offset: int) -> None
```

C API:
```c
None UpdateMeshBuffer(Mesh mesh, int index, const void *data, int dataSize, int offset)
```

### unload_mesh
Unload mesh data from CPU and GPU

Python signature:
```python
def unload_mesh(mesh: Mesh) -> None
```

C API:
```c
None UnloadMesh(Mesh mesh)
```

### draw_mesh
Draw a 3d mesh with material and transform

Python signature:
```python
def draw_mesh(mesh: Mesh, material: Material, transform: Matrix) -> None
```

C API:
```c
None DrawMesh(Mesh mesh, Material material, Matrix transform)
```

### draw_mesh_instanced
Draw multiple mesh instances with material and different transforms

Python signature:
```python
def draw_mesh_instanced(mesh: Mesh, material: Material, transforms: MatrixPtr, instances: int) -> None
```

C API:
```c
None DrawMeshInstanced(Mesh mesh, Material material, const Matrix *transforms, int instances)
```

### export_mesh
Export mesh data to file, returns true on success

Python signature:
```python
def export_mesh(mesh: Mesh, file_name: bytes) -> bool
```

C API:
```c
Bool ExportMesh(Mesh mesh, const char *fileName)
```

### get_mesh_bounding_box
Compute mesh bounding box limits

Python signature:
```python
def get_mesh_bounding_box(mesh: Mesh) -> BoundingBox
```

C API:
```c
BoundingBox GetMeshBoundingBox(Mesh mesh)
```

### gen_mesh_tangents
Compute mesh tangents

Python signature:
```python
def gen_mesh_tangents(mesh: MeshPtr) -> None
```

C API:
```c
None GenMeshTangents(Mesh *mesh)
```

### gen_mesh_poly
Generate polygonal mesh

Python signature:
```python
def gen_mesh_poly(sides: int, radius: float) -> Mesh
```

C API:
```c
Mesh GenMeshPoly(int sides, float radius)
```

### gen_mesh_plane
Generate plane mesh (with subdivisions)

Python signature:
```python
def gen_mesh_plane(width: float, length: float, res_x: int, res_z: int) -> Mesh
```

C API:
```c
Mesh GenMeshPlane(float width, float length, int resX, int resZ)
```

### gen_mesh_cube
Generate cuboid mesh

Python signature:
```python
def gen_mesh_cube(width: float, height: float, length: float) -> Mesh
```

C API:
```c
Mesh GenMeshCube(float width, float height, float length)
```

### gen_mesh_sphere
Generate sphere mesh (standard sphere)

Python signature:
```python
def gen_mesh_sphere(radius: float, rings: int, slices: int) -> Mesh
```

C API:
```c
Mesh GenMeshSphere(float radius, int rings, int slices)
```

### gen_mesh_hemi_sphere
Generate half-sphere mesh (no bottom cap)

Python signature:
```python
def gen_mesh_hemi_sphere(radius: float, rings: int, slices: int) -> Mesh
```

C API:
```c
Mesh GenMeshHemiSphere(float radius, int rings, int slices)
```

### gen_mesh_cylinder
Generate cylinder mesh

Python signature:
```python
def gen_mesh_cylinder(radius: float, height: float, slices: int) -> Mesh
```

C API:
```c
Mesh GenMeshCylinder(float radius, float height, int slices)
```

### gen_mesh_cone
Generate cone/pyramid mesh

Python signature:
```python
def gen_mesh_cone(radius: float, height: float, slices: int) -> Mesh
```

C API:
```c
Mesh GenMeshCone(float radius, float height, int slices)
```

### gen_mesh_torus
Generate torus mesh

Python signature:
```python
def gen_mesh_torus(radius: float, size: float, rad_seg: int, sides: int) -> Mesh
```

C API:
```c
Mesh GenMeshTorus(float radius, float size, int radSeg, int sides)
```

### gen_mesh_knot
Generate trefoil knot mesh

Python signature:
```python
def gen_mesh_knot(radius: float, size: float, rad_seg: int, sides: int) -> Mesh
```

C API:
```c
Mesh GenMeshKnot(float radius, float size, int radSeg, int sides)
```

### gen_mesh_heightmap
Generate heightmap mesh from image data

Python signature:
```python
def gen_mesh_heightmap(heightmap: Image, size: Vector3) -> Mesh
```

C API:
```c
Mesh GenMeshHeightmap(Image heightmap, Vector3 size)
```

### gen_mesh_cubicmap
Generate cubes-based map mesh from image data

Python signature:
```python
def gen_mesh_cubicmap(cubicmap: Image, cube_size: Vector3) -> Mesh
```

C API:
```c
Mesh GenMeshCubicmap(Image cubicmap, Vector3 cubeSize)
```

### load_materials
Load materials from model file

Python signature:
```python
def load_materials(file_name: bytes, material_count: Sequence[int]) -> MaterialPtr
```

C API:
```c
MaterialPtr LoadMaterials(const char *fileName, int *materialCount)
```

### load_material_default
Load default material (Supports: DIFFUSE, SPECULAR, NORMAL maps)

Python signature:
```python
def load_material_default() -> Material
```

C API:
```c
Material LoadMaterialDefault()
```

### unload_material
Unload material from GPU memory (VRAM)

Python signature:
```python
def unload_material(material: Material) -> None
```

C API:
```c
None UnloadMaterial(Material material)
```

### set_material_texture
Set texture for a material map type (MATERIAL_MAP_DIFFUSE, MATERIAL_MAP_SPECULAR...)

Python signature:
```python
def set_material_texture(material: MaterialPtr, map_type: int, texture: Texture2D) -> None
```

C API:
```c
None SetMaterialTexture(Material *material, int mapType, Texture2D texture)
```

### set_model_mesh_material
Set material for a mesh

Python signature:
```python
def set_model_mesh_material(model: ModelPtr, mesh_id: int, material_id: int) -> None
```

C API:
```c
None SetModelMeshMaterial(Model *model, int meshId, int materialId)
```

### load_model_animations
Load model animations from file

Python signature:
```python
def load_model_animations(file_name: bytes, anim_count: Sequence[int]) -> ModelAnimationPtr
```

C API:
```c
ModelAnimationPtr LoadModelAnimations(const char *fileName, unsigned int *animCount)
```

### update_model_animation
Update model animation pose

Python signature:
```python
def update_model_animation(model: Model, anim: ModelAnimation, frame: int) -> None
```

C API:
```c
None UpdateModelAnimation(Model model, ModelAnimation anim, int frame)
```

### unload_model_animation
Unload animation data

Python signature:
```python
def unload_model_animation(anim: ModelAnimation) -> None
```

C API:
```c
None UnloadModelAnimation(ModelAnimation anim)
```

### unload_model_animations
Unload animation array data

Python signature:
```python
def unload_model_animations(animations: ModelAnimationPtr, count: int) -> None
```

C API:
```c
None UnloadModelAnimations(ModelAnimation *animations, unsigned int count)
```

### is_model_animation_valid
Check model animation skeleton match

Python signature:
```python
def is_model_animation_valid(model: Model, anim: ModelAnimation) -> bool
```

C API:
```c
Bool IsModelAnimationValid(Model model, ModelAnimation anim)
```

### check_collision_spheres
Check collision between two spheres

Python signature:
```python
def check_collision_spheres(center1: Vector3, radius1: float, center2: Vector3, radius2: float) -> bool
```

C API:
```c
Bool CheckCollisionSpheres(Vector3 center1, float radius1, Vector3 center2, float radius2)
```

### check_collision_boxes
Check collision between two bounding boxes

Python signature:
```python
def check_collision_boxes(box1: BoundingBox, box2: BoundingBox) -> bool
```

C API:
```c
Bool CheckCollisionBoxes(BoundingBox box1, BoundingBox box2)
```

### check_collision_box_sphere
Check collision between box and sphere

Python signature:
```python
def check_collision_box_sphere(box: BoundingBox, center: Vector3, radius: float) -> bool
```

C API:
```c
Bool CheckCollisionBoxSphere(BoundingBox box, Vector3 center, float radius)
```

### get_ray_collision_sphere
Get collision info between ray and sphere

Python signature:
```python
def get_ray_collision_sphere(ray: Ray, center: Vector3, radius: float) -> RayCollision
```

C API:
```c
RayCollision GetRayCollisionSphere(Ray ray, Vector3 center, float radius)
```

### get_ray_collision_box
Get collision info between ray and box

Python signature:
```python
def get_ray_collision_box(ray: Ray, box: BoundingBox) -> RayCollision
```

C API:
```c
RayCollision GetRayCollisionBox(Ray ray, BoundingBox box)
```

### get_ray_collision_mesh
Get collision info between ray and mesh

Python signature:
```python
def get_ray_collision_mesh(ray: Ray, mesh: Mesh, transform: Matrix) -> RayCollision
```

C API:
```c
RayCollision GetRayCollisionMesh(Ray ray, Mesh mesh, Matrix transform)
```

### get_ray_collision_triangle
Get collision info between ray and triangle

Python signature:
```python
def get_ray_collision_triangle(ray: Ray, p1: Vector3, p2: Vector3, p3: Vector3) -> RayCollision
```

C API:
```c
RayCollision GetRayCollisionTriangle(Ray ray, Vector3 p1, Vector3 p2, Vector3 p3)
```

### get_ray_collision_quad
Get collision info between ray and quad

Python signature:
```python
def get_ray_collision_quad(ray: Ray, p1: Vector3, p2: Vector3, p3: Vector3, p4: Vector3) -> RayCollision
```

C API:
```c
RayCollision GetRayCollisionQuad(Ray ray, Vector3 p1, Vector3 p2, Vector3 p3, Vector3 p4)
```

### init_audio_device
Initialize audio device and context

Python signature:
```python
def init_audio_device() -> None
```

C API:
```c
None InitAudioDevice()
```

### close_audio_device
Close the audio device and context

Python signature:
```python
def close_audio_device() -> None
```

C API:
```c
None CloseAudioDevice()
```

### is_audio_device_ready
Check if audio device has been initialized successfully

Python signature:
```python
def is_audio_device_ready() -> bool
```

C API:
```c
Bool IsAudioDeviceReady()
```

### set_master_volume
Set master volume (listener)

Python signature:
```python
def set_master_volume(volume: float) -> None
```

C API:
```c
None SetMasterVolume(float volume)
```

### load_wave
Load wave data from file

Python signature:
```python
def load_wave(file_name: bytes) -> Wave
```

C API:
```c
Wave LoadWave(const char *fileName)
```

### load_wave_from_memory
Load wave from memory buffer, fileType refers to extension: i.e. '.wav'

Python signature:
```python
def load_wave_from_memory(file_type: bytes, file_data: bytes, data_size: int) -> Wave
```

C API:
```c
Wave LoadWaveFromMemory(const char *fileType, const unsigned char *fileData, int dataSize)
```

### load_sound
Load sound from file

Python signature:
```python
def load_sound(file_name: bytes) -> Sound
```

C API:
```c
Sound LoadSound(const char *fileName)
```

### load_sound_from_wave
Load sound from wave data

Python signature:
```python
def load_sound_from_wave(wave: Wave) -> Sound
```

C API:
```c
Sound LoadSoundFromWave(Wave wave)
```

### update_sound
Update sound buffer with new data

Python signature:
```python
def update_sound(sound: Sound, data: bytes, sample_count: int) -> None
```

C API:
```c
None UpdateSound(Sound sound, const void *data, int sampleCount)
```

### unload_wave
Unload wave data

Python signature:
```python
def unload_wave(wave: Wave) -> None
```

C API:
```c
None UnloadWave(Wave wave)
```

### unload_sound
Unload sound

Python signature:
```python
def unload_sound(sound: Sound) -> None
```

C API:
```c
None UnloadSound(Sound sound)
```

### export_wave
Export wave data to file, returns true on success

Python signature:
```python
def export_wave(wave: Wave, file_name: bytes) -> bool
```

C API:
```c
Bool ExportWave(Wave wave, const char *fileName)
```

### export_wave_as_code
Export wave sample data to code (.h), returns true on success

Python signature:
```python
def export_wave_as_code(wave: Wave, file_name: bytes) -> bool
```

C API:
```c
Bool ExportWaveAsCode(Wave wave, const char *fileName)
```

### play_sound
Play a sound

Python signature:
```python
def play_sound(sound: Sound) -> None
```

C API:
```c
None PlaySound(Sound sound)
```

### stop_sound
Stop playing a sound

Python signature:
```python
def stop_sound(sound: Sound) -> None
```

C API:
```c
None StopSound(Sound sound)
```

### pause_sound
Pause a sound

Python signature:
```python
def pause_sound(sound: Sound) -> None
```

C API:
```c
None PauseSound(Sound sound)
```

### resume_sound
Resume a paused sound

Python signature:
```python
def resume_sound(sound: Sound) -> None
```

C API:
```c
None ResumeSound(Sound sound)
```

### play_sound_multi
Play a sound (using multichannel buffer pool)

Python signature:
```python
def play_sound_multi(sound: Sound) -> None
```

C API:
```c
None PlaySoundMulti(Sound sound)
```

### stop_sound_multi
Stop any sound playing (using multichannel buffer pool)

Python signature:
```python
def stop_sound_multi() -> None
```

C API:
```c
None StopSoundMulti()
```

### get_sounds_playing
Get number of sounds playing in the multichannel

Python signature:
```python
def get_sounds_playing() -> int
```

C API:
```c
Int GetSoundsPlaying()
```

### is_sound_playing
Check if a sound is currently playing

Python signature:
```python
def is_sound_playing(sound: Sound) -> bool
```

C API:
```c
Bool IsSoundPlaying(Sound sound)
```

### set_sound_volume
Set volume for a sound (1.0 is max level)

Python signature:
```python
def set_sound_volume(sound: Sound, volume: float) -> None
```

C API:
```c
None SetSoundVolume(Sound sound, float volume)
```

### set_sound_pitch
Set pitch for a sound (1.0 is base level)

Python signature:
```python
def set_sound_pitch(sound: Sound, pitch: float) -> None
```

C API:
```c
None SetSoundPitch(Sound sound, float pitch)
```

### set_sound_pan
Set pan for a sound (0.5 is center)

Python signature:
```python
def set_sound_pan(sound: Sound, pan: float) -> None
```

C API:
```c
None SetSoundPan(Sound sound, float pan)
```

### wave_copy
Copy a wave to a new wave

Python signature:
```python
def wave_copy(wave: Wave) -> Wave
```

C API:
```c
Wave WaveCopy(Wave wave)
```

### wave_crop
Crop a wave to defined samples range

Python signature:
```python
def wave_crop(wave: WavePtr, init_sample: int, final_sample: int) -> None
```

C API:
```c
None WaveCrop(Wave *wave, int initSample, int finalSample)
```

### wave_format
Convert wave data to desired format

Python signature:
```python
def wave_format(wave: WavePtr, sample_rate: int, sample_size: int, channels: int) -> None
```

C API:
```c
None WaveFormat(Wave *wave, int sampleRate, int sampleSize, int channels)
```

### load_wave_samples
Load samples data from wave as a 32bit float data array

Python signature:
```python
def load_wave_samples(wave: Wave) -> Sequence[float]
```

C API:
```c
FloatPtr LoadWaveSamples(Wave wave)
```

### unload_wave_samples
Unload samples data loaded with LoadWaveSamples()

Python signature:
```python
def unload_wave_samples(samples: Sequence[float]) -> None
```

C API:
```c
None UnloadWaveSamples(float *samples)
```

### load_music_stream
Load music stream from file

Python signature:
```python
def load_music_stream(file_name: bytes) -> Music
```

C API:
```c
Music LoadMusicStream(const char *fileName)
```

### load_music_stream_from_memory
Load music stream from data

Python signature:
```python
def load_music_stream_from_memory(file_type: bytes, data: bytes, data_size: int) -> Music
```

C API:
```c
Music LoadMusicStreamFromMemory(const char *fileType, const unsigned char *data, int dataSize)
```

### unload_music_stream
Unload music stream

Python signature:
```python
def unload_music_stream(music: Music) -> None
```

C API:
```c
None UnloadMusicStream(Music music)
```

### play_music_stream
Start music playing

Python signature:
```python
def play_music_stream(music: Music) -> None
```

C API:
```c
None PlayMusicStream(Music music)
```

### is_music_stream_playing
Check if music is playing

Python signature:
```python
def is_music_stream_playing(music: Music) -> bool
```

C API:
```c
Bool IsMusicStreamPlaying(Music music)
```

### update_music_stream
Updates buffers for music streaming

Python signature:
```python
def update_music_stream(music: Music) -> None
```

C API:
```c
None UpdateMusicStream(Music music)
```

### stop_music_stream
Stop music playing

Python signature:
```python
def stop_music_stream(music: Music) -> None
```

C API:
```c
None StopMusicStream(Music music)
```

### pause_music_stream
Pause music playing

Python signature:
```python
def pause_music_stream(music: Music) -> None
```

C API:
```c
None PauseMusicStream(Music music)
```

### resume_music_stream
Resume playing paused music

Python signature:
```python
def resume_music_stream(music: Music) -> None
```

C API:
```c
None ResumeMusicStream(Music music)
```

### seek_music_stream
Seek music to a position (in seconds)

Python signature:
```python
def seek_music_stream(music: Music, position: float) -> None
```

C API:
```c
None SeekMusicStream(Music music, float position)
```

### set_music_volume
Set volume for music (1.0 is max level)

Python signature:
```python
def set_music_volume(music: Music, volume: float) -> None
```

C API:
```c
None SetMusicVolume(Music music, float volume)
```

### set_music_pitch
Set pitch for a music (1.0 is base level)

Python signature:
```python
def set_music_pitch(music: Music, pitch: float) -> None
```

C API:
```c
None SetMusicPitch(Music music, float pitch)
```

### set_music_pan
Set pan for a music (0.5 is center)

Python signature:
```python
def set_music_pan(music: Music, pan: float) -> None
```

C API:
```c
None SetMusicPan(Music music, float pan)
```

### get_music_time_length
Get music time length (in seconds)

Python signature:
```python
def get_music_time_length(music: Music) -> float
```

C API:
```c
Float GetMusicTimeLength(Music music)
```

### get_music_time_played
Get current music time played (in seconds)

Python signature:
```python
def get_music_time_played(music: Music) -> float
```

C API:
```c
Float GetMusicTimePlayed(Music music)
```

### load_audio_stream
Load audio stream (to stream raw audio pcm data)

Python signature:
```python
def load_audio_stream(sample_rate: int, sample_size: int, channels: int) -> AudioStream
```

C API:
```c
AudioStream LoadAudioStream(unsigned int sampleRate, unsigned int sampleSize, unsigned int channels)
```

### unload_audio_stream
Unload audio stream and free memory

Python signature:
```python
def unload_audio_stream(stream: AudioStream) -> None
```

C API:
```c
None UnloadAudioStream(AudioStream stream)
```

### update_audio_stream
Update audio stream buffers with data

Python signature:
```python
def update_audio_stream(stream: AudioStream, data: bytes, frame_count: int) -> None
```

C API:
```c
None UpdateAudioStream(AudioStream stream, const void *data, int frameCount)
```

### is_audio_stream_processed
Check if any audio stream buffers requires refill

Python signature:
```python
def is_audio_stream_processed(stream: AudioStream) -> bool
```

C API:
```c
Bool IsAudioStreamProcessed(AudioStream stream)
```

### play_audio_stream
Play audio stream

Python signature:
```python
def play_audio_stream(stream: AudioStream) -> None
```

C API:
```c
None PlayAudioStream(AudioStream stream)
```

### pause_audio_stream
Pause audio stream

Python signature:
```python
def pause_audio_stream(stream: AudioStream) -> None
```

C API:
```c
None PauseAudioStream(AudioStream stream)
```

### resume_audio_stream
Resume audio stream

Python signature:
```python
def resume_audio_stream(stream: AudioStream) -> None
```

C API:
```c
None ResumeAudioStream(AudioStream stream)
```

### is_audio_stream_playing
Check if audio stream is playing

Python signature:
```python
def is_audio_stream_playing(stream: AudioStream) -> bool
```

C API:
```c
Bool IsAudioStreamPlaying(AudioStream stream)
```

### stop_audio_stream
Stop audio stream

Python signature:
```python
def stop_audio_stream(stream: AudioStream) -> None
```

C API:
```c
None StopAudioStream(AudioStream stream)
```

### set_audio_stream_volume
Set volume for audio stream (1.0 is max level)

Python signature:
```python
def set_audio_stream_volume(stream: AudioStream, volume: float) -> None
```

C API:
```c
None SetAudioStreamVolume(AudioStream stream, float volume)
```

### set_audio_stream_pitch
Set pitch for audio stream (1.0 is base level)

Python signature:
```python
def set_audio_stream_pitch(stream: AudioStream, pitch: float) -> None
```

C API:
```c
None SetAudioStreamPitch(AudioStream stream, float pitch)
```

### set_audio_stream_pan
Set pan for audio stream (0.5 is centered)

Python signature:
```python
def set_audio_stream_pan(stream: AudioStream, pan: float) -> None
```

C API:
```c
None SetAudioStreamPan(AudioStream stream, float pan)
```

### set_audio_stream_buffer_size_default
Default size for new audio streams

Python signature:
```python
def set_audio_stream_buffer_size_default(size: int) -> None
```

C API:
```c
None SetAudioStreamBufferSizeDefault(int size)
```

### set_audio_stream_callback
Audio thread callback to request new data

Python signature:
```python
def set_audio_stream_callback(stream: AudioStream, callback: AudioCallback) -> None
```

C API:
```c
None SetAudioStreamCallback(AudioStream stream, AudioCallback callback)
```

### attach_audio_stream_processor


Python signature:
```python
def attach_audio_stream_processor(stream: AudioStream, processor: AudioCallback) -> None
```

C API:
```c
None AttachAudioStreamProcessor(AudioStream stream, AudioCallback processor)
```

### detach_audio_stream_processor


Python signature:
```python
def detach_audio_stream_processor(stream: AudioStream, processor: AudioCallback) -> None
```

C API:
```c
None DetachAudioStreamProcessor(AudioStream stream, AudioCallback processor)
```

### clamp
Clamp float value

Python signature:
```python
def clamp(value: float, min_: float, max_: float) -> float
```

C API:
```c
Float Clamp(float value, float min_, float max_)
```

### lerp
Calculate linear interpolation between two floats

Python signature:
```python
def lerp(start: float, end: float, amount: float) -> float
```

C API:
```c
Float Lerp(float start, float end, float amount)
```

### normalize
Calculate linear interpolation between two floats

Python signature:
```python
def normalize(value: float, start: float, end: float) -> float
```

C API:
```c
Float Normalize(float value, float start, float end)
```

### remap
Remap input value within input range to output range

Python signature:
```python
def remap(value: float, input_start: float, input_end: float, output_start: float, output_end: float) -> float
```

C API:
```c
Float Remap(float value, float inputStart, float inputEnd, float outputStart, float outputEnd)
```

### wrap
Wrap input value from min to max

Python signature:
```python
def wrap(value: float, min_: float, max_: float) -> float
```

C API:
```c
Float Wrap(float value, float min_, float max_)
```

### float_equals
Check whether two given floats are almost equal

Python signature:
```python
def float_equals(x: float, y: float) -> int
```

C API:
```c
Int FloatEquals(float x, float y)
```

### vector2zero
Vector with components value 0.0f

Python signature:
```python
def vector2zero() -> Vector2
```

C API:
```c
Vector2 Vector2Zero()
```

### vector2one
Vector with components value 1.0f

Python signature:
```python
def vector2one() -> Vector2
```

C API:
```c
Vector2 Vector2One()
```

### vector2add
Add two vectors (v1 + v2)

Python signature:
```python
def vector2add(v1: Vector2, v2: Vector2) -> Vector2
```

C API:
```c
Vector2 Vector2Add(Vector2 v1, Vector2 v2)
```

### vector2add_value
Add vector and float value

Python signature:
```python
def vector2add_value(v: Vector2, add: float) -> Vector2
```

C API:
```c
Vector2 Vector2AddValue(Vector2 v, float add)
```

### vector2subtract
Subtract two vectors (v1 - v2)

Python signature:
```python
def vector2subtract(v1: Vector2, v2: Vector2) -> Vector2
```

C API:
```c
Vector2 Vector2Subtract(Vector2 v1, Vector2 v2)
```

### vector2subtract_value
Subtract vector by float value

Python signature:
```python
def vector2subtract_value(v: Vector2, sub: float) -> Vector2
```

C API:
```c
Vector2 Vector2SubtractValue(Vector2 v, float sub)
```

### vector2length
Calculate vector length

Python signature:
```python
def vector2length(v: Vector2) -> float
```

C API:
```c
Float Vector2Length(Vector2 v)
```

### vector2length_sqr
Calculate vector square length

Python signature:
```python
def vector2length_sqr(v: Vector2) -> float
```

C API:
```c
Float Vector2LengthSqr(Vector2 v)
```

### vector2dot_product
Calculate two vectors dot product

Python signature:
```python
def vector2dot_product(v1: Vector2, v2: Vector2) -> float
```

C API:
```c
Float Vector2DotProduct(Vector2 v1, Vector2 v2)
```

### vector2distance
Calculate distance between two vectors

Python signature:
```python
def vector2distance(v1: Vector2, v2: Vector2) -> float
```

C API:
```c
Float Vector2Distance(Vector2 v1, Vector2 v2)
```

### vector2distance_sqr
Calculate square distance between two vectors

Python signature:
```python
def vector2distance_sqr(v1: Vector2, v2: Vector2) -> float
```

C API:
```c
Float Vector2DistanceSqr(Vector2 v1, Vector2 v2)
```

### vector2angle
Calculate angle from two vectors

Python signature:
```python
def vector2angle(v1: Vector2, v2: Vector2) -> float
```

C API:
```c
Float Vector2Angle(Vector2 v1, Vector2 v2)
```

### vector2scale
Scale vector (multiply by value)

Python signature:
```python
def vector2scale(v: Vector2, scale: float) -> Vector2
```

C API:
```c
Vector2 Vector2Scale(Vector2 v, float scale)
```

### vector2multiply
Multiply vector by vector

Python signature:
```python
def vector2multiply(v1: Vector2, v2: Vector2) -> Vector2
```

C API:
```c
Vector2 Vector2Multiply(Vector2 v1, Vector2 v2)
```

### vector2negate
Negate vector

Python signature:
```python
def vector2negate(v: Vector2) -> Vector2
```

C API:
```c
Vector2 Vector2Negate(Vector2 v)
```

### vector2divide
Divide vector by vector

Python signature:
```python
def vector2divide(v1: Vector2, v2: Vector2) -> Vector2
```

C API:
```c
Vector2 Vector2Divide(Vector2 v1, Vector2 v2)
```

### vector2normalize
Normalize provided vector

Python signature:
```python
def vector2normalize(v: Vector2) -> Vector2
```

C API:
```c
Vector2 Vector2Normalize(Vector2 v)
```

### vector2transform
Transforms a Vector2 by a given Matrix

Python signature:
```python
def vector2transform(v: Vector2, mat: Matrix) -> Vector2
```

C API:
```c
Vector2 Vector2Transform(Vector2 v, Matrix mat)
```

### vector2lerp
Calculate linear interpolation between two vectors

Python signature:
```python
def vector2lerp(v1: Vector2, v2: Vector2, amount: float) -> Vector2
```

C API:
```c
Vector2 Vector2Lerp(Vector2 v1, Vector2 v2, float amount)
```

### vector2reflect
Calculate reflected vector to normal

Python signature:
```python
def vector2reflect(v1: Vector2, normal: Vector2) -> Vector2
```

C API:
```c
Vector2 Vector2Reflect(Vector2 v1, Vector2 normal)
```

### vector2rotate
Rotate vector by angle

Python signature:
```python
def vector2rotate(v1: Vector2, angle: float) -> Vector2
```

C API:
```c
Vector2 Vector2Rotate(Vector2 v1, float angle)
```

### vector2move_towards
Move Vector towards target

Python signature:
```python
def vector2move_towards(v1: Vector2, target: Vector2, max_distance: float) -> Vector2
```

C API:
```c
Vector2 Vector2MoveTowards(Vector2 v1, Vector2 target, float maxDistance)
```

### vector2invert
Invert the given vector

Python signature:
```python
def vector2invert(v: Vector2) -> Vector2
```

C API:
```c
Vector2 Vector2Invert(Vector2 v)
```

### vector2clamp
Clamp the components of the vector between min and max values specified by the given vectors

Python signature:
```python
def vector2clamp(v: Vector2, min_: Vector2, max_: Vector2) -> Vector2
```

C API:
```c
Vector2 Vector2Clamp(Vector2 v, Vector2 min_, Vector2 max_)
```

### vector2clamp_value
Clamp the magnitude of the vector between two min and max values

Python signature:
```python
def vector2clamp_value(v: Vector2, min_: float, max_: float) -> Vector2
```

C API:
```c
Vector2 Vector2ClampValue(Vector2 v, float min_, float max_)
```

### vector2equals
Check whether two given vectors are almost equal

Python signature:
```python
def vector2equals(p: Vector2, q: Vector2) -> int
```

C API:
```c
Int Vector2Equals(Vector2 p, Vector2 q)
```

### vector3zero
Vector with components value 0.0f

Python signature:
```python
def vector3zero() -> Vector3
```

C API:
```c
Vector3 Vector3Zero()
```

### vector3one
Vector with components value 1.0f

Python signature:
```python
def vector3one() -> Vector3
```

C API:
```c
Vector3 Vector3One()
```

### vector3add
Add two vectors

Python signature:
```python
def vector3add(v1: Vector3, v2: Vector3) -> Vector3
```

C API:
```c
Vector3 Vector3Add(Vector3 v1, Vector3 v2)
```

### vector3add_value
Add vector and float value

Python signature:
```python
def vector3add_value(v: Vector3, add: float) -> Vector3
```

C API:
```c
Vector3 Vector3AddValue(Vector3 v, float add)
```

### vector3subtract
Subtract two vectors

Python signature:
```python
def vector3subtract(v1: Vector3, v2: Vector3) -> Vector3
```

C API:
```c
Vector3 Vector3Subtract(Vector3 v1, Vector3 v2)
```

### vector3subtract_value
Subtract vector and float value

Python signature:
```python
def vector3subtract_value(v: Vector3, sub: float) -> Vector3
```

C API:
```c
Vector3 Vector3SubtractValue(Vector3 v, float sub)
```

### vector3scale
Multiply vector by scalar

Python signature:
```python
def vector3scale(v: Vector3, scalar: float) -> Vector3
```

C API:
```c
Vector3 Vector3Scale(Vector3 v, float scalar)
```

### vector3multiply
Multiply vector by vector

Python signature:
```python
def vector3multiply(v1: Vector3, v2: Vector3) -> Vector3
```

C API:
```c
Vector3 Vector3Multiply(Vector3 v1, Vector3 v2)
```

### vector3cross_product
Calculate two vectors cross product

Python signature:
```python
def vector3cross_product(v1: Vector3, v2: Vector3) -> float
```

C API:
```c
Float Vector3CrossProduct(Vector3 v1, Vector3 v2)
```

### vector3perpendicular
Calculate one vector perpendicular vector

Python signature:
```python
def vector3perpendicular(v1: Vector3) -> Vector3
```

C API:
```c
Vector3 Vector3Perpendicular(Vector3 v1)
```

### vector3length
Calculate vector length

Python signature:
```python
def vector3length(v1: Vector3) -> Vector3
```

C API:
```c
Vector3 Vector3Length(Vector3 v1)
```

### vector3length_sqr
Calculate vector square length

Python signature:
```python
def vector3length_sqr(v1: Vector3) -> Vector3
```

C API:
```c
Vector3 Vector3LengthSqr(Vector3 v1)
```

### vector3dot_product
Calculate two vectors dot product

Python signature:
```python
def vector3dot_product(v1: Vector3, v2: Vector3) -> float
```

C API:
```c
Float Vector3DotProduct(Vector3 v1, Vector3 v2)
```

### vector3distance
Calculate distance between two vectors

Python signature:
```python
def vector3distance(v1: Vector3, v2: Vector3) -> float
```

C API:
```c
Float Vector3Distance(Vector3 v1, Vector3 v2)
```

### vector3distance_sqr
Calculate square distance between two vectors

Python signature:
```python
def vector3distance_sqr(v1: Vector3, v2: Vector3) -> float
```

C API:
```c
Float Vector3DistanceSqr(Vector3 v1, Vector3 v2)
```

### vector3angle
Calculate angle between two vectors

Python signature:
```python
def vector3angle(v1: Vector3, v2: Vector3) -> float
```

C API:
```c
Float Vector3Angle(Vector3 v1, Vector3 v2)
```

### vector3negate
Negate provided vector (invert direction)

Python signature:
```python
def vector3negate(v: Vector3) -> Vector3
```

C API:
```c
Vector3 Vector3Negate(Vector3 v)
```

### vector3divide
Divide vector by vector

Python signature:
```python
def vector3divide(v1: Vector3, v2: Vector3) -> float
```

C API:
```c
Float Vector3Divide(Vector3 v1, Vector3 v2)
```

### vector3normalize
Normalize provided vector

Python signature:
```python
def vector3normalize(v: Vector3) -> Vector3
```

C API:
```c
Vector3 Vector3Normalize(Vector3 v)
```

### vector3ortho_normalize
Makes vectors normalized and orthogonal to each other

Python signature:
```python
def vector3ortho_normalize(v1: Vector3Ptr, v2: Vector3Ptr) -> Vector3
```

C API:
```c
Vector3 Vector3OrthoNormalize(Vector3 *v1, Vector3 *v2)
```

### vector3transform
Transforms a Vector3 by a given Matrix

Python signature:
```python
def vector3transform(v: Vector3, mat: Matrix) -> Vector3
```

C API:
```c
Vector3 Vector3Transform(Vector3 v, Matrix mat)
```

### vector3rotate_by_quaternion
Transform a vector by quaternion rotation

Python signature:
```python
def vector3rotate_by_quaternion(v: Vector3, q: Quaternion) -> Vector3
```

C API:
```c
Vector3 Vector3RotateByQuaternion(Vector3 v, Quaternion q)
```

### vector3rotate_by_axis_angle
Rotates a vector around an axis

Python signature:
```python
def vector3rotate_by_axis_angle(v: Vector3, axis: Vector3, angle: float) -> Vector3
```

C API:
```c
Vector3 Vector3RotateByAxisAngle(Vector3 v, Vector3 axis, float angle)
```

### vector3lerp
Calculate linear interpolation between two vectors

Python signature:
```python
def vector3lerp(v1: Vector3, v2: Vector3, amount: float) -> Vector3
```

C API:
```c
Vector3 Vector3Lerp(Vector3 v1, Vector3 v2, float amount)
```

### vector3reflect
Calculate reflected vector to normal

Python signature:
```python
def vector3reflect(v: Vector3, normal: Vector3) -> Vector3
```

C API:
```c
Vector3 Vector3Reflect(Vector3 v, Vector3 normal)
```

### vector3min
Get min value for each pair of components

Python signature:
```python
def vector3min(v1: Vector3, v2: Vector3) -> Vector3
```

C API:
```c
Vector3 Vector3Min(Vector3 v1, Vector3 v2)
```

### vector3max
Get max value for each pair of components

Python signature:
```python
def vector3max(v1: Vector3, v2: Vector3) -> Vector3
```

C API:
```c
Vector3 Vector3Max(Vector3 v1, Vector3 v2)
```

### vector3barycenter
Compute barycenter coordinates (u, v, w) for point p with respect to triangle (a, b, c). Assumes P is on the plane of the triangle

Python signature:
```python
def vector3barycenter(p: Vector3, a: Vector3, b: Vector3, c: Vector3) -> Vector3
```

C API:
```c
Vector3 Vector3Barycenter(Vector3 p, Vector3 a, Vector3 b, Vector3 c)
```

### vector3unproject
Projects a Vector3 from screen space into object space

Python signature:
```python
def vector3unproject(source: Vector3, projection: Matrix, view: Matrix) -> Vector3
```

C API:
```c
Vector3 Vector3Unproject(Vector3 source, Matrix projection, Matrix view)
```

### vector3to_float_v
Get Vector3 as float array

Python signature:
```python
def vector3to_float_v(v: Vector3) -> Sequence[float]
```

C API:
```c
Float * 3 Vector3ToFloatV(Vector3 v)
```

### vector3invert
Invert the given vector

Python signature:
```python
def vector3invert(v: Vector3) -> Vector3
```

C API:
```c
Vector3 Vector3Invert(Vector3 v)
```

### vector3clamp
Clamp the components of the vector between min and max values specified by the given vectors

Python signature:
```python
def vector3clamp(v: Vector3, min_: Vector3, max_: Vector3) -> Vector3
```

C API:
```c
Vector3 Vector3Clamp(Vector3 v, Vector3 min_, Vector3 max_)
```

### vector3clamp_value
Clamp the magnitude of the vector between two values

Python signature:
```python
def vector3clamp_value(v: Vector3, min_: float, max_: float) -> Vector3
```

C API:
```c
Vector3 Vector3ClampValue(Vector3 v, float min_, float max_)
```

### vector3equals
Check whether two given vectors are almost equal

Python signature:
```python
def vector3equals(v: Vector3, min_: float, max_: float) -> int
```

C API:
```c
Int Vector3Equals(Vector3 v, float min_, float max_)
```

### vector3refract
Compute the direction of a refracted ray where v specifies the normalized direction of the incoming ray, n specifies the normalized normal vector of the interface of two optical media, and r specifies the ratio of the refractive index of the medium from where the ray comes to the refractive index of the medium on the other side of the surface

Python signature:
```python
def vector3refract(v: Vector3, n: Vector3, r: float) -> int
```

C API:
```c
Int Vector3Refract(Vector3 v, Vector3 n, float r)
```

### matrix_determinant
Compute matrix determinant

Python signature:
```python
def matrix_determinant(mat: Matrix) -> float
```

C API:
```c
Float MatrixDeterminant(Matrix mat)
```

### matrix_trace
Get the trace of the matrix (sum of the values along the diagonal)

Python signature:
```python
def matrix_trace(mat: Matrix) -> float
```

C API:
```c
Float MatrixTrace(Matrix mat)
```

### matrix_transpose
Get the trace of the matrix (sum of the values along the diagonal)

Python signature:
```python
def matrix_transpose(mat: Matrix) -> Matrix
```

C API:
```c
Matrix MatrixTranspose(Matrix mat)
```

### matrix_invert
Invert provided matrix

Python signature:
```python
def matrix_invert(mat: Matrix) -> Matrix
```

C API:
```c
Matrix MatrixInvert(Matrix mat)
```

### matrix_identity
Get identity matrix

Python signature:
```python
def matrix_identity() -> Matrix
```

C API:
```c
Matrix MatrixIdentity()
```

### matrix_add
Add two matrices

Python signature:
```python
def matrix_add(left: Matrix, right: Matrix) -> Matrix
```

C API:
```c
Matrix MatrixAdd(Matrix left, Matrix right)
```

### matrix_subtract
Subtract two matrices (left - right)

Python signature:
```python
def matrix_subtract(left: Matrix, right: Matrix) -> Matrix
```

C API:
```c
Matrix MatrixSubtract(Matrix left, Matrix right)
```

### matrix_multiply
Get two matrix multiplication. When multiplying matrices... the order matters!

Python signature:
```python
def matrix_multiply(left: Matrix, right: Matrix) -> Matrix
```

C API:
```c
Matrix MatrixMultiply(Matrix left, Matrix right)
```

### matrix_translate
Get translation matrix

Python signature:
```python
def matrix_translate(x: float, y: float, z: float) -> Matrix
```

C API:
```c
Matrix MatrixTranslate(float x, float y, float z)
```

### matrix_rotate
Create rotation matrix from axis and angle. Angle should be provided in radians

Python signature:
```python
def matrix_rotate(axis: Vector3, angle: float) -> Matrix
```

C API:
```c
Matrix MatrixRotate(Vector3 axis, float angle)
```

### matrix_rotate_x
Get x-rotation matrix. Angle must be provided in radians

Python signature:
```python
def matrix_rotate_x(angle: float) -> Matrix
```

C API:
```c
Matrix MatrixRotateX(float angle)
```

### matrix_rotate_y
Get y-rotation matrix. Angle must be provided in radians

Python signature:
```python
def matrix_rotate_y(angle: float) -> Matrix
```

C API:
```c
Matrix MatrixRotateY(float angle)
```

### matrix_rotate_z
Get z-rotation matrix. Angle must be provided in radians

Python signature:
```python
def matrix_rotate_z(angle: float) -> Matrix
```

C API:
```c
Matrix MatrixRotateZ(float angle)
```

### matrix_rotate_xyz
Get xyz-rotation matrix. Angle must be provided in radians

Python signature:
```python
def matrix_rotate_xyz(angle: Vector3) -> Matrix
```

C API:
```c
Matrix MatrixRotateXYZ(Vector3 angle)
```

### matrix_rotate_zyx
Get zyx-rotation matrix. Angle must be provided in radians

Python signature:
```python
def matrix_rotate_zyx(angle: Vector3) -> Matrix
```

C API:
```c
Matrix MatrixRotateZYX(Vector3 angle)
```

### matrix_scale
Get scaling matrix

Python signature:
```python
def matrix_scale(x: float, y: float, z: float) -> Matrix
```

C API:
```c
Matrix MatrixScale(float x, float y, float z)
```

### matrix_frustum
Get perspective projection matrix

Python signature:
```python
def matrix_frustum(left: float, right: float, bottom: float, top: float, near: float, far: float) -> Matrix
```

C API:
```c
Matrix MatrixFrustum(float left, float right, float bottom, float top, float near, float far)
```

### matrix_perspective
Get perspective projection matrix. Fovy angle must be provided in radians

Python signature:
```python
def matrix_perspective(fovy: float, aspect: float, near: float, far: float) -> Matrix
```

C API:
```c
Matrix MatrixPerspective(float fovy, float aspect, float near, float far)
```

### matrix_ortho
Get orthographic projection matrix

Python signature:
```python
def matrix_ortho(left: float, right: float, bottom: float, top: float, near: float, far: float) -> Matrix
```

C API:
```c
Matrix MatrixOrtho(float left, float right, float bottom, float top, float near, float far)
```

### matrix_look_at
Get camera look-at matrix (view matrix)

Python signature:
```python
def matrix_look_at(eye: Vector3, target: Vector3, up: Vector3) -> Matrix
```

C API:
```c
Matrix MatrixLookAt(Vector3 eye, Vector3 target, Vector3 up)
```

### matrix_to_float_v
Get float array of matrix data

Python signature:
```python
def matrix_to_float_v(mat: Matrix) -> Sequence[float]
```

C API:
```c
Float * 16 MatrixToFloatV(Matrix mat)
```

### quaternion_add
Add two quaternions

Python signature:
```python
def quaternion_add(q1: Quaternion, q2: Quaternion) -> Quaternion
```

C API:
```c
Quaternion QuaternionAdd(Quaternion q1, Quaternion q2)
```

### quaternion_add_value
Add quaternion and float value

Python signature:
```python
def quaternion_add_value(q: Quaternion, add: float) -> Quaternion
```

C API:
```c
Quaternion QuaternionAddValue(Quaternion q, float add)
```

### quaternion_subtract
Subtract two quaternions

Python signature:
```python
def quaternion_subtract(q1: Quaternion, q2: Quaternion) -> Quaternion
```

C API:
```c
Quaternion QuaternionSubtract(Quaternion q1, Quaternion q2)
```

### quaternion_subtract_value
Subtract quaternion and float value

Python signature:
```python
def quaternion_subtract_value(q: Quaternion, sub: float) -> Quaternion
```

C API:
```c
Quaternion QuaternionSubtractValue(Quaternion q, float sub)
```

### quaternion_identity
Get identity quaternion

Python signature:
```python
def quaternion_identity() -> Quaternion
```

C API:
```c
Quaternion QuaternionIdentity()
```

### quaternion_length
Computes the length of a quaternion

Python signature:
```python
def quaternion_length(q: Quaternion) -> Quaternion
```

C API:
```c
Quaternion QuaternionLength(Quaternion q)
```

### quaternion_normalize
Normalize provided quaternion

Python signature:
```python
def quaternion_normalize(q: Quaternion) -> Quaternion
```

C API:
```c
Quaternion QuaternionNormalize(Quaternion q)
```

### quaternion_invert
Invert provided quaternion

Python signature:
```python
def quaternion_invert(q: Quaternion) -> Quaternion
```

C API:
```c
Quaternion QuaternionInvert(Quaternion q)
```

### quaternion_multiply
Calculate two quaternion multiplication

Python signature:
```python
def quaternion_multiply(q1: Quaternion, q2: Quaternion) -> Quaternion
```

C API:
```c
Quaternion QuaternionMultiply(Quaternion q1, Quaternion q2)
```

### quaternion_scale
Scale quaternion by float value

Python signature:
```python
def quaternion_scale(q1: Quaternion, mul: float) -> Quaternion
```

C API:
```c
Quaternion QuaternionScale(Quaternion q1, float mul)
```

### quaternion_divide
Divide two quaternions

Python signature:
```python
def quaternion_divide(q1: Quaternion, q2: Quaternion) -> Quaternion
```

C API:
```c
Quaternion QuaternionDivide(Quaternion q1, Quaternion q2)
```

### quaternion_nlerp
Calculate slerp-optimized interpolation between two quaternions

Python signature:
```python
def quaternion_nlerp(q1: Quaternion, q2: Quaternion, amount: float) -> Quaternion
```

C API:
```c
Quaternion QuaternionNlerp(Quaternion q1, Quaternion q2, float amount)
```

### quaternion_slerp
Calculates spherical linear interpolation between two quaternions

Python signature:
```python
def quaternion_slerp(q1: Quaternion, q2: Quaternion, amount: float) -> Quaternion
```

C API:
```c
Quaternion QuaternionSlerp(Quaternion q1, Quaternion q2, float amount)
```

### quaternion_from_vector3to_vector3
Calculate quaternion based on the rotation from one vector to another

Python signature:
```python
def quaternion_from_vector3to_vector3(from_: Vector3, to: Vector3) -> Quaternion
```

C API:
```c
Quaternion QuaternionFromVector3ToVector3(Vector3 from_, Vector3 to)
```

### quaternion_to_matrix
Get a quaternion for a given rotation matrix

Python signature:
```python
def quaternion_to_matrix(q: Quaternion) -> Matrix
```

C API:
```c
Matrix QuaternionToMatrix(Quaternion q)
```

### quaternion_from_matrix
Get a quaternion for a given rotation matrix

Python signature:
```python
def quaternion_from_matrix(mat: Matrix) -> Quaternion
```

C API:
```c
Quaternion QuaternionFromMatrix(Matrix mat)
```

### quaternion_from_axis_angle
Get rotation quaternion for an angle and axis. Angle must be provided in radians

Python signature:
```python
def quaternion_from_axis_angle(mat: Vector3, angle: float) -> Quaternion
```

C API:
```c
Quaternion QuaternionFromAxisAngle(Vector3 mat, float angle)
```

### quaternion_to_axis_angle
Get the rotation angle and axis for a given quaternion

Python signature:
```python
def quaternion_to_axis_angle(q: Quaternion, out_axis: Vector3Ptr, out_angle: Sequence[float]) -> None
```

C API:
```c
None QuaternionToAxisAngle(Quaternion q, Vector3 *outAxis, float *outAngle)
```

### quaternion_from_euler
Get the quaternion equivalent to Euler angles. Rotation order is ZYX

Python signature:
```python
def quaternion_from_euler(pitch: float, yaw: float, roll: float) -> Quaternion
```

C API:
```c
Quaternion QuaternionFromEuler(float pitch, float yaw, float roll)
```

### quaternion_to_euler
Get the quaternion equivalent to Euler angles. Rotation order is ZYX

Python signature:
```python
def quaternion_to_euler(q: Quaternion) -> Vector3
```

C API:
```c
Vector3 QuaternionToEuler(Quaternion q)
```

### quaternion_transform
Transform a quaternion given a transformation matrix

Python signature:
```python
def quaternion_transform(q: Quaternion, mat: Matrix) -> Quaternion
```

C API:
```c
Quaternion QuaternionTransform(Quaternion q, Matrix mat)
```

### quaternion_equals
Check whether two given quaternions are almost equal

Python signature:
```python
def quaternion_equals(p: Quaternion, q: Quaternion) -> int
```

C API:
```c
Int QuaternionEquals(Quaternion p, Quaternion q)
```




