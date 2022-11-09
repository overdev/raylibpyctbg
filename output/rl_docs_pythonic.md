# Raylib-py API reference

This is an API reference documentation generated for Raylib 4.2.

<h2 id="toc">Table of Contents</h2>

- <a href="#enums">Enumerations</a>
- <a href="#structs">Structures</a>
- <a href="#funcs">Functions</a>
- <a href="#callbacks">Callbacks</a>
- <a href="#contexts">Context Managers</a>

<h2 id="structs">Structures</h2>

<a href="#AudioStream">AudioStream</a> | <a href="#BoneInfo">BoneInfo</a> | <a href="#BoundingBox">BoundingBox</a> | <a href="#Camera2D">Camera2D</a> | <a href="#Camera3D">Camera3D</a> | <a href="#Color">Color</a> | <a href="#FilePathList">FilePathList</a> | <a href="#Font">Font</a> | <a href="#GlyphInfo">GlyphInfo</a> | <a href="#Image">Image</a> | <a href="#Material">Material</a> | <a href="#MaterialMap">MaterialMap</a> | <a href="#Matrix">Matrix</a> | <a href="#Matrix">Matrix</a> | <a href="#Mesh">Mesh</a> | <a href="#Model">Model</a> | <a href="#ModelAnimation">ModelAnimation</a> | <a href="#Music">Music</a> | <a href="#NPatchInfo">NPatchInfo</a> | <a href="#Ray">Ray</a> | <a href="#RayCollision">RayCollision</a> | <a href="#Rectangle">Rectangle</a> | <a href="#RenderTexture">RenderTexture</a> | <a href="#Shader">Shader</a> | <a href="#Sound">Sound</a> | <a href="#Texture">Texture</a> | <a href="#Transform">Transform</a> | <a href="#Vector2">Vector2</a> | <a href="#Vector3">Vector3</a> | <a href="#Vector4">Vector4</a> | <a href="#VrDeviceInfo">VrDeviceInfo</a> | <a href="#VrStereoConfig">VrStereoConfig</a> | <a href="#Wave">Wave</a> | <a href="#rlDrawCall">rlDrawCall</a> | <a href="#rlRenderBatch">rlRenderBatch</a> | <a href="#rlVertexBuffer">rlVertexBuffer</a>

[ <a href="#toc">ToC</a> ]
<h2 id="Vector2"><code>Vector2</code> structure</h2>

Vector2, 2 components

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`x` | `float` | `Float` | `float` | Vector x component
`y` | `float` | `Float` | `float` | Vector y component

### Properties

Name | API
-----|----
`.byref` | *n/a*
`.length` | <a href="#Vector2Length"><code>vector2length</code></a>
`.length_sqr` | <a href="#Vector2LengthSqr"><code>vector2length_sqr</code></a>

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, vector2_sequence)` | *n/a*
*classmethod* | `.one()` | <a href="#Vector2One"><code>vector2one</code></a>
*method* | `.dot_product(self, v2: 'Vector2')` | <a href="#Vector2DotProduct"><code>vector2dot_product</code></a>
*method* | `.distance(self, v2: 'Vector2')` | <a href="#Vector2Distance"><code>vector2distance</code></a>
*method* | `.distance_sqr(self, v2: 'Vector2')` | <a href="#Vector2DistanceSqr"><code>vector2distance_sqr</code></a>
*method* | `.angle(self, v2: 'Vector2')` | <a href="#Vector2Angle"><code>vector2angle</code></a>
*method* | `.normalize(self)` | <a href="#Vector2Normalize"><code>vector2normalize</code></a>
*method* | `.transform(self, mat: 'Matrix')` | <a href="#Vector2Transform"><code>vector2transform</code></a>
*method* | `.lerp(self, v2: 'Vector2', amount: 'float')` | <a href="#Vector2Lerp"><code>vector2lerp</code></a>
*method* | `.reflect(self, normal: 'Vector2')` | <a href="#Vector2Reflect"><code>vector2reflect</code></a>
*method* | `.rotate(self, angle: 'float')` | <a href="#Vector2Rotate"><code>vector2rotate</code></a>
*method* | `.move_towards(self, target: 'Vector2', max_distance: 'float')` | <a href="#Vector2MoveTowards"><code>vector2move_towards</code></a>
*method* | `.clamp(self, min_: 'Vector2', max_: 'Vector2')` | <a href="#Vector2Clamp"><code>vector2clamp</code></a>
*method* | `.clamp_value(self, min_: 'float', max_: 'float')` | <a href="#Vector2ClampValue"><code>vector2clamp_value</code></a>



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3"><code>Vector3</code> structure</h2>

Vector3, 3 components

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`x` | `float` | `Float` | `float` | Vector x component
`y` | `float` | `Float` | `float` | Vector y component
`z` | `float` | `Float` | `float` | Vector z component

### Properties

Name | API
-----|----
`.byref` | *n/a*
`.length` | <a href="#Vector3Length"><code>vector3length</code></a>
`.length_sqr` | <a href="#Vector3LengthSqr"><code>vector3length_sqr</code></a>

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, vector3_sequence)` | *n/a*
*classmethod* | `.one()` | <a href="#Vector3One"><code>vector3one</code></a>
*method* | `.cross_product(self, v2: 'Vector3')` | <a href="#Vector3CrossProduct"><code>vector3cross_product</code></a>
*method* | `.perpendicular(self)` | <a href="#Vector3Perpendicular"><code>vector3perpendicular</code></a>
*method* | `.dot_product(self, v2: 'Vector3')` | <a href="#Vector3DotProduct"><code>vector3dot_product</code></a>
*method* | `.distance(self, v2: 'Vector3')` | <a href="#Vector3Distance"><code>vector3distance</code></a>
*method* | `.distance_sqr(self, v2: 'Vector3')` | <a href="#Vector3DistanceSqr"><code>vector3distance_sqr</code></a>
*method* | `.angle(self, v2: 'Vector3')` | <a href="#Vector3Angle"><code>vector3angle</code></a>
*method* | `.normalize(self)` | <a href="#Vector3Normalize"><code>vector3normalize</code></a>
*method* | `.ortho_normalize(self, v2: 'Vector3Ptr')` | <a href="#Vector3OrthoNormalize"><code>vector3ortho_normalize</code></a>
*method* | `.transform(self, mat: 'Matrix')` | <a href="#Vector3Transform"><code>vector3transform</code></a>
*method* | `.rotate_by_quaternion(self, q: 'Quaternion')` | <a href="#Vector3RotateByQuaternion"><code>vector3rotate_by_quaternion</code></a>
*method* | `.rotate_by_axis_angle(self, axis: 'Vector3', angle: 'float')` | <a href="#Vector3RotateByAxisAngle"><code>vector3rotate_by_axis_angle</code></a>
*method* | `.lerp(self, v2: 'Vector3', amount: 'float')` | <a href="#Vector3Lerp"><code>vector3lerp</code></a>
*method* | `.reflect(self, normal: 'Vector3')` | <a href="#Vector3Reflect"><code>vector3reflect</code></a>
*method* | `.min(self, v2: 'Vector3')` | <a href="#Vector3Min"><code>vector3min</code></a>
*method* | `.max(self, v2: 'Vector3')` | <a href="#Vector3Max"><code>vector3max</code></a>
*method* | `.barycenter(self, a: 'Vector3', b: 'Vector3', c: 'Vector3')` | <a href="#Vector3Barycenter"><code>vector3barycenter</code></a>
*method* | `.unproject(self, projection: 'Matrix', view: 'Matrix')` | <a href="#Vector3Unproject"><code>vector3unproject</code></a>
*method* | `.to_float_v(self)` | <a href="#Vector3ToFloatV"><code>vector3to_float_v</code></a>
*method* | `.clamp(self, min_: 'Vector3', max_: 'Vector3')` | <a href="#Vector3Clamp"><code>vector3clamp</code></a>
*method* | `.clamp_value(self, min_: 'float', max_: 'float')` | <a href="#Vector3ClampValue"><code>vector3clamp_value</code></a>
*method* | `.refract(self, n: 'Vector3', r: 'float')` | <a href="#Vector3Refract"><code>vector3refract</code></a>



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector4"><code>Vector4</code> structure</h2>

Vector4, 4 components

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`x` | `float` | `Float` | `float` | Vector x component
`y` | `float` | `Float` | `float` | Vector y component
`z` | `float` | `Float` | `float` | Vector z component
`w` | `float` | `Float` | `float` | Vector w component

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, vector4_sequence)` | *n/a*



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Matrix"><code>Matrix</code> structure</h2>

Matrix, 4x4 components, column major, OpenGL style, right handed

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`m0` | `float` | `Float` | `float` | Matrix first row (4 components)
`m4` | `float` | `Float` | `float` | Matrix first row (4 components)
`m8` | `float` | `Float` | `float` | Matrix first row (4 components)
`m12` | `float` | `Float` | `float` | Matrix first row (4 components)
`m1` | `float` | `Float` | `float` | Matrix second row (4 components)
`m5` | `float` | `Float` | `float` | Matrix second row (4 components)
`m9` | `float` | `Float` | `float` | Matrix second row (4 components)
`m13` | `float` | `Float` | `float` | Matrix second row (4 components)
`m2` | `float` | `Float` | `float` | Matrix third row (4 components)
`m6` | `float` | `Float` | `float` | Matrix third row (4 components)
`m10` | `float` | `Float` | `float` | Matrix third row (4 components)
`m14` | `float` | `Float` | `float` | Matrix third row (4 components)
`m3` | `float` | `Float` | `float` | Matrix fourth row (4 components)
`m7` | `float` | `Float` | `float` | Matrix fourth row (4 components)
`m11` | `float` | `Float` | `float` | Matrix fourth row (4 components)
`m15` | `float` | `Float` | `float` | Matrix fourth row (4 components)

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, matrix_sequence)` | *n/a*
*classmethod* | `.identity()` | <a href="#MatrixIdentity"><code>matrix_identity</code></a>
*classmethod* | `.translate(cls, x: 'float', y: 'float', z: 'float')` | <a href="#MatrixTranslate"><code>matrix_translate</code></a>
*classmethod* | `.rotate(cls, axis: 'Vector3', angle: 'float')` | <a href="#MatrixRotate"><code>matrix_rotate</code></a>
*classmethod* | `.rotate_x(cls, angle: 'float')` | <a href="#MatrixRotateX"><code>matrix_rotate_x</code></a>
*classmethod* | `.rotate_y(cls, angle: 'float')` | <a href="#MatrixRotateY"><code>matrix_rotate_y</code></a>
*classmethod* | `.rotate_z(cls, angle: 'float')` | <a href="#MatrixRotateZ"><code>matrix_rotate_z</code></a>
*classmethod* | `.rotate_xyz(cls, angle: 'Vector3')` | <a href="#MatrixRotateXYZ"><code>matrix_rotate_xyz</code></a>
*classmethod* | `.rotate_zyx(cls, angle: 'Vector3')` | <a href="#MatrixRotateZYX"><code>matrix_rotate_zyx</code></a>
*classmethod* | `.scale(cls, x: 'float', y: 'float', z: 'float')` | <a href="#MatrixScale"><code>matrix_scale</code></a>
*classmethod* | `.frustum(cls, left: 'float', right: 'float', bottom: 'float', top: 'float', near: 'float', far: 'float')` | <a href="#MatrixFrustum"><code>matrix_frustum</code></a>
*classmethod* | `.perspective(cls, fovy: 'float', aspect: 'float', near: 'float', far: 'float')` | <a href="#MatrixPerspective"><code>matrix_perspective</code></a>
*classmethod* | `.ortho(cls, left: 'float', right: 'float', bottom: 'float', top: 'float', near: 'float', far: 'float')` | <a href="#MatrixOrtho"><code>matrix_ortho</code></a>
*classmethod* | `.look_at(cls, eye: 'Vector3', target: 'Vector3', up: 'Vector3')` | <a href="#MatrixLookAt"><code>matrix_look_at</code></a>
*method* | `.determinant(self)` | <a href="#MatrixDeterminant"><code>matrix_determinant</code></a>
*method* | `.trace(self)` | <a href="#MatrixTrace"><code>matrix_trace</code></a>
*method* | `.transpose(self)` | <a href="#MatrixTranspose"><code>matrix_transpose</code></a>
*method* | `.invert(self)` | <a href="#MatrixInvert"><code>matrix_invert</code></a>



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Color"><code>Color</code> structure</h2>

Color, 4 components, R8G8B8A8 (32bit)

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`r` | `int` | `UChar` | `unsigned char` | Color red value
`g` | `int` | `UChar` | `unsigned char` | Color green value
`b` | `int` | `UChar` | `unsigned char` | Color blue value
`a` | `int` | `UChar` | `unsigned char` | Color alpha value

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, color_sequence)` | *n/a*
*method* | `.fade(self, alpha: 'float')` | <a href="#Fade"><code>fade</code></a>
*method* | `.to_int(self)` | <a href="#ColorToInt"><code>color_to_int</code></a>
*method* | `.to_hsv(self)` | <a href="#ColorToHSV"><code>color_to_hsv</code></a>
*method* | `.from_hsv(self, saturation: 'float', value: 'float')` | <a href="#ColorFromHSV"><code>color_from_hsv</code></a>
*method* | `.alpha(self, alpha: 'float')` | <a href="#ColorAlpha"><code>color_alpha</code></a>
*method* | `.alpha_blend(self, src: 'Color', tint: 'Color')` | <a href="#ColorAlphaBlend"><code>color_alpha_blend</code></a>



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Rectangle"><code>Rectangle</code> structure</h2>

Rectangle, 4 components

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`x` | `float` | `Float` | `float` | Rectangle top-left corner position x
`y` | `float` | `Float` | `float` | Rectangle top-left corner position y
`width` | `float` | `Float` | `float` | Rectangle width
`height` | `float` | `Float` | `float` | Rectangle height

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, rectangle_sequence)` | *n/a*



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Image"><code>Image</code> structure</h2>

Image, pixel data stored in CPU memory (RAM)

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`data` | `bytes` | `VoidPtr` | `void` | Image raw data
`width` | `int` | `Int` | `int` | Image base width
`height` | `int` | `Int` | `int` | Image base height
`mipmaps` | `int` | `Int` | `int` | Mipmap levels, 1 by default
`format` | `int` | `Int` | `int` | Data format (PixelFormat type)

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*staticmethod* | `.unload_colors(colors: 'ColorPtr')` | <a href="#UnloadImageColors"><code>unload_image_colors</code></a>
*staticmethod* | `.unload_palette(colors: 'ColorPtr')` | <a href="#UnloadImagePalette"><code>unload_image_palette</code></a>
*classmethod* | `.array_of(cls, image_sequence)` | *n/a*
*classmethod* | `.load(cls, file_name: 'Union[str, CharPtr]')` | <a href="#LoadImage"><code>load_image</code></a>
*classmethod* | `.load_raw(cls, file_name: 'Union[str, CharPtr]', width: 'int', height: 'int', format: 'int', header_size: 'int')` | <a href="#LoadImageRaw"><code>load_image_raw</code></a>
*classmethod* | `.load_anim(cls, file_name: 'Union[str, CharPtr]', frames: 'Union[Seq[int], IntPtr]')` | <a href="#LoadImageAnim"><code>load_image_anim</code></a>
*classmethod* | `.load_from_memory(cls, file_type: 'Union[str, CharPtr]', file_data: 'Union[Seq[int], UCharPtr]', data_size: 'int')` | <a href="#LoadImageFromMemory"><code>load_image_from_memory</code></a>
*classmethod* | `.load_from_texture(cls, texture: 'Texture2D')` | <a href="#LoadImageFromTexture"><code>load_image_from_texture</code></a>
*classmethod* | `.load_from_screen()` | <a href="#LoadImageFromScreen"><code>load_image_from_screen</code></a>
*classmethod* | `.gen_color(cls, width: 'int', height: 'int', color: 'Color')` | <a href="#GenImageColor"><code>gen_image_color</code></a>
*classmethod* | `.gen_gradient_h(cls, width: 'int', height: 'int', left: 'Color', right: 'Color')` | <a href="#GenImageGradientH"><code>gen_image_gradient_h</code></a>
*classmethod* | `.gen_gradient_v(cls, width: 'int', height: 'int', top: 'Color', bottom: 'Color')` | <a href="#GenImageGradientV"><code>gen_image_gradient_v</code></a>
*classmethod* | `.gen_gradient_radial(cls, width: 'int', height: 'int', density: 'float', inner: 'Color', outer: 'Color')` | <a href="#GenImageGradientRadial"><code>gen_image_gradient_radial</code></a>
*classmethod* | `.gen_checked(cls, width: 'int', height: 'int', checks_x: 'int', checks_y: 'int', col1: 'Color', col2: 'Color')` | <a href="#GenImageChecked"><code>gen_image_checked</code></a>
*classmethod* | `.gen_white_noise(cls, width: 'int', height: 'int', factor: 'float')` | <a href="#GenImageWhiteNoise"><code>gen_image_white_noise</code></a>
*classmethod* | `.gen_cellular(cls, width: 'int', height: 'int', tile_size: 'int')` | <a href="#GenImageCellular"><code>gen_image_cellular</code></a>
*classmethod* | `.from_image(cls, image: 'Image', rec: 'Rectangle')` | <a href="#ImageFromImage"><code>image_from_image</code></a>
*classmethod* | `.text(cls, text: 'Union[str, CharPtr]', font_size: 'int', color: 'Color')` | <a href="#ImageText"><code>image_text</code></a>
*classmethod* | `.text_ex(cls, font: 'Font', text: 'Union[str, CharPtr]', font_size: 'float', spacing: 'float', tint: 'Color')` | <a href="#ImageTextEx"><code>image_text_ex</code></a>
*method* | `.unload(self)` | <a href="#UnloadImage"><code>unload_image</code></a>
*method* | `.export(self, file_name: 'Union[str, CharPtr]')` | <a href="#ExportImage"><code>export_image</code></a>
*method* | `.export_as_code(self, file_name: 'Union[str, CharPtr]')` | <a href="#ExportImageAsCode"><code>export_image_as_code</code></a>
*method* | `.copy(self)` | <a href="#ImageCopy"><code>image_copy</code></a>
*method* | `.format(self, new_format: 'int')` | <a href="#ImageFormat"><code>image_format</code></a>
*method* | `.to_pot(self, fill: 'Color')` | <a href="#ImageToPOT"><code>image_to_pot</code></a>
*method* | `.crop(self, crop: 'Rectangle')` | <a href="#ImageCrop"><code>image_crop</code></a>
*method* | `.alpha_crop(self, threshold: 'float')` | <a href="#ImageAlphaCrop"><code>image_alpha_crop</code></a>
*method* | `.alpha_clear(self, color: 'Color', threshold: 'float')` | <a href="#ImageAlphaClear"><code>image_alpha_clear</code></a>
*method* | `.alpha_mask(self, alpha_mask: 'Image')` | <a href="#ImageAlphaMask"><code>image_alpha_mask</code></a>
*method* | `.alpha_premultiply(self)` | <a href="#ImageAlphaPremultiply"><code>image_alpha_premultiply</code></a>
*method* | `.resize(self, new_width: 'int', new_height: 'int')` | <a href="#ImageResize"><code>image_resize</code></a>
*method* | `.resize_nn(self, new_width: 'int', new_height: 'int')` | <a href="#ImageResizeNN"><code>image_resize_nn</code></a>
*method* | `.resize_canvas(self, new_width: 'int', new_height: 'int', offset_x: 'int', offset_y: 'int', fill: 'Color')` | <a href="#ImageResizeCanvas"><code>image_resize_canvas</code></a>
*method* | `.mipmaps(self)` | <a href="#ImageMipmaps"><code>image_mipmaps</code></a>
*method* | `.dither(self, r_bpp: 'int', g_bpp: 'int', b_bpp: 'int', a_bpp: 'int')` | <a href="#ImageDither"><code>image_dither</code></a>
*method* | `.flip_vertical(self)` | <a href="#ImageFlipVertical"><code>image_flip_vertical</code></a>
*method* | `.flip_horizontal(self)` | <a href="#ImageFlipHorizontal"><code>image_flip_horizontal</code></a>
*method* | `.rotate_cw(self)` | <a href="#ImageRotateCW"><code>image_rotate_cw</code></a>
*method* | `.rotate_ccw(self)` | <a href="#ImageRotateCCW"><code>image_rotate_ccw</code></a>
*method* | `.color_tint(self, color: 'Color')` | <a href="#ImageColorTint"><code>image_color_tint</code></a>
*method* | `.color_invert(self)` | <a href="#ImageColorInvert"><code>image_color_invert</code></a>
*method* | `.color_grayscale(self)` | <a href="#ImageColorGrayscale"><code>image_color_grayscale</code></a>
*method* | `.color_contrast(self, contrast: 'float')` | <a href="#ImageColorContrast"><code>image_color_contrast</code></a>
*method* | `.color_brightness(self, brightness: 'int')` | <a href="#ImageColorBrightness"><code>image_color_brightness</code></a>
*method* | `.color_replace(self, color: 'Color', replace: 'Color')` | <a href="#ImageColorReplace"><code>image_color_replace</code></a>
*method* | `.clear_background(self, color: 'Color')` | <a href="#ImageClearBackground"><code>image_clear_background</code></a>
*method* | `.draw_pixel(self, pos_x: 'int', pos_y: 'int', color: 'Color')` | <a href="#ImageDrawPixel"><code>image_draw_pixel</code></a>
*method* | `.draw_pixel_v(self, position: 'Vector2', color: 'Color')` | <a href="#ImageDrawPixelV"><code>image_draw_pixel_v</code></a>
*method* | `.draw_line(self, start_pos_x: 'int', start_pos_y: 'int', end_pos_x: 'int', end_pos_y: 'int', color: 'Color')` | <a href="#ImageDrawLine"><code>image_draw_line</code></a>
*method* | `.draw_line_v(self, start: 'Vector2', end: 'Vector2', color: 'Color')` | <a href="#ImageDrawLineV"><code>image_draw_line_v</code></a>
*method* | `.draw_circle(self, center_x: 'int', center_y: 'int', radius: 'int', color: 'Color')` | <a href="#ImageDrawCircle"><code>image_draw_circle</code></a>
*method* | `.draw_circle_v(self, center: 'Vector2', radius: 'int', color: 'Color')` | <a href="#ImageDrawCircleV"><code>image_draw_circle_v</code></a>
*method* | `.draw_rectangle(self, pos_x: 'int', pos_y: 'int', width: 'int', height: 'int', color: 'Color')` | <a href="#ImageDrawRectangle"><code>image_draw_rectangle</code></a>
*method* | `.draw_rectangle_v(self, position: 'Vector2', size: 'Vector2', color: 'Color')` | <a href="#ImageDrawRectangleV"><code>image_draw_rectangle_v</code></a>
*method* | `.draw_rectangle_rec(self, rec: 'Rectangle', color: 'Color')` | <a href="#ImageDrawRectangleRec"><code>image_draw_rectangle_rec</code></a>
*method* | `.draw_rectangle_lines(self, rec: 'Rectangle', thick: 'int', color: 'Color')` | <a href="#ImageDrawRectangleLines"><code>image_draw_rectangle_lines</code></a>
*method* | `.draw(self, src: 'Image', src_rec: 'Rectangle', dst_rec: 'Rectangle', tint: 'Color')` | <a href="#ImageDraw"><code>image_draw</code></a>
*method* | `.draw_text(self, text: 'Union[str, CharPtr]', pos_x: 'int', pos_y: 'int', font_size: 'int', color: 'Color')` | <a href="#ImageDrawText"><code>image_draw_text</code></a>
*method* | `.draw_text_ex(self, font: 'Font', text: 'Union[str, CharPtr]', position: 'Vector2', font_size: 'float', spacing: 'float', tint: 'Color')` | <a href="#ImageDrawTextEx"><code>image_draw_text_ex</code></a>
*method* | `.load_colors(self)` | <a href="#LoadImageColors"><code>load_image_colors</code></a>
*method* | `.load_palette(self, max_palette_size: 'int')` | <a href="#LoadImagePalette"><code>load_image_palette</code></a>
*method* | `.get_alpha_border(self, threshold: 'float')` | <a href="#GetImageAlphaBorder"><code>get_image_alpha_border</code></a>
*method* | `.get_color(self, x: 'int', y: 'int')` | <a href="#GetImageColor"><code>get_image_color</code></a>



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Texture"><code>Texture</code> structure</h2>

Texture, tex data stored in GPU memory (VRAM)

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`id` | `int` | `UInt` | `unsigned int` | OpenGL texture id
`width` | `int` | `Int` | `int` | Texture base width
`height` | `int` | `Int` | `int` | Texture base height
`mipmaps` | `int` | `Int` | `int` | Mipmap levels, 1 by default
`format` | `int` | `Int` | `int` | Data format (PixelFormat type)

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, texture_sequence)` | *n/a*



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="RenderTexture"><code>RenderTexture</code> structure</h2>

RenderTexture, fbo for texture rendering

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`id` | `int` | `UInt` | `unsigned int` | OpenGL framebuffer object id
`texture` | `Texture` | `Texture` | `Texture` | Color buffer attachment texture
`depth` | `Texture` | `Texture` | `Texture` | Depth buffer attachment texture

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, render_texture_sequence)` | *n/a*



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="NPatchInfo"><code>NPatchInfo</code> structure</h2>

NPatchInfo, n-patch layout info

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`source` | `Rectangle` | `Rectangle` | `Rectangle` | Texture source rectangle
`left` | `int` | `Int` | `int` | Left border offset
`top` | `int` | `Int` | `int` | Top border offset
`right` | `int` | `Int` | `int` | Right border offset
`bottom` | `int` | `Int` | `int` | Bottom border offset
`layout` | `int` | `Int` | `int` | Layout of the n-patch: 3x3, 1x3 or 3x1

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, npatch_info_sequence)` | *n/a*



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GlyphInfo"><code>GlyphInfo</code> structure</h2>

GlyphInfo, font characters glyphs info

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`value` | `int` | `Int` | `int` | Character value (Unicode)
`offset_x` | `int` | `Int` | `int` | Character offset X when drawing
`offset_y` | `int` | `Int` | `int` | Character offset Y when drawing
`advance_x` | `int` | `Int` | `int` | Character advance position X
`image` | `Image` | `Image` | `Image` | Character image data

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, glyph_info_sequence)` | *n/a*



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Font"><code>Font</code> structure</h2>

Font, font texture and GlyphInfo array data

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`base_size` | `int` | `Int` | `int` | Base size (default chars height)
`glyph_count` | `int` | `Int` | `int` | Number of glyph characters
`glyph_padding` | `int` | `Int` | `int` | Padding around the glyph characters
`texture` | `Texture2D` | `Texture2D` | `Texture2D` | Texture atlas containing the glyphs
`recs` | `RectanglePtr` | `RectanglePtr` | `Rectangle *` | Rectangles in texture for the glyphs
`glyphs` | `GlyphInfoPtr` | `GlyphInfoPtr` | `GlyphInfo *` | Glyphs info data

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*staticmethod* | `.load_data(file_data: 'Union[Seq[int], UCharPtr]', data_size: 'int', font_size: 'int', font_chars: 'Union[Seq[int], IntPtr]', glyph_count: 'int', type: 'int')` | <a href="#LoadFontData"><code>load_font_data</code></a>
*staticmethod* | `.unload_data(chars: 'GlyphInfoPtr', glyph_count: 'int')` | <a href="#UnloadFontData"><code>unload_font_data</code></a>
*classmethod* | `.array_of(cls, font_sequence)` | *n/a*
*classmethod* | `.load(cls, file_name: 'Union[str, CharPtr]')` | <a href="#LoadFont"><code>load_font</code></a>
*classmethod* | `.load_ex(cls, file_name: 'Union[str, CharPtr]', font_size: 'int', font_chars: 'Union[Seq[int], IntPtr]', glyph_count: 'int')` | <a href="#LoadFontEx"><code>load_font_ex</code></a>
*classmethod* | `.load_from_image(cls, image: 'Image', key: 'Color', first_char: 'int')` | <a href="#LoadFontFromImage"><code>load_font_from_image</code></a>
*classmethod* | `.load_from_memory(cls, file_type: 'Union[str, CharPtr]', file_data: 'Union[Seq[int], UCharPtr]', data_size: 'int', font_size: 'int', font_chars: 'Union[Seq[int], IntPtr]', glyph_count: 'int')` | <a href="#LoadFontFromMemory"><code>load_font_from_memory</code></a>
*method* | `.unload(self)` | <a href="#UnloadFont"><code>unload_font</code></a>
*method* | `.draw_text_ex(self, text: 'Union[str, CharPtr]', position: 'Vector2', font_size: 'float', spacing: 'float', tint: 'Color')` | <a href="#DrawTextEx"><code>draw_text_ex</code></a>
*method* | `.draw_text_pro(self, text: 'Union[str, CharPtr]', position: 'Vector2', origin: 'Vector2', rotation: 'float', font_size: 'float', spacing: 'float', tint: 'Color')` | <a href="#DrawTextPro"><code>draw_text_pro</code></a>
*method* | `.draw_text_codepoint(self, codepoint: 'int', position: 'Vector2', font_size: 'float', tint: 'Color')` | <a href="#DrawTextCodepoint"><code>draw_text_codepoint</code></a>
*method* | `.draw_text_codepoints(self, codepoints: 'Union[Seq[int], IntPtr]', position: 'Vector2', font_size: 'float', spacing: 'float', tint: 'Color')` | <a href="#DrawTextCodepoints"><code>draw_text_codepoints</code></a>
*method* | `.measure_text_ex(self, text: 'Union[str, CharPtr]', font_size: 'float', spacing: 'float')` | <a href="#MeasureTextEx"><code>measure_text_ex</code></a>
*method* | `.get_glyph_index(self, codepoint: 'int')` | <a href="#GetGlyphIndex"><code>get_glyph_index</code></a>
*method* | `.get_glyph_info(self, codepoint: 'int')` | <a href="#GetGlyphInfo"><code>get_glyph_info</code></a>
*method* | `.get_glyph_atlas_rec(self, codepoint: 'int')` | <a href="#GetGlyphAtlasRec"><code>get_glyph_atlas_rec</code></a>



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Camera3D"><code>Camera3D</code> structure</h2>

Camera, defines position/orientation in 3d space

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`position` | `Vector3` | `Vector3` | `Vector3` | Camera position
`target` | `Vector3` | `Vector3` | `Vector3` | Camera target it looks-at
`up` | `Vector3` | `Vector3` | `Vector3` | Camera up vector (rotation over its axis)
`fovy` | `float` | `Float` | `float` | Camera field-of-view apperture in Y (degrees) in perspective, used as near plane width in orthographic
`projection` | `int` | `Int` | `int` | Camera projection: CAMERA_PERSPECTIVE or CAMERA_ORTHOGRAPHIC

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, camera3d_sequence)` | *n/a*
*method* | `.set_mode(self, mode: 'int')` | <a href="#SetCameraMode"><code>set_camera_mode</code></a>

### Context Manager

Context | API
--------|----
Enter | begin_mode3d
Leave | end_mode3d



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Camera2D"><code>Camera2D</code> structure</h2>

Camera2D, defines position/orientation in 2d space

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`offset` | `Vector2` | `Vector2` | `Vector2` | Camera offset (displacement from target)
`target` | `Vector2` | `Vector2` | `Vector2` | Camera target (rotation and zoom origin)
`rotation` | `float` | `Float` | `float` | Camera rotation in degrees
`zoom` | `float` | `Float` | `float` | Camera zoom (scaling), should be 1.0f by default

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, camera2d_sequence)` | *n/a*

### Context Manager

Context | API
--------|----
Enter | begin_mode2d
Leave | end_mode2d



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Mesh"><code>Mesh</code> structure</h2>

Mesh, vertex data and vao/vbo

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`vertex_count` | `int` | `Int` | `int` | Number of vertices stored in arrays
`triangle_count` | `int` | `Int` | `int` | Number of triangles stored (indexed or not)
`vertices` | `Union[Seq[float], FloatPtr]` | `FloatPtr` | `float` | Vertex position (XYZ - 3 components per vertex) (shader-location = 0)
`texcoords` | `Union[Seq[float], FloatPtr]` | `FloatPtr` | `float` | Vertex texture coordinates (UV - 2 components per vertex) (shader-location = 1)
`texcoords2` | `Union[Seq[float], FloatPtr]` | `FloatPtr` | `float` | Vertex texture second coordinates (UV - 2 components per vertex) (shader-location = 5)
`normals` | `Union[Seq[float], FloatPtr]` | `FloatPtr` | `float` | Vertex normals (XYZ - 3 components per vertex) (shader-location = 2)
`tangents` | `Union[Seq[float], FloatPtr]` | `FloatPtr` | `float` | Vertex tangents (XYZW - 4 components per vertex) (shader-location = 4)
`colors` | `Union[Seq[int], UCharPtr]` | `UCharPtr` | `unsigned char *` | Vertex colors (RGBA - 4 components per vertex) (shader-location = 3)
`indices` | `Union[Seq[int], UShortPtr]` | `UShortPtr` | `unsigned short` | Vertex indices (in case vertex data comes indexed)
`anim_vertices` | `Union[Seq[float], FloatPtr]` | `FloatPtr` | `float` | Animated vertex positions (after bones transformations)
`anim_normals` | `Union[Seq[float], FloatPtr]` | `FloatPtr` | `float` | Animated normals (after bones transformations)
`bone_ids` | `Union[Seq[int], UCharPtr]` | `UCharPtr` | `unsigned char *` | Vertex bone ids, max 255 bone ids, up to 4 bones influence by vertex (skinning)
`bone_weights` | `Union[Seq[float], FloatPtr]` | `FloatPtr` | `float` | Vertex bone weight, up to 4 bones influence by vertex (skinning)
`vao_id` | `int` | `UInt` | `unsigned int` | OpenGL Vertex Array Object id
`vbo_id` | `Union[Seq[int], UIntPtr]` | `UIntPtr` | `unsigned int` | OpenGL Vertex Buffer Objects id (default vertex data)

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, mesh_sequence)` | *n/a*
*classmethod* | `.gen_poly(cls, sides: 'int', radius: 'float')` | <a href="#GenMeshPoly"><code>gen_mesh_poly</code></a>
*classmethod* | `.gen_plane(cls, width: 'float', length: 'float', res_x: 'int', res_z: 'int')` | <a href="#GenMeshPlane"><code>gen_mesh_plane</code></a>
*classmethod* | `.gen_cube(cls, width: 'float', height: 'float', length: 'float')` | <a href="#GenMeshCube"><code>gen_mesh_cube</code></a>
*classmethod* | `.gen_sphere(cls, radius: 'float', rings: 'int', slices: 'int')` | <a href="#GenMeshSphere"><code>gen_mesh_sphere</code></a>
*classmethod* | `.gen_hemi_sphere(cls, radius: 'float', rings: 'int', slices: 'int')` | <a href="#GenMeshHemiSphere"><code>gen_mesh_hemi_sphere</code></a>
*classmethod* | `.gen_cylinder(cls, radius: 'float', height: 'float', slices: 'int')` | <a href="#GenMeshCylinder"><code>gen_mesh_cylinder</code></a>
*classmethod* | `.gen_cone(cls, radius: 'float', height: 'float', slices: 'int')` | <a href="#GenMeshCone"><code>gen_mesh_cone</code></a>
*classmethod* | `.gen_torus(cls, radius: 'float', size: 'float', rad_seg: 'int', sides: 'int')` | <a href="#GenMeshTorus"><code>gen_mesh_torus</code></a>
*classmethod* | `.gen_knot(cls, radius: 'float', size: 'float', rad_seg: 'int', sides: 'int')` | <a href="#GenMeshKnot"><code>gen_mesh_knot</code></a>
*classmethod* | `.gen_heightmap(cls, heightmap: 'Image', size: 'Vector3')` | <a href="#GenMeshHeightmap"><code>gen_mesh_heightmap</code></a>
*classmethod* | `.gen_cubicmap(cls, cubicmap: 'Image', cube_size: 'Vector3')` | <a href="#GenMeshCubicmap"><code>gen_mesh_cubicmap</code></a>
*method* | `.upload(self, dynamic: 'bool')` | <a href="#UploadMesh"><code>upload_mesh</code></a>
*method* | `.update_buffer(self, index: 'int', data: 'bytes', data_size: 'int', offset: 'int')` | <a href="#UpdateMeshBuffer"><code>update_mesh_buffer</code></a>
*method* | `.unload(self)` | <a href="#UnloadMesh"><code>unload_mesh</code></a>
*method* | `.draw(self, material: 'Material', transform: 'Matrix')` | <a href="#DrawMesh"><code>draw_mesh</code></a>
*method* | `.draw_instanced(self, material: 'Material', transforms: 'MatrixPtr', instances: 'int')` | <a href="#DrawMeshInstanced"><code>draw_mesh_instanced</code></a>
*method* | `.export(self, file_name: 'Union[str, CharPtr]')` | <a href="#ExportMesh"><code>export_mesh</code></a>
*method* | `.get_bounding_box(self)` | <a href="#GetMeshBoundingBox"><code>get_mesh_bounding_box</code></a>
*method* | `.gen_tangents(self)` | <a href="#GenMeshTangents"><code>gen_mesh_tangents</code></a>



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Shader"><code>Shader</code> structure</h2>

Shader

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`id` | `int` | `UInt` | `unsigned int` | Shader program id
`locs` | `Union[Seq[int], IntPtr]` | `IntPtr` | `int` | Shader locations array (RL_MAX_SHADER_LOCATIONS)

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, shader_sequence)` | *n/a*
*classmethod* | `.load(cls, vs_file_name: 'Union[str, CharPtr]', fs_file_name: 'Union[str, CharPtr]')` | <a href="#LoadShader"><code>load_shader</code></a>
*classmethod* | `.load_from_memory(cls, vs_code: 'Union[str, CharPtr]', fs_code: 'Union[str, CharPtr]')` | <a href="#LoadShaderFromMemory"><code>load_shader_from_memory</code></a>
*method* | `.get_location(self, uniform_name: 'Union[str, CharPtr]')` | <a href="#GetShaderLocation"><code>get_shader_location</code></a>
*method* | `.get_location_attrib(self, attrib_name: 'Union[str, CharPtr]')` | <a href="#GetShaderLocationAttrib"><code>get_shader_location_attrib</code></a>
*method* | `.set_value(self, loc_index: 'int', value: 'bytes', uniform_type: 'int')` | <a href="#SetShaderValue"><code>set_shader_value</code></a>
*method* | `.set_value_v(self, loc_index: 'int', value: 'bytes', uniform_type: 'int', count: 'int')` | <a href="#SetShaderValueV"><code>set_shader_value_v</code></a>
*method* | `.set_value_matrix(self, loc_index: 'int', mat: 'Matrix')` | <a href="#SetShaderValueMatrix"><code>set_shader_value_matrix</code></a>
*method* | `.set_value_texture(self, loc_index: 'int', texture: 'Texture2D')` | <a href="#SetShaderValueTexture"><code>set_shader_value_texture</code></a>
*method* | `.unload(self)` | <a href="#UnloadShader"><code>unload_shader</code></a>

### Context Manager

Context | API
--------|----
Enter | begin_shader_mode
Leave | end_shader_mode



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MaterialMap"><code>MaterialMap</code> structure</h2>

MaterialMap

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`texture` | `Texture2D` | `Texture2D` | `Texture2D` | Material map texture
`color` | `Color` | `Color` | `Color` | Material map color
`value` | `float` | `Float` | `float` | Material map value

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, material_map_sequence)` | *n/a*



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Material"><code>Material</code> structure</h2>

Material, includes shader and maps

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`shader` | `Shader` | `Shader` | `Shader` | Material shader
`maps` | `MaterialMapPtr` | `MaterialMapPtr` | `MaterialMap *` | Material maps array (MAX_MATERIAL_MAPS)
`params` | `Seq[float]` | `Float * 4` | `float[4]` | Material generic parameters (if required)

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, material_sequence)` | *n/a*
*classmethod* | `.load_materials(cls, file_name: 'Union[str, CharPtr]')` | <a href="#LoadMaterials"><code>load_materials</code></a>
*classmethod* | `.load_default()` | <a href="#LoadMaterialDefault"><code>load_material_default</code></a>
*method* | `.unload(self)` | <a href="#UnloadMaterial"><code>unload_material</code></a>
*method* | `.set_texture(self, map_type: 'int', texture: 'Texture2D')` | <a href="#SetMaterialTexture"><code>set_material_texture</code></a>



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Transform"><code>Transform</code> structure</h2>

Transform, vectex transformation data

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`translation` | `Vector3` | `Vector3` | `Vector3` | Translation
`rotation` | `Quaternion` | `Quaternion` | `Quaternion` | Rotation
`scale` | `Vector3` | `Vector3` | `Vector3` | Scale

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, transform_sequence)` | *n/a*



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="BoneInfo"><code>BoneInfo</code> structure</h2>

Bone, skeletal animation bone

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`name` | `str` | `CharPtr` | `char[32]` | Bone name
`parent` | `int` | `Int` | `int` | Bone parent

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, bone_info_sequence)` | *n/a*



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Model"><code>Model</code> structure</h2>

Model, meshes, materials and animation data

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`transform` | `Matrix` | `Matrix` | `Matrix` | Local transform matrix
`mesh_count` | `int` | `Int` | `int` | Number of meshes
`material_count` | `int` | `Int` | `int` | Number of materials
`meshes` | `MeshPtr` | `MeshPtr` | `Mesh *` | Meshes array
`materials` | `MaterialPtr` | `MaterialPtr` | `Material *` | Materials array
`mesh_material` | `Union[Seq[int], IntPtr]` | `IntPtr` | `int` | Mesh material number
`bone_count` | `int` | `Int` | `int` | Number of bones
`bones` | `BoneInfoPtr` | `BoneInfoPtr` | `BoneInfo *` | Bones information (skeleton)
`bind_pose` | `TransformPtr` | `TransformPtr` | `Transform *` | Bones base transformation (pose)

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, model_sequence)` | *n/a*
*classmethod* | `.load(cls, file_name: 'Union[str, CharPtr]')` | <a href="#LoadModel"><code>load_model</code></a>
*classmethod* | `.load_from_mesh(cls, mesh: 'Mesh')` | <a href="#LoadModelFromMesh"><code>load_model_from_mesh</code></a>
*method* | `.is_animation_valid(self, anim: 'ModelAnimation')` | <a href="#IsModelAnimationValid"><code>is_model_animation_valid</code></a>
*method* | `.update_animation(self, anim: 'ModelAnimation', frame: 'int')` | <a href="#UpdateModelAnimation"><code>update_model_animation</code></a>
*method* | `.set_mesh_material(self, mesh_id: 'int', material_id: 'int')` | <a href="#SetModelMeshMaterial"><code>set_model_mesh_material</code></a>
*method* | `.unload(self)` | <a href="#UnloadModel"><code>unload_model</code></a>
*method* | `.unload_keep_meshes(self)` | <a href="#UnloadModelKeepMeshes"><code>unload_model_keep_meshes</code></a>
*method* | `.get_bounding_box(self)` | <a href="#GetModelBoundingBox"><code>get_model_bounding_box</code></a>
*method* | `.draw(self, position: 'Vector3', scale: 'float', tint: 'Color')` | <a href="#DrawModel"><code>draw_model</code></a>
*method* | `.draw_ex(self, position: 'Vector3', rotation_axis: 'Vector3', rotation_angle: 'float', scale: 'Vector3', tint: 'Color')` | <a href="#DrawModelEx"><code>draw_model_ex</code></a>
*method* | `.draw_wires(self, position: 'Vector3', scale: 'float', tint: 'Color')` | <a href="#DrawModelWires"><code>draw_model_wires</code></a>
*method* | `.draw_wires_ex(self, position: 'Vector3', rotation_axis: 'Vector3', rotation_angle: 'float', scale: 'Vector3', tint: 'Color')` | <a href="#DrawModelWiresEx"><code>draw_model_wires_ex</code></a>



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ModelAnimation"><code>ModelAnimation</code> structure</h2>

ModelAnimation

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`bone_count` | `int` | `Int` | `int` | Number of bones
`frame_count` | `int` | `Int` | `int` | Number of animation frames
`bones` | `BoneInfoPtr` | `BoneInfoPtr` | `BoneInfo *` | Bones information (skeleton)
`frame_poses` | `TransformPtr` | `TransformPtr` | `Transform **` | Poses array by frame

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, model_animation_sequence)` | *n/a*



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Ray"><code>Ray</code> structure</h2>

Ray, ray for raycasting

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`position` | `Vector3` | `Vector3` | `Vector3` | Ray position (origin)
`direction` | `Vector3` | `Vector3` | `Vector3` | Ray direction

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, ray_sequence)` | *n/a*



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="RayCollision"><code>RayCollision</code> structure</h2>

RayCollision, ray hit information

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`hit` | `bool` | `Bool` | `bool` | Did the ray hit something?
`distance` | `float` | `Float` | `float` | Distance to nearest hit
`point` | `Vector3` | `Vector3` | `Vector3` | Point of nearest hit
`normal` | `Vector3` | `Vector3` | `Vector3` | Surface normal of hit

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, ray_collision_sequence)` | *n/a*



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="BoundingBox"><code>BoundingBox</code> structure</h2>

BoundingBox

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`min` | `Vector3` | `Vector3` | `Vector3` | Minimum vertex box-corner
`max` | `Vector3` | `Vector3` | `Vector3` | Maximum vertex box-corner

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, bounding_box_sequence)` | *n/a*



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Wave"><code>Wave</code> structure</h2>

Wave, audio wave data

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`frame_count` | `int` | `UInt` | `unsigned int` | Total number of frames (considering channels)
`sample_rate` | `int` | `UInt` | `unsigned int` | Frequency (samples per second)
`sample_size` | `int` | `UInt` | `unsigned int` | Bit depth (bits per sample): 8, 16, 32 (24 not supported)
`channels` | `int` | `UInt` | `unsigned int` | Number of channels (1-mono, 2-stereo, ...)
`data` | `bytes` | `VoidPtr` | `void` | Buffer data pointer

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, wave_sequence)` | *n/a*
*classmethod* | `.load(cls, file_name: 'Union[str, CharPtr]')` | <a href="#LoadWave"><code>load_wave</code></a>
*classmethod* | `.load_from_memory(cls, file_type: 'Union[str, CharPtr]', file_data: 'Union[Seq[int], UCharPtr]', data_size: 'int')` | <a href="#LoadWaveFromMemory"><code>load_wave_from_memory</code></a>
*method* | `.copy(self)` | <a href="#WaveCopy"><code>wave_copy</code></a>
*method* | `.crop(self, init_sample: 'int', final_sample: 'int')` | <a href="#WaveCrop"><code>wave_crop</code></a>
*method* | `.format(self, sample_rate: 'int', sample_size: 'int', channels: 'int')` | <a href="#WaveFormat"><code>wave_format</code></a>
*method* | `.format(self)` | <a href="#LoadWaveSamples"><code>load_wave_samples</code></a>
*method* | `.export(self, file_name: 'Union[str, CharPtr]')` | <a href="#ExportWave"><code>export_wave</code></a>
*method* | `.export_as_code(self, file_name: 'Union[str, CharPtr]')` | <a href="#ExportWaveAsCode"><code>export_wave_as_code</code></a>
*method* | `.unload(self)` | <a href="#UnloadWave"><code>unload_wave</code></a>
*method* | `.unload_samples(self)` | <a href="#UnloadWaveSamples"><code>unload_wave_samples</code></a>



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="AudioStream"><code>AudioStream</code> structure</h2>

AudioStream, custom audio stream

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`buffer` | `rAudioBufferPtr` | `rAudioBufferPtr` | `rAudioBuffer *` | Pointer to internal data used by the audio system
`processor` | `rAudioProcessorPtr` | `rAudioProcessorPtr` | `rAudioProcessor *` | Pointer to internal data processor, useful for audio effects
`sample_rate` | `int` | `UInt` | `unsigned int` | Frequency (samples per second)
`sample_size` | `int` | `UInt` | `unsigned int` | Bit depth (bits per sample): 8, 16, 32 (24 not supported)
`channels` | `int` | `UInt` | `unsigned int` | Number of channels (1-mono, 2-stereo, ...)

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, audio_stream_sequence)` | *n/a*
*classmethod* | `.load(cls, sample_rate: 'int', sample_size: 'int', channels: 'int')` | <a href="#LoadAudioStream"><code>load_audio_stream</code></a>
*method* | `.unload(self)` | <a href="#UnloadAudioStream"><code>unload_audio_stream</code></a>
*method* | `.update(self, data: 'bytes', frame_count: 'int')` | <a href="#UpdateAudioStream"><code>update_audio_stream</code></a>
*method* | `.is_processed(self)` | <a href="#IsAudioStreamProcessed"><code>is_audio_stream_processed</code></a>
*method* | `.play(self)` | <a href="#PlayAudioStream"><code>play_audio_stream</code></a>
*method* | `.pause(self)` | <a href="#PauseAudioStream"><code>pause_audio_stream</code></a>
*method* | `.resume(self)` | <a href="#ResumeAudioStream"><code>resume_audio_stream</code></a>
*method* | `.is_playing(self)` | <a href="#IsAudioStreamPlaying"><code>is_audio_stream_playing</code></a>
*method* | `.stop(self)` | <a href="#StopAudioStream"><code>stop_audio_stream</code></a>
*method* | `.set_volume(self, volume: 'float')` | <a href="#SetAudioStreamVolume"><code>set_audio_stream_volume</code></a>
*method* | `.set_pitch(self, pitch: 'float')` | <a href="#SetAudioStreamPitch"><code>set_audio_stream_pitch</code></a>
*method* | `.set_pan(self, pan: 'float')` | <a href="#SetAudioStreamPan"><code>set_audio_stream_pan</code></a>
*method* | `.set_buffer_size_default(self)` | <a href="#SetAudioStreamBufferSizeDefault"><code>set_audio_stream_buffer_size_default</code></a>
*method* | `.set_callback(self, callback: 'AudioCallback')` | <a href="#SetAudioStreamCallback"><code>set_audio_stream_callback</code></a>
*method* | `.attach_processor(self, processor: 'AudioCallback')` | <a href="#AttachAudioStreamProcessor"><code>attach_audio_stream_processor</code></a>
*method* | `.detach_processor(self, processor: 'AudioCallback')` | <a href="#DetachAudioStreamProcessor"><code>detach_audio_stream_processor</code></a>



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Sound"><code>Sound</code> structure</h2>

Sound

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`stream` | `AudioStream` | `AudioStream` | `AudioStream` | Audio stream
`frame_count` | `int` | `UInt` | `unsigned int` | Total number of frames (considering channels)

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*staticmethod* | `.get_sounds_playing()` | <a href="#GetSoundsPlaying"><code>get_sounds_playing</code></a>
*staticmethod* | `.stop_multi()` | <a href="#StopSoundMulti"><code>stop_sound_multi</code></a>
*classmethod* | `.array_of(cls, sound_sequence)` | *n/a*
*classmethod* | `.load(cls, file_name: 'Union[str, CharPtr]')` | <a href="#LoadSound"><code>load_sound</code></a>
*classmethod* | `.load_from_wave(cls, wave: 'Wave')` | <a href="#LoadSoundFromWave"><code>load_sound_from_wave</code></a>
*method* | `.play(self)` | <a href="#PlaySound"><code>play_sound</code></a>
*method* | `.stop(self)` | <a href="#StopSound"><code>stop_sound</code></a>
*method* | `.pause(self)` | <a href="#PauseSound"><code>pause_sound</code></a>
*method* | `.resume(self)` | <a href="#ResumeSound"><code>resume_sound</code></a>
*method* | `.play_multi(self)` | <a href="#PlaySoundMulti"><code>play_sound_multi</code></a>
*method* | `.is_playing(self)` | <a href="#IsSoundPlaying"><code>is_sound_playing</code></a>
*method* | `.set_volume(self, volume: 'float')` | <a href="#SetSoundVolume"><code>set_sound_volume</code></a>
*method* | `.set_pitch(self, pitch: 'float')` | <a href="#SetSoundPitch"><code>set_sound_pitch</code></a>
*method* | `.set_pan(self, pan: 'float')` | <a href="#SetSoundPan"><code>set_sound_pan</code></a>
*method* | `.unload(self)` | <a href="#UnloadSound"><code>unload_sound</code></a>
*method* | `.update(self, data: 'bytes', sample_count: 'int')` | <a href="#UpdateSound"><code>update_sound</code></a>



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Music"><code>Music</code> structure</h2>

Music, audio stream, anything longer than ~10 seconds should be streamed

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`stream` | `AudioStream` | `AudioStream` | `AudioStream` | Audio stream
`frame_count` | `int` | `UInt` | `unsigned int` | Total number of frames (considering channels)
`looping` | `bool` | `Bool` | `bool` | Music looping enable
`ctx_type` | `int` | `Int` | `int` | Type of music context (audio filetype)
`ctx_data` | `bytes` | `VoidPtr` | `void` | Audio context data, depends on type

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*staticmethod* | `.load(file_name: 'Union[str, CharPtr]')` | <a href="#LoadMusicStream"><code>load_music_stream</code></a>
*staticmethod* | `.load_from_memory(file_type: 'Union[str, CharPtr]', data: 'Union[Seq[int], UCharPtr]', data_size: 'int')` | <a href="#LoadMusicStreamFromMemory"><code>load_music_stream_from_memory</code></a>
*classmethod* | `.array_of(cls, music_sequence)` | *n/a*
*method* | `.play(self)` | <a href="#PlayMusicStream"><code>play_music_stream</code></a>
*method* | `.is_playing(self)` | <a href="#IsMusicStreamPlaying"><code>is_music_stream_playing</code></a>
*method* | `.update(self)` | <a href="#UpdateMusicStream"><code>update_music_stream</code></a>
*method* | `.stop(self)` | <a href="#StopMusicStream"><code>stop_music_stream</code></a>
*method* | `.pause(self)` | <a href="#PauseMusicStream"><code>pause_music_stream</code></a>
*method* | `.resume(self)` | <a href="#ResumeMusicStream"><code>resume_music_stream</code></a>
*method* | `.seek(self, position: 'float')` | <a href="#SeekMusicStream"><code>seek_music_stream</code></a>
*method* | `.set_volume(self, volume: 'float')` | <a href="#SetMusicVolume"><code>set_music_volume</code></a>
*method* | `.set_pitch(self, pitch: 'float')` | <a href="#SetMusicPitch"><code>set_music_pitch</code></a>
*method* | `.set_pan(self, pan: 'float')` | <a href="#SetMusicPan"><code>set_music_pan</code></a>
*method* | `.get_time_length(self)` | <a href="#GetMusicTimeLength"><code>get_music_time_length</code></a>
*method* | `.get_time_played(self)` | <a href="#GetMusicTimePlayed"><code>get_music_time_played</code></a>



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="VrDeviceInfo"><code>VrDeviceInfo</code> structure</h2>

VrDeviceInfo, Head-Mounted-Display device parameters

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`h_resolution` | `int` | `Int` | `int` | Horizontal resolution in pixels
`v_resolution` | `int` | `Int` | `int` | Vertical resolution in pixels
`h_screen_size` | `float` | `Float` | `float` | Horizontal size in meters
`v_screen_size` | `float` | `Float` | `float` | Vertical size in meters
`v_screen_center` | `float` | `Float` | `float` | Screen center in meters
`eye_to_screen_distance` | `float` | `Float` | `float` | Distance between eye and display in meters
`lens_separation_distance` | `float` | `Float` | `float` | Lens separation distance in meters
`interpupillary_distance` | `float` | `Float` | `float` | IPD (distance between pupils) in meters
`lens_distortion_values` | `Seq[float]` | `Float * 4` | `float[4]` | Lens distortion constant parameters
`chroma_ab_correction` | `Seq[float]` | `Float * 4` | `float[4]` | Chromatic aberration correction parameters

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, vr_device_info_sequence)` | *n/a*



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="VrStereoConfig"><code>VrStereoConfig</code> structure</h2>

VrStereoConfig, VR stereo rendering configuration for simulator

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`projection` | `Seq[Matrix]` | `Matrix * 2` | `Matrix[2]` | VR projection matrices (per eye)
`view_offset` | `Seq[Matrix]` | `Matrix * 2` | `Matrix[2]` | VR view offset matrices (per eye)
`left_lens_center` | `Seq[float]` | `Float * 2` | `float[2]` | VR left lens center
`right_lens_center` | `Seq[float]` | `Float * 2` | `float[2]` | VR right lens center
`left_screen_center` | `Seq[float]` | `Float * 2` | `float[2]` | VR left screen center
`right_screen_center` | `Seq[float]` | `Float * 2` | `float[2]` | VR right screen center
`scale` | `Seq[float]` | `Float * 2` | `float[2]` | VR distortion scale
`scale_in` | `Seq[float]` | `Float * 2` | `float[2]` | VR distortion scale in

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, vr_stereo_config_sequence)` | *n/a*

### Context Manager

Context | API
--------|----
Enter | begin_vr_stereo_mode
Leave | end_vr_stereo_mode



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="FilePathList"><code>FilePathList</code> structure</h2>

File path list

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`capacity` | `int` | `UInt` | `unsigned int` | Filepaths max entries
`count` | `int` | `UInt` | `unsigned int` | Filepaths entries count
`paths` | `Seq[Union[str, CharPtr]]` | `CharPtrPtr` | `char **` | Filepaths entries

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, file_path_list_sequence)` | *n/a*



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlVertexBuffer"><code>rlVertexBuffer</code> structure</h2>

Dynamic vertex buffers (position + texcoords + colors + indices arrays)

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`element_count` | `int` | `Int` | `int` | Number of elements in the buffer (QUADS)
`vertices` | `Union[Seq[float], FloatPtr]` | `FloatPtr` | `float` | Vertex position (XYZ - 3 components per vertex) (shader-location = 0)
`texcoords` | `Union[Seq[float], FloatPtr]` | `FloatPtr` | `float` | Vertex texture coordinates (UV - 2 components per vertex) (shader-location = 1)
`colors` | `Union[Seq[int], UCharPtr]` | `UCharPtr` | `unsigned char *` | Vertex colors (RGBA - 4 components per vertex) (shader-location = 3)
`indices` | `Union[Seq[int], UIntPtr]` | `UIntPtr` | `unsigned int` | Vertex indices (in case vertex data comes indexed) (6 indices per quad)
`vao_id` | `int` | `UInt` | `unsigned int` | OpenGL Vertex Array Object id
`vbo_id` | `Seq[int]` | `Int * 4` | `unsigned int[4]` | OpenGL Vertex Buffer Objects id (4 types of vertex data)

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, rl_vertex_buffer_sequence)` | *n/a*



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDrawCall"><code>rlDrawCall</code> structure</h2>

of those state-change happens (this is done in core module)

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`mode` | `int` | `Int` | `int` | Drawing mode: LINES, TRIANGLES, QUADS
`vertex_count` | `int` | `Int` | `int` | Number of vertex of the draw
`vertex_alignment` | `int` | `Int` | `int` | Number of vertex required for index alignment (LINES, TRIANGLES)
`texture_id` | `int` | `UInt` | `unsigned int` | Texture id to be used on the draw -> Use to create new draw call if changes

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, rl_draw_call_sequence)` | *n/a*



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlRenderBatch"><code>rlRenderBatch</code> structure</h2>

rlRenderBatch type

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`buffer_count` | `int` | `Int` | `int` | Number of vertex buffers (multi-buffering support)
`current_buffer` | `int` | `Int` | `int` | Current buffer tracking in case of multi-buffering
`vertex_buffer` | `rlVertexBufferPtr` | `rlVertexBufferPtr` | `rlVertexBuffer *` | Dynamic buffer(s) for vertex data
`draws` | `rlDrawCallPtr` | `rlDrawCallPtr` | `rlDrawCall *` | Draw calls array, depends on textureId
`draw_counter` | `int` | `Int` | `int` | Draw calls counter
`current_depth` | `float` | `Float` | `float` | Current depth value for next draw

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, rl_render_batch_sequence)` | *n/a*



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Matrix"><code>Matrix</code> structure</h2>

Matrix, 4x4 components, column major, OpenGL style, right handed

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`m0` | `float` | `Float` | `float` | Matrix first row (4 components)
`m4` | `float` | `Float` | `float` | Matrix first row (4 components)
`m8` | `float` | `Float` | `float` | Matrix first row (4 components)
`m12` | `float` | `Float` | `float` | Matrix first row (4 components)
`m1` | `float` | `Float` | `float` | Matrix second row (4 components)
`m5` | `float` | `Float` | `float` | Matrix second row (4 components)
`m9` | `float` | `Float` | `float` | Matrix second row (4 components)
`m13` | `float` | `Float` | `float` | Matrix second row (4 components)
`m2` | `float` | `Float` | `float` | Matrix third row (4 components)
`m6` | `float` | `Float` | `float` | Matrix third row (4 components)
`m10` | `float` | `Float` | `float` | Matrix third row (4 components)
`m14` | `float` | `Float` | `float` | Matrix third row (4 components)
`m3` | `float` | `Float` | `float` | Matrix fourth row (4 components)
`m7` | `float` | `Float` | `float` | Matrix fourth row (4 components)
`m11` | `float` | `Float` | `float` | Matrix fourth row (4 components)
`m15` | `float` | `Float` | `float` | Matrix fourth row (4 components)

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, matrix_sequence)` | *n/a*
*classmethod* | `.identity()` | <a href="#MatrixIdentity"><code>matrix_identity</code></a>
*classmethod* | `.translate(cls, x: 'float', y: 'float', z: 'float')` | <a href="#MatrixTranslate"><code>matrix_translate</code></a>
*classmethod* | `.rotate(cls, axis: 'Vector3', angle: 'float')` | <a href="#MatrixRotate"><code>matrix_rotate</code></a>
*classmethod* | `.rotate_x(cls, angle: 'float')` | <a href="#MatrixRotateX"><code>matrix_rotate_x</code></a>
*classmethod* | `.rotate_y(cls, angle: 'float')` | <a href="#MatrixRotateY"><code>matrix_rotate_y</code></a>
*classmethod* | `.rotate_z(cls, angle: 'float')` | <a href="#MatrixRotateZ"><code>matrix_rotate_z</code></a>
*classmethod* | `.rotate_xyz(cls, angle: 'Vector3')` | <a href="#MatrixRotateXYZ"><code>matrix_rotate_xyz</code></a>
*classmethod* | `.rotate_zyx(cls, angle: 'Vector3')` | <a href="#MatrixRotateZYX"><code>matrix_rotate_zyx</code></a>
*classmethod* | `.scale(cls, x: 'float', y: 'float', z: 'float')` | <a href="#MatrixScale"><code>matrix_scale</code></a>
*classmethod* | `.frustum(cls, left: 'float', right: 'float', bottom: 'float', top: 'float', near: 'float', far: 'float')` | <a href="#MatrixFrustum"><code>matrix_frustum</code></a>
*classmethod* | `.perspective(cls, fovy: 'float', aspect: 'float', near: 'float', far: 'float')` | <a href="#MatrixPerspective"><code>matrix_perspective</code></a>
*classmethod* | `.ortho(cls, left: 'float', right: 'float', bottom: 'float', top: 'float', near: 'float', far: 'float')` | <a href="#MatrixOrtho"><code>matrix_ortho</code></a>
*classmethod* | `.look_at(cls, eye: 'Vector3', target: 'Vector3', up: 'Vector3')` | <a href="#MatrixLookAt"><code>matrix_look_at</code></a>
*method* | `.determinant(self)` | <a href="#MatrixDeterminant"><code>matrix_determinant</code></a>
*method* | `.trace(self)` | <a href="#MatrixTrace"><code>matrix_trace</code></a>
*method* | `.transpose(self)` | <a href="#MatrixTranspose"><code>matrix_transpose</code></a>
*method* | `.invert(self)` | <a href="#MatrixInvert"><code>matrix_invert</code></a>



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="enums">Enumerations</h2>

<a href="#BlendMode">BlendMode</a> | <a href="#CameraMode">CameraMode</a> | <a href="#CameraProjection">CameraProjection</a> | <a href="#ConfigFlags">ConfigFlags</a> | <a href="#CubemapLayout">CubemapLayout</a> | <a href="#FontType">FontType</a> | <a href="#GamepadAxis">GamepadAxis</a> | <a href="#GamepadButton">GamepadButton</a> | <a href="#Gesture">Gesture</a> | <a href="#KeyboardKey">KeyboardKey</a> | <a href="#MaterialMapIndex">MaterialMapIndex</a> | <a href="#MouseButton">MouseButton</a> | <a href="#MouseCursor">MouseCursor</a> | <a href="#NPatchLayout">NPatchLayout</a> | <a href="#PixelFormat">PixelFormat</a> | <a href="#ShaderAttributeDataType">ShaderAttributeDataType</a> | <a href="#ShaderLocationIndex">ShaderLocationIndex</a> | <a href="#ShaderUniformDataType">ShaderUniformDataType</a> | <a href="#TextureFilter">TextureFilter</a> | <a href="#TextureWrap">TextureWrap</a> | <a href="#TraceLogLevel">TraceLogLevel</a> | <a href="#rlBlendMode">rlBlendMode</a> | <a href="#rlFramebufferAttachTextureType">rlFramebufferAttachTextureType</a> | <a href="#rlFramebufferAttachType">rlFramebufferAttachType</a> | <a href="#rlGlVersion">rlGlVersion</a> | <a href="#rlPixelFormat">rlPixelFormat</a> | <a href="#rlShaderAttributeDataType">rlShaderAttributeDataType</a> | <a href="#rlShaderLocationIndex">rlShaderLocationIndex</a> | <a href="#rlShaderUniformDataType">rlShaderUniformDataType</a> | <a href="#rlTextureFilter">rlTextureFilter</a> | <a href="#rlTraceLogLevel">rlTraceLogLevel</a>

[ <a href="#toc">ToC</a> ]

<h2 id="ConfigFlags"><code>ConfigFlags</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`FLAG_VSYNC_HINT` | `64` | Set to try enabling V-Sync on GPU
`FLAG_FULLSCREEN_MODE` | `2` | Set to run program in fullscreen
`FLAG_WINDOW_RESIZABLE` | `4` | Set to allow resizable window
`FLAG_WINDOW_UNDECORATED` | `8` | Set to disable window decoration (frame and buttons)
`FLAG_WINDOW_HIDDEN` | `128` | Set to hide window
`FLAG_WINDOW_MINIMIZED` | `512` | Set to minimize window (iconify)
`FLAG_WINDOW_MAXIMIZED` | `1024` | Set to maximize window (expanded to monitor)
`FLAG_WINDOW_UNFOCUSED` | `2048` | Set to window non focused
`FLAG_WINDOW_TOPMOST` | `4096` | Set to window always on top
`FLAG_WINDOW_ALWAYS_RUN` | `256` | Set to allow windows running while minimized
`FLAG_WINDOW_TRANSPARENT` | `16` | Set to allow transparent framebuffer
`FLAG_WINDOW_HIGHDPI` | `8192` | Set to support HighDPI
`FLAG_WINDOW_MOUSE_PASSTHROUGH` | `16384` | Set to support mouse passthrough, only supported when FLAG_WINDOW_UNDECORATED
`FLAG_MSAA_4X_HINT` | `32` | Set to try enabling MSAA 4X
`FLAG_INTERLACED_HINT` | `65536` | Set to try enabling interlaced video format (for V3D)

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TraceLogLevel"><code>TraceLogLevel</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`LOG_ALL` | `0` | Display all logs
`LOG_TRACE` | `1` | Trace logging, intended for internal use only
`LOG_DEBUG` | `2` | Debug logging, used for internal debugging, it should be disabled on release builds
`LOG_INFO` | `3` | Info logging, used for program execution info
`LOG_WARNING` | `4` | Warning logging, used on recoverable failures
`LOG_ERROR` | `5` | Error logging, used on unrecoverable failures
`LOG_FATAL` | `6` | Fatal logging, used to abort program: exit(EXIT_FAILURE)
`LOG_NONE` | `7` | Disable logging

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="KeyboardKey"><code>KeyboardKey</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`KEY_NULL` | `0` | Key: NULL, used for no key pressed
`KEY_APOSTROPHE` | `39` | Key: '
`KEY_COMMA` | `44` | Key: ,
`KEY_MINUS` | `45` | Key: -
`KEY_PERIOD` | `46` | Key: .
`KEY_SLASH` | `47` | Key: /
`KEY_ZERO` | `48` | Key: 0
`KEY_ONE` | `49` | Key: 1
`KEY_TWO` | `50` | Key: 2
`KEY_THREE` | `51` | Key: 3
`KEY_FOUR` | `52` | Key: 4
`KEY_FIVE` | `53` | Key: 5
`KEY_SIX` | `54` | Key: 6
`KEY_SEVEN` | `55` | Key: 7
`KEY_EIGHT` | `56` | Key: 8
`KEY_NINE` | `57` | Key: 9
`KEY_SEMICOLON` | `59` | Key: ;
`KEY_EQUAL` | `61` | Key: =
`KEY_A` | `65` | Key: A | a
`KEY_B` | `66` | Key: B | b
`KEY_C` | `67` | Key: C | c
`KEY_D` | `68` | Key: D | d
`KEY_E` | `69` | Key: E | e
`KEY_F` | `70` | Key: F | f
`KEY_G` | `71` | Key: G | g
`KEY_H` | `72` | Key: H | h
`KEY_I` | `73` | Key: I | i
`KEY_J` | `74` | Key: J | j
`KEY_K` | `75` | Key: K | k
`KEY_L` | `76` | Key: L | l
`KEY_M` | `77` | Key: M | m
`KEY_N` | `78` | Key: N | n
`KEY_O` | `79` | Key: O | o
`KEY_P` | `80` | Key: P | p
`KEY_Q` | `81` | Key: Q | q
`KEY_R` | `82` | Key: R | r
`KEY_S` | `83` | Key: S | s
`KEY_T` | `84` | Key: T | t
`KEY_U` | `85` | Key: U | u
`KEY_V` | `86` | Key: V | v
`KEY_W` | `87` | Key: W | w
`KEY_X` | `88` | Key: X | x
`KEY_Y` | `89` | Key: Y | y
`KEY_Z` | `90` | Key: Z | z
`KEY_LEFT_BRACKET` | `91` | Key: [
`KEY_BACKSLASH` | `92` | Key: '\'
`KEY_RIGHT_BRACKET` | `93` | Key: ]
`KEY_GRAVE` | `96` | Key: `
`KEY_SPACE` | `32` | Key: Space
`KEY_ESCAPE` | `256` | Key: Esc
`KEY_ENTER` | `257` | Key: Enter
`KEY_TAB` | `258` | Key: Tab
`KEY_BACKSPACE` | `259` | Key: Backspace
`KEY_INSERT` | `260` | Key: Ins
`KEY_DELETE` | `261` | Key: Del
`KEY_RIGHT` | `262` | Key: Cursor right
`KEY_LEFT` | `263` | Key: Cursor left
`KEY_DOWN` | `264` | Key: Cursor down
`KEY_UP` | `265` | Key: Cursor up
`KEY_PAGE_UP` | `266` | Key: Page up
`KEY_PAGE_DOWN` | `267` | Key: Page down
`KEY_HOME` | `268` | Key: Home
`KEY_END` | `269` | Key: End
`KEY_CAPS_LOCK` | `280` | Key: Caps lock
`KEY_SCROLL_LOCK` | `281` | Key: Scroll down
`KEY_NUM_LOCK` | `282` | Key: Num lock
`KEY_PRINT_SCREEN` | `283` | Key: Print screen
`KEY_PAUSE` | `284` | Key: Pause
`KEY_F1` | `290` | Key: F1
`KEY_F2` | `291` | Key: F2
`KEY_F3` | `292` | Key: F3
`KEY_F4` | `293` | Key: F4
`KEY_F5` | `294` | Key: F5
`KEY_F6` | `295` | Key: F6
`KEY_F7` | `296` | Key: F7
`KEY_F8` | `297` | Key: F8
`KEY_F9` | `298` | Key: F9
`KEY_F10` | `299` | Key: F10
`KEY_F11` | `300` | Key: F11
`KEY_F12` | `301` | Key: F12
`KEY_LEFT_SHIFT` | `340` | Key: Shift left
`KEY_LEFT_CONTROL` | `341` | Key: Control left
`KEY_LEFT_ALT` | `342` | Key: Alt left
`KEY_LEFT_SUPER` | `343` | Key: Super left
`KEY_RIGHT_SHIFT` | `344` | Key: Shift right
`KEY_RIGHT_CONTROL` | `345` | Key: Control right
`KEY_RIGHT_ALT` | `346` | Key: Alt right
`KEY_RIGHT_SUPER` | `347` | Key: Super right
`KEY_KB_MENU` | `348` | Key: KB menu
`KEY_KP_0` | `320` | Key: Keypad 0
`KEY_KP_1` | `321` | Key: Keypad 1
`KEY_KP_2` | `322` | Key: Keypad 2
`KEY_KP_3` | `323` | Key: Keypad 3
`KEY_KP_4` | `324` | Key: Keypad 4
`KEY_KP_5` | `325` | Key: Keypad 5
`KEY_KP_6` | `326` | Key: Keypad 6
`KEY_KP_7` | `327` | Key: Keypad 7
`KEY_KP_8` | `328` | Key: Keypad 8
`KEY_KP_9` | `329` | Key: Keypad 9
`KEY_KP_DECIMAL` | `330` | Key: Keypad .
`KEY_KP_DIVIDE` | `331` | Key: Keypad /
`KEY_KP_MULTIPLY` | `332` | Key: Keypad *
`KEY_KP_SUBTRACT` | `333` | Key: Keypad -
`KEY_KP_ADD` | `334` | Key: Keypad +
`KEY_KP_ENTER` | `335` | Key: Keypad Enter
`KEY_KP_EQUAL` | `336` | Key: Keypad =
`KEY_BACK` | `4` | Key: Android back button
`KEY_MENU` | `82` | Key: Android menu button
`KEY_VOLUME_UP` | `24` | Key: Android volume up button
`KEY_VOLUME_DOWN` | `25` | Key: Android volume down button

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MouseButton"><code>MouseButton</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`MOUSE_BUTTON_LEFT` | `0` | Mouse button left
`MOUSE_BUTTON_RIGHT` | `1` | Mouse button right
`MOUSE_BUTTON_MIDDLE` | `2` | Mouse button middle (pressed wheel)
`MOUSE_BUTTON_SIDE` | `3` | Mouse button side (advanced mouse device)
`MOUSE_BUTTON_EXTRA` | `4` | Mouse button extra (advanced mouse device)
`MOUSE_BUTTON_FORWARD` | `5` | Mouse button fordward (advanced mouse device)
`MOUSE_BUTTON_BACK` | `6` | Mouse button back (advanced mouse device)

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MouseCursor"><code>MouseCursor</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`MOUSE_CURSOR_DEFAULT` | `0` | Default pointer shape
`MOUSE_CURSOR_ARROW` | `1` | Arrow shape
`MOUSE_CURSOR_IBEAM` | `2` | Text writing cursor shape
`MOUSE_CURSOR_CROSSHAIR` | `3` | Cross shape
`MOUSE_CURSOR_POINTING_HAND` | `4` | Pointing hand cursor
`MOUSE_CURSOR_RESIZE_EW` | `5` | Horizontal resize/move arrow shape
`MOUSE_CURSOR_RESIZE_NS` | `6` | Vertical resize/move arrow shape
`MOUSE_CURSOR_RESIZE_NWSE` | `7` | Top-left to bottom-right diagonal resize/move arrow shape
`MOUSE_CURSOR_RESIZE_NESW` | `8` | The top-right to bottom-left diagonal resize/move arrow shape
`MOUSE_CURSOR_RESIZE_ALL` | `9` | The omni-directional resize/move cursor shape
`MOUSE_CURSOR_NOT_ALLOWED` | `10` | The operation-not-allowed shape

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GamepadButton"><code>GamepadButton</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`GAMEPAD_BUTTON_UNKNOWN` | `0` | Unknown button, just for error checking
`GAMEPAD_BUTTON_LEFT_FACE_UP` | `1` | Gamepad left DPAD up button
`GAMEPAD_BUTTON_LEFT_FACE_RIGHT` | `2` | Gamepad left DPAD right button
`GAMEPAD_BUTTON_LEFT_FACE_DOWN` | `3` | Gamepad left DPAD down button
`GAMEPAD_BUTTON_LEFT_FACE_LEFT` | `4` | Gamepad left DPAD left button
`GAMEPAD_BUTTON_RIGHT_FACE_UP` | `5` | Gamepad right button up (i.e. PS3: Triangle, Xbox: Y)
`GAMEPAD_BUTTON_RIGHT_FACE_RIGHT` | `6` | Gamepad right button right (i.e. PS3: Square, Xbox: X)
`GAMEPAD_BUTTON_RIGHT_FACE_DOWN` | `7` | Gamepad right button down (i.e. PS3: Cross, Xbox: A)
`GAMEPAD_BUTTON_RIGHT_FACE_LEFT` | `8` | Gamepad right button left (i.e. PS3: Circle, Xbox: B)
`GAMEPAD_BUTTON_LEFT_TRIGGER_1` | `9` | Gamepad top/back trigger left (first), it could be a trailing button
`GAMEPAD_BUTTON_LEFT_TRIGGER_2` | `10` | Gamepad top/back trigger left (second), it could be a trailing button
`GAMEPAD_BUTTON_RIGHT_TRIGGER_1` | `11` | Gamepad top/back trigger right (one), it could be a trailing button
`GAMEPAD_BUTTON_RIGHT_TRIGGER_2` | `12` | Gamepad top/back trigger right (second), it could be a trailing button
`GAMEPAD_BUTTON_MIDDLE_LEFT` | `13` | Gamepad center buttons, left one (i.e. PS3: Select)
`GAMEPAD_BUTTON_MIDDLE` | `14` | Gamepad center buttons, middle one (i.e. PS3: PS, Xbox: XBOX)
`GAMEPAD_BUTTON_MIDDLE_RIGHT` | `15` | Gamepad center buttons, right one (i.e. PS3: Start)
`GAMEPAD_BUTTON_LEFT_THUMB` | `16` | Gamepad joystick pressed button left
`GAMEPAD_BUTTON_RIGHT_THUMB` | `17` | Gamepad joystick pressed button right

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GamepadAxis"><code>GamepadAxis</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`GAMEPAD_AXIS_LEFT_X` | `0` | Gamepad left stick X axis
`GAMEPAD_AXIS_LEFT_Y` | `1` | Gamepad left stick Y axis
`GAMEPAD_AXIS_RIGHT_X` | `2` | Gamepad right stick X axis
`GAMEPAD_AXIS_RIGHT_Y` | `3` | Gamepad right stick Y axis
`GAMEPAD_AXIS_LEFT_TRIGGER` | `4` | Gamepad back trigger left, pressure level: [1..-1]
`GAMEPAD_AXIS_RIGHT_TRIGGER` | `5` | Gamepad back trigger right, pressure level: [1..-1]

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MaterialMapIndex"><code>MaterialMapIndex</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`MATERIAL_MAP_ALBEDO` | `0` | Albedo material (same as: MATERIAL_MAP_DIFFUSE)
`MATERIAL_MAP_METALNESS` | `1` | Metalness material (same as: MATERIAL_MAP_SPECULAR)
`MATERIAL_MAP_NORMAL` | `2` | Normal material
`MATERIAL_MAP_ROUGHNESS` | `3` | Roughness material
`MATERIAL_MAP_OCCLUSION` | `4` | Ambient occlusion material
`MATERIAL_MAP_EMISSION` | `5` | Emission material
`MATERIAL_MAP_HEIGHT` | `6` | Heightmap material
`MATERIAL_MAP_CUBEMAP` | `7` | Cubemap material (NOTE: Uses GL_TEXTURE_CUBE_MAP)
`MATERIAL_MAP_IRRADIANCE` | `8` | Irradiance material (NOTE: Uses GL_TEXTURE_CUBE_MAP)
`MATERIAL_MAP_PREFILTER` | `9` | Prefilter material (NOTE: Uses GL_TEXTURE_CUBE_MAP)
`MATERIAL_MAP_BRDF` | `10` | Brdf material

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ShaderLocationIndex"><code>ShaderLocationIndex</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`SHADER_LOC_VERTEX_POSITION` | `0` | Shader location: vertex attribute: position
`SHADER_LOC_VERTEX_TEXCOORD01` | `1` | Shader location: vertex attribute: texcoord01
`SHADER_LOC_VERTEX_TEXCOORD02` | `2` | Shader location: vertex attribute: texcoord02
`SHADER_LOC_VERTEX_NORMAL` | `3` | Shader location: vertex attribute: normal
`SHADER_LOC_VERTEX_TANGENT` | `4` | Shader location: vertex attribute: tangent
`SHADER_LOC_VERTEX_COLOR` | `5` | Shader location: vertex attribute: color
`SHADER_LOC_MATRIX_MVP` | `6` | Shader location: matrix uniform: model-view-projection
`SHADER_LOC_MATRIX_VIEW` | `7` | Shader location: matrix uniform: view (camera transform)
`SHADER_LOC_MATRIX_PROJECTION` | `8` | Shader location: matrix uniform: projection
`SHADER_LOC_MATRIX_MODEL` | `9` | Shader location: matrix uniform: model (transform)
`SHADER_LOC_MATRIX_NORMAL` | `10` | Shader location: matrix uniform: normal
`SHADER_LOC_VECTOR_VIEW` | `11` | Shader location: vector uniform: view
`SHADER_LOC_COLOR_DIFFUSE` | `12` | Shader location: vector uniform: diffuse color
`SHADER_LOC_COLOR_SPECULAR` | `13` | Shader location: vector uniform: specular color
`SHADER_LOC_COLOR_AMBIENT` | `14` | Shader location: vector uniform: ambient color
`SHADER_LOC_MAP_ALBEDO` | `15` | Shader location: sampler2d texture: albedo (same as: SHADER_LOC_MAP_DIFFUSE)
`SHADER_LOC_MAP_METALNESS` | `16` | Shader location: sampler2d texture: metalness (same as: SHADER_LOC_MAP_SPECULAR)
`SHADER_LOC_MAP_NORMAL` | `17` | Shader location: sampler2d texture: normal
`SHADER_LOC_MAP_ROUGHNESS` | `18` | Shader location: sampler2d texture: roughness
`SHADER_LOC_MAP_OCCLUSION` | `19` | Shader location: sampler2d texture: occlusion
`SHADER_LOC_MAP_EMISSION` | `20` | Shader location: sampler2d texture: emission
`SHADER_LOC_MAP_HEIGHT` | `21` | Shader location: sampler2d texture: height
`SHADER_LOC_MAP_CUBEMAP` | `22` | Shader location: samplerCube texture: cubemap
`SHADER_LOC_MAP_IRRADIANCE` | `23` | Shader location: samplerCube texture: irradiance
`SHADER_LOC_MAP_PREFILTER` | `24` | Shader location: samplerCube texture: prefilter
`SHADER_LOC_MAP_BRDF` | `25` | Shader location: sampler2d texture: brdf

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ShaderUniformDataType"><code>ShaderUniformDataType</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`SHADER_UNIFORM_FLOAT` | `0` | Shader uniform type: float
`SHADER_UNIFORM_VEC2` | `1` | Shader uniform type: vec2 (2 float)
`SHADER_UNIFORM_VEC3` | `2` | Shader uniform type: vec3 (3 float)
`SHADER_UNIFORM_VEC4` | `3` | Shader uniform type: vec4 (4 float)
`SHADER_UNIFORM_INT` | `4` | Shader uniform type: int
`SHADER_UNIFORM_IVEC2` | `5` | Shader uniform type: ivec2 (2 int)
`SHADER_UNIFORM_IVEC3` | `6` | Shader uniform type: ivec3 (3 int)
`SHADER_UNIFORM_IVEC4` | `7` | Shader uniform type: ivec4 (4 int)
`SHADER_UNIFORM_SAMPLER2D` | `8` | Shader uniform type: sampler2d

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ShaderAttributeDataType"><code>ShaderAttributeDataType</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`SHADER_ATTRIB_FLOAT` | `0` | Shader attribute type: float
`SHADER_ATTRIB_VEC2` | `1` | Shader attribute type: vec2 (2 float)
`SHADER_ATTRIB_VEC3` | `2` | Shader attribute type: vec3 (3 float)
`SHADER_ATTRIB_VEC4` | `3` | Shader attribute type: vec4 (4 float)

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="PixelFormat"><code>PixelFormat</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`PIXELFORMAT_UNCOMPRESSED_GRAYSCALE` | `1` | 8 bit per pixel (no alpha)
`PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA` | `2` | 8*2 bpp (2 channels)
`PIXELFORMAT_UNCOMPRESSED_R5G6B5` | `3` | 16 bpp
`PIXELFORMAT_UNCOMPRESSED_R8G8B8` | `4` | 24 bpp
`PIXELFORMAT_UNCOMPRESSED_R5G5B5A1` | `5` | 16 bpp (1 bit alpha)
`PIXELFORMAT_UNCOMPRESSED_R4G4B4A4` | `6` | 16 bpp (4 bit alpha)
`PIXELFORMAT_UNCOMPRESSED_R8G8B8A8` | `7` | 32 bpp
`PIXELFORMAT_UNCOMPRESSED_R32` | `8` | 32 bpp (1 channel - float)
`PIXELFORMAT_UNCOMPRESSED_R32G32B32` | `9` | 32*3 bpp (3 channels - float)
`PIXELFORMAT_UNCOMPRESSED_R32G32B32A32` | `10` | 32*4 bpp (4 channels - float)
`PIXELFORMAT_COMPRESSED_DXT1_RGB` | `11` | 4 bpp (no alpha)
`PIXELFORMAT_COMPRESSED_DXT1_RGBA` | `12` | 4 bpp (1 bit alpha)
`PIXELFORMAT_COMPRESSED_DXT3_RGBA` | `13` | 8 bpp
`PIXELFORMAT_COMPRESSED_DXT5_RGBA` | `14` | 8 bpp
`PIXELFORMAT_COMPRESSED_ETC1_RGB` | `15` | 4 bpp
`PIXELFORMAT_COMPRESSED_ETC2_RGB` | `16` | 4 bpp
`PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA` | `17` | 8 bpp
`PIXELFORMAT_COMPRESSED_PVRT_RGB` | `18` | 4 bpp
`PIXELFORMAT_COMPRESSED_PVRT_RGBA` | `19` | 4 bpp
`PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA` | `20` | 8 bpp
`PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA` | `21` | 2 bpp

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextureFilter"><code>TextureFilter</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`TEXTURE_FILTER_POINT` | `0` | No filter, just pixel approximation
`TEXTURE_FILTER_BILINEAR` | `1` | Linear filtering
`TEXTURE_FILTER_TRILINEAR` | `2` | Trilinear filtering (linear with mipmaps)
`TEXTURE_FILTER_ANISOTROPIC_4X` | `3` | Anisotropic filtering 4x
`TEXTURE_FILTER_ANISOTROPIC_8X` | `4` | Anisotropic filtering 8x
`TEXTURE_FILTER_ANISOTROPIC_16X` | `5` | Anisotropic filtering 16x

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextureWrap"><code>TextureWrap</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`TEXTURE_WRAP_REPEAT` | `0` | Repeats texture in tiled mode
`TEXTURE_WRAP_CLAMP` | `1` | Clamps texture to edge pixel in tiled mode
`TEXTURE_WRAP_MIRROR_REPEAT` | `2` | Mirrors and repeats the texture in tiled mode
`TEXTURE_WRAP_MIRROR_CLAMP` | `3` | Mirrors and clamps to border the texture in tiled mode

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CubemapLayout"><code>CubemapLayout</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`CUBEMAP_LAYOUT_AUTO_DETECT` | `0` | Automatically detect layout type
`CUBEMAP_LAYOUT_LINE_VERTICAL` | `1` | Layout is defined by a vertical line with faces
`CUBEMAP_LAYOUT_LINE_HORIZONTAL` | `2` | Layout is defined by an horizontal line with faces
`CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR` | `3` | Layout is defined by a 3x4 cross with cubemap faces
`CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE` | `4` | Layout is defined by a 4x3 cross with cubemap faces
`CUBEMAP_LAYOUT_PANORAMA` | `5` | Layout is defined by a panorama image (equirectangular map)

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="FontType"><code>FontType</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`FONT_DEFAULT` | `0` | Default font generation, anti-aliased
`FONT_BITMAP` | `1` | Bitmap font generation, no anti-aliasing
`FONT_SDF` | `2` | SDF font generation, requires external shader

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="BlendMode"><code>BlendMode</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`BLEND_ALPHA` | `0` | Blend textures considering alpha (default)
`BLEND_ADDITIVE` | `1` | Blend textures adding colors
`BLEND_MULTIPLIED` | `2` | Blend textures multiplying colors
`BLEND_ADD_COLORS` | `3` | Blend textures adding colors (alternative)
`BLEND_SUBTRACT_COLORS` | `4` | Blend textures subtracting colors (alternative)
`BLEND_ALPHA_PREMULTIPLY` | `5` | Blend premultiplied textures considering alpha
`BLEND_CUSTOM` | `6` | Blend textures using custom src/dst factors (use rlSetBlendMode())

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Gesture"><code>Gesture</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`GESTURE_NONE` | `0` | No gesture
`GESTURE_TAP` | `1` | Tap gesture
`GESTURE_DOUBLETAP` | `2` | Double tap gesture
`GESTURE_HOLD` | `4` | Hold gesture
`GESTURE_DRAG` | `8` | Drag gesture
`GESTURE_SWIPE_RIGHT` | `16` | Swipe right gesture
`GESTURE_SWIPE_LEFT` | `32` | Swipe left gesture
`GESTURE_SWIPE_UP` | `64` | Swipe up gesture
`GESTURE_SWIPE_DOWN` | `128` | Swipe down gesture
`GESTURE_PINCH_IN` | `256` | Pinch in gesture
`GESTURE_PINCH_OUT` | `512` | Pinch out gesture

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CameraMode"><code>CameraMode</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`CAMERA_CUSTOM` | `0` | Custom camera
`CAMERA_FREE` | `1` | Free camera
`CAMERA_ORBITAL` | `2` | Orbital camera
`CAMERA_FIRST_PERSON` | `3` | First person camera
`CAMERA_THIRD_PERSON` | `4` | Third person camera

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CameraProjection"><code>CameraProjection</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`CAMERA_PERSPECTIVE` | `0` | Perspective projection
`CAMERA_ORTHOGRAPHIC` | `1` | Orthographic projection

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="NPatchLayout"><code>NPatchLayout</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`NPATCH_NINE_PATCH` | `0` | Npatch layout: 3x3 tiles
`NPATCH_THREE_PATCH_VERTICAL` | `1` | Npatch layout: 1x3 tiles
`NPATCH_THREE_PATCH_HORIZONTAL` | `2` | Npatch layout: 3x1 tiles

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGlVersion"><code>rlGlVersion</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`OPENGL_11` | `1` | 
`OPENGL_21` | `2` | 
`OPENGL_33` | `3` | 
`OPENGL_43` | `4` | 
`OPENGL_ES_20` | `5` | 

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlFramebufferAttachType"><code>rlFramebufferAttachType</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`RL_ATTACHMENT_COLOR_CHANNEL0` | `0` | 
`RL_ATTACHMENT_COLOR_CHANNEL1` | `1` | 
`RL_ATTACHMENT_COLOR_CHANNEL2` | `2` | 
`RL_ATTACHMENT_COLOR_CHANNEL3` | `3` | 
`RL_ATTACHMENT_COLOR_CHANNEL4` | `4` | 
`RL_ATTACHMENT_COLOR_CHANNEL5` | `5` | 
`RL_ATTACHMENT_COLOR_CHANNEL6` | `6` | 
`RL_ATTACHMENT_COLOR_CHANNEL7` | `7` | 
`RL_ATTACHMENT_DEPTH` | `100` | 
`RL_ATTACHMENT_STENCIL` | `200` | 

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlFramebufferAttachTextureType"><code>rlFramebufferAttachTextureType</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`RL_ATTACHMENT_CUBEMAP_POSITIVE_X` | `0` | 
`RL_ATTACHMENT_CUBEMAP_NEGATIVE_X` | `1` | 
`RL_ATTACHMENT_CUBEMAP_POSITIVE_Y` | `2` | 
`RL_ATTACHMENT_CUBEMAP_NEGATIVE_Y` | `3` | 
`RL_ATTACHMENT_CUBEMAP_POSITIVE_Z` | `4` | 
`RL_ATTACHMENT_CUBEMAP_NEGATIVE_Z` | `5` | 
`RL_ATTACHMENT_TEXTURE2D` | `100` | 
`RL_ATTACHMENT_RENDERBUFFER` | `200` | 

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlTraceLogLevel"><code>rlTraceLogLevel</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`RL_LOG_ALL` | `0` | Display all logs
`RL_LOG_TRACE` | `1` | Trace logging, intended for internal use only
`RL_LOG_DEBUG` | `2` | Debug logging, used for internal debugging, it should be disabled on release builds
`RL_LOG_INFO` | `3` | Info logging, used for program execution info
`RL_LOG_WARNING` | `4` | Warning logging, used on recoverable failures
`RL_LOG_ERROR` | `5` | Error logging, used on unrecoverable failures
`RL_LOG_FATAL` | `6` | Fatal logging, used to abort program: exit(EXIT_FAILURE)
`RL_LOG_NONE` | `7` | Disable logging

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlPixelFormat"><code>rlPixelFormat</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`RL_PIXELFORMAT_UNCOMPRESSED_GRAYSCALE` | `1` | 8 bit per pixel (no alpha)
`RL_PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA` | `2` | 8*2 bpp (2 channels)
`RL_PIXELFORMAT_UNCOMPRESSED_R5G6B5` | `3` | 16 bpp
`RL_PIXELFORMAT_UNCOMPRESSED_R8G8B8` | `4` | 24 bpp
`RL_PIXELFORMAT_UNCOMPRESSED_R5G5B5A1` | `5` | 16 bpp (1 bit alpha)
`RL_PIXELFORMAT_UNCOMPRESSED_R4G4B4A4` | `6` | 16 bpp (4 bit alpha)
`RL_PIXELFORMAT_UNCOMPRESSED_R8G8B8A8` | `7` | 32 bpp
`RL_PIXELFORMAT_UNCOMPRESSED_R32` | `8` | 32 bpp (1 channel - float)
`RL_PIXELFORMAT_UNCOMPRESSED_R32G32B32` | `9` | 32*3 bpp (3 channels - float)
`RL_PIXELFORMAT_UNCOMPRESSED_R32G32B32A32` | `10` | 32*4 bpp (4 channels - float)
`RL_PIXELFORMAT_COMPRESSED_DXT1_RGB` | `11` | 4 bpp (no alpha)
`RL_PIXELFORMAT_COMPRESSED_DXT1_RGBA` | `12` | 4 bpp (1 bit alpha)
`RL_PIXELFORMAT_COMPRESSED_DXT3_RGBA` | `13` | 8 bpp
`RL_PIXELFORMAT_COMPRESSED_DXT5_RGBA` | `14` | 8 bpp
`RL_PIXELFORMAT_COMPRESSED_ETC1_RGB` | `15` | 4 bpp
`RL_PIXELFORMAT_COMPRESSED_ETC2_RGB` | `16` | 4 bpp
`RL_PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA` | `17` | 8 bpp
`RL_PIXELFORMAT_COMPRESSED_PVRT_RGB` | `18` | 4 bpp
`RL_PIXELFORMAT_COMPRESSED_PVRT_RGBA` | `19` | 4 bpp
`RL_PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA` | `20` | 8 bpp
`RL_PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA` | `21` | 2 bpp

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlTextureFilter"><code>rlTextureFilter</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`RL_TEXTURE_FILTER_POINT` | `0` | No filter, just pixel approximation
`RL_TEXTURE_FILTER_BILINEAR` | `1` | Linear filtering
`RL_TEXTURE_FILTER_TRILINEAR` | `2` | Trilinear filtering (linear with mipmaps)
`RL_TEXTURE_FILTER_ANISOTROPIC_4X` | `3` | Anisotropic filtering 4x
`RL_TEXTURE_FILTER_ANISOTROPIC_8X` | `4` | Anisotropic filtering 8x
`RL_TEXTURE_FILTER_ANISOTROPIC_16X` | `5` | Anisotropic filtering 16x

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlBlendMode"><code>rlBlendMode</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`RL_BLEND_ALPHA` | `0` | Blend textures considering alpha (default)
`RL_BLEND_ADDITIVE` | `1` | Blend textures adding colors
`RL_BLEND_MULTIPLIED` | `2` | Blend textures multiplying colors
`RL_BLEND_ADD_COLORS` | `3` | Blend textures adding colors (alternative)
`RL_BLEND_SUBTRACT_COLORS` | `4` | Blend textures subtracting colors (alternative)
`RL_BLEND_ALPHA_PREMULTIPLY` | `5` | Blend premultiplied textures considering alpha
`RL_BLEND_CUSTOM` | `6` | Blend textures using custom src/dst factors (use rlSetBlendFactors())

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlShaderLocationIndex"><code>rlShaderLocationIndex</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`RL_SHADER_LOC_VERTEX_POSITION` | `0` | Shader location: vertex attribute: position
`RL_SHADER_LOC_VERTEX_TEXCOORD01` | `1` | Shader location: vertex attribute: texcoord01
`RL_SHADER_LOC_VERTEX_TEXCOORD02` | `2` | Shader location: vertex attribute: texcoord02
`RL_SHADER_LOC_VERTEX_NORMAL` | `3` | Shader location: vertex attribute: normal
`RL_SHADER_LOC_VERTEX_TANGENT` | `4` | Shader location: vertex attribute: tangent
`RL_SHADER_LOC_VERTEX_COLOR` | `5` | Shader location: vertex attribute: color
`RL_SHADER_LOC_MATRIX_MVP` | `6` | Shader location: matrix uniform: model-view-projection
`RL_SHADER_LOC_MATRIX_VIEW` | `7` | Shader location: matrix uniform: view (camera transform)
`RL_SHADER_LOC_MATRIX_PROJECTION` | `8` | Shader location: matrix uniform: projection
`RL_SHADER_LOC_MATRIX_MODEL` | `9` | Shader location: matrix uniform: model (transform)
`RL_SHADER_LOC_MATRIX_NORMAL` | `10` | Shader location: matrix uniform: normal
`RL_SHADER_LOC_VECTOR_VIEW` | `11` | Shader location: vector uniform: view
`RL_SHADER_LOC_COLOR_DIFFUSE` | `12` | Shader location: vector uniform: diffuse color
`RL_SHADER_LOC_COLOR_SPECULAR` | `13` | Shader location: vector uniform: specular color
`RL_SHADER_LOC_COLOR_AMBIENT` | `14` | Shader location: vector uniform: ambient color
`RL_SHADER_LOC_MAP_ALBEDO` | `15` | Shader location: sampler2d texture: albedo (same as: RL_SHADER_LOC_MAP_DIFFUSE)
`RL_SHADER_LOC_MAP_METALNESS` | `16` | Shader location: sampler2d texture: metalness (same as: RL_SHADER_LOC_MAP_SPECULAR)
`RL_SHADER_LOC_MAP_NORMAL` | `17` | Shader location: sampler2d texture: normal
`RL_SHADER_LOC_MAP_ROUGHNESS` | `18` | Shader location: sampler2d texture: roughness
`RL_SHADER_LOC_MAP_OCCLUSION` | `19` | Shader location: sampler2d texture: occlusion
`RL_SHADER_LOC_MAP_EMISSION` | `20` | Shader location: sampler2d texture: emission
`RL_SHADER_LOC_MAP_HEIGHT` | `21` | Shader location: sampler2d texture: height
`RL_SHADER_LOC_MAP_CUBEMAP` | `22` | Shader location: samplerCube texture: cubemap
`RL_SHADER_LOC_MAP_IRRADIANCE` | `23` | Shader location: samplerCube texture: irradiance
`RL_SHADER_LOC_MAP_PREFILTER` | `24` | Shader location: samplerCube texture: prefilter
`RL_SHADER_LOC_MAP_BRDF` | `25` | Shader location: sampler2d texture: brdf

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlShaderUniformDataType"><code>rlShaderUniformDataType</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`RL_SHADER_UNIFORM_FLOAT` | `0` | Shader uniform type: float
`RL_SHADER_UNIFORM_VEC2` | `1` | Shader uniform type: vec2 (2 float)
`RL_SHADER_UNIFORM_VEC3` | `2` | Shader uniform type: vec3 (3 float)
`RL_SHADER_UNIFORM_VEC4` | `3` | Shader uniform type: vec4 (4 float)
`RL_SHADER_UNIFORM_INT` | `4` | Shader uniform type: int
`RL_SHADER_UNIFORM_IVEC2` | `5` | Shader uniform type: ivec2 (2 int)
`RL_SHADER_UNIFORM_IVEC3` | `6` | Shader uniform type: ivec3 (3 int)
`RL_SHADER_UNIFORM_IVEC4` | `7` | Shader uniform type: ivec4 (4 int)
`RL_SHADER_UNIFORM_SAMPLER2D` | `8` | Shader uniform type: sampler2d

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlShaderAttributeDataType"><code>rlShaderAttributeDataType</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
`RL_SHADER_ATTRIB_FLOAT` | `0` | Shader attribute type: float
`RL_SHADER_ATTRIB_VEC2` | `1` | Shader attribute type: vec2 (2 float)
`RL_SHADER_ATTRIB_VEC3` | `2` | Shader attribute type: vec3 (3 float)
`RL_SHADER_ATTRIB_VEC4` | `3` | Shader attribute type: vec4 (4 float)

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
<h2 id="funcs">Functions</h2>

<a href="#AttachAudioStreamProcessor">AttachAudioStreamProcessor</a> | <a href="#BeginBlendMode">BeginBlendMode</a> | <a href="#BeginDrawing">BeginDrawing</a> | <a href="#BeginMode2D">BeginMode2D</a> | <a href="#BeginMode3D">BeginMode3D</a> | <a href="#BeginScissorMode">BeginScissorMode</a> | <a href="#BeginShaderMode">BeginShaderMode</a> | <a href="#BeginTextureMode">BeginTextureMode</a> | <a href="#BeginVrStereoMode">BeginVrStereoMode</a> | <a href="#ChangeDirectory">ChangeDirectory</a> | <a href="#CheckCollisionBoxSphere">CheckCollisionBoxSphere</a> | <a href="#CheckCollisionBoxes">CheckCollisionBoxes</a> | <a href="#CheckCollisionCircleRec">CheckCollisionCircleRec</a> | <a href="#CheckCollisionCircles">CheckCollisionCircles</a> | <a href="#CheckCollisionLines">CheckCollisionLines</a> | <a href="#CheckCollisionPointCircle">CheckCollisionPointCircle</a> | <a href="#CheckCollisionPointLine">CheckCollisionPointLine</a> | <a href="#CheckCollisionPointRec">CheckCollisionPointRec</a> | <a href="#CheckCollisionPointTriangle">CheckCollisionPointTriangle</a> | <a href="#CheckCollisionRecs">CheckCollisionRecs</a> | <a href="#CheckCollisionSpheres">CheckCollisionSpheres</a> | <a href="#Clamp">Clamp</a> | <a href="#ClearBackground">ClearBackground</a> | <a href="#ClearWindowState">ClearWindowState</a> | <a href="#CloseAudioDevice">CloseAudioDevice</a> | <a href="#CloseWindow">CloseWindow</a> | <a href="#CodepointToUTF8">CodepointToUTF8</a> | <a href="#ColorAlpha">ColorAlpha</a> | <a href="#ColorAlphaBlend">ColorAlphaBlend</a> | <a href="#ColorFromHSV">ColorFromHSV</a> | <a href="#ColorFromNormalized">ColorFromNormalized</a> | <a href="#ColorNormalize">ColorNormalize</a> | <a href="#ColorToHSV">ColorToHSV</a> | <a href="#ColorToInt">ColorToInt</a> | <a href="#CompressData">CompressData</a> | <a href="#DecodeDataBase64">DecodeDataBase64</a> | <a href="#DecompressData">DecompressData</a> | <a href="#DetachAudioStreamProcessor">DetachAudioStreamProcessor</a> | <a href="#DirectoryExists">DirectoryExists</a> | <a href="#DisableCursor">DisableCursor</a> | <a href="#DisableEventWaiting">DisableEventWaiting</a> | <a href="#DrawBillboard">DrawBillboard</a> | <a href="#DrawBillboardPro">DrawBillboardPro</a> | <a href="#DrawBillboardRec">DrawBillboardRec</a> | <a href="#DrawBoundingBox">DrawBoundingBox</a> | <a href="#DrawCircle">DrawCircle</a> | <a href="#DrawCircle3D">DrawCircle3D</a> | <a href="#DrawCircleGradient">DrawCircleGradient</a> | <a href="#DrawCircleLines">DrawCircleLines</a> | <a href="#DrawCircleSector">DrawCircleSector</a> | <a href="#DrawCircleSectorLines">DrawCircleSectorLines</a> | <a href="#DrawCircleV">DrawCircleV</a> | <a href="#DrawCube">DrawCube</a> | <a href="#DrawCubeTexture">DrawCubeTexture</a> | <a href="#DrawCubeTextureRec">DrawCubeTextureRec</a> | <a href="#DrawCubeV">DrawCubeV</a> | <a href="#DrawCubeWires">DrawCubeWires</a> | <a href="#DrawCubeWiresV">DrawCubeWiresV</a> | <a href="#DrawCylinder">DrawCylinder</a> | <a href="#DrawCylinderEx">DrawCylinderEx</a> | <a href="#DrawCylinderWires">DrawCylinderWires</a> | <a href="#DrawCylinderWiresEx">DrawCylinderWiresEx</a> | <a href="#DrawEllipse">DrawEllipse</a> | <a href="#DrawEllipseLines">DrawEllipseLines</a> | <a href="#DrawFPS">DrawFPS</a> | <a href="#DrawGrid">DrawGrid</a> | <a href="#DrawLine">DrawLine</a> | <a href="#DrawLine3D">DrawLine3D</a> | <a href="#DrawLineBezier">DrawLineBezier</a> | <a href="#DrawLineBezierCubic">DrawLineBezierCubic</a> | <a href="#DrawLineBezierQuad">DrawLineBezierQuad</a> | <a href="#DrawLineEx">DrawLineEx</a> | <a href="#DrawLineStrip">DrawLineStrip</a> | <a href="#DrawLineV">DrawLineV</a> | <a href="#DrawMesh">DrawMesh</a> | <a href="#DrawMeshInstanced">DrawMeshInstanced</a> | <a href="#DrawModel">DrawModel</a> | <a href="#DrawModelEx">DrawModelEx</a> | <a href="#DrawModelWires">DrawModelWires</a> | <a href="#DrawModelWiresEx">DrawModelWiresEx</a> | <a href="#DrawPixel">DrawPixel</a> | <a href="#DrawPixelV">DrawPixelV</a> | <a href="#DrawPlane">DrawPlane</a> | <a href="#DrawPoint3D">DrawPoint3D</a> | <a href="#DrawPoly">DrawPoly</a> | <a href="#DrawPolyLines">DrawPolyLines</a> | <a href="#DrawPolyLinesEx">DrawPolyLinesEx</a> | <a href="#DrawRay">DrawRay</a> | <a href="#DrawRectangle">DrawRectangle</a> | <a href="#DrawRectangleGradientEx">DrawRectangleGradientEx</a> | <a href="#DrawRectangleGradientH">DrawRectangleGradientH</a> | <a href="#DrawRectangleGradientV">DrawRectangleGradientV</a> | <a href="#DrawRectangleLines">DrawRectangleLines</a> | <a href="#DrawRectangleLinesEx">DrawRectangleLinesEx</a> | <a href="#DrawRectanglePro">DrawRectanglePro</a> | <a href="#DrawRectangleRec">DrawRectangleRec</a> | <a href="#DrawRectangleRounded">DrawRectangleRounded</a> | <a href="#DrawRectangleRoundedLines">DrawRectangleRoundedLines</a> | <a href="#DrawRectangleV">DrawRectangleV</a> | <a href="#DrawRing">DrawRing</a> | <a href="#DrawRingLines">DrawRingLines</a> | <a href="#DrawSphere">DrawSphere</a> | <a href="#DrawSphereEx">DrawSphereEx</a> | <a href="#DrawSphereWires">DrawSphereWires</a> | <a href="#DrawText">DrawText</a> | <a href="#DrawTextCodepoint">DrawTextCodepoint</a> | <a href="#DrawTextCodepoints">DrawTextCodepoints</a> | <a href="#DrawTextEx">DrawTextEx</a> | <a href="#DrawTextPro">DrawTextPro</a> | <a href="#DrawTexture">DrawTexture</a> | <a href="#DrawTextureEx">DrawTextureEx</a> | <a href="#DrawTextureNPatch">DrawTextureNPatch</a> | <a href="#DrawTexturePoly">DrawTexturePoly</a> | <a href="#DrawTexturePro">DrawTexturePro</a> | <a href="#DrawTextureQuad">DrawTextureQuad</a> | <a href="#DrawTextureRec">DrawTextureRec</a> | <a href="#DrawTextureTiled">DrawTextureTiled</a> | <a href="#DrawTextureV">DrawTextureV</a> | <a href="#DrawTriangle">DrawTriangle</a> | <a href="#DrawTriangle3D">DrawTriangle3D</a> | <a href="#DrawTriangleFan">DrawTriangleFan</a> | <a href="#DrawTriangleLines">DrawTriangleLines</a> | <a href="#DrawTriangleStrip">DrawTriangleStrip</a> | <a href="#DrawTriangleStrip3D">DrawTriangleStrip3D</a> | <a href="#EnableCursor">EnableCursor</a> | <a href="#EnableEventWaiting">EnableEventWaiting</a> | <a href="#EncodeDataBase64">EncodeDataBase64</a> | <a href="#EndBlendMode">EndBlendMode</a> | <a href="#EndDrawing">EndDrawing</a> | <a href="#EndMode2D">EndMode2D</a> | <a href="#EndMode3D">EndMode3D</a> | <a href="#EndScissorMode">EndScissorMode</a> | <a href="#EndShaderMode">EndShaderMode</a> | <a href="#EndTextureMode">EndTextureMode</a> | <a href="#EndVrStereoMode">EndVrStereoMode</a> | <a href="#ExportDataAsCode">ExportDataAsCode</a> | <a href="#ExportFontAsCode">ExportFontAsCode</a> | <a href="#ExportImage">ExportImage</a> | <a href="#ExportImageAsCode">ExportImageAsCode</a> | <a href="#ExportMesh">ExportMesh</a> | <a href="#ExportWave">ExportWave</a> | <a href="#ExportWaveAsCode">ExportWaveAsCode</a> | <a href="#Fade">Fade</a> | <a href="#FileExists">FileExists</a> | <a href="#FloatEquals">FloatEquals</a> | <a href="#GenImageCellular">GenImageCellular</a> | <a href="#GenImageChecked">GenImageChecked</a> | <a href="#GenImageColor">GenImageColor</a> | <a href="#GenImageFontAtlas">GenImageFontAtlas</a> | <a href="#GenImageGradientH">GenImageGradientH</a> | <a href="#GenImageGradientRadial">GenImageGradientRadial</a> | <a href="#GenImageGradientV">GenImageGradientV</a> | <a href="#GenImageWhiteNoise">GenImageWhiteNoise</a> | <a href="#GenMeshCone">GenMeshCone</a> | <a href="#GenMeshCube">GenMeshCube</a> | <a href="#GenMeshCubicmap">GenMeshCubicmap</a> | <a href="#GenMeshCylinder">GenMeshCylinder</a> | <a href="#GenMeshHeightmap">GenMeshHeightmap</a> | <a href="#GenMeshHemiSphere">GenMeshHemiSphere</a> | <a href="#GenMeshKnot">GenMeshKnot</a> | <a href="#GenMeshPlane">GenMeshPlane</a> | <a href="#GenMeshPoly">GenMeshPoly</a> | <a href="#GenMeshSphere">GenMeshSphere</a> | <a href="#GenMeshTangents">GenMeshTangents</a> | <a href="#GenMeshTorus">GenMeshTorus</a> | <a href="#GenTextureMipmaps">GenTextureMipmaps</a> | <a href="#GetApplicationDirectory">GetApplicationDirectory</a> | <a href="#GetCameraMatrix">GetCameraMatrix</a> | <a href="#GetCameraMatrix2D">GetCameraMatrix2D</a> | <a href="#GetCharPressed">GetCharPressed</a> | <a href="#GetClipboardText">GetClipboardText</a> | <a href="#GetCodepoint">GetCodepoint</a> | <a href="#GetCodepointCount">GetCodepointCount</a> | <a href="#GetCollisionRec">GetCollisionRec</a> | <a href="#GetColor">GetColor</a> | <a href="#GetCurrentMonitor">GetCurrentMonitor</a> | <a href="#GetDirectoryPath">GetDirectoryPath</a> | <a href="#GetFPS">GetFPS</a> | <a href="#GetFileExtension">GetFileExtension</a> | <a href="#GetFileLength">GetFileLength</a> | <a href="#GetFileModTime">GetFileModTime</a> | <a href="#GetFileName">GetFileName</a> | <a href="#GetFileNameWithoutExt">GetFileNameWithoutExt</a> | <a href="#GetFontDefault">GetFontDefault</a> | <a href="#GetFrameTime">GetFrameTime</a> | <a href="#GetGamepadAxisCount">GetGamepadAxisCount</a> | <a href="#GetGamepadAxisMovement">GetGamepadAxisMovement</a> | <a href="#GetGamepadButtonPressed">GetGamepadButtonPressed</a> | <a href="#GetGamepadName">GetGamepadName</a> | <a href="#GetGestureDetected">GetGestureDetected</a> | <a href="#GetGestureDragAngle">GetGestureDragAngle</a> | <a href="#GetGestureDragVector">GetGestureDragVector</a> | <a href="#GetGestureHoldDuration">GetGestureHoldDuration</a> | <a href="#GetGesturePinchAngle">GetGesturePinchAngle</a> | <a href="#GetGesturePinchVector">GetGesturePinchVector</a> | <a href="#GetGlyphAtlasRec">GetGlyphAtlasRec</a> | <a href="#GetGlyphIndex">GetGlyphIndex</a> | <a href="#GetGlyphInfo">GetGlyphInfo</a> | <a href="#GetImageAlphaBorder">GetImageAlphaBorder</a> | <a href="#GetImageColor">GetImageColor</a> | <a href="#GetKeyPressed">GetKeyPressed</a> | <a href="#GetMeshBoundingBox">GetMeshBoundingBox</a> | <a href="#GetModelBoundingBox">GetModelBoundingBox</a> | <a href="#GetMonitorCount">GetMonitorCount</a> | <a href="#GetMonitorHeight">GetMonitorHeight</a> | <a href="#GetMonitorName">GetMonitorName</a> | <a href="#GetMonitorPhysicalHeight">GetMonitorPhysicalHeight</a> | <a href="#GetMonitorPhysicalWidth">GetMonitorPhysicalWidth</a> | <a href="#GetMonitorPosition">GetMonitorPosition</a> | <a href="#GetMonitorRefreshRate">GetMonitorRefreshRate</a> | <a href="#GetMonitorWidth">GetMonitorWidth</a> | <a href="#GetMouseDelta">GetMouseDelta</a> | <a href="#GetMousePosition">GetMousePosition</a> | <a href="#GetMouseRay">GetMouseRay</a> | <a href="#GetMouseWheelMove">GetMouseWheelMove</a> | <a href="#GetMouseWheelMoveV">GetMouseWheelMoveV</a> | <a href="#GetMouseX">GetMouseX</a> | <a href="#GetMouseY">GetMouseY</a> | <a href="#GetMusicTimeLength">GetMusicTimeLength</a> | <a href="#GetMusicTimePlayed">GetMusicTimePlayed</a> | <a href="#GetPixelColor">GetPixelColor</a> | <a href="#GetPixelDataSize">GetPixelDataSize</a> | <a href="#GetPrevDirectoryPath">GetPrevDirectoryPath</a> | <a href="#GetRandomValue">GetRandomValue</a> | <a href="#GetRayCollisionBox">GetRayCollisionBox</a> | <a href="#GetRayCollisionMesh">GetRayCollisionMesh</a> | <a href="#GetRayCollisionQuad">GetRayCollisionQuad</a> | <a href="#GetRayCollisionSphere">GetRayCollisionSphere</a> | <a href="#GetRayCollisionTriangle">GetRayCollisionTriangle</a> | <a href="#GetRenderHeight">GetRenderHeight</a> | <a href="#GetRenderWidth">GetRenderWidth</a> | <a href="#GetScreenHeight">GetScreenHeight</a> | <a href="#GetScreenToWorld2D">GetScreenToWorld2D</a> | <a href="#GetScreenWidth">GetScreenWidth</a> | <a href="#GetShaderLocation">GetShaderLocation</a> | <a href="#GetShaderLocationAttrib">GetShaderLocationAttrib</a> | <a href="#GetSoundsPlaying">GetSoundsPlaying</a> | <a href="#GetTime">GetTime</a> | <a href="#GetTouchPointCount">GetTouchPointCount</a> | <a href="#GetTouchPointId">GetTouchPointId</a> | <a href="#GetTouchPosition">GetTouchPosition</a> | <a href="#GetTouchX">GetTouchX</a> | <a href="#GetTouchY">GetTouchY</a> | <a href="#GetWindowHandle">GetWindowHandle</a> | <a href="#GetWindowPosition">GetWindowPosition</a> | <a href="#GetWindowScaleDPI">GetWindowScaleDPI</a> | <a href="#GetWorkingDirectory">GetWorkingDirectory</a> | <a href="#GetWorldToScreen">GetWorldToScreen</a> | <a href="#GetWorldToScreen2D">GetWorldToScreen2D</a> | <a href="#GetWorldToScreenEx">GetWorldToScreenEx</a> | <a href="#HideCursor">HideCursor</a> | <a href="#ImageAlphaClear">ImageAlphaClear</a> | <a href="#ImageAlphaCrop">ImageAlphaCrop</a> | <a href="#ImageAlphaMask">ImageAlphaMask</a> | <a href="#ImageAlphaPremultiply">ImageAlphaPremultiply</a> | <a href="#ImageClearBackground">ImageClearBackground</a> | <a href="#ImageColorBrightness">ImageColorBrightness</a> | <a href="#ImageColorContrast">ImageColorContrast</a> | <a href="#ImageColorGrayscale">ImageColorGrayscale</a> | <a href="#ImageColorInvert">ImageColorInvert</a> | <a href="#ImageColorReplace">ImageColorReplace</a> | <a href="#ImageColorTint">ImageColorTint</a> | <a href="#ImageCopy">ImageCopy</a> | <a href="#ImageCrop">ImageCrop</a> | <a href="#ImageDither">ImageDither</a> | <a href="#ImageDraw">ImageDraw</a> | <a href="#ImageDrawCircle">ImageDrawCircle</a> | <a href="#ImageDrawCircleV">ImageDrawCircleV</a> | <a href="#ImageDrawLine">ImageDrawLine</a> | <a href="#ImageDrawLineV">ImageDrawLineV</a> | <a href="#ImageDrawPixel">ImageDrawPixel</a> | <a href="#ImageDrawPixelV">ImageDrawPixelV</a> | <a href="#ImageDrawRectangle">ImageDrawRectangle</a> | <a href="#ImageDrawRectangleLines">ImageDrawRectangleLines</a> | <a href="#ImageDrawRectangleRec">ImageDrawRectangleRec</a> | <a href="#ImageDrawRectangleV">ImageDrawRectangleV</a> | <a href="#ImageDrawText">ImageDrawText</a> | <a href="#ImageDrawTextEx">ImageDrawTextEx</a> | <a href="#ImageFlipHorizontal">ImageFlipHorizontal</a> | <a href="#ImageFlipVertical">ImageFlipVertical</a> | <a href="#ImageFormat">ImageFormat</a> | <a href="#ImageFromImage">ImageFromImage</a> | <a href="#ImageMipmaps">ImageMipmaps</a> | <a href="#ImageResize">ImageResize</a> | <a href="#ImageResizeCanvas">ImageResizeCanvas</a> | <a href="#ImageResizeNN">ImageResizeNN</a> | <a href="#ImageRotateCCW">ImageRotateCCW</a> | <a href="#ImageRotateCW">ImageRotateCW</a> | <a href="#ImageText">ImageText</a> | <a href="#ImageTextEx">ImageTextEx</a> | <a href="#ImageToPOT">ImageToPOT</a> | <a href="#InitAudioDevice">InitAudioDevice</a> | <a href="#InitWindow">InitWindow</a> | <a href="#IsAudioDeviceReady">IsAudioDeviceReady</a> | <a href="#IsAudioStreamPlaying">IsAudioStreamPlaying</a> | <a href="#IsAudioStreamProcessed">IsAudioStreamProcessed</a> | <a href="#IsCursorHidden">IsCursorHidden</a> | <a href="#IsCursorOnScreen">IsCursorOnScreen</a> | <a href="#IsFileDropped">IsFileDropped</a> | <a href="#IsFileExtension">IsFileExtension</a> | <a href="#IsGamepadAvailable">IsGamepadAvailable</a> | <a href="#IsGamepadButtonDown">IsGamepadButtonDown</a> | <a href="#IsGamepadButtonPressed">IsGamepadButtonPressed</a> | <a href="#IsGamepadButtonReleased">IsGamepadButtonReleased</a> | <a href="#IsGamepadButtonUp">IsGamepadButtonUp</a> | <a href="#IsGestureDetected">IsGestureDetected</a> | <a href="#IsKeyDown">IsKeyDown</a> | <a href="#IsKeyPressed">IsKeyPressed</a> | <a href="#IsKeyReleased">IsKeyReleased</a> | <a href="#IsKeyUp">IsKeyUp</a> | <a href="#IsModelAnimationValid">IsModelAnimationValid</a> | <a href="#IsMouseButtonDown">IsMouseButtonDown</a> | <a href="#IsMouseButtonPressed">IsMouseButtonPressed</a> | <a href="#IsMouseButtonReleased">IsMouseButtonReleased</a> | <a href="#IsMouseButtonUp">IsMouseButtonUp</a> | <a href="#IsMusicStreamPlaying">IsMusicStreamPlaying</a> | <a href="#IsPathFile">IsPathFile</a> | <a href="#IsSoundPlaying">IsSoundPlaying</a> | <a href="#IsWindowFocused">IsWindowFocused</a> | <a href="#IsWindowFullscreen">IsWindowFullscreen</a> | <a href="#IsWindowHidden">IsWindowHidden</a> | <a href="#IsWindowMaximized">IsWindowMaximized</a> | <a href="#IsWindowMinimized">IsWindowMinimized</a> | <a href="#IsWindowReady">IsWindowReady</a> | <a href="#IsWindowResized">IsWindowResized</a> | <a href="#IsWindowState">IsWindowState</a> | <a href="#Lerp">Lerp</a> | <a href="#LoadAudioStream">LoadAudioStream</a> | <a href="#LoadCodepoints">LoadCodepoints</a> | <a href="#LoadDirectoryFiles">LoadDirectoryFiles</a> | <a href="#LoadDirectoryFilesEx">LoadDirectoryFilesEx</a> | <a href="#LoadDroppedFiles">LoadDroppedFiles</a> | <a href="#LoadFileData">LoadFileData</a> | <a href="#LoadFileText">LoadFileText</a> | <a href="#LoadFont">LoadFont</a> | <a href="#LoadFontData">LoadFontData</a> | <a href="#LoadFontEx">LoadFontEx</a> | <a href="#LoadFontFromImage">LoadFontFromImage</a> | <a href="#LoadFontFromMemory">LoadFontFromMemory</a> | <a href="#LoadImage">LoadImage</a> | <a href="#LoadImageAnim">LoadImageAnim</a> | <a href="#LoadImageColors">LoadImageColors</a> | <a href="#LoadImageFromMemory">LoadImageFromMemory</a> | <a href="#LoadImageFromScreen">LoadImageFromScreen</a> | <a href="#LoadImageFromTexture">LoadImageFromTexture</a> | <a href="#LoadImagePalette">LoadImagePalette</a> | <a href="#LoadImageRaw">LoadImageRaw</a> | <a href="#LoadMaterialDefault">LoadMaterialDefault</a> | <a href="#LoadMaterials">LoadMaterials</a> | <a href="#LoadModel">LoadModel</a> | <a href="#LoadModelAnimations">LoadModelAnimations</a> | <a href="#LoadModelFromMesh">LoadModelFromMesh</a> | <a href="#LoadMusicStream">LoadMusicStream</a> | <a href="#LoadMusicStreamFromMemory">LoadMusicStreamFromMemory</a> | <a href="#LoadRenderTexture">LoadRenderTexture</a> | <a href="#LoadShader">LoadShader</a> | <a href="#LoadShaderFromMemory">LoadShaderFromMemory</a> | <a href="#LoadSound">LoadSound</a> | <a href="#LoadSoundFromWave">LoadSoundFromWave</a> | <a href="#LoadTexture">LoadTexture</a> | <a href="#LoadTextureCubemap">LoadTextureCubemap</a> | <a href="#LoadTextureFromImage">LoadTextureFromImage</a> | <a href="#LoadVrStereoConfig">LoadVrStereoConfig</a> | <a href="#LoadWave">LoadWave</a> | <a href="#LoadWaveFromMemory">LoadWaveFromMemory</a> | <a href="#LoadWaveSamples">LoadWaveSamples</a> | <a href="#MatrixAdd">MatrixAdd</a> | <a href="#MatrixDeterminant">MatrixDeterminant</a> | <a href="#MatrixFrustum">MatrixFrustum</a> | <a href="#MatrixIdentity">MatrixIdentity</a> | <a href="#MatrixInvert">MatrixInvert</a> | <a href="#MatrixLookAt">MatrixLookAt</a> | <a href="#MatrixMultiply">MatrixMultiply</a> | <a href="#MatrixOrtho">MatrixOrtho</a> | <a href="#MatrixPerspective">MatrixPerspective</a> | <a href="#MatrixRotate">MatrixRotate</a> | <a href="#MatrixRotateX">MatrixRotateX</a> | <a href="#MatrixRotateXYZ">MatrixRotateXYZ</a> | <a href="#MatrixRotateY">MatrixRotateY</a> | <a href="#MatrixRotateZ">MatrixRotateZ</a> | <a href="#MatrixRotateZYX">MatrixRotateZYX</a> | <a href="#MatrixScale">MatrixScale</a> | <a href="#MatrixSubtract">MatrixSubtract</a> | <a href="#MatrixToFloatV">MatrixToFloatV</a> | <a href="#MatrixTrace">MatrixTrace</a> | <a href="#MatrixTranslate">MatrixTranslate</a> | <a href="#MatrixTranspose">MatrixTranspose</a> | <a href="#MaximizeWindow">MaximizeWindow</a> | <a href="#MeasureText">MeasureText</a> | <a href="#MeasureTextEx">MeasureTextEx</a> | <a href="#MemAlloc">MemAlloc</a> | <a href="#MemFree">MemFree</a> | <a href="#MemRealloc">MemRealloc</a> | <a href="#MinimizeWindow">MinimizeWindow</a> | <a href="#Normalize">Normalize</a> | <a href="#OpenURL">OpenURL</a> | <a href="#PauseAudioStream">PauseAudioStream</a> | <a href="#PauseMusicStream">PauseMusicStream</a> | <a href="#PauseSound">PauseSound</a> | <a href="#PlayAudioStream">PlayAudioStream</a> | <a href="#PlayMusicStream">PlayMusicStream</a> | <a href="#PlaySound">PlaySound</a> | <a href="#PlaySoundMulti">PlaySoundMulti</a> | <a href="#PollInputEvents">PollInputEvents</a> | <a href="#QuaternionAdd">QuaternionAdd</a> | <a href="#QuaternionAddValue">QuaternionAddValue</a> | <a href="#QuaternionDivide">QuaternionDivide</a> | <a href="#QuaternionEquals">QuaternionEquals</a> | <a href="#QuaternionFromAxisAngle">QuaternionFromAxisAngle</a> | <a href="#QuaternionFromEuler">QuaternionFromEuler</a> | <a href="#QuaternionFromMatrix">QuaternionFromMatrix</a> | <a href="#QuaternionFromVector3ToVector3">QuaternionFromVector3ToVector3</a> | <a href="#QuaternionIdentity">QuaternionIdentity</a> | <a href="#QuaternionInvert">QuaternionInvert</a> | <a href="#QuaternionLength">QuaternionLength</a> | <a href="#QuaternionMultiply">QuaternionMultiply</a> | <a href="#QuaternionNlerp">QuaternionNlerp</a> | <a href="#QuaternionNormalize">QuaternionNormalize</a> | <a href="#QuaternionScale">QuaternionScale</a> | <a href="#QuaternionSlerp">QuaternionSlerp</a> | <a href="#QuaternionSubtract">QuaternionSubtract</a> | <a href="#QuaternionSubtractValue">QuaternionSubtractValue</a> | <a href="#QuaternionToAxisAngle">QuaternionToAxisAngle</a> | <a href="#QuaternionToEuler">QuaternionToEuler</a> | <a href="#QuaternionToMatrix">QuaternionToMatrix</a> | <a href="#QuaternionTransform">QuaternionTransform</a> | <a href="#Remap">Remap</a> | <a href="#RestoreWindow">RestoreWindow</a> | <a href="#ResumeAudioStream">ResumeAudioStream</a> | <a href="#ResumeMusicStream">ResumeMusicStream</a> | <a href="#ResumeSound">ResumeSound</a> | <a href="#SaveFileData">SaveFileData</a> | <a href="#SaveFileText">SaveFileText</a> | <a href="#SeekMusicStream">SeekMusicStream</a> | <a href="#SetAudioStreamBufferSizeDefault">SetAudioStreamBufferSizeDefault</a> | <a href="#SetAudioStreamCallback">SetAudioStreamCallback</a> | <a href="#SetAudioStreamPan">SetAudioStreamPan</a> | <a href="#SetAudioStreamPitch">SetAudioStreamPitch</a> | <a href="#SetAudioStreamVolume">SetAudioStreamVolume</a> | <a href="#SetCameraAltControl">SetCameraAltControl</a> | <a href="#SetCameraMode">SetCameraMode</a> | <a href="#SetCameraMoveControls">SetCameraMoveControls</a> | <a href="#SetCameraPanControl">SetCameraPanControl</a> | <a href="#SetCameraSmoothZoomControl">SetCameraSmoothZoomControl</a> | <a href="#SetClipboardText">SetClipboardText</a> | <a href="#SetConfigFlags">SetConfigFlags</a> | <a href="#SetExitKey">SetExitKey</a> | <a href="#SetGamepadMappings">SetGamepadMappings</a> | <a href="#SetGesturesEnabled">SetGesturesEnabled</a> | <a href="#SetLoadFileDataCallback">SetLoadFileDataCallback</a> | <a href="#SetLoadFileTextCallback">SetLoadFileTextCallback</a> | <a href="#SetMasterVolume">SetMasterVolume</a> | <a href="#SetMaterialTexture">SetMaterialTexture</a> | <a href="#SetModelMeshMaterial">SetModelMeshMaterial</a> | <a href="#SetMouseCursor">SetMouseCursor</a> | <a href="#SetMouseOffset">SetMouseOffset</a> | <a href="#SetMousePosition">SetMousePosition</a> | <a href="#SetMouseScale">SetMouseScale</a> | <a href="#SetMusicPan">SetMusicPan</a> | <a href="#SetMusicPitch">SetMusicPitch</a> | <a href="#SetMusicVolume">SetMusicVolume</a> | <a href="#SetPixelColor">SetPixelColor</a> | <a href="#SetRandomSeed">SetRandomSeed</a> | <a href="#SetSaveFileDataCallback">SetSaveFileDataCallback</a> | <a href="#SetSaveFileTextCallback">SetSaveFileTextCallback</a> | <a href="#SetShaderValue">SetShaderValue</a> | <a href="#SetShaderValueMatrix">SetShaderValueMatrix</a> | <a href="#SetShaderValueTexture">SetShaderValueTexture</a> | <a href="#SetShaderValueV">SetShaderValueV</a> | <a href="#SetShapesTexture">SetShapesTexture</a> | <a href="#SetSoundPan">SetSoundPan</a> | <a href="#SetSoundPitch">SetSoundPitch</a> | <a href="#SetSoundVolume">SetSoundVolume</a> | <a href="#SetTargetFPS">SetTargetFPS</a> | <a href="#SetTextureFilter">SetTextureFilter</a> | <a href="#SetTextureWrap">SetTextureWrap</a> | <a href="#SetTraceLogCallback">SetTraceLogCallback</a> | <a href="#SetTraceLogLevel">SetTraceLogLevel</a> | <a href="#SetWindowIcon">SetWindowIcon</a> | <a href="#SetWindowMinSize">SetWindowMinSize</a> | <a href="#SetWindowMonitor">SetWindowMonitor</a> | <a href="#SetWindowOpacity">SetWindowOpacity</a> | <a href="#SetWindowPosition">SetWindowPosition</a> | <a href="#SetWindowSize">SetWindowSize</a> | <a href="#SetWindowState">SetWindowState</a> | <a href="#SetWindowTitle">SetWindowTitle</a> | <a href="#ShowCursor">ShowCursor</a> | <a href="#StopAudioStream">StopAudioStream</a> | <a href="#StopMusicStream">StopMusicStream</a> | <a href="#StopSound">StopSound</a> | <a href="#StopSoundMulti">StopSoundMulti</a> | <a href="#SwapScreenBuffer">SwapScreenBuffer</a> | <a href="#TakeScreenshot">TakeScreenshot</a> | <a href="#TextAppend">TextAppend</a> | <a href="#TextCodepointsToUTF8">TextCodepointsToUTF8</a> | <a href="#TextCopy">TextCopy</a> | <a href="#TextFindIndex">TextFindIndex</a> | <a href="#TextFormat">TextFormat</a> | <a href="#TextInsert">TextInsert</a> | <a href="#TextIsEqual">TextIsEqual</a> | <a href="#TextJoin">TextJoin</a> | <a href="#TextLength">TextLength</a> | <a href="#TextReplace">TextReplace</a> | <a href="#TextSplit">TextSplit</a> | <a href="#TextSubtext">TextSubtext</a> | <a href="#TextToInteger">TextToInteger</a> | <a href="#TextToLower">TextToLower</a> | <a href="#TextToPascal">TextToPascal</a> | <a href="#TextToUpper">TextToUpper</a> | <a href="#ToggleFullscreen">ToggleFullscreen</a> | <a href="#TraceLog">TraceLog</a> | <a href="#UnloadAudioStream">UnloadAudioStream</a> | <a href="#UnloadCodepoints">UnloadCodepoints</a> | <a href="#UnloadDirectoryFiles">UnloadDirectoryFiles</a> | <a href="#UnloadDroppedFiles">UnloadDroppedFiles</a> | <a href="#UnloadFileData">UnloadFileData</a> | <a href="#UnloadFileText">UnloadFileText</a> | <a href="#UnloadFont">UnloadFont</a> | <a href="#UnloadFontData">UnloadFontData</a> | <a href="#UnloadImage">UnloadImage</a> | <a href="#UnloadImageColors">UnloadImageColors</a> | <a href="#UnloadImagePalette">UnloadImagePalette</a> | <a href="#UnloadMaterial">UnloadMaterial</a> | <a href="#UnloadMesh">UnloadMesh</a> | <a href="#UnloadModel">UnloadModel</a> | <a href="#UnloadModelAnimation">UnloadModelAnimation</a> | <a href="#UnloadModelAnimations">UnloadModelAnimations</a> | <a href="#UnloadModelKeepMeshes">UnloadModelKeepMeshes</a> | <a href="#UnloadMusicStream">UnloadMusicStream</a> | <a href="#UnloadRenderTexture">UnloadRenderTexture</a> | <a href="#UnloadShader">UnloadShader</a> | <a href="#UnloadSound">UnloadSound</a> | <a href="#UnloadTexture">UnloadTexture</a> | <a href="#UnloadVrStereoConfig">UnloadVrStereoConfig</a> | <a href="#UnloadWave">UnloadWave</a> | <a href="#UnloadWaveSamples">UnloadWaveSamples</a> | <a href="#UpdateAudioStream">UpdateAudioStream</a> | <a href="#UpdateCamera">UpdateCamera</a> | <a href="#UpdateMeshBuffer">UpdateMeshBuffer</a> | <a href="#UpdateModelAnimation">UpdateModelAnimation</a> | <a href="#UpdateMusicStream">UpdateMusicStream</a> | <a href="#UpdateSound">UpdateSound</a> | <a href="#UpdateTexture">UpdateTexture</a> | <a href="#UpdateTextureRec">UpdateTextureRec</a> | <a href="#UploadMesh">UploadMesh</a> | <a href="#Vector2Add">Vector2Add</a> | <a href="#Vector2AddValue">Vector2AddValue</a> | <a href="#Vector2Angle">Vector2Angle</a> | <a href="#Vector2Clamp">Vector2Clamp</a> | <a href="#Vector2ClampValue">Vector2ClampValue</a> | <a href="#Vector2Distance">Vector2Distance</a> | <a href="#Vector2DistanceSqr">Vector2DistanceSqr</a> | <a href="#Vector2Divide">Vector2Divide</a> | <a href="#Vector2DotProduct">Vector2DotProduct</a> | <a href="#Vector2Equals">Vector2Equals</a> | <a href="#Vector2Invert">Vector2Invert</a> | <a href="#Vector2Length">Vector2Length</a> | <a href="#Vector2LengthSqr">Vector2LengthSqr</a> | <a href="#Vector2Lerp">Vector2Lerp</a> | <a href="#Vector2MoveTowards">Vector2MoveTowards</a> | <a href="#Vector2Multiply">Vector2Multiply</a> | <a href="#Vector2Negate">Vector2Negate</a> | <a href="#Vector2Normalize">Vector2Normalize</a> | <a href="#Vector2One">Vector2One</a> | <a href="#Vector2Reflect">Vector2Reflect</a> | <a href="#Vector2Rotate">Vector2Rotate</a> | <a href="#Vector2Scale">Vector2Scale</a> | <a href="#Vector2Subtract">Vector2Subtract</a> | <a href="#Vector2SubtractValue">Vector2SubtractValue</a> | <a href="#Vector2Transform">Vector2Transform</a> | <a href="#Vector2Zero">Vector2Zero</a> | <a href="#Vector3Add">Vector3Add</a> | <a href="#Vector3AddValue">Vector3AddValue</a> | <a href="#Vector3Angle">Vector3Angle</a> | <a href="#Vector3Barycenter">Vector3Barycenter</a> | <a href="#Vector3Clamp">Vector3Clamp</a> | <a href="#Vector3ClampValue">Vector3ClampValue</a> | <a href="#Vector3CrossProduct">Vector3CrossProduct</a> | <a href="#Vector3Distance">Vector3Distance</a> | <a href="#Vector3DistanceSqr">Vector3DistanceSqr</a> | <a href="#Vector3Divide">Vector3Divide</a> | <a href="#Vector3DotProduct">Vector3DotProduct</a> | <a href="#Vector3Equals">Vector3Equals</a> | <a href="#Vector3Invert">Vector3Invert</a> | <a href="#Vector3Length">Vector3Length</a> | <a href="#Vector3LengthSqr">Vector3LengthSqr</a> | <a href="#Vector3Lerp">Vector3Lerp</a> | <a href="#Vector3Max">Vector3Max</a> | <a href="#Vector3Min">Vector3Min</a> | <a href="#Vector3Multiply">Vector3Multiply</a> | <a href="#Vector3Negate">Vector3Negate</a> | <a href="#Vector3Normalize">Vector3Normalize</a> | <a href="#Vector3One">Vector3One</a> | <a href="#Vector3OrthoNormalize">Vector3OrthoNormalize</a> | <a href="#Vector3Perpendicular">Vector3Perpendicular</a> | <a href="#Vector3Reflect">Vector3Reflect</a> | <a href="#Vector3Refract">Vector3Refract</a> | <a href="#Vector3RotateByAxisAngle">Vector3RotateByAxisAngle</a> | <a href="#Vector3RotateByQuaternion">Vector3RotateByQuaternion</a> | <a href="#Vector3Scale">Vector3Scale</a> | <a href="#Vector3Subtract">Vector3Subtract</a> | <a href="#Vector3SubtractValue">Vector3SubtractValue</a> | <a href="#Vector3ToFloatV">Vector3ToFloatV</a> | <a href="#Vector3Transform">Vector3Transform</a> | <a href="#Vector3Unproject">Vector3Unproject</a> | <a href="#Vector3Zero">Vector3Zero</a> | <a href="#WaitTime">WaitTime</a> | <a href="#WaveCopy">WaveCopy</a> | <a href="#WaveCrop">WaveCrop</a> | <a href="#WaveFormat">WaveFormat</a> | <a href="#WindowShouldClose">WindowShouldClose</a> | <a href="#Wrap">Wrap</a> | <a href="#rlActiveDrawBuffers">rlActiveDrawBuffers</a> | <a href="#rlActiveTextureSlot">rlActiveTextureSlot</a> | <a href="#rlBegin">rlBegin</a> | <a href="#rlBindImageTexture">rlBindImageTexture</a> | <a href="#rlBindShaderBuffer">rlBindShaderBuffer</a> | <a href="#rlCheckErrors">rlCheckErrors</a> | <a href="#rlCheckRenderBatchLimit">rlCheckRenderBatchLimit</a> | <a href="#rlClearColor">rlClearColor</a> | <a href="#rlClearScreenBuffers">rlClearScreenBuffers</a> | <a href="#rlColor3f">rlColor3f</a> | <a href="#rlColor4f">rlColor4f</a> | <a href="#rlColor4ub">rlColor4ub</a> | <a href="#rlCompileShader">rlCompileShader</a> | <a href="#rlComputeShaderDispatch">rlComputeShaderDispatch</a> | <a href="#rlCopyBuffersElements">rlCopyBuffersElements</a> | <a href="#rlDisableBackfaceCulling">rlDisableBackfaceCulling</a> | <a href="#rlDisableColorBlend">rlDisableColorBlend</a> | <a href="#rlDisableDepthMask">rlDisableDepthMask</a> | <a href="#rlDisableDepthTest">rlDisableDepthTest</a> | <a href="#rlDisableFramebuffer">rlDisableFramebuffer</a> | <a href="#rlDisableScissorTest">rlDisableScissorTest</a> | <a href="#rlDisableShader">rlDisableShader</a> | <a href="#rlDisableSmoothLines">rlDisableSmoothLines</a> | <a href="#rlDisableStereoRender">rlDisableStereoRender</a> | <a href="#rlDisableTexture">rlDisableTexture</a> | <a href="#rlDisableTextureCubemap">rlDisableTextureCubemap</a> | <a href="#rlDisableVertexArray">rlDisableVertexArray</a> | <a href="#rlDisableVertexAttribute">rlDisableVertexAttribute</a> | <a href="#rlDisableVertexBuffer">rlDisableVertexBuffer</a> | <a href="#rlDisableVertexBufferElement">rlDisableVertexBufferElement</a> | <a href="#rlDisableWireMode">rlDisableWireMode</a> | <a href="#rlDrawRenderBatch">rlDrawRenderBatch</a> | <a href="#rlDrawRenderBatchActive">rlDrawRenderBatchActive</a> | <a href="#rlDrawVertexArray">rlDrawVertexArray</a> | <a href="#rlDrawVertexArrayElements">rlDrawVertexArrayElements</a> | <a href="#rlDrawVertexArrayElementsInstanced">rlDrawVertexArrayElementsInstanced</a> | <a href="#rlDrawVertexArrayInstanced">rlDrawVertexArrayInstanced</a> | <a href="#rlEnableBackfaceCulling">rlEnableBackfaceCulling</a> | <a href="#rlEnableColorBlend">rlEnableColorBlend</a> | <a href="#rlEnableDepthMask">rlEnableDepthMask</a> | <a href="#rlEnableDepthTest">rlEnableDepthTest</a> | <a href="#rlEnableFramebuffer">rlEnableFramebuffer</a> | <a href="#rlEnableScissorTest">rlEnableScissorTest</a> | <a href="#rlEnableShader">rlEnableShader</a> | <a href="#rlEnableSmoothLines">rlEnableSmoothLines</a> | <a href="#rlEnableStereoRender">rlEnableStereoRender</a> | <a href="#rlEnableTexture">rlEnableTexture</a> | <a href="#rlEnableTextureCubemap">rlEnableTextureCubemap</a> | <a href="#rlEnableVertexArray">rlEnableVertexArray</a> | <a href="#rlEnableVertexAttribute">rlEnableVertexAttribute</a> | <a href="#rlEnableVertexBuffer">rlEnableVertexBuffer</a> | <a href="#rlEnableVertexBufferElement">rlEnableVertexBufferElement</a> | <a href="#rlEnableWireMode">rlEnableWireMode</a> | <a href="#rlEnd">rlEnd</a> | <a href="#rlFramebufferAttach">rlFramebufferAttach</a> | <a href="#rlFramebufferComplete">rlFramebufferComplete</a> | <a href="#rlFrustum">rlFrustum</a> | <a href="#rlGenTextureMipmaps">rlGenTextureMipmaps</a> | <a href="#rlGetFramebufferHeight">rlGetFramebufferHeight</a> | <a href="#rlGetFramebufferWidth">rlGetFramebufferWidth</a> | <a href="#rlGetGlTextureFormats">rlGetGlTextureFormats</a> | <a href="#rlGetLineWidth">rlGetLineWidth</a> | <a href="#rlGetLocationAttrib">rlGetLocationAttrib</a> | <a href="#rlGetLocationUniform">rlGetLocationUniform</a> | <a href="#rlGetMatrixModelview">rlGetMatrixModelview</a> | <a href="#rlGetMatrixProjection">rlGetMatrixProjection</a> | <a href="#rlGetMatrixProjectionStereo">rlGetMatrixProjectionStereo</a> | <a href="#rlGetMatrixTransform">rlGetMatrixTransform</a> | <a href="#rlGetMatrixViewOffsetStereo">rlGetMatrixViewOffsetStereo</a> | <a href="#rlGetPixelFormatName">rlGetPixelFormatName</a> | <a href="#rlGetShaderBufferSize">rlGetShaderBufferSize</a> | <a href="#rlGetShaderIdDefault">rlGetShaderIdDefault</a> | <a href="#rlGetShaderLocsDefault">rlGetShaderLocsDefault</a> | <a href="#rlGetTextureIdDefault">rlGetTextureIdDefault</a> | <a href="#rlGetVersion">rlGetVersion</a> | <a href="#rlIsStereoRenderEnabled">rlIsStereoRenderEnabled</a> | <a href="#rlLoadComputeShaderProgram">rlLoadComputeShaderProgram</a> | <a href="#rlLoadDrawCube">rlLoadDrawCube</a> | <a href="#rlLoadDrawQuad">rlLoadDrawQuad</a> | <a href="#rlLoadExtensions">rlLoadExtensions</a> | <a href="#rlLoadFramebuffer">rlLoadFramebuffer</a> | <a href="#rlLoadIdentity">rlLoadIdentity</a> | <a href="#rlLoadRenderBatch">rlLoadRenderBatch</a> | <a href="#rlLoadShaderBuffer">rlLoadShaderBuffer</a> | <a href="#rlLoadShaderCode">rlLoadShaderCode</a> | <a href="#rlLoadShaderProgram">rlLoadShaderProgram</a> | <a href="#rlLoadTexture">rlLoadTexture</a> | <a href="#rlLoadTextureCubemap">rlLoadTextureCubemap</a> | <a href="#rlLoadTextureDepth">rlLoadTextureDepth</a> | <a href="#rlLoadVertexArray">rlLoadVertexArray</a> | <a href="#rlLoadVertexBuffer">rlLoadVertexBuffer</a> | <a href="#rlLoadVertexBufferElement">rlLoadVertexBufferElement</a> | <a href="#rlMatrixMode">rlMatrixMode</a> | <a href="#rlMultMatrixf">rlMultMatrixf</a> | <a href="#rlNormal3f">rlNormal3f</a> | <a href="#rlOrtho">rlOrtho</a> | <a href="#rlPopMatrix">rlPopMatrix</a> | <a href="#rlPushMatrix">rlPushMatrix</a> | <a href="#rlReadScreenPixels">rlReadScreenPixels</a> | <a href="#rlReadShaderBufferElements">rlReadShaderBufferElements</a> | <a href="#rlReadTexturePixels">rlReadTexturePixels</a> | <a href="#rlRotatef">rlRotatef</a> | <a href="#rlScalef">rlScalef</a> | <a href="#rlScissor">rlScissor</a> | <a href="#rlSetBlendFactors">rlSetBlendFactors</a> | <a href="#rlSetBlendMode">rlSetBlendMode</a> | <a href="#rlSetFramebufferHeight">rlSetFramebufferHeight</a> | <a href="#rlSetFramebufferWidth">rlSetFramebufferWidth</a> | <a href="#rlSetLineWidth">rlSetLineWidth</a> | <a href="#rlSetMatrixModelview">rlSetMatrixModelview</a> | <a href="#rlSetMatrixProjection">rlSetMatrixProjection</a> | <a href="#rlSetMatrixProjectionStereo">rlSetMatrixProjectionStereo</a> | <a href="#rlSetMatrixViewOffsetStereo">rlSetMatrixViewOffsetStereo</a> | <a href="#rlSetRenderBatchActive">rlSetRenderBatchActive</a> | <a href="#rlSetShader">rlSetShader</a> | <a href="#rlSetTexture">rlSetTexture</a> | <a href="#rlSetUniform">rlSetUniform</a> | <a href="#rlSetUniformMatrix">rlSetUniformMatrix</a> | <a href="#rlSetUniformSampler">rlSetUniformSampler</a> | <a href="#rlSetVertexAttribute">rlSetVertexAttribute</a> | <a href="#rlSetVertexAttributeDefault">rlSetVertexAttributeDefault</a> | <a href="#rlSetVertexAttributeDivisor">rlSetVertexAttributeDivisor</a> | <a href="#rlTexCoord2f">rlTexCoord2f</a> | <a href="#rlTextureParameters">rlTextureParameters</a> | <a href="#rlTranslatef">rlTranslatef</a> | <a href="#rlUnloadFramebuffer">rlUnloadFramebuffer</a> | <a href="#rlUnloadRenderBatch">rlUnloadRenderBatch</a> | <a href="#rlUnloadShaderBuffer">rlUnloadShaderBuffer</a> | <a href="#rlUnloadShaderProgram">rlUnloadShaderProgram</a> | <a href="#rlUnloadTexture">rlUnloadTexture</a> | <a href="#rlUnloadVertexArray">rlUnloadVertexArray</a> | <a href="#rlUnloadVertexBuffer">rlUnloadVertexBuffer</a> | <a href="#rlUpdateShaderBufferElements">rlUpdateShaderBufferElements</a> | <a href="#rlUpdateTexture">rlUpdateTexture</a> | <a href="#rlUpdateVertexBuffer">rlUpdateVertexBuffer</a> | <a href="#rlUpdateVertexBufferElements">rlUpdateVertexBufferElements</a> | <a href="#rlVertex2f">rlVertex2f</a> | <a href="#rlVertex2i">rlVertex2i</a> | <a href="#rlVertex3f">rlVertex3f</a> | <a href="#rlViewport">rlViewport</a> | <a href="#rlglClose">rlglClose</a> | <a href="#rlglInit">rlglInit</a>

[ <a href="#toc">ToC</a> ]

<h2 id="InitWindow"><code>init_window</code> function</h2>

> Initialize window and OpenGL context

Defined in raylib.h:

```c
void InitWindow(int width, int height, char * title) 
```

Python wrapper:

```python
def init_window(width: int, height: int, title: Union[str, CharPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="WindowShouldClose"><code>window_should_close</code> function</h2>

> Check if KEY_ESCAPE pressed or Close icon pressed

Defined in raylib.h:

```c
bool WindowShouldClose() 
```

Python wrapper:

```python
def window_should_close() -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CloseWindow"><code>close_window</code> function</h2>

> Close window and unload OpenGL context

Defined in raylib.h:

```c
void CloseWindow() 
```

Python wrapper:

```python
def close_window() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsWindowReady"><code>is_window_ready</code> function</h2>

> Check if window has been initialized successfully

Defined in raylib.h:

```c
bool IsWindowReady() 
```

Python wrapper:

```python
def is_window_ready() -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsWindowFullscreen"><code>is_window_fullscreen</code> function</h2>

> Check if window is currently fullscreen

Defined in raylib.h:

```c
bool IsWindowFullscreen() 
```

Python wrapper:

```python
def is_window_fullscreen() -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsWindowHidden"><code>is_window_hidden</code> function</h2>

> Check if window is currently hidden (only PLATFORM_DESKTOP)

Defined in raylib.h:

```c
bool IsWindowHidden() 
```

Python wrapper:

```python
def is_window_hidden() -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsWindowMinimized"><code>is_window_minimized</code> function</h2>

> Check if window is currently minimized (only PLATFORM_DESKTOP)

Defined in raylib.h:

```c
bool IsWindowMinimized() 
```

Python wrapper:

```python
def is_window_minimized() -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsWindowMaximized"><code>is_window_maximized</code> function</h2>

> Check if window is currently maximized (only PLATFORM_DESKTOP)

Defined in raylib.h:

```c
bool IsWindowMaximized() 
```

Python wrapper:

```python
def is_window_maximized() -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsWindowFocused"><code>is_window_focused</code> function</h2>

> Check if window is currently focused (only PLATFORM_DESKTOP)

Defined in raylib.h:

```c
bool IsWindowFocused() 
```

Python wrapper:

```python
def is_window_focused() -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsWindowResized"><code>is_window_resized</code> function</h2>

> Check if window has been resized last frame

Defined in raylib.h:

```c
bool IsWindowResized() 
```

Python wrapper:

```python
def is_window_resized() -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsWindowState"><code>is_window_state</code> function</h2>

> Check if one specific window flag is enabled

Defined in raylib.h:

```c
bool IsWindowState(unsigned int flag) 
```

Python wrapper:

```python
def is_window_state(flag: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetWindowState"><code>set_window_state</code> function</h2>

> Set window configuration state using flags (only PLATFORM_DESKTOP)

Defined in raylib.h:

```c
void SetWindowState(unsigned int flags) 
```

Python wrapper:

```python
def set_window_state(flags: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ClearWindowState"><code>clear_window_state</code> function</h2>

> Clear window configuration state flags

Defined in raylib.h:

```c
void ClearWindowState(unsigned int flags) 
```

Python wrapper:

```python
def clear_window_state(flags: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ToggleFullscreen"><code>toggle_fullscreen</code> function</h2>

> Toggle window state: fullscreen/windowed (only PLATFORM_DESKTOP)

Defined in raylib.h:

```c
void ToggleFullscreen() 
```

Python wrapper:

```python
def toggle_fullscreen() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MaximizeWindow"><code>maximize_window</code> function</h2>

> Set window state: maximized, if resizable (only PLATFORM_DESKTOP)

Defined in raylib.h:

```c
void MaximizeWindow() 
```

Python wrapper:

```python
def maximize_window() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MinimizeWindow"><code>minimize_window</code> function</h2>

> Set window state: minimized, if resizable (only PLATFORM_DESKTOP)

Defined in raylib.h:

```c
void MinimizeWindow() 
```

Python wrapper:

```python
def minimize_window() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="RestoreWindow"><code>restore_window</code> function</h2>

> Set window state: not minimized/maximized (only PLATFORM_DESKTOP)

Defined in raylib.h:

```c
void RestoreWindow() 
```

Python wrapper:

```python
def restore_window() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetWindowIcon"><code>set_window_icon</code> function</h2>

> Set icon for window (only PLATFORM_DESKTOP)

Defined in raylib.h:

```c
void SetWindowIcon(Image image) 
```

Python wrapper:

```python
def set_window_icon(image: Image) -> None
```

See also: <a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetWindowTitle"><code>set_window_title</code> function</h2>

> Set title for window (only PLATFORM_DESKTOP)

Defined in raylib.h:

```c
void SetWindowTitle(char * title) 
```

Python wrapper:

```python
def set_window_title(title: Union[str, CharPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetWindowPosition"><code>set_window_position</code> function</h2>

> Set window position on screen (only PLATFORM_DESKTOP)

Defined in raylib.h:

```c
void SetWindowPosition(int x, int y) 
```

Python wrapper:

```python
def set_window_position(x: int, y: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetWindowMonitor"><code>set_window_monitor</code> function</h2>

> Set monitor for the current window (fullscreen mode)

Defined in raylib.h:

```c
void SetWindowMonitor(int monitor) 
```

Python wrapper:

```python
def set_window_monitor(monitor: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetWindowMinSize"><code>set_window_min_size</code> function</h2>

> Set window minimum dimensions (for FLAG_WINDOW_RESIZABLE)

Defined in raylib.h:

```c
void SetWindowMinSize(int width, int height) 
```

Python wrapper:

```python
def set_window_min_size(width: int, height: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetWindowSize"><code>set_window_size</code> function</h2>

> Set window dimensions

Defined in raylib.h:

```c
void SetWindowSize(int width, int height) 
```

Python wrapper:

```python
def set_window_size(width: int, height: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetWindowOpacity"><code>set_window_opacity</code> function</h2>

> Set window opacity [0.0f..1.0f] (only PLATFORM_DESKTOP)

Defined in raylib.h:

```c
void SetWindowOpacity(float opacity) 
```

Python wrapper:

```python
def set_window_opacity(opacity: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetWindowHandle"><code>get_window_handle</code> function</h2>

> Get native window handle

Defined in raylib.h:

```c
void GetWindowHandle() 
```

Python wrapper:

```python
def get_window_handle() -> bytes
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetScreenWidth"><code>get_screen_width</code> function</h2>

> Get current screen width

Defined in raylib.h:

```c
int GetScreenWidth() 
```

Python wrapper:

```python
def get_screen_width() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetScreenHeight"><code>get_screen_height</code> function</h2>

> Get current screen height

Defined in raylib.h:

```c
int GetScreenHeight() 
```

Python wrapper:

```python
def get_screen_height() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetRenderWidth"><code>get_render_width</code> function</h2>

> Get current render width (it considers HiDPI)

Defined in raylib.h:

```c
int GetRenderWidth() 
```

Python wrapper:

```python
def get_render_width() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetRenderHeight"><code>get_render_height</code> function</h2>

> Get current render height (it considers HiDPI)

Defined in raylib.h:

```c
int GetRenderHeight() 
```

Python wrapper:

```python
def get_render_height() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMonitorCount"><code>get_monitor_count</code> function</h2>

> Get number of connected monitors

Defined in raylib.h:

```c
int GetMonitorCount() 
```

Python wrapper:

```python
def get_monitor_count() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetCurrentMonitor"><code>get_current_monitor</code> function</h2>

> Get current connected monitor

Defined in raylib.h:

```c
int GetCurrentMonitor() 
```

Python wrapper:

```python
def get_current_monitor() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMonitorPosition"><code>get_monitor_position</code> function</h2>

> Get specified monitor position

Defined in raylib.h:

```c
Vector2 GetMonitorPosition(int monitor) 
```

Python wrapper:

```python
def get_monitor_position(monitor: int) -> Vector2
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMonitorWidth"><code>get_monitor_width</code> function</h2>

> Get specified monitor width (current video mode used by monitor)

Defined in raylib.h:

```c
int GetMonitorWidth(int monitor) 
```

Python wrapper:

```python
def get_monitor_width(monitor: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMonitorHeight"><code>get_monitor_height</code> function</h2>

> Get specified monitor height (current video mode used by monitor)

Defined in raylib.h:

```c
int GetMonitorHeight(int monitor) 
```

Python wrapper:

```python
def get_monitor_height(monitor: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMonitorPhysicalWidth"><code>get_monitor_physical_width</code> function</h2>

> Get specified monitor physical width in millimetres

Defined in raylib.h:

```c
int GetMonitorPhysicalWidth(int monitor) 
```

Python wrapper:

```python
def get_monitor_physical_width(monitor: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMonitorPhysicalHeight"><code>get_monitor_physical_height</code> function</h2>

> Get specified monitor physical height in millimetres

Defined in raylib.h:

```c
int GetMonitorPhysicalHeight(int monitor) 
```

Python wrapper:

```python
def get_monitor_physical_height(monitor: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMonitorRefreshRate"><code>get_monitor_refresh_rate</code> function</h2>

> Get specified monitor refresh rate

Defined in raylib.h:

```c
int GetMonitorRefreshRate(int monitor) 
```

Python wrapper:

```python
def get_monitor_refresh_rate(monitor: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetWindowPosition"><code>get_window_position</code> function</h2>

> Get window position XY on monitor

Defined in raylib.h:

```c
Vector2 GetWindowPosition() 
```

Python wrapper:

```python
def get_window_position() -> Vector2
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetWindowScaleDPI"><code>get_window_scale_dpi</code> function</h2>

> Get window scale DPI factor

Defined in raylib.h:

```c
Vector2 GetWindowScaleDPI() 
```

Python wrapper:

```python
def get_window_scale_dpi() -> Vector2
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMonitorName"><code>get_monitor_name</code> function</h2>

> Get the human-readable, UTF-8 encoded name of the primary monitor

Defined in raylib.h:

```c
char * GetMonitorName(int monitor) 
```

Python wrapper:

```python
def get_monitor_name(monitor: int) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetClipboardText"><code>set_clipboard_text</code> function</h2>

> Set clipboard text content

Defined in raylib.h:

```c
void SetClipboardText(char * text) 
```

Python wrapper:

```python
def set_clipboard_text(text: Union[str, CharPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetClipboardText"><code>get_clipboard_text</code> function</h2>

> Get clipboard text content

Defined in raylib.h:

```c
char * GetClipboardText() 
```

Python wrapper:

```python
def get_clipboard_text() -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="EnableEventWaiting"><code>enable_event_waiting</code> function</h2>

> Enable waiting for events on EndDrawing(), no automatic event polling

Defined in raylib.h:

```c
void EnableEventWaiting() 
```

Python wrapper:

```python
def enable_event_waiting() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DisableEventWaiting"><code>disable_event_waiting</code> function</h2>

> Disable waiting for events on EndDrawing(), automatic events polling

Defined in raylib.h:

```c
void DisableEventWaiting() 
```

Python wrapper:

```python
def disable_event_waiting() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SwapScreenBuffer"><code>swap_screen_buffer</code> function</h2>

> Swap back buffer with front buffer (screen drawing)

Defined in raylib.h:

```c
void SwapScreenBuffer() 
```

Python wrapper:

```python
def swap_screen_buffer() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="PollInputEvents"><code>poll_input_events</code> function</h2>

> Register all input events

Defined in raylib.h:

```c
void PollInputEvents() 
```

Python wrapper:

```python
def poll_input_events() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="WaitTime"><code>wait_time</code> function</h2>

> Wait for some time (halt program execution)

Defined in raylib.h:

```c
void WaitTime(double seconds) 
```

Python wrapper:

```python
def wait_time(seconds: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ShowCursor"><code>show_cursor</code> function</h2>

> Shows cursor

Defined in raylib.h:

```c
void ShowCursor() 
```

Python wrapper:

```python
def show_cursor() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="HideCursor"><code>hide_cursor</code> function</h2>

> Hides cursor

Defined in raylib.h:

```c
void HideCursor() 
```

Python wrapper:

```python
def hide_cursor() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsCursorHidden"><code>is_cursor_hidden</code> function</h2>

> Check if cursor is not visible

Defined in raylib.h:

```c
bool IsCursorHidden() 
```

Python wrapper:

```python
def is_cursor_hidden() -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="EnableCursor"><code>enable_cursor</code> function</h2>

> Enables cursor (unlock cursor)

Defined in raylib.h:

```c
void EnableCursor() 
```

Python wrapper:

```python
def enable_cursor() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DisableCursor"><code>disable_cursor</code> function</h2>

> Disables cursor (lock cursor)

Defined in raylib.h:

```c
void DisableCursor() 
```

Python wrapper:

```python
def disable_cursor() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsCursorOnScreen"><code>is_cursor_on_screen</code> function</h2>

> Check if cursor is on the screen

Defined in raylib.h:

```c
bool IsCursorOnScreen() 
```

Python wrapper:

```python
def is_cursor_on_screen() -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ClearBackground"><code>clear_background</code> function</h2>

> Set background color (framebuffer clear color)

Defined in raylib.h:

```c
void ClearBackground(Color color) 
```

Python wrapper:

```python
def clear_background(color: Color) -> None
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="BeginDrawing"><code>begin_drawing</code> function</h2>

> Setup canvas (framebuffer) to start drawing

Defined in raylib.h:

```c
void BeginDrawing() 
```

Python wrapper:

```python
def begin_drawing() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="EndDrawing"><code>end_drawing</code> function</h2>

> End canvas drawing and swap buffers (double buffering)

Defined in raylib.h:

```c
void EndDrawing() 
```

Python wrapper:

```python
def end_drawing() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="BeginMode2D"><code>begin_mode2d</code> function</h2>

> Begin 2D mode with custom camera (2D)

Defined in raylib.h:

```c
void BeginMode2D(Camera2D camera) 
```

Python wrapper:

```python
def begin_mode2d(camera: Camera2D) -> None
```

See also: <a href="#Camera2D">Camera2D</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="EndMode2D"><code>end_mode2d</code> function</h2>

> Ends 2D mode with custom camera

Defined in raylib.h:

```c
void EndMode2D() 
```

Python wrapper:

```python
def end_mode2d() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="BeginMode3D"><code>begin_mode3d</code> function</h2>

> Begin 3D mode with custom camera (3D)

Defined in raylib.h:

```c
void BeginMode3D(Camera3D camera) 
```

Python wrapper:

```python
def begin_mode3d(camera: Camera3D) -> None
```

See also: <a href="#Camera3D">Camera3D</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="EndMode3D"><code>end_mode3d</code> function</h2>

> Ends 3D mode and returns to default 2D orthographic mode

Defined in raylib.h:

```c
void EndMode3D() 
```

Python wrapper:

```python
def end_mode3d() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="BeginTextureMode"><code>begin_texture_mode</code> function</h2>

> Begin drawing to render texture

Defined in raylib.h:

```c
void BeginTextureMode(RenderTexture2D target) 
```

Python wrapper:

```python
def begin_texture_mode(target: RenderTexture2D) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="EndTextureMode"><code>end_texture_mode</code> function</h2>

> Ends drawing to render texture

Defined in raylib.h:

```c
void EndTextureMode() 
```

Python wrapper:

```python
def end_texture_mode() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="BeginShaderMode"><code>begin_shader_mode</code> function</h2>

> Begin custom shader drawing

Defined in raylib.h:

```c
void BeginShaderMode(Shader shader) 
```

Python wrapper:

```python
def begin_shader_mode(shader: Shader) -> None
```

See also: <a href="#Shader">Shader</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="EndShaderMode"><code>end_shader_mode</code> function</h2>

> End custom shader drawing (use default shader)

Defined in raylib.h:

```c
void EndShaderMode() 
```

Python wrapper:

```python
def end_shader_mode() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="BeginBlendMode"><code>begin_blend_mode</code> function</h2>

> Begin blending mode (alpha, additive, multiplied, subtract, custom)

Defined in raylib.h:

```c
void BeginBlendMode(int mode) 
```

Python wrapper:

```python
def begin_blend_mode(mode: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="EndBlendMode"><code>end_blend_mode</code> function</h2>

> End blending mode (reset to default: alpha blending)

Defined in raylib.h:

```c
void EndBlendMode() 
```

Python wrapper:

```python
def end_blend_mode() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="BeginScissorMode"><code>begin_scissor_mode</code> function</h2>

> Begin scissor mode (define screen area for following drawing)

Defined in raylib.h:

```c
void BeginScissorMode(int x, int y, int width, int height) 
```

Python wrapper:

```python
def begin_scissor_mode(x: int, y: int, width: int, height: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="EndScissorMode"><code>end_scissor_mode</code> function</h2>

> End scissor mode

Defined in raylib.h:

```c
void EndScissorMode() 
```

Python wrapper:

```python
def end_scissor_mode() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="BeginVrStereoMode"><code>begin_vr_stereo_mode</code> function</h2>

> Begin stereo rendering (requires VR simulator)

Defined in raylib.h:

```c
void BeginVrStereoMode(VrStereoConfig config) 
```

Python wrapper:

```python
def begin_vr_stereo_mode(config: VrStereoConfig) -> None
```

See also: <a href="#VrStereoConfig">VrStereoConfig</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="EndVrStereoMode"><code>end_vr_stereo_mode</code> function</h2>

> End stereo rendering (requires VR simulator)

Defined in raylib.h:

```c
void EndVrStereoMode() 
```

Python wrapper:

```python
def end_vr_stereo_mode() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadVrStereoConfig"><code>load_vr_stereo_config</code> function</h2>

> Load VR stereo config for VR simulator device parameters

Defined in raylib.h:

```c
VrStereoConfig LoadVrStereoConfig(VrDeviceInfo device) 
```

Python wrapper:

```python
def load_vr_stereo_config(device: VrDeviceInfo) -> VrStereoConfig
```

See also: <a href="#VrDeviceInfo">VrDeviceInfo</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadVrStereoConfig"><code>unload_vr_stereo_config</code> function</h2>

> Unload VR stereo config

Defined in raylib.h:

```c
void UnloadVrStereoConfig(VrStereoConfig config) 
```

Python wrapper:

```python
def unload_vr_stereo_config(config: VrStereoConfig) -> None
```

See also: <a href="#VrStereoConfig">VrStereoConfig</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadShader"><code>load_shader</code> function</h2>

> Load shader from files and bind default locations

Defined in raylib.h:

```c
Shader LoadShader(char * vs_file_name, char * fs_file_name) 
```

Python wrapper:

```python
def load_shader(vs_file_name: Union[str, CharPtr], fs_file_name: Union[str, CharPtr]) -> Shader
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadShaderFromMemory"><code>load_shader_from_memory</code> function</h2>

> Load shader from code strings and bind default locations

Defined in raylib.h:

```c
Shader LoadShaderFromMemory(char * vs_code, char * fs_code) 
```

Python wrapper:

```python
def load_shader_from_memory(vs_code: Union[str, CharPtr], fs_code: Union[str, CharPtr]) -> Shader
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetShaderLocation"><code>get_shader_location</code> function</h2>

> Get shader uniform location

Defined in raylib.h:

```c
int GetShaderLocation(Shader shader, char * uniform_name) 
```

Python wrapper:

```python
def get_shader_location(shader: Shader, uniform_name: Union[str, CharPtr]) -> int
```

See also: <a href="#Shader">Shader</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetShaderLocationAttrib"><code>get_shader_location_attrib</code> function</h2>

> Get shader attribute location

Defined in raylib.h:

```c
int GetShaderLocationAttrib(Shader shader, char * attrib_name) 
```

Python wrapper:

```python
def get_shader_location_attrib(shader: Shader, attrib_name: Union[str, CharPtr]) -> int
```

See also: <a href="#Shader">Shader</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetShaderValue"><code>set_shader_value</code> function</h2>

> Set shader uniform value

Defined in raylib.h:

```c
void SetShaderValue(Shader shader, int loc_index, void value, int uniform_type) 
```

Python wrapper:

```python
def set_shader_value(shader: Shader, loc_index: int, value: bytes, uniform_type: int) -> None
```

See also: <a href="#Shader">Shader</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetShaderValueV"><code>set_shader_value_v</code> function</h2>

> Set shader uniform value vector

Defined in raylib.h:

```c
void SetShaderValueV(Shader shader, int loc_index, void value, int uniform_type, int count) 
```

Python wrapper:

```python
def set_shader_value_v(shader: Shader, loc_index: int, value: bytes, uniform_type: int, count: int) -> None
```

See also: <a href="#Shader">Shader</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetShaderValueMatrix"><code>set_shader_value_matrix</code> function</h2>

> Set shader uniform value (matrix 4x4)

Defined in raylib.h:

```c
void SetShaderValueMatrix(Shader shader, int loc_index, Matrix mat) 
```

Python wrapper:

```python
def set_shader_value_matrix(shader: Shader, loc_index: int, mat: Matrix) -> None
```

See also: <a href="#Shader">Shader</a>, <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetShaderValueTexture"><code>set_shader_value_texture</code> function</h2>

> Set shader uniform value for texture (sampler2d)

Defined in raylib.h:

```c
void SetShaderValueTexture(Shader shader, int loc_index, Texture2D texture) 
```

Python wrapper:

```python
def set_shader_value_texture(shader: Shader, loc_index: int, texture: Texture2D) -> None
```

See also: <a href="#Shader">Shader</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadShader"><code>unload_shader</code> function</h2>

> Unload shader from GPU memory (VRAM)

Defined in raylib.h:

```c
void UnloadShader(Shader shader) 
```

Python wrapper:

```python
def unload_shader(shader: Shader) -> None
```

See also: <a href="#Shader">Shader</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMouseRay"><code>get_mouse_ray</code> function</h2>

> Get a ray trace from mouse position

Defined in raylib.h:

```c
Ray GetMouseRay(Vector2 mouse_position, Camera camera) 
```

Python wrapper:

```python
def get_mouse_ray(mouse_position: Vector2, camera: Camera) -> Ray
```

See also: <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetCameraMatrix"><code>get_camera_matrix</code> function</h2>

> Get camera transform matrix (view matrix)

Defined in raylib.h:

```c
Matrix GetCameraMatrix(Camera camera) 
```

Python wrapper:

```python
def get_camera_matrix(camera: Camera) -> Matrix
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetCameraMatrix2D"><code>get_camera_matrix2d</code> function</h2>

> Get camera 2d transform matrix

Defined in raylib.h:

```c
Matrix GetCameraMatrix2D(Camera2D camera) 
```

Python wrapper:

```python
def get_camera_matrix2d(camera: Camera2D) -> Matrix
```

See also: <a href="#Camera2D">Camera2D</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetWorldToScreen"><code>get_world_to_screen</code> function</h2>

> Get the screen space position for a 3d world space position

Defined in raylib.h:

```c
Vector2 GetWorldToScreen(Vector3 position, Camera camera) 
```

Python wrapper:

```python
def get_world_to_screen(position: Vector3, camera: Camera) -> Vector2
```

See also: <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetScreenToWorld2D"><code>get_screen_to_world2d</code> function</h2>

> Get the world space position for a 2d camera screen space position

Defined in raylib.h:

```c
Vector2 GetScreenToWorld2D(Vector2 position, Camera2D camera) 
```

Python wrapper:

```python
def get_screen_to_world2d(position: Vector2, camera: Camera2D) -> Vector2
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Camera2D">Camera2D</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetWorldToScreenEx"><code>get_world_to_screen_ex</code> function</h2>

> Get size position for a 3d world space position

Defined in raylib.h:

```c
Vector2 GetWorldToScreenEx(Vector3 position, Camera camera, int width, int height) 
```

Python wrapper:

```python
def get_world_to_screen_ex(position: Vector3, camera: Camera, width: int, height: int) -> Vector2
```

See also: <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetWorldToScreen2D"><code>get_world_to_screen2d</code> function</h2>

> Get the screen space position for a 2d camera world space position

Defined in raylib.h:

```c
Vector2 GetWorldToScreen2D(Vector2 position, Camera2D camera) 
```

Python wrapper:

```python
def get_world_to_screen2d(position: Vector2, camera: Camera2D) -> Vector2
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Camera2D">Camera2D</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetTargetFPS"><code>set_target_fps</code> function</h2>

> Set target FPS (maximum)

Defined in raylib.h:

```c
void SetTargetFPS(int fps) 
```

Python wrapper:

```python
def set_target_fps(fps: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetFPS"><code>get_fps</code> function</h2>

> Get current FPS

Defined in raylib.h:

```c
int GetFPS() 
```

Python wrapper:

```python
def get_fps() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetFrameTime"><code>get_frame_time</code> function</h2>

> Get time in seconds for last frame drawn (delta time)

Defined in raylib.h:

```c
float GetFrameTime() 
```

Python wrapper:

```python
def get_frame_time() -> float
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetTime"><code>get_time</code> function</h2>

> Get elapsed time in seconds since InitWindow()

Defined in raylib.h:

```c
double GetTime() 
```

Python wrapper:

```python
def get_time() -> float
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetRandomValue"><code>get_random_value</code> function</h2>

> Get a random value between min and max (both included)

Defined in raylib.h:

```c
int GetRandomValue(int min, int max) 
```

Python wrapper:

```python
def get_random_value(min: int, max: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetRandomSeed"><code>set_random_seed</code> function</h2>

> Set the seed for the random number generator

Defined in raylib.h:

```c
void SetRandomSeed(unsigned int seed) 
```

Python wrapper:

```python
def set_random_seed(seed: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TakeScreenshot"><code>take_screenshot</code> function</h2>

> Takes a screenshot of current screen (filename extension defines format)

Defined in raylib.h:

```c
void TakeScreenshot(char * file_name) 
```

Python wrapper:

```python
def take_screenshot(file_name: Union[str, CharPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetConfigFlags"><code>set_config_flags</code> function</h2>

> Setup init configuration flags (view FLAGS)

Defined in raylib.h:

```c
void SetConfigFlags(unsigned int flags) 
```

Python wrapper:

```python
def set_config_flags(flags: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TraceLog"><code>trace_log</code> function</h2>

> Show trace log messages (LOG_DEBUG, LOG_INFO, LOG_WARNING, LOG_ERROR...)

Defined in raylib.h:

```c
void TraceLog(int log_level, char * text, va_list args) 
```

Python wrapper:

```python
def trace_log(log_level: int, text: Union[str, CharPtr], args: bytes) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetTraceLogLevel"><code>set_trace_log_level</code> function</h2>

> Set the current threshold (minimum) log level

Defined in raylib.h:

```c
void SetTraceLogLevel(int log_level) 
```

Python wrapper:

```python
def set_trace_log_level(log_level: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MemAlloc"><code>mem_alloc</code> function</h2>

> Internal memory allocator

Defined in raylib.h:

```c
void MemAlloc(int size) 
```

Python wrapper:

```python
def mem_alloc(size: int) -> bytes
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MemRealloc"><code>mem_realloc</code> function</h2>

> Internal memory reallocator

Defined in raylib.h:

```c
void MemRealloc(void ptr, int size) 
```

Python wrapper:

```python
def mem_realloc(ptr: bytes, size: int) -> bytes
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MemFree"><code>mem_free</code> function</h2>

> Internal memory free

Defined in raylib.h:

```c
void MemFree(void ptr) 
```

Python wrapper:

```python
def mem_free(ptr: bytes) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="OpenURL"><code>open_url</code> function</h2>

> Open URL with default system browser (if available)

Defined in raylib.h:

```c
void OpenURL(char * url) 
```

Python wrapper:

```python
def open_url(url: Union[str, CharPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetTraceLogCallback"><code>set_trace_log_callback</code> function</h2>

> Set custom trace log

Defined in raylib.h:

```c
void SetTraceLogCallback(TraceLogCallback callback) 
```

Python wrapper:

```python
def set_trace_log_callback(callback: TraceLogCallback) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetLoadFileDataCallback"><code>set_load_file_data_callback</code> function</h2>

> Set custom file binary data loader

Defined in raylib.h:

```c
void SetLoadFileDataCallback(LoadFileDataCallback callback) 
```

Python wrapper:

```python
def set_load_file_data_callback(callback: LoadFileDataCallback) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetSaveFileDataCallback"><code>set_save_file_data_callback</code> function</h2>

> Set custom file binary data saver

Defined in raylib.h:

```c
void SetSaveFileDataCallback(SaveFileDataCallback callback) 
```

Python wrapper:

```python
def set_save_file_data_callback(callback: SaveFileDataCallback) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetLoadFileTextCallback"><code>set_load_file_text_callback</code> function</h2>

> Set custom file text data loader

Defined in raylib.h:

```c
void SetLoadFileTextCallback(LoadFileTextCallback callback) 
```

Python wrapper:

```python
def set_load_file_text_callback(callback: LoadFileTextCallback) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetSaveFileTextCallback"><code>set_save_file_text_callback</code> function</h2>

> Set custom file text data saver

Defined in raylib.h:

```c
void SetSaveFileTextCallback(SaveFileTextCallback callback) 
```

Python wrapper:

```python
def set_save_file_text_callback(callback: SaveFileTextCallback) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadFileData"><code>load_file_data</code> function</h2>

> Load file data as byte array (read)

Defined in raylib.h:

```c
unsigned char * LoadFileData(char * file_name, unsigned int bytes_read) 
```

Python wrapper:

```python
def load_file_data(file_name: Union[str, CharPtr], bytes_read: Union[Seq[int], UIntPtr]) -> Union[Seq[int], UCharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadFileData"><code>unload_file_data</code> function</h2>

> Unload file data allocated by LoadFileData()

Defined in raylib.h:

```c
void UnloadFileData(unsigned char * data) 
```

Python wrapper:

```python
def unload_file_data(data: Union[Seq[int], UCharPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SaveFileData"><code>save_file_data</code> function</h2>

> Save data to file from byte array (write), returns true on success

Defined in raylib.h:

```c
bool SaveFileData(char * file_name, void data, unsigned int bytes_to_write) 
```

Python wrapper:

```python
def save_file_data(file_name: Union[str, CharPtr], data: bytes, bytes_to_write: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ExportDataAsCode"><code>export_data_as_code</code> function</h2>

> Export data to code (.h), returns true on success

Defined in raylib.h:

```c
bool ExportDataAsCode(char * data, unsigned int size, char * file_name) 
```

Python wrapper:

```python
def export_data_as_code(data: Union[str, CharPtr], size: int, file_name: Union[str, CharPtr]) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadFileText"><code>load_file_text</code> function</h2>

> Load text data from file (read), returns a '\0' terminated string

Defined in raylib.h:

```c
char * LoadFileText(char * file_name) 
```

Python wrapper:

```python
def load_file_text(file_name: Union[str, CharPtr]) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadFileText"><code>unload_file_text</code> function</h2>

> Unload file text data allocated by LoadFileText()

Defined in raylib.h:

```c
void UnloadFileText(char * text) 
```

Python wrapper:

```python
def unload_file_text(text: Union[str, CharPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SaveFileText"><code>save_file_text</code> function</h2>

> Save text data to file (write), string must be '\0' terminated, returns true on success

Defined in raylib.h:

```c
bool SaveFileText(char * file_name, char * text) 
```

Python wrapper:

```python
def save_file_text(file_name: Union[str, CharPtr], text: Union[str, CharPtr]) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="FileExists"><code>file_exists</code> function</h2>

> Check if file exists

Defined in raylib.h:

```c
bool FileExists(char * file_name) 
```

Python wrapper:

```python
def file_exists(file_name: Union[str, CharPtr]) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DirectoryExists"><code>directory_exists</code> function</h2>

> Check if a directory path exists

Defined in raylib.h:

```c
bool DirectoryExists(char * dir_path) 
```

Python wrapper:

```python
def directory_exists(dir_path: Union[str, CharPtr]) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsFileExtension"><code>is_file_extension</code> function</h2>

> Check file extension (including point: .png, .wav)

Defined in raylib.h:

```c
bool IsFileExtension(char * file_name, char * ext) 
```

Python wrapper:

```python
def is_file_extension(file_name: Union[str, CharPtr], ext: Union[str, CharPtr]) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetFileLength"><code>get_file_length</code> function</h2>

> Get file length in bytes (NOTE: GetFileSize() conflicts with windows.h)

Defined in raylib.h:

```c
int GetFileLength(char * file_name) 
```

Python wrapper:

```python
def get_file_length(file_name: Union[str, CharPtr]) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetFileExtension"><code>get_file_extension</code> function</h2>

> Get pointer to extension for a filename string (includes dot: '.png')

Defined in raylib.h:

```c
char * GetFileExtension(char * file_name) 
```

Python wrapper:

```python
def get_file_extension(file_name: Union[str, CharPtr]) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetFileName"><code>get_file_name</code> function</h2>

> Get pointer to filename for a path string

Defined in raylib.h:

```c
char * GetFileName(char * file_path) 
```

Python wrapper:

```python
def get_file_name(file_path: Union[str, CharPtr]) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetFileNameWithoutExt"><code>get_file_name_without_ext</code> function</h2>

> Get filename string without extension (uses static string)

Defined in raylib.h:

```c
char * GetFileNameWithoutExt(char * file_path) 
```

Python wrapper:

```python
def get_file_name_without_ext(file_path: Union[str, CharPtr]) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetDirectoryPath"><code>get_directory_path</code> function</h2>

> Get full path for a given fileName with path (uses static string)

Defined in raylib.h:

```c
char * GetDirectoryPath(char * file_path) 
```

Python wrapper:

```python
def get_directory_path(file_path: Union[str, CharPtr]) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetPrevDirectoryPath"><code>get_prev_directory_path</code> function</h2>

> Get previous directory path for a given path (uses static string)

Defined in raylib.h:

```c
char * GetPrevDirectoryPath(char * dir_path) 
```

Python wrapper:

```python
def get_prev_directory_path(dir_path: Union[str, CharPtr]) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetWorkingDirectory"><code>get_working_directory</code> function</h2>

> Get current working directory (uses static string)

Defined in raylib.h:

```c
char * GetWorkingDirectory() 
```

Python wrapper:

```python
def get_working_directory() -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetApplicationDirectory"><code>get_application_directory</code> function</h2>

> Get the directory if the running application (uses static string)

Defined in raylib.h:

```c
char * GetApplicationDirectory() 
```

Python wrapper:

```python
def get_application_directory() -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ChangeDirectory"><code>change_directory</code> function</h2>

> Change working directory, return true on success

Defined in raylib.h:

```c
bool ChangeDirectory(char * dir) 
```

Python wrapper:

```python
def change_directory(dir: Union[str, CharPtr]) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsPathFile"><code>is_path_file</code> function</h2>

> Check if a given path is a file or a directory

Defined in raylib.h:

```c
bool IsPathFile(char * path) 
```

Python wrapper:

```python
def is_path_file(path: Union[str, CharPtr]) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadDirectoryFiles"><code>load_directory_files</code> function</h2>

> Load directory filepaths

Defined in raylib.h:

```c
FilePathList LoadDirectoryFiles(char * dir_path) 
```

Python wrapper:

```python
def load_directory_files(dir_path: Union[str, CharPtr]) -> FilePathList
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadDirectoryFilesEx"><code>load_directory_files_ex</code> function</h2>

> Load directory filepaths with extension filtering and recursive directory scan

Defined in raylib.h:

```c
FilePathList LoadDirectoryFilesEx(char * base_path, char * filter, bool scan_subdirs) 
```

Python wrapper:

```python
def load_directory_files_ex(base_path: Union[str, CharPtr], filter: Union[str, CharPtr], scan_subdirs: bool) -> FilePathList
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadDirectoryFiles"><code>unload_directory_files</code> function</h2>

> Unload filepaths

Defined in raylib.h:

```c
void UnloadDirectoryFiles(FilePathList files) 
```

Python wrapper:

```python
def unload_directory_files(files: FilePathList) -> None
```

See also: <a href="#FilePathList">FilePathList</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsFileDropped"><code>is_file_dropped</code> function</h2>

> Check if a file has been dropped into window

Defined in raylib.h:

```c
bool IsFileDropped() 
```

Python wrapper:

```python
def is_file_dropped() -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadDroppedFiles"><code>load_dropped_files</code> function</h2>

> Load dropped filepaths

Defined in raylib.h:

```c
FilePathList LoadDroppedFiles() 
```

Python wrapper:

```python
def load_dropped_files() -> FilePathList
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadDroppedFiles"><code>unload_dropped_files</code> function</h2>

> Unload dropped filepaths

Defined in raylib.h:

```c
void UnloadDroppedFiles(FilePathList files) 
```

Python wrapper:

```python
def unload_dropped_files(files: FilePathList) -> None
```

See also: <a href="#FilePathList">FilePathList</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetFileModTime"><code>get_file_mod_time</code> function</h2>

> Get file modification time (last write time)

Defined in raylib.h:

```c
long GetFileModTime(char * file_name) 
```

Python wrapper:

```python
def get_file_mod_time(file_name: Union[str, CharPtr]) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CompressData"><code>compress_data</code> function</h2>

> Compress data (DEFLATE algorithm), memory must be MemFree()

Defined in raylib.h:

```c
unsigned char * CompressData(unsigned char * data, int data_size, int comp_data_size) 
```

Python wrapper:

```python
def compress_data(data: Union[Seq[int], UCharPtr], data_size: int, comp_data_size: Union[Seq[int], IntPtr]) -> Union[Seq[int], UCharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DecompressData"><code>decompress_data</code> function</h2>

> Decompress data (DEFLATE algorithm), memory must be MemFree()

Defined in raylib.h:

```c
unsigned char * DecompressData(unsigned char * comp_data, int comp_data_size, int data_size) 
```

Python wrapper:

```python
def decompress_data(comp_data: Union[Seq[int], UCharPtr], comp_data_size: int, data_size: Union[Seq[int], IntPtr]) -> Union[Seq[int], UCharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="EncodeDataBase64"><code>encode_data_base64</code> function</h2>

> Encode data to Base64 string, memory must be MemFree()

Defined in raylib.h:

```c
char * EncodeDataBase64(unsigned char * data, int data_size, int output_size) 
```

Python wrapper:

```python
def encode_data_base64(data: Union[Seq[int], UCharPtr], data_size: int, output_size: Union[Seq[int], IntPtr]) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DecodeDataBase64"><code>decode_data_base64</code> function</h2>

> Decode Base64 string data, memory must be MemFree()

Defined in raylib.h:

```c
unsigned char * DecodeDataBase64(unsigned char * data, int output_size) 
```

Python wrapper:

```python
def decode_data_base64(data: Union[Seq[int], UCharPtr], output_size: Union[Seq[int], IntPtr]) -> Union[Seq[int], UCharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsKeyPressed"><code>is_key_pressed</code> function</h2>

> Check if a key has been pressed once

Defined in raylib.h:

```c
bool IsKeyPressed(int key) 
```

Python wrapper:

```python
def is_key_pressed(key: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsKeyDown"><code>is_key_down</code> function</h2>

> Check if a key is being pressed

Defined in raylib.h:

```c
bool IsKeyDown(int key) 
```

Python wrapper:

```python
def is_key_down(key: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsKeyReleased"><code>is_key_released</code> function</h2>

> Check if a key has been released once

Defined in raylib.h:

```c
bool IsKeyReleased(int key) 
```

Python wrapper:

```python
def is_key_released(key: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsKeyUp"><code>is_key_up</code> function</h2>

> Check if a key is NOT being pressed

Defined in raylib.h:

```c
bool IsKeyUp(int key) 
```

Python wrapper:

```python
def is_key_up(key: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetExitKey"><code>set_exit_key</code> function</h2>

> Set a custom key to exit program (default is ESC)

Defined in raylib.h:

```c
void SetExitKey(int key) 
```

Python wrapper:

```python
def set_exit_key(key: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetKeyPressed"><code>get_key_pressed</code> function</h2>

> Get key pressed (keycode), call it multiple times for keys queued, returns 0 when the queue is empty

Defined in raylib.h:

```c
int GetKeyPressed() 
```

Python wrapper:

```python
def get_key_pressed() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetCharPressed"><code>get_char_pressed</code> function</h2>

> Get char pressed (unicode), call it multiple times for chars queued, returns 0 when the queue is empty

Defined in raylib.h:

```c
int GetCharPressed() 
```

Python wrapper:

```python
def get_char_pressed() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsGamepadAvailable"><code>is_gamepad_available</code> function</h2>

> Check if a gamepad is available

Defined in raylib.h:

```c
bool IsGamepadAvailable(int gamepad) 
```

Python wrapper:

```python
def is_gamepad_available(gamepad: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetGamepadName"><code>get_gamepad_name</code> function</h2>

> Get gamepad internal name id

Defined in raylib.h:

```c
char * GetGamepadName(int gamepad) 
```

Python wrapper:

```python
def get_gamepad_name(gamepad: int) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsGamepadButtonPressed"><code>is_gamepad_button_pressed</code> function</h2>

> Check if a gamepad button has been pressed once

Defined in raylib.h:

```c
bool IsGamepadButtonPressed(int gamepad, int button) 
```

Python wrapper:

```python
def is_gamepad_button_pressed(gamepad: int, button: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsGamepadButtonDown"><code>is_gamepad_button_down</code> function</h2>

> Check if a gamepad button is being pressed

Defined in raylib.h:

```c
bool IsGamepadButtonDown(int gamepad, int button) 
```

Python wrapper:

```python
def is_gamepad_button_down(gamepad: int, button: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsGamepadButtonReleased"><code>is_gamepad_button_released</code> function</h2>

> Check if a gamepad button has been released once

Defined in raylib.h:

```c
bool IsGamepadButtonReleased(int gamepad, int button) 
```

Python wrapper:

```python
def is_gamepad_button_released(gamepad: int, button: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsGamepadButtonUp"><code>is_gamepad_button_up</code> function</h2>

> Check if a gamepad button is NOT being pressed

Defined in raylib.h:

```c
bool IsGamepadButtonUp(int gamepad, int button) 
```

Python wrapper:

```python
def is_gamepad_button_up(gamepad: int, button: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetGamepadButtonPressed"><code>get_gamepad_button_pressed</code> function</h2>

> Get the last gamepad button pressed

Defined in raylib.h:

```c
int GetGamepadButtonPressed() 
```

Python wrapper:

```python
def get_gamepad_button_pressed() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetGamepadAxisCount"><code>get_gamepad_axis_count</code> function</h2>

> Get gamepad axis count for a gamepad

Defined in raylib.h:

```c
int GetGamepadAxisCount(int gamepad) 
```

Python wrapper:

```python
def get_gamepad_axis_count(gamepad: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetGamepadAxisMovement"><code>get_gamepad_axis_movement</code> function</h2>

> Get axis movement value for a gamepad axis

Defined in raylib.h:

```c
float GetGamepadAxisMovement(int gamepad, int axis) 
```

Python wrapper:

```python
def get_gamepad_axis_movement(gamepad: int, axis: int) -> float
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetGamepadMappings"><code>set_gamepad_mappings</code> function</h2>

> Set internal gamepad mappings (SDL_GameControllerDB)

Defined in raylib.h:

```c
int SetGamepadMappings(char * mappings) 
```

Python wrapper:

```python
def set_gamepad_mappings(mappings: Union[str, CharPtr]) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsMouseButtonPressed"><code>is_mouse_button_pressed</code> function</h2>

> Check if a mouse button has been pressed once

Defined in raylib.h:

```c
bool IsMouseButtonPressed(int button) 
```

Python wrapper:

```python
def is_mouse_button_pressed(button: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsMouseButtonDown"><code>is_mouse_button_down</code> function</h2>

> Check if a mouse button is being pressed

Defined in raylib.h:

```c
bool IsMouseButtonDown(int button) 
```

Python wrapper:

```python
def is_mouse_button_down(button: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsMouseButtonReleased"><code>is_mouse_button_released</code> function</h2>

> Check if a mouse button has been released once

Defined in raylib.h:

```c
bool IsMouseButtonReleased(int button) 
```

Python wrapper:

```python
def is_mouse_button_released(button: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsMouseButtonUp"><code>is_mouse_button_up</code> function</h2>

> Check if a mouse button is NOT being pressed

Defined in raylib.h:

```c
bool IsMouseButtonUp(int button) 
```

Python wrapper:

```python
def is_mouse_button_up(button: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMouseX"><code>get_mouse_x</code> function</h2>

> Get mouse position X

Defined in raylib.h:

```c
int GetMouseX() 
```

Python wrapper:

```python
def get_mouse_x() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMouseY"><code>get_mouse_y</code> function</h2>

> Get mouse position Y

Defined in raylib.h:

```c
int GetMouseY() 
```

Python wrapper:

```python
def get_mouse_y() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMousePosition"><code>get_mouse_position</code> function</h2>

> Get mouse position XY

Defined in raylib.h:

```c
Vector2 GetMousePosition() 
```

Python wrapper:

```python
def get_mouse_position() -> Vector2
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMouseDelta"><code>get_mouse_delta</code> function</h2>

> Get mouse delta between frames

Defined in raylib.h:

```c
Vector2 GetMouseDelta() 
```

Python wrapper:

```python
def get_mouse_delta() -> Vector2
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetMousePosition"><code>set_mouse_position</code> function</h2>

> Set mouse position XY

Defined in raylib.h:

```c
void SetMousePosition(int x, int y) 
```

Python wrapper:

```python
def set_mouse_position(x: int, y: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetMouseOffset"><code>set_mouse_offset</code> function</h2>

> Set mouse offset

Defined in raylib.h:

```c
void SetMouseOffset(int offset_x, int offset_y) 
```

Python wrapper:

```python
def set_mouse_offset(offset_x: int, offset_y: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetMouseScale"><code>set_mouse_scale</code> function</h2>

> Set mouse scaling

Defined in raylib.h:

```c
void SetMouseScale(float scale_x, float scale_y) 
```

Python wrapper:

```python
def set_mouse_scale(scale_x: float, scale_y: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMouseWheelMove"><code>get_mouse_wheel_move</code> function</h2>

> Get mouse wheel movement for X or Y, whichever is larger

Defined in raylib.h:

```c
float GetMouseWheelMove() 
```

Python wrapper:

```python
def get_mouse_wheel_move() -> float
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMouseWheelMoveV"><code>get_mouse_wheel_move_v</code> function</h2>

> Get mouse wheel movement for both X and Y

Defined in raylib.h:

```c
Vector2 GetMouseWheelMoveV() 
```

Python wrapper:

```python
def get_mouse_wheel_move_v() -> Vector2
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetMouseCursor"><code>set_mouse_cursor</code> function</h2>

> Set mouse cursor

Defined in raylib.h:

```c
void SetMouseCursor(int cursor) 
```

Python wrapper:

```python
def set_mouse_cursor(cursor: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetTouchX"><code>get_touch_x</code> function</h2>

> Get touch position X for touch point 0 (relative to screen size)

Defined in raylib.h:

```c
int GetTouchX() 
```

Python wrapper:

```python
def get_touch_x() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetTouchY"><code>get_touch_y</code> function</h2>

> Get touch position Y for touch point 0 (relative to screen size)

Defined in raylib.h:

```c
int GetTouchY() 
```

Python wrapper:

```python
def get_touch_y() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetTouchPosition"><code>get_touch_position</code> function</h2>

> Get touch position XY for a touch point index (relative to screen size)

Defined in raylib.h:

```c
Vector2 GetTouchPosition(int index) 
```

Python wrapper:

```python
def get_touch_position(index: int) -> Vector2
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetTouchPointId"><code>get_touch_point_id</code> function</h2>

> Get touch point identifier for given index

Defined in raylib.h:

```c
int GetTouchPointId(int index) 
```

Python wrapper:

```python
def get_touch_point_id(index: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetTouchPointCount"><code>get_touch_point_count</code> function</h2>

> Get number of touch points

Defined in raylib.h:

```c
int GetTouchPointCount() 
```

Python wrapper:

```python
def get_touch_point_count() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetGesturesEnabled"><code>set_gestures_enabled</code> function</h2>

> Enable a set of gestures using flags

Defined in raylib.h:

```c
void SetGesturesEnabled(unsigned int flags) 
```

Python wrapper:

```python
def set_gestures_enabled(flags: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsGestureDetected"><code>is_gesture_detected</code> function</h2>

> Check if a gesture have been detected

Defined in raylib.h:

```c
bool IsGestureDetected(int gesture) 
```

Python wrapper:

```python
def is_gesture_detected(gesture: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetGestureDetected"><code>get_gesture_detected</code> function</h2>

> Get latest detected gesture

Defined in raylib.h:

```c
int GetGestureDetected() 
```

Python wrapper:

```python
def get_gesture_detected() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetGestureHoldDuration"><code>get_gesture_hold_duration</code> function</h2>

> Get gesture hold time in milliseconds

Defined in raylib.h:

```c
float GetGestureHoldDuration() 
```

Python wrapper:

```python
def get_gesture_hold_duration() -> float
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetGestureDragVector"><code>get_gesture_drag_vector</code> function</h2>

> Get gesture drag vector

Defined in raylib.h:

```c
Vector2 GetGestureDragVector() 
```

Python wrapper:

```python
def get_gesture_drag_vector() -> Vector2
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetGestureDragAngle"><code>get_gesture_drag_angle</code> function</h2>

> Get gesture drag angle

Defined in raylib.h:

```c
float GetGestureDragAngle() 
```

Python wrapper:

```python
def get_gesture_drag_angle() -> float
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetGesturePinchVector"><code>get_gesture_pinch_vector</code> function</h2>

> Get gesture pinch delta

Defined in raylib.h:

```c
Vector2 GetGesturePinchVector() 
```

Python wrapper:

```python
def get_gesture_pinch_vector() -> Vector2
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetGesturePinchAngle"><code>get_gesture_pinch_angle</code> function</h2>

> Get gesture pinch angle

Defined in raylib.h:

```c
float GetGesturePinchAngle() 
```

Python wrapper:

```python
def get_gesture_pinch_angle() -> float
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetCameraMode"><code>set_camera_mode</code> function</h2>

> Set camera mode (multiple camera modes available)

Defined in raylib.h:

```c
void SetCameraMode(Camera camera, int mode) 
```

Python wrapper:

```python
def set_camera_mode(camera: Camera, mode: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UpdateCamera"><code>update_camera</code> function</h2>

> Update camera position for selected mode

Defined in raylib.h:

```c
void UpdateCamera(Camera * camera) 
```

Python wrapper:

```python
def update_camera(camera: CameraPtr) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetCameraPanControl"><code>set_camera_pan_control</code> function</h2>

> Set camera pan key to combine with mouse movement (free camera)

Defined in raylib.h:

```c
void SetCameraPanControl(int key_pan) 
```

Python wrapper:

```python
def set_camera_pan_control(key_pan: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetCameraAltControl"><code>set_camera_alt_control</code> function</h2>

> Set camera alt key to combine with mouse movement (free camera)

Defined in raylib.h:

```c
void SetCameraAltControl(int key_alt) 
```

Python wrapper:

```python
def set_camera_alt_control(key_alt: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetCameraSmoothZoomControl"><code>set_camera_smooth_zoom_control</code> function</h2>

> Set camera smooth zoom key to combine with mouse (free camera)

Defined in raylib.h:

```c
void SetCameraSmoothZoomControl(int key_smooth_zoom) 
```

Python wrapper:

```python
def set_camera_smooth_zoom_control(key_smooth_zoom: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetCameraMoveControls"><code>set_camera_move_controls</code> function</h2>

> Set camera move controls (1st person and 3rd person cameras)

Defined in raylib.h:

```c
void SetCameraMoveControls(int key_front, int key_back, int key_right, int key_left, int key_up, int key_down) 
```

Python wrapper:

```python
def set_camera_move_controls(key_front: int, key_back: int, key_right: int, key_left: int, key_up: int, key_down: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetShapesTexture"><code>set_shapes_texture</code> function</h2>

> Set texture and rectangle to be used on shapes drawing

Defined in raylib.h:

```c
void SetShapesTexture(Texture2D texture, Rectangle source) 
```

Python wrapper:

```python
def set_shapes_texture(texture: Texture2D, source: Rectangle) -> None
```

See also: <a href="#Rectangle">Rectangle</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawPixel"><code>draw_pixel</code> function</h2>

> Draw a pixel

Defined in raylib.h:

```c
void DrawPixel(int pos_x, int pos_y, Color color) 
```

Python wrapper:

```python
def draw_pixel(pos_x: int, pos_y: int, color: Color) -> None
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawPixelV"><code>draw_pixel_v</code> function</h2>

> Draw a pixel (Vector version)

Defined in raylib.h:

```c
void DrawPixelV(Vector2 position, Color color) 
```

Python wrapper:

```python
def draw_pixel_v(position: Vector2, color: Color) -> None
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawLine"><code>draw_line</code> function</h2>

> Draw a line

Defined in raylib.h:

```c
void DrawLine(int start_pos_x, int start_pos_y, int end_pos_x, int end_pos_y, Color color) 
```

Python wrapper:

```python
def draw_line(start_pos_x: int, start_pos_y: int, end_pos_x: int, end_pos_y: int, color: Color) -> None
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawLineV"><code>draw_line_v</code> function</h2>

> Draw a line (Vector version)

Defined in raylib.h:

```c
void DrawLineV(Vector2 start_pos, Vector2 end_pos, Color color) 
```

Python wrapper:

```python
def draw_line_v(start_pos: Vector2, end_pos: Vector2, color: Color) -> None
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawLineEx"><code>draw_line_ex</code> function</h2>

> Draw a line defining thickness

Defined in raylib.h:

```c
void DrawLineEx(Vector2 start_pos, Vector2 end_pos, float thick, Color color) 
```

Python wrapper:

```python
def draw_line_ex(start_pos: Vector2, end_pos: Vector2, thick: float, color: Color) -> None
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawLineBezier"><code>draw_line_bezier</code> function</h2>

> Draw a line using cubic-bezier curves in-out

Defined in raylib.h:

```c
void DrawLineBezier(Vector2 start_pos, Vector2 end_pos, float thick, Color color) 
```

Python wrapper:

```python
def draw_line_bezier(start_pos: Vector2, end_pos: Vector2, thick: float, color: Color) -> None
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawLineBezierQuad"><code>draw_line_bezier_quad</code> function</h2>

> Draw line using quadratic bezier curves with a control point

Defined in raylib.h:

```c
void DrawLineBezierQuad(Vector2 start_pos, Vector2 end_pos, Vector2 control_pos, float thick, Color color) 
```

Python wrapper:

```python
def draw_line_bezier_quad(start_pos: Vector2, end_pos: Vector2, control_pos: Vector2, thick: float, color: Color) -> None
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawLineBezierCubic"><code>draw_line_bezier_cubic</code> function</h2>

> Draw line using cubic bezier curves with 2 control points

Defined in raylib.h:

```c
void DrawLineBezierCubic(Vector2 start_pos, Vector2 end_pos, Vector2 start_control_pos, Vector2 end_control_pos, float thick, Color color) 
```

Python wrapper:

```python
def draw_line_bezier_cubic(start_pos: Vector2, end_pos: Vector2, start_control_pos: Vector2, end_control_pos: Vector2, thick: float, color: Color) -> None
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawLineStrip"><code>draw_line_strip</code> function</h2>

> Draw lines sequence

Defined in raylib.h:

```c
void DrawLineStrip(Vector2 * points, int point_count, Color color) 
```

Python wrapper:

```python
def draw_line_strip(points: Vector2Ptr, point_count: int, color: Color) -> None
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCircle"><code>draw_circle</code> function</h2>

> Draw a color-filled circle

Defined in raylib.h:

```c
void DrawCircle(int center_x, int center_y, float radius, Color color) 
```

Python wrapper:

```python
def draw_circle(center_x: int, center_y: int, radius: float, color: Color) -> None
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCircleSector"><code>draw_circle_sector</code> function</h2>

> Draw a piece of a circle

Defined in raylib.h:

```c
void DrawCircleSector(Vector2 center, float radius, float start_angle, float end_angle, int segments, Color color) 
```

Python wrapper:

```python
def draw_circle_sector(center: Vector2, radius: float, start_angle: float, end_angle: float, segments: int, color: Color) -> None
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCircleSectorLines"><code>draw_circle_sector_lines</code> function</h2>

> Draw circle sector outline

Defined in raylib.h:

```c
void DrawCircleSectorLines(Vector2 center, float radius, float start_angle, float end_angle, int segments, Color color) 
```

Python wrapper:

```python
def draw_circle_sector_lines(center: Vector2, radius: float, start_angle: float, end_angle: float, segments: int, color: Color) -> None
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCircleGradient"><code>draw_circle_gradient</code> function</h2>

> Draw a gradient-filled circle

Defined in raylib.h:

```c
void DrawCircleGradient(int center_x, int center_y, float radius, Color color1, Color color2) 
```

Python wrapper:

```python
def draw_circle_gradient(center_x: int, center_y: int, radius: float, color1: Color, color2: Color) -> None
```

See also: <a href="#Color">Color</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCircleV"><code>draw_circle_v</code> function</h2>

> Draw a color-filled circle (Vector version)

Defined in raylib.h:

```c
void DrawCircleV(Vector2 center, float radius, Color color) 
```

Python wrapper:

```python
def draw_circle_v(center: Vector2, radius: float, color: Color) -> None
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCircleLines"><code>draw_circle_lines</code> function</h2>

> Draw circle outline

Defined in raylib.h:

```c
void DrawCircleLines(int center_x, int center_y, float radius, Color color) 
```

Python wrapper:

```python
def draw_circle_lines(center_x: int, center_y: int, radius: float, color: Color) -> None
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawEllipse"><code>draw_ellipse</code> function</h2>

> Draw ellipse

Defined in raylib.h:

```c
void DrawEllipse(int center_x, int center_y, float radius_h, float radius_v, Color color) 
```

Python wrapper:

```python
def draw_ellipse(center_x: int, center_y: int, radius_h: float, radius_v: float, color: Color) -> None
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawEllipseLines"><code>draw_ellipse_lines</code> function</h2>

> Draw ellipse outline

Defined in raylib.h:

```c
void DrawEllipseLines(int center_x, int center_y, float radius_h, float radius_v, Color color) 
```

Python wrapper:

```python
def draw_ellipse_lines(center_x: int, center_y: int, radius_h: float, radius_v: float, color: Color) -> None
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRing"><code>draw_ring</code> function</h2>

> Draw ring

Defined in raylib.h:

```c
void DrawRing(Vector2 center, float inner_radius, float outer_radius, float start_angle, float end_angle, int segments, Color color) 
```

Python wrapper:

```python
def draw_ring(center: Vector2, inner_radius: float, outer_radius: float, start_angle: float, end_angle: float, segments: int, color: Color) -> None
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRingLines"><code>draw_ring_lines</code> function</h2>

> Draw ring outline

Defined in raylib.h:

```c
void DrawRingLines(Vector2 center, float inner_radius, float outer_radius, float start_angle, float end_angle, int segments, Color color) 
```

Python wrapper:

```python
def draw_ring_lines(center: Vector2, inner_radius: float, outer_radius: float, start_angle: float, end_angle: float, segments: int, color: Color) -> None
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRectangle"><code>draw_rectangle</code> function</h2>

> Draw a color-filled rectangle

Defined in raylib.h:

```c
void DrawRectangle(int pos_x, int pos_y, int width, int height, Color color) 
```

Python wrapper:

```python
def draw_rectangle(pos_x: int, pos_y: int, width: int, height: int, color: Color) -> None
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRectangleV"><code>draw_rectangle_v</code> function</h2>

> Draw a color-filled rectangle (Vector version)

Defined in raylib.h:

```c
void DrawRectangleV(Vector2 position, Vector2 size, Color color) 
```

Python wrapper:

```python
def draw_rectangle_v(position: Vector2, size: Vector2, color: Color) -> None
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRectangleRec"><code>draw_rectangle_rec</code> function</h2>

> Draw a color-filled rectangle

Defined in raylib.h:

```c
void DrawRectangleRec(Rectangle rec, Color color) 
```

Python wrapper:

```python
def draw_rectangle_rec(rec: Rectangle, color: Color) -> None
```

See also: <a href="#Rectangle">Rectangle</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRectanglePro"><code>draw_rectangle_pro</code> function</h2>

> Draw a color-filled rectangle with pro parameters

Defined in raylib.h:

```c
void DrawRectanglePro(Rectangle rec, Vector2 origin, float rotation, Color color) 
```

Python wrapper:

```python
def draw_rectangle_pro(rec: Rectangle, origin: Vector2, rotation: float, color: Color) -> None
```

See also: <a href="#Rectangle">Rectangle</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRectangleGradientV"><code>draw_rectangle_gradient_v</code> function</h2>

> Draw a vertical-gradient-filled rectangle

Defined in raylib.h:

```c
void DrawRectangleGradientV(int pos_x, int pos_y, int width, int height, Color color1, Color color2) 
```

Python wrapper:

```python
def draw_rectangle_gradient_v(pos_x: int, pos_y: int, width: int, height: int, color1: Color, color2: Color) -> None
```

See also: <a href="#Color">Color</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRectangleGradientH"><code>draw_rectangle_gradient_h</code> function</h2>

> Draw a horizontal-gradient-filled rectangle

Defined in raylib.h:

```c
void DrawRectangleGradientH(int pos_x, int pos_y, int width, int height, Color color1, Color color2) 
```

Python wrapper:

```python
def draw_rectangle_gradient_h(pos_x: int, pos_y: int, width: int, height: int, color1: Color, color2: Color) -> None
```

See also: <a href="#Color">Color</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRectangleGradientEx"><code>draw_rectangle_gradient_ex</code> function</h2>

> Draw a gradient-filled rectangle with custom vertex colors

Defined in raylib.h:

```c
void DrawRectangleGradientEx(Rectangle rec, Color col1, Color col2, Color col3, Color col4) 
```

Python wrapper:

```python
def draw_rectangle_gradient_ex(rec: Rectangle, col1: Color, col2: Color, col3: Color, col4: Color) -> None
```

See also: <a href="#Rectangle">Rectangle</a>, <a href="#Color">Color</a>, <a href="#Color">Color</a>, <a href="#Color">Color</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRectangleLines"><code>draw_rectangle_lines</code> function</h2>

> Draw rectangle outline

Defined in raylib.h:

```c
void DrawRectangleLines(int pos_x, int pos_y, int width, int height, Color color) 
```

Python wrapper:

```python
def draw_rectangle_lines(pos_x: int, pos_y: int, width: int, height: int, color: Color) -> None
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRectangleLinesEx"><code>draw_rectangle_lines_ex</code> function</h2>

> Draw rectangle outline with extended parameters

Defined in raylib.h:

```c
void DrawRectangleLinesEx(Rectangle rec, float line_thick, Color color) 
```

Python wrapper:

```python
def draw_rectangle_lines_ex(rec: Rectangle, line_thick: float, color: Color) -> None
```

See also: <a href="#Rectangle">Rectangle</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRectangleRounded"><code>draw_rectangle_rounded</code> function</h2>

> Draw rectangle with rounded edges

Defined in raylib.h:

```c
void DrawRectangleRounded(Rectangle rec, float roundness, int segments, Color color) 
```

Python wrapper:

```python
def draw_rectangle_rounded(rec: Rectangle, roundness: float, segments: int, color: Color) -> None
```

See also: <a href="#Rectangle">Rectangle</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRectangleRoundedLines"><code>draw_rectangle_rounded_lines</code> function</h2>

> Draw rectangle with rounded edges outline

Defined in raylib.h:

```c
void DrawRectangleRoundedLines(Rectangle rec, float roundness, int segments, float line_thick, Color color) 
```

Python wrapper:

```python
def draw_rectangle_rounded_lines(rec: Rectangle, roundness: float, segments: int, line_thick: float, color: Color) -> None
```

See also: <a href="#Rectangle">Rectangle</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTriangle"><code>draw_triangle</code> function</h2>

> Draw a color-filled triangle (vertex in counter-clockwise order!)

Defined in raylib.h:

```c
void DrawTriangle(Vector2 v1, Vector2 v2, Vector2 v3, Color color) 
```

Python wrapper:

```python
def draw_triangle(v1: Vector2, v2: Vector2, v3: Vector2, color: Color) -> None
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTriangleLines"><code>draw_triangle_lines</code> function</h2>

> Draw triangle outline (vertex in counter-clockwise order!)

Defined in raylib.h:

```c
void DrawTriangleLines(Vector2 v1, Vector2 v2, Vector2 v3, Color color) 
```

Python wrapper:

```python
def draw_triangle_lines(v1: Vector2, v2: Vector2, v3: Vector2, color: Color) -> None
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTriangleFan"><code>draw_triangle_fan</code> function</h2>

> Draw a triangle fan defined by points (first vertex is the center)

Defined in raylib.h:

```c
void DrawTriangleFan(Vector2 * points, int point_count, Color color) 
```

Python wrapper:

```python
def draw_triangle_fan(points: Vector2Ptr, point_count: int, color: Color) -> None
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTriangleStrip"><code>draw_triangle_strip</code> function</h2>

> Draw a triangle strip defined by points

Defined in raylib.h:

```c
void DrawTriangleStrip(Vector2 * points, int point_count, Color color) 
```

Python wrapper:

```python
def draw_triangle_strip(points: Vector2Ptr, point_count: int, color: Color) -> None
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawPoly"><code>draw_poly</code> function</h2>

> Draw a regular polygon (Vector version)

Defined in raylib.h:

```c
void DrawPoly(Vector2 center, int sides, float radius, float rotation, Color color) 
```

Python wrapper:

```python
def draw_poly(center: Vector2, sides: int, radius: float, rotation: float, color: Color) -> None
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawPolyLines"><code>draw_poly_lines</code> function</h2>

> Draw a polygon outline of n sides

Defined in raylib.h:

```c
void DrawPolyLines(Vector2 center, int sides, float radius, float rotation, Color color) 
```

Python wrapper:

```python
def draw_poly_lines(center: Vector2, sides: int, radius: float, rotation: float, color: Color) -> None
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawPolyLinesEx"><code>draw_poly_lines_ex</code> function</h2>

> Draw a polygon outline of n sides with extended parameters

Defined in raylib.h:

```c
void DrawPolyLinesEx(Vector2 center, int sides, float radius, float rotation, float line_thick, Color color) 
```

Python wrapper:

```python
def draw_poly_lines_ex(center: Vector2, sides: int, radius: float, rotation: float, line_thick: float, color: Color) -> None
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CheckCollisionRecs"><code>check_collision_recs</code> function</h2>

> Check collision between two rectangles

Defined in raylib.h:

```c
bool CheckCollisionRecs(Rectangle rec1, Rectangle rec2) 
```

Python wrapper:

```python
def check_collision_recs(rec1: Rectangle, rec2: Rectangle) -> bool
```

See also: <a href="#Rectangle">Rectangle</a>, <a href="#Rectangle">Rectangle</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CheckCollisionCircles"><code>check_collision_circles</code> function</h2>

> Check collision between two circles

Defined in raylib.h:

```c
bool CheckCollisionCircles(Vector2 center1, float radius1, Vector2 center2, float radius2) 
```

Python wrapper:

```python
def check_collision_circles(center1: Vector2, radius1: float, center2: Vector2, radius2: float) -> bool
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CheckCollisionCircleRec"><code>check_collision_circle_rec</code> function</h2>

> Check collision between circle and rectangle

Defined in raylib.h:

```c
bool CheckCollisionCircleRec(Vector2 center, float radius, Rectangle rec) 
```

Python wrapper:

```python
def check_collision_circle_rec(center: Vector2, radius: float, rec: Rectangle) -> bool
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Rectangle">Rectangle</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CheckCollisionPointRec"><code>check_collision_point_rec</code> function</h2>

> Check if point is inside rectangle

Defined in raylib.h:

```c
bool CheckCollisionPointRec(Vector2 point, Rectangle rec) 
```

Python wrapper:

```python
def check_collision_point_rec(point: Vector2, rec: Rectangle) -> bool
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Rectangle">Rectangle</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CheckCollisionPointCircle"><code>check_collision_point_circle</code> function</h2>

> Check if point is inside circle

Defined in raylib.h:

```c
bool CheckCollisionPointCircle(Vector2 point, Vector2 center, float radius) 
```

Python wrapper:

```python
def check_collision_point_circle(point: Vector2, center: Vector2, radius: float) -> bool
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CheckCollisionPointTriangle"><code>check_collision_point_triangle</code> function</h2>

> Check if point is inside a triangle

Defined in raylib.h:

```c
bool CheckCollisionPointTriangle(Vector2 point, Vector2 p1, Vector2 p2, Vector2 p3) 
```

Python wrapper:

```python
def check_collision_point_triangle(point: Vector2, p1: Vector2, p2: Vector2, p3: Vector2) -> bool
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CheckCollisionLines"><code>check_collision_lines</code> function</h2>

> Check the collision between two lines defined by two points each, returns collision point by reference

Defined in raylib.h:

```c
bool CheckCollisionLines(Vector2 start_pos1, Vector2 end_pos1, Vector2 start_pos2, Vector2 end_pos2, Vector2 * collision_point) 
```

Python wrapper:

```python
def check_collision_lines(start_pos1: Vector2, end_pos1: Vector2, start_pos2: Vector2, end_pos2: Vector2, collision_point: Vector2Ptr) -> bool
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CheckCollisionPointLine"><code>check_collision_point_line</code> function</h2>

> Check if point belongs to line created between two points [p1] and [p2] with defined margin in pixels [threshold]

Defined in raylib.h:

```c
bool CheckCollisionPointLine(Vector2 point, Vector2 p1, Vector2 p2, int threshold) 
```

Python wrapper:

```python
def check_collision_point_line(point: Vector2, p1: Vector2, p2: Vector2, threshold: int) -> bool
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetCollisionRec"><code>get_collision_rec</code> function</h2>

> Get collision rectangle for two rectangles collision

Defined in raylib.h:

```c
Rectangle GetCollisionRec(Rectangle rec1, Rectangle rec2) 
```

Python wrapper:

```python
def get_collision_rec(rec1: Rectangle, rec2: Rectangle) -> Rectangle
```

See also: <a href="#Rectangle">Rectangle</a>, <a href="#Rectangle">Rectangle</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadImage"><code>load_image</code> function</h2>

> Load image from file into CPU memory (RAM)

Defined in raylib.h:

```c
Image LoadImage(char * file_name) 
```

Python wrapper:

```python
def load_image(file_name: Union[str, CharPtr]) -> Image
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadImageRaw"><code>load_image_raw</code> function</h2>

> Load image from RAW file data

Defined in raylib.h:

```c
Image LoadImageRaw(char * file_name, int width, int height, int format, int header_size) 
```

Python wrapper:

```python
def load_image_raw(file_name: Union[str, CharPtr], width: int, height: int, format: int, header_size: int) -> Image
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadImageAnim"><code>load_image_anim</code> function</h2>

> Load image sequence from file (frames appended to image.data)

Defined in raylib.h:

```c
Image LoadImageAnim(char * file_name, int frames) 
```

Python wrapper:

```python
def load_image_anim(file_name: Union[str, CharPtr], frames: Union[Seq[int], IntPtr]) -> Image
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadImageFromMemory"><code>load_image_from_memory</code> function</h2>

> Load image from memory buffer, fileType refers to extension: i.e. '.png'

Defined in raylib.h:

```c
Image LoadImageFromMemory(char * file_type, unsigned char * file_data, int data_size) 
```

Python wrapper:

```python
def load_image_from_memory(file_type: Union[str, CharPtr], file_data: Union[Seq[int], UCharPtr], data_size: int) -> Image
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadImageFromTexture"><code>load_image_from_texture</code> function</h2>

> Load image from GPU texture data

Defined in raylib.h:

```c
Image LoadImageFromTexture(Texture2D texture) 
```

Python wrapper:

```python
def load_image_from_texture(texture: Texture2D) -> Image
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadImageFromScreen"><code>load_image_from_screen</code> function</h2>

> Load image from screen buffer and (screenshot)

Defined in raylib.h:

```c
Image LoadImageFromScreen() 
```

Python wrapper:

```python
def load_image_from_screen() -> Image
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadImage"><code>unload_image</code> function</h2>

> Unload image from CPU memory (RAM)

Defined in raylib.h:

```c
void UnloadImage(Image image) 
```

Python wrapper:

```python
def unload_image(image: Image) -> None
```

See also: <a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ExportImage"><code>export_image</code> function</h2>

> Export image data to file, returns true on success

Defined in raylib.h:

```c
bool ExportImage(Image image, char * file_name) 
```

Python wrapper:

```python
def export_image(image: Image, file_name: Union[str, CharPtr]) -> bool
```

See also: <a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ExportImageAsCode"><code>export_image_as_code</code> function</h2>

> Export image as code file defining an array of bytes, returns true on success

Defined in raylib.h:

```c
bool ExportImageAsCode(Image image, char * file_name) 
```

Python wrapper:

```python
def export_image_as_code(image: Image, file_name: Union[str, CharPtr]) -> bool
```

See also: <a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenImageColor"><code>gen_image_color</code> function</h2>

> Generate image: plain color

Defined in raylib.h:

```c
Image GenImageColor(int width, int height, Color color) 
```

Python wrapper:

```python
def gen_image_color(width: int, height: int, color: Color) -> Image
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenImageGradientV"><code>gen_image_gradient_v</code> function</h2>

> Generate image: vertical gradient

Defined in raylib.h:

```c
Image GenImageGradientV(int width, int height, Color top, Color bottom) 
```

Python wrapper:

```python
def gen_image_gradient_v(width: int, height: int, top: Color, bottom: Color) -> Image
```

See also: <a href="#Color">Color</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenImageGradientH"><code>gen_image_gradient_h</code> function</h2>

> Generate image: horizontal gradient

Defined in raylib.h:

```c
Image GenImageGradientH(int width, int height, Color left, Color right) 
```

Python wrapper:

```python
def gen_image_gradient_h(width: int, height: int, left: Color, right: Color) -> Image
```

See also: <a href="#Color">Color</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenImageGradientRadial"><code>gen_image_gradient_radial</code> function</h2>

> Generate image: radial gradient

Defined in raylib.h:

```c
Image GenImageGradientRadial(int width, int height, float density, Color inner, Color outer) 
```

Python wrapper:

```python
def gen_image_gradient_radial(width: int, height: int, density: float, inner: Color, outer: Color) -> Image
```

See also: <a href="#Color">Color</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenImageChecked"><code>gen_image_checked</code> function</h2>

> Generate image: checked

Defined in raylib.h:

```c
Image GenImageChecked(int width, int height, int checks_x, int checks_y, Color col1, Color col2) 
```

Python wrapper:

```python
def gen_image_checked(width: int, height: int, checks_x: int, checks_y: int, col1: Color, col2: Color) -> Image
```

See also: <a href="#Color">Color</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenImageWhiteNoise"><code>gen_image_white_noise</code> function</h2>

> Generate image: white noise

Defined in raylib.h:

```c
Image GenImageWhiteNoise(int width, int height, float factor) 
```

Python wrapper:

```python
def gen_image_white_noise(width: int, height: int, factor: float) -> Image
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenImageCellular"><code>gen_image_cellular</code> function</h2>

> Generate image: cellular algorithm, bigger tileSize means bigger cells

Defined in raylib.h:

```c
Image GenImageCellular(int width, int height, int tile_size) 
```

Python wrapper:

```python
def gen_image_cellular(width: int, height: int, tile_size: int) -> Image
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageCopy"><code>image_copy</code> function</h2>

> Create an image duplicate (useful for transformations)

Defined in raylib.h:

```c
Image ImageCopy(Image image) 
```

Python wrapper:

```python
def image_copy(image: Image) -> Image
```

See also: <a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageFromImage"><code>image_from_image</code> function</h2>

> Create an image from another image piece

Defined in raylib.h:

```c
Image ImageFromImage(Image image, Rectangle rec) 
```

Python wrapper:

```python
def image_from_image(image: Image, rec: Rectangle) -> Image
```

See also: <a href="#Image">Image</a>, <a href="#Rectangle">Rectangle</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageText"><code>image_text</code> function</h2>

> Create an image from text (default font)

Defined in raylib.h:

```c
Image ImageText(char * text, int font_size, Color color) 
```

Python wrapper:

```python
def image_text(text: Union[str, CharPtr], font_size: int, color: Color) -> Image
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageTextEx"><code>image_text_ex</code> function</h2>

> Create an image from text (custom sprite font)

Defined in raylib.h:

```c
Image ImageTextEx(Font font, char * text, float font_size, float spacing, Color tint) 
```

Python wrapper:

```python
def image_text_ex(font: Font, text: Union[str, CharPtr], font_size: float, spacing: float, tint: Color) -> Image
```

See also: <a href="#Font">Font</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageFormat"><code>image_format</code> function</h2>

> Convert image data to desired format

Defined in raylib.h:

```c
void ImageFormat(Image * image, int new_format) 
```

Python wrapper:

```python
def image_format(image: ImagePtr, new_format: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageToPOT"><code>image_to_pot</code> function</h2>

> Convert image to POT (power-of-two)

Defined in raylib.h:

```c
void ImageToPOT(Image * image, Color fill) 
```

Python wrapper:

```python
def image_to_pot(image: ImagePtr, fill: Color) -> None
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageCrop"><code>image_crop</code> function</h2>

> Crop an image to a defined rectangle

Defined in raylib.h:

```c
void ImageCrop(Image * image, Rectangle crop) 
```

Python wrapper:

```python
def image_crop(image: ImagePtr, crop: Rectangle) -> None
```

See also: <a href="#Rectangle">Rectangle</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageAlphaCrop"><code>image_alpha_crop</code> function</h2>

> Crop image depending on alpha value

Defined in raylib.h:

```c
void ImageAlphaCrop(Image * image, float threshold) 
```

Python wrapper:

```python
def image_alpha_crop(image: ImagePtr, threshold: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageAlphaClear"><code>image_alpha_clear</code> function</h2>

> Clear alpha channel to desired color

Defined in raylib.h:

```c
void ImageAlphaClear(Image * image, Color color, float threshold) 
```

Python wrapper:

```python
def image_alpha_clear(image: ImagePtr, color: Color, threshold: float) -> None
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageAlphaMask"><code>image_alpha_mask</code> function</h2>

> Apply alpha mask to image

Defined in raylib.h:

```c
void ImageAlphaMask(Image * image, Image alpha_mask) 
```

Python wrapper:

```python
def image_alpha_mask(image: ImagePtr, alpha_mask: Image) -> None
```

See also: <a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageAlphaPremultiply"><code>image_alpha_premultiply</code> function</h2>

> Premultiply alpha channel

Defined in raylib.h:

```c
void ImageAlphaPremultiply(Image * image) 
```

Python wrapper:

```python
def image_alpha_premultiply(image: ImagePtr) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageResize"><code>image_resize</code> function</h2>

> Resize image (Bicubic scaling algorithm)

Defined in raylib.h:

```c
void ImageResize(Image * image, int new_width, int new_height) 
```

Python wrapper:

```python
def image_resize(image: ImagePtr, new_width: int, new_height: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageResizeNN"><code>image_resize_nn</code> function</h2>

> Resize image (Nearest-Neighbor scaling algorithm)

Defined in raylib.h:

```c
void ImageResizeNN(Image * image, int new_width, int new_height) 
```

Python wrapper:

```python
def image_resize_nn(image: ImagePtr, new_width: int, new_height: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageResizeCanvas"><code>image_resize_canvas</code> function</h2>

> Resize canvas and fill with color

Defined in raylib.h:

```c
void ImageResizeCanvas(Image * image, int new_width, int new_height, int offset_x, int offset_y, Color fill) 
```

Python wrapper:

```python
def image_resize_canvas(image: ImagePtr, new_width: int, new_height: int, offset_x: int, offset_y: int, fill: Color) -> None
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageMipmaps"><code>image_mipmaps</code> function</h2>

> Compute all mipmap levels for a provided image

Defined in raylib.h:

```c
void ImageMipmaps(Image * image) 
```

Python wrapper:

```python
def image_mipmaps(image: ImagePtr) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDither"><code>image_dither</code> function</h2>

> Dither image data to 16bpp or lower (Floyd-Steinberg dithering)

Defined in raylib.h:

```c
void ImageDither(Image * image, int r_bpp, int g_bpp, int b_bpp, int a_bpp) 
```

Python wrapper:

```python
def image_dither(image: ImagePtr, r_bpp: int, g_bpp: int, b_bpp: int, a_bpp: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageFlipVertical"><code>image_flip_vertical</code> function</h2>

> Flip image vertically

Defined in raylib.h:

```c
void ImageFlipVertical(Image * image) 
```

Python wrapper:

```python
def image_flip_vertical(image: ImagePtr) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageFlipHorizontal"><code>image_flip_horizontal</code> function</h2>

> Flip image horizontally

Defined in raylib.h:

```c
void ImageFlipHorizontal(Image * image) 
```

Python wrapper:

```python
def image_flip_horizontal(image: ImagePtr) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageRotateCW"><code>image_rotate_cw</code> function</h2>

> Rotate image clockwise 90deg

Defined in raylib.h:

```c
void ImageRotateCW(Image * image) 
```

Python wrapper:

```python
def image_rotate_cw(image: ImagePtr) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageRotateCCW"><code>image_rotate_ccw</code> function</h2>

> Rotate image counter-clockwise 90deg

Defined in raylib.h:

```c
void ImageRotateCCW(Image * image) 
```

Python wrapper:

```python
def image_rotate_ccw(image: ImagePtr) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageColorTint"><code>image_color_tint</code> function</h2>

> Modify image color: tint

Defined in raylib.h:

```c
void ImageColorTint(Image * image, Color color) 
```

Python wrapper:

```python
def image_color_tint(image: ImagePtr, color: Color) -> None
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageColorInvert"><code>image_color_invert</code> function</h2>

> Modify image color: invert

Defined in raylib.h:

```c
void ImageColorInvert(Image * image) 
```

Python wrapper:

```python
def image_color_invert(image: ImagePtr) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageColorGrayscale"><code>image_color_grayscale</code> function</h2>

> Modify image color: grayscale

Defined in raylib.h:

```c
void ImageColorGrayscale(Image * image) 
```

Python wrapper:

```python
def image_color_grayscale(image: ImagePtr) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageColorContrast"><code>image_color_contrast</code> function</h2>

> Modify image color: contrast (-100 to 100)

Defined in raylib.h:

```c
void ImageColorContrast(Image * image, float contrast) 
```

Python wrapper:

```python
def image_color_contrast(image: ImagePtr, contrast: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageColorBrightness"><code>image_color_brightness</code> function</h2>

> Modify image color: brightness (-255 to 255)

Defined in raylib.h:

```c
void ImageColorBrightness(Image * image, int brightness) 
```

Python wrapper:

```python
def image_color_brightness(image: ImagePtr, brightness: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageColorReplace"><code>image_color_replace</code> function</h2>

> Modify image color: replace color

Defined in raylib.h:

```c
void ImageColorReplace(Image * image, Color color, Color replace) 
```

Python wrapper:

```python
def image_color_replace(image: ImagePtr, color: Color, replace: Color) -> None
```

See also: <a href="#Color">Color</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadImageColors"><code>load_image_colors</code> function</h2>

> Load color data from image as a Color array (RGBA - 32bit)

Defined in raylib.h:

```c
Color * LoadImageColors(Image image) 
```

Python wrapper:

```python
def load_image_colors(image: Image) -> ColorPtr
```

See also: <a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadImagePalette"><code>load_image_palette</code> function</h2>

> Load colors palette from image as a Color array (RGBA - 32bit)

Defined in raylib.h:

```c
Color * LoadImagePalette(Image image, int max_palette_size, int color_count) 
```

Python wrapper:

```python
def load_image_palette(image: Image, max_palette_size: int, color_count: Union[Seq[int], IntPtr]) -> ColorPtr
```

See also: <a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadImageColors"><code>unload_image_colors</code> function</h2>

> Unload color data loaded with LoadImageColors()

Defined in raylib.h:

```c
void UnloadImageColors(Color * colors) 
```

Python wrapper:

```python
def unload_image_colors(colors: ColorPtr) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadImagePalette"><code>unload_image_palette</code> function</h2>

> Unload colors palette loaded with LoadImagePalette()

Defined in raylib.h:

```c
void UnloadImagePalette(Color * colors) 
```

Python wrapper:

```python
def unload_image_palette(colors: ColorPtr) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetImageAlphaBorder"><code>get_image_alpha_border</code> function</h2>

> Get image alpha border rectangle

Defined in raylib.h:

```c
Rectangle GetImageAlphaBorder(Image image, float threshold) 
```

Python wrapper:

```python
def get_image_alpha_border(image: Image, threshold: float) -> Rectangle
```

See also: <a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetImageColor"><code>get_image_color</code> function</h2>

> Get image pixel color at (x, y) position

Defined in raylib.h:

```c
Color GetImageColor(Image image, int x, int y) 
```

Python wrapper:

```python
def get_image_color(image: Image, x: int, y: int) -> Color
```

See also: <a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageClearBackground"><code>image_clear_background</code> function</h2>

> Clear image background with given color

Defined in raylib.h:

```c
void ImageClearBackground(Image * dst, Color color) 
```

Python wrapper:

```python
def image_clear_background(dst: ImagePtr, color: Color) -> None
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDrawPixel"><code>image_draw_pixel</code> function</h2>

> Draw pixel within an image

Defined in raylib.h:

```c
void ImageDrawPixel(Image * dst, int pos_x, int pos_y, Color color) 
```

Python wrapper:

```python
def image_draw_pixel(dst: ImagePtr, pos_x: int, pos_y: int, color: Color) -> None
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDrawPixelV"><code>image_draw_pixel_v</code> function</h2>

> Draw pixel within an image (Vector version)

Defined in raylib.h:

```c
void ImageDrawPixelV(Image * dst, Vector2 position, Color color) 
```

Python wrapper:

```python
def image_draw_pixel_v(dst: ImagePtr, position: Vector2, color: Color) -> None
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDrawLine"><code>image_draw_line</code> function</h2>

> Draw line within an image

Defined in raylib.h:

```c
void ImageDrawLine(Image * dst, int start_pos_x, int start_pos_y, int end_pos_x, int end_pos_y, Color color) 
```

Python wrapper:

```python
def image_draw_line(dst: ImagePtr, start_pos_x: int, start_pos_y: int, end_pos_x: int, end_pos_y: int, color: Color) -> None
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDrawLineV"><code>image_draw_line_v</code> function</h2>

> Draw line within an image (Vector version)

Defined in raylib.h:

```c
void ImageDrawLineV(Image * dst, Vector2 start, Vector2 end, Color color) 
```

Python wrapper:

```python
def image_draw_line_v(dst: ImagePtr, start: Vector2, end: Vector2, color: Color) -> None
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDrawCircle"><code>image_draw_circle</code> function</h2>

> Draw circle within an image

Defined in raylib.h:

```c
void ImageDrawCircle(Image * dst, int center_x, int center_y, int radius, Color color) 
```

Python wrapper:

```python
def image_draw_circle(dst: ImagePtr, center_x: int, center_y: int, radius: int, color: Color) -> None
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDrawCircleV"><code>image_draw_circle_v</code> function</h2>

> Draw circle within an image (Vector version)

Defined in raylib.h:

```c
void ImageDrawCircleV(Image * dst, Vector2 center, int radius, Color color) 
```

Python wrapper:

```python
def image_draw_circle_v(dst: ImagePtr, center: Vector2, radius: int, color: Color) -> None
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDrawRectangle"><code>image_draw_rectangle</code> function</h2>

> Draw rectangle within an image

Defined in raylib.h:

```c
void ImageDrawRectangle(Image * dst, int pos_x, int pos_y, int width, int height, Color color) 
```

Python wrapper:

```python
def image_draw_rectangle(dst: ImagePtr, pos_x: int, pos_y: int, width: int, height: int, color: Color) -> None
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDrawRectangleV"><code>image_draw_rectangle_v</code> function</h2>

> Draw rectangle within an image (Vector version)

Defined in raylib.h:

```c
void ImageDrawRectangleV(Image * dst, Vector2 position, Vector2 size, Color color) 
```

Python wrapper:

```python
def image_draw_rectangle_v(dst: ImagePtr, position: Vector2, size: Vector2, color: Color) -> None
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDrawRectangleRec"><code>image_draw_rectangle_rec</code> function</h2>

> Draw rectangle within an image

Defined in raylib.h:

```c
void ImageDrawRectangleRec(Image * dst, Rectangle rec, Color color) 
```

Python wrapper:

```python
def image_draw_rectangle_rec(dst: ImagePtr, rec: Rectangle, color: Color) -> None
```

See also: <a href="#Rectangle">Rectangle</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDrawRectangleLines"><code>image_draw_rectangle_lines</code> function</h2>

> Draw rectangle lines within an image

Defined in raylib.h:

```c
void ImageDrawRectangleLines(Image * dst, Rectangle rec, int thick, Color color) 
```

Python wrapper:

```python
def image_draw_rectangle_lines(dst: ImagePtr, rec: Rectangle, thick: int, color: Color) -> None
```

See also: <a href="#Rectangle">Rectangle</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDraw"><code>image_draw</code> function</h2>

> Draw a source image within a destination image (tint applied to source)

Defined in raylib.h:

```c
void ImageDraw(Image * dst, Image src, Rectangle src_rec, Rectangle dst_rec, Color tint) 
```

Python wrapper:

```python
def image_draw(dst: ImagePtr, src: Image, src_rec: Rectangle, dst_rec: Rectangle, tint: Color) -> None
```

See also: <a href="#Image">Image</a>, <a href="#Rectangle">Rectangle</a>, <a href="#Rectangle">Rectangle</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDrawText"><code>image_draw_text</code> function</h2>

> Draw text (using default font) within an image (destination)

Defined in raylib.h:

```c
void ImageDrawText(Image * dst, char * text, int pos_x, int pos_y, int font_size, Color color) 
```

Python wrapper:

```python
def image_draw_text(dst: ImagePtr, text: Union[str, CharPtr], pos_x: int, pos_y: int, font_size: int, color: Color) -> None
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDrawTextEx"><code>image_draw_text_ex</code> function</h2>

> Draw text (custom sprite font) within an image (destination)

Defined in raylib.h:

```c
void ImageDrawTextEx(Image * dst, Font font, char * text, Vector2 position, float font_size, float spacing, Color tint) 
```

Python wrapper:

```python
def image_draw_text_ex(dst: ImagePtr, font: Font, text: Union[str, CharPtr], position: Vector2, font_size: float, spacing: float, tint: Color) -> None
```

See also: <a href="#Font">Font</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadTexture"><code>load_texture</code> function</h2>

> Load texture from file into GPU memory (VRAM)

Defined in raylib.h:

```c
Texture2D LoadTexture(char * file_name) 
```

Python wrapper:

```python
def load_texture(file_name: Union[str, CharPtr]) -> Texture2D
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadTextureFromImage"><code>load_texture_from_image</code> function</h2>

> Load texture from image data

Defined in raylib.h:

```c
Texture2D LoadTextureFromImage(Image image) 
```

Python wrapper:

```python
def load_texture_from_image(image: Image) -> Texture2D
```

See also: <a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadTextureCubemap"><code>load_texture_cubemap</code> function</h2>

> Load cubemap from image, multiple image cubemap layouts supported

Defined in raylib.h:

```c
TextureCubemap LoadTextureCubemap(Image image, int layout) 
```

Python wrapper:

```python
def load_texture_cubemap(image: Image, layout: int) -> TextureCubemap
```

See also: <a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadRenderTexture"><code>load_render_texture</code> function</h2>

> Load texture for rendering (framebuffer)

Defined in raylib.h:

```c
RenderTexture2D LoadRenderTexture(int width, int height) 
```

Python wrapper:

```python
def load_render_texture(width: int, height: int) -> RenderTexture2D
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadTexture"><code>unload_texture</code> function</h2>

> Unload texture from GPU memory (VRAM)

Defined in raylib.h:

```c
void UnloadTexture(Texture2D texture) 
```

Python wrapper:

```python
def unload_texture(texture: Texture2D) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadRenderTexture"><code>unload_render_texture</code> function</h2>

> Unload render texture from GPU memory (VRAM)

Defined in raylib.h:

```c
void UnloadRenderTexture(RenderTexture2D target) 
```

Python wrapper:

```python
def unload_render_texture(target: RenderTexture2D) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UpdateTexture"><code>update_texture</code> function</h2>

> Update GPU texture with new data

Defined in raylib.h:

```c
void UpdateTexture(Texture2D texture, void pixels) 
```

Python wrapper:

```python
def update_texture(texture: Texture2D, pixels: bytes) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UpdateTextureRec"><code>update_texture_rec</code> function</h2>

> Update GPU texture rectangle with new data

Defined in raylib.h:

```c
void UpdateTextureRec(Texture2D texture, Rectangle rec, void pixels) 
```

Python wrapper:

```python
def update_texture_rec(texture: Texture2D, rec: Rectangle, pixels: bytes) -> None
```

See also: <a href="#Rectangle">Rectangle</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenTextureMipmaps"><code>gen_texture_mipmaps</code> function</h2>

> Generate GPU mipmaps for a texture

Defined in raylib.h:

```c
void GenTextureMipmaps(Texture2D * texture) 
```

Python wrapper:

```python
def gen_texture_mipmaps(texture: Texture2DPtr) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetTextureFilter"><code>set_texture_filter</code> function</h2>

> Set texture scaling filter mode

Defined in raylib.h:

```c
void SetTextureFilter(Texture2D texture, int filter) 
```

Python wrapper:

```python
def set_texture_filter(texture: Texture2D, filter: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetTextureWrap"><code>set_texture_wrap</code> function</h2>

> Set texture wrapping mode

Defined in raylib.h:

```c
void SetTextureWrap(Texture2D texture, int wrap) 
```

Python wrapper:

```python
def set_texture_wrap(texture: Texture2D, wrap: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTexture"><code>draw_texture</code> function</h2>

> Draw a Texture2D

Defined in raylib.h:

```c
void DrawTexture(Texture2D texture, int pos_x, int pos_y, Color tint) 
```

Python wrapper:

```python
def draw_texture(texture: Texture2D, pos_x: int, pos_y: int, tint: Color) -> None
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTextureV"><code>draw_texture_v</code> function</h2>

> Draw a Texture2D with position defined as Vector2

Defined in raylib.h:

```c
void DrawTextureV(Texture2D texture, Vector2 position, Color tint) 
```

Python wrapper:

```python
def draw_texture_v(texture: Texture2D, position: Vector2, tint: Color) -> None
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTextureEx"><code>draw_texture_ex</code> function</h2>

> Draw a Texture2D with extended parameters

Defined in raylib.h:

```c
void DrawTextureEx(Texture2D texture, Vector2 position, float rotation, float scale, Color tint) 
```

Python wrapper:

```python
def draw_texture_ex(texture: Texture2D, position: Vector2, rotation: float, scale: float, tint: Color) -> None
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTextureRec"><code>draw_texture_rec</code> function</h2>

> Draw a part of a texture defined by a rectangle

Defined in raylib.h:

```c
void DrawTextureRec(Texture2D texture, Rectangle source, Vector2 position, Color tint) 
```

Python wrapper:

```python
def draw_texture_rec(texture: Texture2D, source: Rectangle, position: Vector2, tint: Color) -> None
```

See also: <a href="#Rectangle">Rectangle</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTextureQuad"><code>draw_texture_quad</code> function</h2>

> Draw texture quad with tiling and offset parameters

Defined in raylib.h:

```c
void DrawTextureQuad(Texture2D texture, Vector2 tiling, Vector2 offset, Rectangle quad, Color tint) 
```

Python wrapper:

```python
def draw_texture_quad(texture: Texture2D, tiling: Vector2, offset: Vector2, quad: Rectangle, tint: Color) -> None
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>, <a href="#Rectangle">Rectangle</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTextureTiled"><code>draw_texture_tiled</code> function</h2>

> Draw part of a texture (defined by a rectangle) with rotation and scale tiled into dest.

Defined in raylib.h:

```c
void DrawTextureTiled(Texture2D texture, Rectangle source, Rectangle dest, Vector2 origin, float rotation, float scale, Color tint) 
```

Python wrapper:

```python
def draw_texture_tiled(texture: Texture2D, source: Rectangle, dest: Rectangle, origin: Vector2, rotation: float, scale: float, tint: Color) -> None
```

See also: <a href="#Rectangle">Rectangle</a>, <a href="#Rectangle">Rectangle</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTexturePro"><code>draw_texture_pro</code> function</h2>

> Draw a part of a texture defined by a rectangle with 'pro' parameters

Defined in raylib.h:

```c
void DrawTexturePro(Texture2D texture, Rectangle source, Rectangle dest, Vector2 origin, float rotation, Color tint) 
```

Python wrapper:

```python
def draw_texture_pro(texture: Texture2D, source: Rectangle, dest: Rectangle, origin: Vector2, rotation: float, tint: Color) -> None
```

See also: <a href="#Rectangle">Rectangle</a>, <a href="#Rectangle">Rectangle</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTextureNPatch"><code>draw_texture_npatch</code> function</h2>

> Draws a texture (or part of it) that stretches or shrinks nicely

Defined in raylib.h:

```c
void DrawTextureNPatch(Texture2D texture, NPatchInfo n_patch_info, Rectangle dest, Vector2 origin, float rotation, Color tint) 
```

Python wrapper:

```python
def draw_texture_npatch(texture: Texture2D, n_patch_info: NPatchInfo, dest: Rectangle, origin: Vector2, rotation: float, tint: Color) -> None
```

See also: <a href="#NPatchInfo">NPatchInfo</a>, <a href="#Rectangle">Rectangle</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTexturePoly"><code>draw_texture_poly</code> function</h2>

> Draw a textured polygon

Defined in raylib.h:

```c
void DrawTexturePoly(Texture2D texture, Vector2 center, Vector2 * points, Vector2 * texcoords, int point_count, Color tint) 
```

Python wrapper:

```python
def draw_texture_poly(texture: Texture2D, center: Vector2, points: Vector2Ptr, texcoords: Vector2Ptr, point_count: int, tint: Color) -> None
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Fade"><code>fade</code> function</h2>

> Get color with alpha applied, alpha goes from 0.0f to 1.0f

Defined in raylib.h:

```c
Color Fade(Color color, float alpha) 
```

Python wrapper:

```python
def fade(color: Color, alpha: float) -> Color
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ColorToInt"><code>color_to_int</code> function</h2>

> Get hexadecimal value for a Color

Defined in raylib.h:

```c
int ColorToInt(Color color) 
```

Python wrapper:

```python
def color_to_int(color: Color) -> int
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ColorNormalize"><code>color_normalize</code> function</h2>

> Get Color normalized as float [0..1]

Defined in raylib.h:

```c
Vector4 ColorNormalize(Color color) 
```

Python wrapper:

```python
def color_normalize(color: Color) -> Vector4
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ColorFromNormalized"><code>color_from_normalized</code> function</h2>

> Get Color from normalized values [0..1]

Defined in raylib.h:

```c
Color ColorFromNormalized(Vector4 normalized) 
```

Python wrapper:

```python
def color_from_normalized(normalized: Vector4) -> Color
```

See also: <a href="#Vector4">Vector4</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ColorToHSV"><code>color_to_hsv</code> function</h2>

> Get HSV values for a Color, hue [0..360], saturation/value [0..1]

Defined in raylib.h:

```c
Vector3 ColorToHSV(Color color) 
```

Python wrapper:

```python
def color_to_hsv(color: Color) -> Vector3
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ColorFromHSV"><code>color_from_hsv</code> function</h2>

> Get a Color from HSV values, hue [0..360], saturation/value [0..1]

Defined in raylib.h:

```c
Color ColorFromHSV(float hue, float saturation, float value) 
```

Python wrapper:

```python
def color_from_hsv(hue: float, saturation: float, value: float) -> Color
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ColorAlpha"><code>color_alpha</code> function</h2>

> Get color with alpha applied, alpha goes from 0.0f to 1.0f

Defined in raylib.h:

```c
Color ColorAlpha(Color color, float alpha) 
```

Python wrapper:

```python
def color_alpha(color: Color, alpha: float) -> Color
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ColorAlphaBlend"><code>color_alpha_blend</code> function</h2>

> Get src alpha-blended into dst color with tint

Defined in raylib.h:

```c
Color ColorAlphaBlend(Color dst, Color src, Color tint) 
```

Python wrapper:

```python
def color_alpha_blend(dst: Color, src: Color, tint: Color) -> Color
```

See also: <a href="#Color">Color</a>, <a href="#Color">Color</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetColor"><code>get_color</code> function</h2>

> Get Color structure from hexadecimal value

Defined in raylib.h:

```c
Color GetColor(unsigned int hex_value) 
```

Python wrapper:

```python
def get_color(hex_value: int) -> Color
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetPixelColor"><code>get_pixel_color</code> function</h2>

> Get Color from a source pixel pointer of certain format

Defined in raylib.h:

```c
Color GetPixelColor(void src_ptr, int format) 
```

Python wrapper:

```python
def get_pixel_color(src_ptr: bytes, format: int) -> Color
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetPixelColor"><code>set_pixel_color</code> function</h2>

> Set color formatted into destination pixel pointer

Defined in raylib.h:

```c
void SetPixelColor(void dst_ptr, Color color, int format) 
```

Python wrapper:

```python
def set_pixel_color(dst_ptr: bytes, color: Color, format: int) -> None
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetPixelDataSize"><code>get_pixel_data_size</code> function</h2>

> Get pixel data size in bytes for certain format

Defined in raylib.h:

```c
int GetPixelDataSize(int width, int height, int format) 
```

Python wrapper:

```python
def get_pixel_data_size(width: int, height: int, format: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetFontDefault"><code>get_font_default</code> function</h2>

> Get the default Font

Defined in raylib.h:

```c
Font GetFontDefault() 
```

Python wrapper:

```python
def get_font_default() -> Font
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadFont"><code>load_font</code> function</h2>

> Load font from file into GPU memory (VRAM)

Defined in raylib.h:

```c
Font LoadFont(char * file_name) 
```

Python wrapper:

```python
def load_font(file_name: Union[str, CharPtr]) -> Font
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadFontEx"><code>load_font_ex</code> function</h2>

> Load font from file with extended parameters, use NULL for fontChars and 0 for glyphCount to load the default character set

Defined in raylib.h:

```c
Font LoadFontEx(char * file_name, int font_size, int font_chars, int glyph_count) 
```

Python wrapper:

```python
def load_font_ex(file_name: Union[str, CharPtr], font_size: int, font_chars: Union[Seq[int], IntPtr], glyph_count: int) -> Font
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadFontFromImage"><code>load_font_from_image</code> function</h2>

> Load font from Image (XNA style)

Defined in raylib.h:

```c
Font LoadFontFromImage(Image image, Color key, int first_char) 
```

Python wrapper:

```python
def load_font_from_image(image: Image, key: Color, first_char: int) -> Font
```

See also: <a href="#Image">Image</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadFontFromMemory"><code>load_font_from_memory</code> function</h2>

> Load font from memory buffer, fileType refers to extension: i.e. '.ttf'

Defined in raylib.h:

```c
Font LoadFontFromMemory(char * file_type, unsigned char * file_data, int data_size, int font_size, int font_chars, int glyph_count) 
```

Python wrapper:

```python
def load_font_from_memory(file_type: Union[str, CharPtr], file_data: Union[Seq[int], UCharPtr], data_size: int, font_size: int, font_chars: Union[Seq[int], IntPtr], glyph_count: int) -> Font
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadFontData"><code>load_font_data</code> function</h2>

> Load font data for further use

Defined in raylib.h:

```c
GlyphInfo * LoadFontData(unsigned char * file_data, int data_size, int font_size, int font_chars, int glyph_count, int type) 
```

Python wrapper:

```python
def load_font_data(file_data: Union[Seq[int], UCharPtr], data_size: int, font_size: int, font_chars: Union[Seq[int], IntPtr], glyph_count: int, type: int) -> GlyphInfoPtr
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenImageFontAtlas"><code>gen_image_font_atlas</code> function</h2>

> Generate image font atlas using chars info

Defined in raylib.h:

```c
Image GenImageFontAtlas(GlyphInfo * chars, Rectangle ** recs, int glyph_count, int font_size, int padding, int pack_method) 
```

Python wrapper:

```python
def gen_image_font_atlas(chars: GlyphInfoPtr, recs: RectanglePtr, glyph_count: int, font_size: int, padding: int, pack_method: int) -> Image
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadFontData"><code>unload_font_data</code> function</h2>

> Unload font chars info data (RAM)

Defined in raylib.h:

```c
void UnloadFontData(GlyphInfo * chars, int glyph_count) 
```

Python wrapper:

```python
def unload_font_data(chars: GlyphInfoPtr, glyph_count: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadFont"><code>unload_font</code> function</h2>

> Unload font from GPU memory (VRAM)

Defined in raylib.h:

```c
void UnloadFont(Font font) 
```

Python wrapper:

```python
def unload_font(font: Font) -> None
```

See also: <a href="#Font">Font</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ExportFontAsCode"><code>export_font_as_code</code> function</h2>

> Export font as code file, returns true on success

Defined in raylib.h:

```c
bool ExportFontAsCode(Font font, char * file_name) 
```

Python wrapper:

```python
def export_font_as_code(font: Font, file_name: Union[str, CharPtr]) -> bool
```

See also: <a href="#Font">Font</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawFPS"><code>draw_fps</code> function</h2>

> Draw current FPS

Defined in raylib.h:

```c
void DrawFPS(int pos_x, int pos_y) 
```

Python wrapper:

```python
def draw_fps(pos_x: int, pos_y: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawText"><code>draw_text</code> function</h2>

> Draw text (using default font)

Defined in raylib.h:

```c
void DrawText(char * text, int pos_x, int pos_y, int font_size, Color color) 
```

Python wrapper:

```python
def draw_text(text: Union[str, CharPtr], pos_x: int, pos_y: int, font_size: int, color: Color) -> None
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTextEx"><code>draw_text_ex</code> function</h2>

> Draw text using font and additional parameters

Defined in raylib.h:

```c
void DrawTextEx(Font font, char * text, Vector2 position, float font_size, float spacing, Color tint) 
```

Python wrapper:

```python
def draw_text_ex(font: Font, text: Union[str, CharPtr], position: Vector2, font_size: float, spacing: float, tint: Color) -> None
```

See also: <a href="#Font">Font</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTextPro"><code>draw_text_pro</code> function</h2>

> Draw text using Font and pro parameters (rotation)

Defined in raylib.h:

```c
void DrawTextPro(Font font, char * text, Vector2 position, Vector2 origin, float rotation, float font_size, float spacing, Color tint) 
```

Python wrapper:

```python
def draw_text_pro(font: Font, text: Union[str, CharPtr], position: Vector2, origin: Vector2, rotation: float, font_size: float, spacing: float, tint: Color) -> None
```

See also: <a href="#Font">Font</a>, <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTextCodepoint"><code>draw_text_codepoint</code> function</h2>

> Draw one character (codepoint)

Defined in raylib.h:

```c
void DrawTextCodepoint(Font font, int codepoint, Vector2 position, float font_size, Color tint) 
```

Python wrapper:

```python
def draw_text_codepoint(font: Font, codepoint: int, position: Vector2, font_size: float, tint: Color) -> None
```

See also: <a href="#Font">Font</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTextCodepoints"><code>draw_text_codepoints</code> function</h2>

> Draw multiple character (codepoint)

Defined in raylib.h:

```c
void DrawTextCodepoints(Font font, int codepoints, int count, Vector2 position, float font_size, float spacing, Color tint) 
```

Python wrapper:

```python
def draw_text_codepoints(font: Font, codepoints: Union[Seq[int], IntPtr], count: int, position: Vector2, font_size: float, spacing: float, tint: Color) -> None
```

See also: <a href="#Font">Font</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MeasureText"><code>measure_text</code> function</h2>

> Measure string width for default font

Defined in raylib.h:

```c
int MeasureText(char * text, int font_size) 
```

Python wrapper:

```python
def measure_text(text: Union[str, CharPtr], font_size: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MeasureTextEx"><code>measure_text_ex</code> function</h2>

> Measure string size for Font

Defined in raylib.h:

```c
Vector2 MeasureTextEx(Font font, char * text, float font_size, float spacing) 
```

Python wrapper:

```python
def measure_text_ex(font: Font, text: Union[str, CharPtr], font_size: float, spacing: float) -> Vector2
```

See also: <a href="#Font">Font</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetGlyphIndex"><code>get_glyph_index</code> function</h2>

> Get glyph index position in font for a codepoint (unicode character), fallback to '?' if not found

Defined in raylib.h:

```c
int GetGlyphIndex(Font font, int codepoint) 
```

Python wrapper:

```python
def get_glyph_index(font: Font, codepoint: int) -> int
```

See also: <a href="#Font">Font</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetGlyphInfo"><code>get_glyph_info</code> function</h2>

> Get glyph font info data for a codepoint (unicode character), fallback to '?' if not found

Defined in raylib.h:

```c
GlyphInfo GetGlyphInfo(Font font, int codepoint) 
```

Python wrapper:

```python
def get_glyph_info(font: Font, codepoint: int) -> GlyphInfo
```

See also: <a href="#Font">Font</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetGlyphAtlasRec"><code>get_glyph_atlas_rec</code> function</h2>

> Get glyph rectangle in font atlas for a codepoint (unicode character), fallback to '?' if not found

Defined in raylib.h:

```c
Rectangle GetGlyphAtlasRec(Font font, int codepoint) 
```

Python wrapper:

```python
def get_glyph_atlas_rec(font: Font, codepoint: int) -> Rectangle
```

See also: <a href="#Font">Font</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadCodepoints"><code>load_codepoints</code> function</h2>

> Load all codepoints from a UTF-8 text string, codepoints count returned by parameter

Defined in raylib.h:

```c
int LoadCodepoints(char * text, int count) 
```

Python wrapper:

```python
def load_codepoints(text: Union[str, CharPtr], count: Union[Seq[int], IntPtr]) -> Union[Seq[int], IntPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadCodepoints"><code>unload_codepoints</code> function</h2>

> Unload codepoints data from memory

Defined in raylib.h:

```c
void UnloadCodepoints(int codepoints) 
```

Python wrapper:

```python
def unload_codepoints(codepoints: Union[Seq[int], IntPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetCodepointCount"><code>get_codepoint_count</code> function</h2>

> Get total number of codepoints in a UTF-8 encoded string

Defined in raylib.h:

```c
int GetCodepointCount(char * text) 
```

Python wrapper:

```python
def get_codepoint_count(text: Union[str, CharPtr]) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetCodepoint"><code>get_codepoint</code> function</h2>

> Get next codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure

Defined in raylib.h:

```c
int GetCodepoint(char * text, int bytes_processed) 
```

Python wrapper:

```python
def get_codepoint(text: Union[str, CharPtr], bytes_processed: Union[Seq[int], IntPtr]) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CodepointToUTF8"><code>codepoint_to_utf8</code> function</h2>

> Encode one codepoint into UTF-8 byte array (array length returned as parameter)

Defined in raylib.h:

```c
char * CodepointToUTF8(int codepoint, int byte_size) 
```

Python wrapper:

```python
def codepoint_to_utf8(codepoint: int, byte_size: Union[Seq[int], IntPtr]) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextCodepointsToUTF8"><code>text_codepoints_to_utf8</code> function</h2>

> Encode text as codepoints array into UTF-8 text string (WARNING: memory must be freed!)

Defined in raylib.h:

```c
char * TextCodepointsToUTF8(int codepoints, int length) 
```

Python wrapper:

```python
def text_codepoints_to_utf8(codepoints: Union[Seq[int], IntPtr], length: int) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextCopy"><code>text_copy</code> function</h2>

> Copy one string to another, returns bytes copied

Defined in raylib.h:

```c
int TextCopy(char * dst, char * src) 
```

Python wrapper:

```python
def text_copy(dst: Union[str, CharPtr], src: Union[str, CharPtr]) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextIsEqual"><code>text_is_equal</code> function</h2>

> Check if two text string are equal

Defined in raylib.h:

```c
bool TextIsEqual(char * text1, char * text2) 
```

Python wrapper:

```python
def text_is_equal(text1: Union[str, CharPtr], text2: Union[str, CharPtr]) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextLength"><code>text_length</code> function</h2>

> Get text length, checks for '\0' ending

Defined in raylib.h:

```c
unsigned int TextLength(char * text) 
```

Python wrapper:

```python
def text_length(text: Union[str, CharPtr]) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextFormat"><code>text_format</code> function</h2>

> Text formatting with variables (sprintf() style)

Defined in raylib.h:

```c
char * TextFormat(char * text, va_list args) 
```

Python wrapper:

```python
def text_format(text: Union[str, CharPtr], args: bytes) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextSubtext"><code>text_subtext</code> function</h2>

> Get a piece of a text string

Defined in raylib.h:

```c
char * TextSubtext(char * text, int position, int length) 
```

Python wrapper:

```python
def text_subtext(text: Union[str, CharPtr], position: int, length: int) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextReplace"><code>text_replace</code> function</h2>

> Replace text string (WARNING: memory must be freed!)

Defined in raylib.h:

```c
char * TextReplace(char * text, char * replace, char * by) 
```

Python wrapper:

```python
def text_replace(text: Union[str, CharPtr], replace: Union[str, CharPtr], by: Union[str, CharPtr]) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextInsert"><code>text_insert</code> function</h2>

> Insert text in a position (WARNING: memory must be freed!)

Defined in raylib.h:

```c
char * TextInsert(char * text, char * insert, int position) 
```

Python wrapper:

```python
def text_insert(text: Union[str, CharPtr], insert: Union[str, CharPtr], position: int) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextJoin"><code>text_join</code> function</h2>

> Join text strings with delimiter

Defined in raylib.h:

```c
char * TextJoin(char ** text_list, int count, char * delimiter) 
```

Python wrapper:

```python
def text_join(text_list: Seq[Union[str, CharPtr]], count: int, delimiter: Union[str, CharPtr]) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextSplit"><code>text_split</code> function</h2>

> Split text into multiple strings

Defined in raylib.h:

```c
char ** TextSplit(char * text, char delimiter, int count) 
```

Python wrapper:

```python
def text_split(text: Union[str, CharPtr], delimiter: int, count: Union[Seq[int], IntPtr]) -> Seq[Union[str, CharPtr]]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextAppend"><code>text_append</code> function</h2>

> Append text at specific position and move cursor!

Defined in raylib.h:

```c
void TextAppend(char * text, char * append, int position) 
```

Python wrapper:

```python
def text_append(text: Union[str, CharPtr], append: Union[str, CharPtr], position: Union[Seq[int], IntPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextFindIndex"><code>text_find_index</code> function</h2>

> Find first text occurrence within a string

Defined in raylib.h:

```c
int TextFindIndex(char * text, char * find) 
```

Python wrapper:

```python
def text_find_index(text: Union[str, CharPtr], find: Union[str, CharPtr]) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextToUpper"><code>text_to_upper</code> function</h2>

> Get upper case version of provided string

Defined in raylib.h:

```c
char * TextToUpper(char * text) 
```

Python wrapper:

```python
def text_to_upper(text: Union[str, CharPtr]) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextToLower"><code>text_to_lower</code> function</h2>

> Get lower case version of provided string

Defined in raylib.h:

```c
char * TextToLower(char * text) 
```

Python wrapper:

```python
def text_to_lower(text: Union[str, CharPtr]) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextToPascal"><code>text_to_pascal</code> function</h2>

> Get Pascal case notation version of provided string

Defined in raylib.h:

```c
char * TextToPascal(char * text) 
```

Python wrapper:

```python
def text_to_pascal(text: Union[str, CharPtr]) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextToInteger"><code>text_to_integer</code> function</h2>

> Get integer value from text (negative values not supported)

Defined in raylib.h:

```c
int TextToInteger(char * text) 
```

Python wrapper:

```python
def text_to_integer(text: Union[str, CharPtr]) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawLine3D"><code>draw_line3d</code> function</h2>

> Draw a line in 3D world space

Defined in raylib.h:

```c
void DrawLine3D(Vector3 start_pos, Vector3 end_pos, Color color) 
```

Python wrapper:

```python
def draw_line3d(start_pos: Vector3, end_pos: Vector3, color: Color) -> None
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawPoint3D"><code>draw_point3d</code> function</h2>

> Draw a point in 3D space, actually a small line

Defined in raylib.h:

```c
void DrawPoint3D(Vector3 position, Color color) 
```

Python wrapper:

```python
def draw_point3d(position: Vector3, color: Color) -> None
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCircle3D"><code>draw_circle3d</code> function</h2>

> Draw a circle in 3D world space

Defined in raylib.h:

```c
void DrawCircle3D(Vector3 center, float radius, Vector3 rotation_axis, float rotation_angle, Color color) 
```

Python wrapper:

```python
def draw_circle3d(center: Vector3, radius: float, rotation_axis: Vector3, rotation_angle: float, color: Color) -> None
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTriangle3D"><code>draw_triangle3d</code> function</h2>

> Draw a color-filled triangle (vertex in counter-clockwise order!)

Defined in raylib.h:

```c
void DrawTriangle3D(Vector3 v1, Vector3 v2, Vector3 v3, Color color) 
```

Python wrapper:

```python
def draw_triangle3d(v1: Vector3, v2: Vector3, v3: Vector3, color: Color) -> None
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTriangleStrip3D"><code>draw_triangle_strip3d</code> function</h2>

> Draw a triangle strip defined by points

Defined in raylib.h:

```c
void DrawTriangleStrip3D(Vector3 * points, int point_count, Color color) 
```

Python wrapper:

```python
def draw_triangle_strip3d(points: Vector3Ptr, point_count: int, color: Color) -> None
```

See also: <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCube"><code>draw_cube</code> function</h2>

> Draw cube

Defined in raylib.h:

```c
void DrawCube(Vector3 position, float width, float height, float length, Color color) 
```

Python wrapper:

```python
def draw_cube(position: Vector3, width: float, height: float, length: float, color: Color) -> None
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCubeV"><code>draw_cube_v</code> function</h2>

> Draw cube (Vector version)

Defined in raylib.h:

```c
void DrawCubeV(Vector3 position, Vector3 size, Color color) 
```

Python wrapper:

```python
def draw_cube_v(position: Vector3, size: Vector3, color: Color) -> None
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCubeWires"><code>draw_cube_wires</code> function</h2>

> Draw cube wires

Defined in raylib.h:

```c
void DrawCubeWires(Vector3 position, float width, float height, float length, Color color) 
```

Python wrapper:

```python
def draw_cube_wires(position: Vector3, width: float, height: float, length: float, color: Color) -> None
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCubeWiresV"><code>draw_cube_wires_v</code> function</h2>

> Draw cube wires (Vector version)

Defined in raylib.h:

```c
void DrawCubeWiresV(Vector3 position, Vector3 size, Color color) 
```

Python wrapper:

```python
def draw_cube_wires_v(position: Vector3, size: Vector3, color: Color) -> None
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCubeTexture"><code>draw_cube_texture</code> function</h2>

> Draw cube textured

Defined in raylib.h:

```c
void DrawCubeTexture(Texture2D texture, Vector3 position, float width, float height, float length, Color color) 
```

Python wrapper:

```python
def draw_cube_texture(texture: Texture2D, position: Vector3, width: float, height: float, length: float, color: Color) -> None
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCubeTextureRec"><code>draw_cube_texture_rec</code> function</h2>

> Draw cube with a region of a texture

Defined in raylib.h:

```c
void DrawCubeTextureRec(Texture2D texture, Rectangle source, Vector3 position, float width, float height, float length, Color color) 
```

Python wrapper:

```python
def draw_cube_texture_rec(texture: Texture2D, source: Rectangle, position: Vector3, width: float, height: float, length: float, color: Color) -> None
```

See also: <a href="#Rectangle">Rectangle</a>, <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawSphere"><code>draw_sphere</code> function</h2>

> Draw sphere

Defined in raylib.h:

```c
void DrawSphere(Vector3 center_pos, float radius, Color color) 
```

Python wrapper:

```python
def draw_sphere(center_pos: Vector3, radius: float, color: Color) -> None
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawSphereEx"><code>draw_sphere_ex</code> function</h2>

> Draw sphere with extended parameters

Defined in raylib.h:

```c
void DrawSphereEx(Vector3 center_pos, float radius, int rings, int slices, Color color) 
```

Python wrapper:

```python
def draw_sphere_ex(center_pos: Vector3, radius: float, rings: int, slices: int, color: Color) -> None
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawSphereWires"><code>draw_sphere_wires</code> function</h2>

> Draw sphere wires

Defined in raylib.h:

```c
void DrawSphereWires(Vector3 center_pos, float radius, int rings, int slices, Color color) 
```

Python wrapper:

```python
def draw_sphere_wires(center_pos: Vector3, radius: float, rings: int, slices: int, color: Color) -> None
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCylinder"><code>draw_cylinder</code> function</h2>

> Draw a cylinder/cone

Defined in raylib.h:

```c
void DrawCylinder(Vector3 position, float radius_top, float radius_bottom, float height, int slices, Color color) 
```

Python wrapper:

```python
def draw_cylinder(position: Vector3, radius_top: float, radius_bottom: float, height: float, slices: int, color: Color) -> None
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCylinderEx"><code>draw_cylinder_ex</code> function</h2>

> Draw a cylinder with base at startPos and top at endPos

Defined in raylib.h:

```c
void DrawCylinderEx(Vector3 start_pos, Vector3 end_pos, float start_radius, float end_radius, int sides, Color color) 
```

Python wrapper:

```python
def draw_cylinder_ex(start_pos: Vector3, end_pos: Vector3, start_radius: float, end_radius: float, sides: int, color: Color) -> None
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCylinderWires"><code>draw_cylinder_wires</code> function</h2>

> Draw a cylinder/cone wires

Defined in raylib.h:

```c
void DrawCylinderWires(Vector3 position, float radius_top, float radius_bottom, float height, int slices, Color color) 
```

Python wrapper:

```python
def draw_cylinder_wires(position: Vector3, radius_top: float, radius_bottom: float, height: float, slices: int, color: Color) -> None
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCylinderWiresEx"><code>draw_cylinder_wires_ex</code> function</h2>

> Draw a cylinder wires with base at startPos and top at endPos

Defined in raylib.h:

```c
void DrawCylinderWiresEx(Vector3 start_pos, Vector3 end_pos, float start_radius, float end_radius, int sides, Color color) 
```

Python wrapper:

```python
def draw_cylinder_wires_ex(start_pos: Vector3, end_pos: Vector3, start_radius: float, end_radius: float, sides: int, color: Color) -> None
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawPlane"><code>draw_plane</code> function</h2>

> Draw a plane XZ

Defined in raylib.h:

```c
void DrawPlane(Vector3 center_pos, Vector2 size, Color color) 
```

Python wrapper:

```python
def draw_plane(center_pos: Vector3, size: Vector2, color: Color) -> None
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRay"><code>draw_ray</code> function</h2>

> Draw a ray line

Defined in raylib.h:

```c
void DrawRay(Ray ray, Color color) 
```

Python wrapper:

```python
def draw_ray(ray: Ray, color: Color) -> None
```

See also: <a href="#Ray">Ray</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawGrid"><code>draw_grid</code> function</h2>

> Draw a grid (centered at (0, 0, 0))

Defined in raylib.h:

```c
void DrawGrid(int slices, float spacing) 
```

Python wrapper:

```python
def draw_grid(slices: int, spacing: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadModel"><code>load_model</code> function</h2>

> Load model from files (meshes and materials)

Defined in raylib.h:

```c
Model LoadModel(char * file_name) 
```

Python wrapper:

```python
def load_model(file_name: Union[str, CharPtr]) -> Model
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadModelFromMesh"><code>load_model_from_mesh</code> function</h2>

> Load model from generated mesh (default material)

Defined in raylib.h:

```c
Model LoadModelFromMesh(Mesh mesh) 
```

Python wrapper:

```python
def load_model_from_mesh(mesh: Mesh) -> Model
```

See also: <a href="#Mesh">Mesh</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadModel"><code>unload_model</code> function</h2>

> Unload model (including meshes) from memory (RAM and/or VRAM)

Defined in raylib.h:

```c
void UnloadModel(Model model) 
```

Python wrapper:

```python
def unload_model(model: Model) -> None
```

See also: <a href="#Model">Model</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadModelKeepMeshes"><code>unload_model_keep_meshes</code> function</h2>

> Unload model (but not meshes) from memory (RAM and/or VRAM)

Defined in raylib.h:

```c
void UnloadModelKeepMeshes(Model model) 
```

Python wrapper:

```python
def unload_model_keep_meshes(model: Model) -> None
```

See also: <a href="#Model">Model</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetModelBoundingBox"><code>get_model_bounding_box</code> function</h2>

> Compute model bounding box limits (considers all meshes)

Defined in raylib.h:

```c
BoundingBox GetModelBoundingBox(Model model) 
```

Python wrapper:

```python
def get_model_bounding_box(model: Model) -> BoundingBox
```

See also: <a href="#Model">Model</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawModel"><code>draw_model</code> function</h2>

> Draw a model (with texture if set)

Defined in raylib.h:

```c
void DrawModel(Model model, Vector3 position, float scale, Color tint) 
```

Python wrapper:

```python
def draw_model(model: Model, position: Vector3, scale: float, tint: Color) -> None
```

See also: <a href="#Model">Model</a>, <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawModelEx"><code>draw_model_ex</code> function</h2>

> Draw a model with extended parameters

Defined in raylib.h:

```c
void DrawModelEx(Model model, Vector3 position, Vector3 rotation_axis, float rotation_angle, Vector3 scale, Color tint) 
```

Python wrapper:

```python
def draw_model_ex(model: Model, position: Vector3, rotation_axis: Vector3, rotation_angle: float, scale: Vector3, tint: Color) -> None
```

See also: <a href="#Model">Model</a>, <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawModelWires"><code>draw_model_wires</code> function</h2>

> Draw a model wires (with texture if set)

Defined in raylib.h:

```c
void DrawModelWires(Model model, Vector3 position, float scale, Color tint) 
```

Python wrapper:

```python
def draw_model_wires(model: Model, position: Vector3, scale: float, tint: Color) -> None
```

See also: <a href="#Model">Model</a>, <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawModelWiresEx"><code>draw_model_wires_ex</code> function</h2>

> Draw a model wires (with texture if set) with extended parameters

Defined in raylib.h:

```c
void DrawModelWiresEx(Model model, Vector3 position, Vector3 rotation_axis, float rotation_angle, Vector3 scale, Color tint) 
```

Python wrapper:

```python
def draw_model_wires_ex(model: Model, position: Vector3, rotation_axis: Vector3, rotation_angle: float, scale: Vector3, tint: Color) -> None
```

See also: <a href="#Model">Model</a>, <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawBoundingBox"><code>draw_bounding_box</code> function</h2>

> Draw bounding box (wires)

Defined in raylib.h:

```c
void DrawBoundingBox(BoundingBox box, Color color) 
```

Python wrapper:

```python
def draw_bounding_box(box: BoundingBox, color: Color) -> None
```

See also: <a href="#BoundingBox">BoundingBox</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawBillboard"><code>draw_billboard</code> function</h2>

> Draw a billboard texture

Defined in raylib.h:

```c
void DrawBillboard(Camera camera, Texture2D texture, Vector3 position, float size, Color tint) 
```

Python wrapper:

```python
def draw_billboard(camera: Camera, texture: Texture2D, position: Vector3, size: float, tint: Color) -> None
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawBillboardRec"><code>draw_billboard_rec</code> function</h2>

> Draw a billboard texture defined by source

Defined in raylib.h:

```c
void DrawBillboardRec(Camera camera, Texture2D texture, Rectangle source, Vector3 position, Vector2 size, Color tint) 
```

Python wrapper:

```python
def draw_billboard_rec(camera: Camera, texture: Texture2D, source: Rectangle, position: Vector3, size: Vector2, tint: Color) -> None
```

See also: <a href="#Rectangle">Rectangle</a>, <a href="#Vector3">Vector3</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawBillboardPro"><code>draw_billboard_pro</code> function</h2>

> Draw a billboard texture defined by source and rotation

Defined in raylib.h:

```c
void DrawBillboardPro(Camera camera, Texture2D texture, Rectangle source, Vector3 position, Vector3 up, Vector2 size, Vector2 origin, float rotation, Color tint) 
```

Python wrapper:

```python
def draw_billboard_pro(camera: Camera, texture: Texture2D, source: Rectangle, position: Vector3, up: Vector3, size: Vector2, origin: Vector2, rotation: float, tint: Color) -> None
```

See also: <a href="#Rectangle">Rectangle</a>, <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>, <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UploadMesh"><code>upload_mesh</code> function</h2>

> Upload mesh vertex data in GPU and provide VAO/VBO ids

Defined in raylib.h:

```c
void UploadMesh(Mesh * mesh, bool dynamic) 
```

Python wrapper:

```python
def upload_mesh(mesh: MeshPtr, dynamic: bool) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UpdateMeshBuffer"><code>update_mesh_buffer</code> function</h2>

> Update mesh vertex data in GPU for a specific buffer index

Defined in raylib.h:

```c
void UpdateMeshBuffer(Mesh mesh, int index, void data, int data_size, int offset) 
```

Python wrapper:

```python
def update_mesh_buffer(mesh: Mesh, index: int, data: bytes, data_size: int, offset: int) -> None
```

See also: <a href="#Mesh">Mesh</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadMesh"><code>unload_mesh</code> function</h2>

> Unload mesh data from CPU and GPU

Defined in raylib.h:

```c
void UnloadMesh(Mesh mesh) 
```

Python wrapper:

```python
def unload_mesh(mesh: Mesh) -> None
```

See also: <a href="#Mesh">Mesh</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawMesh"><code>draw_mesh</code> function</h2>

> Draw a 3d mesh with material and transform

Defined in raylib.h:

```c
void DrawMesh(Mesh mesh, Material material, Matrix transform) 
```

Python wrapper:

```python
def draw_mesh(mesh: Mesh, material: Material, transform: Matrix) -> None
```

See also: <a href="#Mesh">Mesh</a>, <a href="#Material">Material</a>, <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawMeshInstanced"><code>draw_mesh_instanced</code> function</h2>

> Draw multiple mesh instances with material and different transforms

Defined in raylib.h:

```c
void DrawMeshInstanced(Mesh mesh, Material material, Matrix * transforms, int instances) 
```

Python wrapper:

```python
def draw_mesh_instanced(mesh: Mesh, material: Material, transforms: MatrixPtr, instances: int) -> None
```

See also: <a href="#Mesh">Mesh</a>, <a href="#Material">Material</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ExportMesh"><code>export_mesh</code> function</h2>

> Export mesh data to file, returns true on success

Defined in raylib.h:

```c
bool ExportMesh(Mesh mesh, char * file_name) 
```

Python wrapper:

```python
def export_mesh(mesh: Mesh, file_name: Union[str, CharPtr]) -> bool
```

See also: <a href="#Mesh">Mesh</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMeshBoundingBox"><code>get_mesh_bounding_box</code> function</h2>

> Compute mesh bounding box limits

Defined in raylib.h:

```c
BoundingBox GetMeshBoundingBox(Mesh mesh) 
```

Python wrapper:

```python
def get_mesh_bounding_box(mesh: Mesh) -> BoundingBox
```

See also: <a href="#Mesh">Mesh</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenMeshTangents"><code>gen_mesh_tangents</code> function</h2>

> Compute mesh tangents

Defined in raylib.h:

```c
void GenMeshTangents(Mesh * mesh) 
```

Python wrapper:

```python
def gen_mesh_tangents(mesh: MeshPtr) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenMeshPoly"><code>gen_mesh_poly</code> function</h2>

> Generate polygonal mesh

Defined in raylib.h:

```c
Mesh GenMeshPoly(int sides, float radius) 
```

Python wrapper:

```python
def gen_mesh_poly(sides: int, radius: float) -> Mesh
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenMeshPlane"><code>gen_mesh_plane</code> function</h2>

> Generate plane mesh (with subdivisions)

Defined in raylib.h:

```c
Mesh GenMeshPlane(float width, float length, int res_x, int res_z) 
```

Python wrapper:

```python
def gen_mesh_plane(width: float, length: float, res_x: int, res_z: int) -> Mesh
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenMeshCube"><code>gen_mesh_cube</code> function</h2>

> Generate cuboid mesh

Defined in raylib.h:

```c
Mesh GenMeshCube(float width, float height, float length) 
```

Python wrapper:

```python
def gen_mesh_cube(width: float, height: float, length: float) -> Mesh
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenMeshSphere"><code>gen_mesh_sphere</code> function</h2>

> Generate sphere mesh (standard sphere)

Defined in raylib.h:

```c
Mesh GenMeshSphere(float radius, int rings, int slices) 
```

Python wrapper:

```python
def gen_mesh_sphere(radius: float, rings: int, slices: int) -> Mesh
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenMeshHemiSphere"><code>gen_mesh_hemi_sphere</code> function</h2>

> Generate half-sphere mesh (no bottom cap)

Defined in raylib.h:

```c
Mesh GenMeshHemiSphere(float radius, int rings, int slices) 
```

Python wrapper:

```python
def gen_mesh_hemi_sphere(radius: float, rings: int, slices: int) -> Mesh
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenMeshCylinder"><code>gen_mesh_cylinder</code> function</h2>

> Generate cylinder mesh

Defined in raylib.h:

```c
Mesh GenMeshCylinder(float radius, float height, int slices) 
```

Python wrapper:

```python
def gen_mesh_cylinder(radius: float, height: float, slices: int) -> Mesh
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenMeshCone"><code>gen_mesh_cone</code> function</h2>

> Generate cone/pyramid mesh

Defined in raylib.h:

```c
Mesh GenMeshCone(float radius, float height, int slices) 
```

Python wrapper:

```python
def gen_mesh_cone(radius: float, height: float, slices: int) -> Mesh
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenMeshTorus"><code>gen_mesh_torus</code> function</h2>

> Generate torus mesh

Defined in raylib.h:

```c
Mesh GenMeshTorus(float radius, float size, int rad_seg, int sides) 
```

Python wrapper:

```python
def gen_mesh_torus(radius: float, size: float, rad_seg: int, sides: int) -> Mesh
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenMeshKnot"><code>gen_mesh_knot</code> function</h2>

> Generate trefoil knot mesh

Defined in raylib.h:

```c
Mesh GenMeshKnot(float radius, float size, int rad_seg, int sides) 
```

Python wrapper:

```python
def gen_mesh_knot(radius: float, size: float, rad_seg: int, sides: int) -> Mesh
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenMeshHeightmap"><code>gen_mesh_heightmap</code> function</h2>

> Generate heightmap mesh from image data

Defined in raylib.h:

```c
Mesh GenMeshHeightmap(Image heightmap, Vector3 size) 
```

Python wrapper:

```python
def gen_mesh_heightmap(heightmap: Image, size: Vector3) -> Mesh
```

See also: <a href="#Image">Image</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenMeshCubicmap"><code>gen_mesh_cubicmap</code> function</h2>

> Generate cubes-based map mesh from image data

Defined in raylib.h:

```c
Mesh GenMeshCubicmap(Image cubicmap, Vector3 cube_size) 
```

Python wrapper:

```python
def gen_mesh_cubicmap(cubicmap: Image, cube_size: Vector3) -> Mesh
```

See also: <a href="#Image">Image</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadMaterials"><code>load_materials</code> function</h2>

> Load materials from model file

Defined in raylib.h:

```c
Material * LoadMaterials(char * file_name, int material_count) 
```

Python wrapper:

```python
def load_materials(file_name: Union[str, CharPtr], material_count: Union[Seq[int], IntPtr]) -> MaterialPtr
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadMaterialDefault"><code>load_material_default</code> function</h2>

> Load default material (Supports: DIFFUSE, SPECULAR, NORMAL maps)

Defined in raylib.h:

```c
Material LoadMaterialDefault() 
```

Python wrapper:

```python
def load_material_default() -> Material
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadMaterial"><code>unload_material</code> function</h2>

> Unload material from GPU memory (VRAM)

Defined in raylib.h:

```c
void UnloadMaterial(Material material) 
```

Python wrapper:

```python
def unload_material(material: Material) -> None
```

See also: <a href="#Material">Material</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetMaterialTexture"><code>set_material_texture</code> function</h2>

> Set texture for a material map type (MATERIAL_MAP_DIFFUSE, MATERIAL_MAP_SPECULAR...)

Defined in raylib.h:

```c
void SetMaterialTexture(Material * material, int map_type, Texture2D texture) 
```

Python wrapper:

```python
def set_material_texture(material: MaterialPtr, map_type: int, texture: Texture2D) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetModelMeshMaterial"><code>set_model_mesh_material</code> function</h2>

> Set material for a mesh

Defined in raylib.h:

```c
void SetModelMeshMaterial(Model * model, int mesh_id, int material_id) 
```

Python wrapper:

```python
def set_model_mesh_material(model: ModelPtr, mesh_id: int, material_id: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadModelAnimations"><code>load_model_animations</code> function</h2>

> Load model animations from file

Defined in raylib.h:

```c
ModelAnimation * LoadModelAnimations(char * file_name, unsigned int anim_count) 
```

Python wrapper:

```python
def load_model_animations(file_name: Union[str, CharPtr], anim_count: Union[Seq[int], UIntPtr]) -> ModelAnimationPtr
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UpdateModelAnimation"><code>update_model_animation</code> function</h2>

> Update model animation pose

Defined in raylib.h:

```c
void UpdateModelAnimation(Model model, ModelAnimation anim, int frame) 
```

Python wrapper:

```python
def update_model_animation(model: Model, anim: ModelAnimation, frame: int) -> None
```

See also: <a href="#Model">Model</a>, <a href="#ModelAnimation">ModelAnimation</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadModelAnimation"><code>unload_model_animation</code> function</h2>

> Unload animation data

Defined in raylib.h:

```c
void UnloadModelAnimation(ModelAnimation anim) 
```

Python wrapper:

```python
def unload_model_animation(anim: ModelAnimation) -> None
```

See also: <a href="#ModelAnimation">ModelAnimation</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadModelAnimations"><code>unload_model_animations</code> function</h2>

> Unload animation array data

Defined in raylib.h:

```c
void UnloadModelAnimations(ModelAnimation * animations, unsigned int count) 
```

Python wrapper:

```python
def unload_model_animations(animations: ModelAnimationPtr, count: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsModelAnimationValid"><code>is_model_animation_valid</code> function</h2>

> Check model animation skeleton match

Defined in raylib.h:

```c
bool IsModelAnimationValid(Model model, ModelAnimation anim) 
```

Python wrapper:

```python
def is_model_animation_valid(model: Model, anim: ModelAnimation) -> bool
```

See also: <a href="#Model">Model</a>, <a href="#ModelAnimation">ModelAnimation</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CheckCollisionSpheres"><code>check_collision_spheres</code> function</h2>

> Check collision between two spheres

Defined in raylib.h:

```c
bool CheckCollisionSpheres(Vector3 center1, float radius1, Vector3 center2, float radius2) 
```

Python wrapper:

```python
def check_collision_spheres(center1: Vector3, radius1: float, center2: Vector3, radius2: float) -> bool
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CheckCollisionBoxes"><code>check_collision_boxes</code> function</h2>

> Check collision between two bounding boxes

Defined in raylib.h:

```c
bool CheckCollisionBoxes(BoundingBox box1, BoundingBox box2) 
```

Python wrapper:

```python
def check_collision_boxes(box1: BoundingBox, box2: BoundingBox) -> bool
```

See also: <a href="#BoundingBox">BoundingBox</a>, <a href="#BoundingBox">BoundingBox</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CheckCollisionBoxSphere"><code>check_collision_box_sphere</code> function</h2>

> Check collision between box and sphere

Defined in raylib.h:

```c
bool CheckCollisionBoxSphere(BoundingBox box, Vector3 center, float radius) 
```

Python wrapper:

```python
def check_collision_box_sphere(box: BoundingBox, center: Vector3, radius: float) -> bool
```

See also: <a href="#BoundingBox">BoundingBox</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetRayCollisionSphere"><code>get_ray_collision_sphere</code> function</h2>

> Get collision info between ray and sphere

Defined in raylib.h:

```c
RayCollision GetRayCollisionSphere(Ray ray, Vector3 center, float radius) 
```

Python wrapper:

```python
def get_ray_collision_sphere(ray: Ray, center: Vector3, radius: float) -> RayCollision
```

See also: <a href="#Ray">Ray</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetRayCollisionBox"><code>get_ray_collision_box</code> function</h2>

> Get collision info between ray and box

Defined in raylib.h:

```c
RayCollision GetRayCollisionBox(Ray ray, BoundingBox box) 
```

Python wrapper:

```python
def get_ray_collision_box(ray: Ray, box: BoundingBox) -> RayCollision
```

See also: <a href="#Ray">Ray</a>, <a href="#BoundingBox">BoundingBox</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetRayCollisionMesh"><code>get_ray_collision_mesh</code> function</h2>

> Get collision info between ray and mesh

Defined in raylib.h:

```c
RayCollision GetRayCollisionMesh(Ray ray, Mesh mesh, Matrix transform) 
```

Python wrapper:

```python
def get_ray_collision_mesh(ray: Ray, mesh: Mesh, transform: Matrix) -> RayCollision
```

See also: <a href="#Ray">Ray</a>, <a href="#Mesh">Mesh</a>, <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetRayCollisionTriangle"><code>get_ray_collision_triangle</code> function</h2>

> Get collision info between ray and triangle

Defined in raylib.h:

```c
RayCollision GetRayCollisionTriangle(Ray ray, Vector3 p1, Vector3 p2, Vector3 p3) 
```

Python wrapper:

```python
def get_ray_collision_triangle(ray: Ray, p1: Vector3, p2: Vector3, p3: Vector3) -> RayCollision
```

See also: <a href="#Ray">Ray</a>, <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetRayCollisionQuad"><code>get_ray_collision_quad</code> function</h2>

> Get collision info between ray and quad

Defined in raylib.h:

```c
RayCollision GetRayCollisionQuad(Ray ray, Vector3 p1, Vector3 p2, Vector3 p3, Vector3 p4) 
```

Python wrapper:

```python
def get_ray_collision_quad(ray: Ray, p1: Vector3, p2: Vector3, p3: Vector3, p4: Vector3) -> RayCollision
```

See also: <a href="#Ray">Ray</a>, <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="InitAudioDevice"><code>init_audio_device</code> function</h2>

> Initialize audio device and context

Defined in raylib.h:

```c
void InitAudioDevice() 
```

Python wrapper:

```python
def init_audio_device() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CloseAudioDevice"><code>close_audio_device</code> function</h2>

> Close the audio device and context

Defined in raylib.h:

```c
void CloseAudioDevice() 
```

Python wrapper:

```python
def close_audio_device() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsAudioDeviceReady"><code>is_audio_device_ready</code> function</h2>

> Check if audio device has been initialized successfully

Defined in raylib.h:

```c
bool IsAudioDeviceReady() 
```

Python wrapper:

```python
def is_audio_device_ready() -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetMasterVolume"><code>set_master_volume</code> function</h2>

> Set master volume (listener)

Defined in raylib.h:

```c
void SetMasterVolume(float volume) 
```

Python wrapper:

```python
def set_master_volume(volume: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadWave"><code>load_wave</code> function</h2>

> Load wave data from file

Defined in raylib.h:

```c
Wave LoadWave(char * file_name) 
```

Python wrapper:

```python
def load_wave(file_name: Union[str, CharPtr]) -> Wave
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadWaveFromMemory"><code>load_wave_from_memory</code> function</h2>

> Load wave from memory buffer, fileType refers to extension: i.e. '.wav'

Defined in raylib.h:

```c
Wave LoadWaveFromMemory(char * file_type, unsigned char * file_data, int data_size) 
```

Python wrapper:

```python
def load_wave_from_memory(file_type: Union[str, CharPtr], file_data: Union[Seq[int], UCharPtr], data_size: int) -> Wave
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadSound"><code>load_sound</code> function</h2>

> Load sound from file

Defined in raylib.h:

```c
Sound LoadSound(char * file_name) 
```

Python wrapper:

```python
def load_sound(file_name: Union[str, CharPtr]) -> Sound
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadSoundFromWave"><code>load_sound_from_wave</code> function</h2>

> Load sound from wave data

Defined in raylib.h:

```c
Sound LoadSoundFromWave(Wave wave) 
```

Python wrapper:

```python
def load_sound_from_wave(wave: Wave) -> Sound
```

See also: <a href="#Wave">Wave</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UpdateSound"><code>update_sound</code> function</h2>

> Update sound buffer with new data

Defined in raylib.h:

```c
void UpdateSound(Sound sound, void data, int sample_count) 
```

Python wrapper:

```python
def update_sound(sound: Sound, data: bytes, sample_count: int) -> None
```

See also: <a href="#Sound">Sound</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadWave"><code>unload_wave</code> function</h2>

> Unload wave data

Defined in raylib.h:

```c
void UnloadWave(Wave wave) 
```

Python wrapper:

```python
def unload_wave(wave: Wave) -> None
```

See also: <a href="#Wave">Wave</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadSound"><code>unload_sound</code> function</h2>

> Unload sound

Defined in raylib.h:

```c
void UnloadSound(Sound sound) 
```

Python wrapper:

```python
def unload_sound(sound: Sound) -> None
```

See also: <a href="#Sound">Sound</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ExportWave"><code>export_wave</code> function</h2>

> Export wave data to file, returns true on success

Defined in raylib.h:

```c
bool ExportWave(Wave wave, char * file_name) 
```

Python wrapper:

```python
def export_wave(wave: Wave, file_name: Union[str, CharPtr]) -> bool
```

See also: <a href="#Wave">Wave</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ExportWaveAsCode"><code>export_wave_as_code</code> function</h2>

> Export wave sample data to code (.h), returns true on success

Defined in raylib.h:

```c
bool ExportWaveAsCode(Wave wave, char * file_name) 
```

Python wrapper:

```python
def export_wave_as_code(wave: Wave, file_name: Union[str, CharPtr]) -> bool
```

See also: <a href="#Wave">Wave</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="PlaySound"><code>play_sound</code> function</h2>

> Play a sound

Defined in raylib.h:

```c
void PlaySound(Sound sound) 
```

Python wrapper:

```python
def play_sound(sound: Sound) -> None
```

See also: <a href="#Sound">Sound</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="StopSound"><code>stop_sound</code> function</h2>

> Stop playing a sound

Defined in raylib.h:

```c
void StopSound(Sound sound) 
```

Python wrapper:

```python
def stop_sound(sound: Sound) -> None
```

See also: <a href="#Sound">Sound</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="PauseSound"><code>pause_sound</code> function</h2>

> Pause a sound

Defined in raylib.h:

```c
void PauseSound(Sound sound) 
```

Python wrapper:

```python
def pause_sound(sound: Sound) -> None
```

See also: <a href="#Sound">Sound</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ResumeSound"><code>resume_sound</code> function</h2>

> Resume a paused sound

Defined in raylib.h:

```c
void ResumeSound(Sound sound) 
```

Python wrapper:

```python
def resume_sound(sound: Sound) -> None
```

See also: <a href="#Sound">Sound</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="PlaySoundMulti"><code>play_sound_multi</code> function</h2>

> Play a sound (using multichannel buffer pool)

Defined in raylib.h:

```c
void PlaySoundMulti(Sound sound) 
```

Python wrapper:

```python
def play_sound_multi(sound: Sound) -> None
```

See also: <a href="#Sound">Sound</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="StopSoundMulti"><code>stop_sound_multi</code> function</h2>

> Stop any sound playing (using multichannel buffer pool)

Defined in raylib.h:

```c
void StopSoundMulti() 
```

Python wrapper:

```python
def stop_sound_multi() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetSoundsPlaying"><code>get_sounds_playing</code> function</h2>

> Get number of sounds playing in the multichannel

Defined in raylib.h:

```c
int GetSoundsPlaying() 
```

Python wrapper:

```python
def get_sounds_playing() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsSoundPlaying"><code>is_sound_playing</code> function</h2>

> Check if a sound is currently playing

Defined in raylib.h:

```c
bool IsSoundPlaying(Sound sound) 
```

Python wrapper:

```python
def is_sound_playing(sound: Sound) -> bool
```

See also: <a href="#Sound">Sound</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetSoundVolume"><code>set_sound_volume</code> function</h2>

> Set volume for a sound (1.0 is max level)

Defined in raylib.h:

```c
void SetSoundVolume(Sound sound, float volume) 
```

Python wrapper:

```python
def set_sound_volume(sound: Sound, volume: float) -> None
```

See also: <a href="#Sound">Sound</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetSoundPitch"><code>set_sound_pitch</code> function</h2>

> Set pitch for a sound (1.0 is base level)

Defined in raylib.h:

```c
void SetSoundPitch(Sound sound, float pitch) 
```

Python wrapper:

```python
def set_sound_pitch(sound: Sound, pitch: float) -> None
```

See also: <a href="#Sound">Sound</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetSoundPan"><code>set_sound_pan</code> function</h2>

> Set pan for a sound (0.5 is center)

Defined in raylib.h:

```c
void SetSoundPan(Sound sound, float pan) 
```

Python wrapper:

```python
def set_sound_pan(sound: Sound, pan: float) -> None
```

See also: <a href="#Sound">Sound</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="WaveCopy"><code>wave_copy</code> function</h2>

> Copy a wave to a new wave

Defined in raylib.h:

```c
Wave WaveCopy(Wave wave) 
```

Python wrapper:

```python
def wave_copy(wave: Wave) -> Wave
```

See also: <a href="#Wave">Wave</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="WaveCrop"><code>wave_crop</code> function</h2>

> Crop a wave to defined samples range

Defined in raylib.h:

```c
void WaveCrop(Wave * wave, int init_sample, int final_sample) 
```

Python wrapper:

```python
def wave_crop(wave: WavePtr, init_sample: int, final_sample: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="WaveFormat"><code>wave_format</code> function</h2>

> Convert wave data to desired format

Defined in raylib.h:

```c
void WaveFormat(Wave * wave, int sample_rate, int sample_size, int channels) 
```

Python wrapper:

```python
def wave_format(wave: WavePtr, sample_rate: int, sample_size: int, channels: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadWaveSamples"><code>load_wave_samples</code> function</h2>

> Load samples data from wave as a 32bit float data array

Defined in raylib.h:

```c
float LoadWaveSamples(Wave wave) 
```

Python wrapper:

```python
def load_wave_samples(wave: Wave) -> Union[Seq[float], FloatPtr]
```

See also: <a href="#Wave">Wave</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadWaveSamples"><code>unload_wave_samples</code> function</h2>

> Unload samples data loaded with LoadWaveSamples()

Defined in raylib.h:

```c
void UnloadWaveSamples(float samples) 
```

Python wrapper:

```python
def unload_wave_samples(samples: Union[Seq[float], FloatPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadMusicStream"><code>load_music_stream</code> function</h2>

> Load music stream from file

Defined in raylib.h:

```c
Music LoadMusicStream(char * file_name) 
```

Python wrapper:

```python
def load_music_stream(file_name: Union[str, CharPtr]) -> Music
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadMusicStreamFromMemory"><code>load_music_stream_from_memory</code> function</h2>

> Load music stream from data

Defined in raylib.h:

```c
Music LoadMusicStreamFromMemory(char * file_type, unsigned char * data, int data_size) 
```

Python wrapper:

```python
def load_music_stream_from_memory(file_type: Union[str, CharPtr], data: Union[Seq[int], UCharPtr], data_size: int) -> Music
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadMusicStream"><code>unload_music_stream</code> function</h2>

> Unload music stream

Defined in raylib.h:

```c
void UnloadMusicStream(Music music) 
```

Python wrapper:

```python
def unload_music_stream(music: Music) -> None
```

See also: <a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="PlayMusicStream"><code>play_music_stream</code> function</h2>

> Start music playing

Defined in raylib.h:

```c
void PlayMusicStream(Music music) 
```

Python wrapper:

```python
def play_music_stream(music: Music) -> None
```

See also: <a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsMusicStreamPlaying"><code>is_music_stream_playing</code> function</h2>

> Check if music is playing

Defined in raylib.h:

```c
bool IsMusicStreamPlaying(Music music) 
```

Python wrapper:

```python
def is_music_stream_playing(music: Music) -> bool
```

See also: <a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UpdateMusicStream"><code>update_music_stream</code> function</h2>

> Updates buffers for music streaming

Defined in raylib.h:

```c
void UpdateMusicStream(Music music) 
```

Python wrapper:

```python
def update_music_stream(music: Music) -> None
```

See also: <a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="StopMusicStream"><code>stop_music_stream</code> function</h2>

> Stop music playing

Defined in raylib.h:

```c
void StopMusicStream(Music music) 
```

Python wrapper:

```python
def stop_music_stream(music: Music) -> None
```

See also: <a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="PauseMusicStream"><code>pause_music_stream</code> function</h2>

> Pause music playing

Defined in raylib.h:

```c
void PauseMusicStream(Music music) 
```

Python wrapper:

```python
def pause_music_stream(music: Music) -> None
```

See also: <a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ResumeMusicStream"><code>resume_music_stream</code> function</h2>

> Resume playing paused music

Defined in raylib.h:

```c
void ResumeMusicStream(Music music) 
```

Python wrapper:

```python
def resume_music_stream(music: Music) -> None
```

See also: <a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SeekMusicStream"><code>seek_music_stream</code> function</h2>

> Seek music to a position (in seconds)

Defined in raylib.h:

```c
void SeekMusicStream(Music music, float position) 
```

Python wrapper:

```python
def seek_music_stream(music: Music, position: float) -> None
```

See also: <a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetMusicVolume"><code>set_music_volume</code> function</h2>

> Set volume for music (1.0 is max level)

Defined in raylib.h:

```c
void SetMusicVolume(Music music, float volume) 
```

Python wrapper:

```python
def set_music_volume(music: Music, volume: float) -> None
```

See also: <a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetMusicPitch"><code>set_music_pitch</code> function</h2>

> Set pitch for a music (1.0 is base level)

Defined in raylib.h:

```c
void SetMusicPitch(Music music, float pitch) 
```

Python wrapper:

```python
def set_music_pitch(music: Music, pitch: float) -> None
```

See also: <a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetMusicPan"><code>set_music_pan</code> function</h2>

> Set pan for a music (0.5 is center)

Defined in raylib.h:

```c
void SetMusicPan(Music music, float pan) 
```

Python wrapper:

```python
def set_music_pan(music: Music, pan: float) -> None
```

See also: <a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMusicTimeLength"><code>get_music_time_length</code> function</h2>

> Get music time length (in seconds)

Defined in raylib.h:

```c
float GetMusicTimeLength(Music music) 
```

Python wrapper:

```python
def get_music_time_length(music: Music) -> float
```

See also: <a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMusicTimePlayed"><code>get_music_time_played</code> function</h2>

> Get current music time played (in seconds)

Defined in raylib.h:

```c
float GetMusicTimePlayed(Music music) 
```

Python wrapper:

```python
def get_music_time_played(music: Music) -> float
```

See also: <a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadAudioStream"><code>load_audio_stream</code> function</h2>

> Load audio stream (to stream raw audio pcm data)

Defined in raylib.h:

```c
AudioStream LoadAudioStream(unsigned int sample_rate, unsigned int sample_size, unsigned int channels) 
```

Python wrapper:

```python
def load_audio_stream(sample_rate: int, sample_size: int, channels: int) -> AudioStream
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadAudioStream"><code>unload_audio_stream</code> function</h2>

> Unload audio stream and free memory

Defined in raylib.h:

```c
void UnloadAudioStream(AudioStream stream) 
```

Python wrapper:

```python
def unload_audio_stream(stream: AudioStream) -> None
```

See also: <a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UpdateAudioStream"><code>update_audio_stream</code> function</h2>

> Update audio stream buffers with data

Defined in raylib.h:

```c
void UpdateAudioStream(AudioStream stream, void data, int frame_count) 
```

Python wrapper:

```python
def update_audio_stream(stream: AudioStream, data: bytes, frame_count: int) -> None
```

See also: <a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsAudioStreamProcessed"><code>is_audio_stream_processed</code> function</h2>

> Check if any audio stream buffers requires refill

Defined in raylib.h:

```c
bool IsAudioStreamProcessed(AudioStream stream) 
```

Python wrapper:

```python
def is_audio_stream_processed(stream: AudioStream) -> bool
```

See also: <a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="PlayAudioStream"><code>play_audio_stream</code> function</h2>

> Play audio stream

Defined in raylib.h:

```c
void PlayAudioStream(AudioStream stream) 
```

Python wrapper:

```python
def play_audio_stream(stream: AudioStream) -> None
```

See also: <a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="PauseAudioStream"><code>pause_audio_stream</code> function</h2>

> Pause audio stream

Defined in raylib.h:

```c
void PauseAudioStream(AudioStream stream) 
```

Python wrapper:

```python
def pause_audio_stream(stream: AudioStream) -> None
```

See also: <a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ResumeAudioStream"><code>resume_audio_stream</code> function</h2>

> Resume audio stream

Defined in raylib.h:

```c
void ResumeAudioStream(AudioStream stream) 
```

Python wrapper:

```python
def resume_audio_stream(stream: AudioStream) -> None
```

See also: <a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsAudioStreamPlaying"><code>is_audio_stream_playing</code> function</h2>

> Check if audio stream is playing

Defined in raylib.h:

```c
bool IsAudioStreamPlaying(AudioStream stream) 
```

Python wrapper:

```python
def is_audio_stream_playing(stream: AudioStream) -> bool
```

See also: <a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="StopAudioStream"><code>stop_audio_stream</code> function</h2>

> Stop audio stream

Defined in raylib.h:

```c
void StopAudioStream(AudioStream stream) 
```

Python wrapper:

```python
def stop_audio_stream(stream: AudioStream) -> None
```

See also: <a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetAudioStreamVolume"><code>set_audio_stream_volume</code> function</h2>

> Set volume for audio stream (1.0 is max level)

Defined in raylib.h:

```c
void SetAudioStreamVolume(AudioStream stream, float volume) 
```

Python wrapper:

```python
def set_audio_stream_volume(stream: AudioStream, volume: float) -> None
```

See also: <a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetAudioStreamPitch"><code>set_audio_stream_pitch</code> function</h2>

> Set pitch for audio stream (1.0 is base level)

Defined in raylib.h:

```c
void SetAudioStreamPitch(AudioStream stream, float pitch) 
```

Python wrapper:

```python
def set_audio_stream_pitch(stream: AudioStream, pitch: float) -> None
```

See also: <a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetAudioStreamPan"><code>set_audio_stream_pan</code> function</h2>

> Set pan for audio stream (0.5 is centered)

Defined in raylib.h:

```c
void SetAudioStreamPan(AudioStream stream, float pan) 
```

Python wrapper:

```python
def set_audio_stream_pan(stream: AudioStream, pan: float) -> None
```

See also: <a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetAudioStreamBufferSizeDefault"><code>set_audio_stream_buffer_size_default</code> function</h2>

> Default size for new audio streams

Defined in raylib.h:

```c
void SetAudioStreamBufferSizeDefault(int size) 
```

Python wrapper:

```python
def set_audio_stream_buffer_size_default(size: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetAudioStreamCallback"><code>set_audio_stream_callback</code> function</h2>

> Audio thread callback to request new data

Defined in raylib.h:

```c
void SetAudioStreamCallback(AudioStream stream, AudioCallback callback) 
```

Python wrapper:

```python
def set_audio_stream_callback(stream: AudioStream, callback: AudioCallback) -> None
```

See also: <a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="AttachAudioStreamProcessor"><code>attach_audio_stream_processor</code> function</h2>

> 

Defined in raylib.h:

```c
void AttachAudioStreamProcessor(AudioStream stream, AudioCallback processor) 
```

Python wrapper:

```python
def attach_audio_stream_processor(stream: AudioStream, processor: AudioCallback) -> None
```

See also: <a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DetachAudioStreamProcessor"><code>detach_audio_stream_processor</code> function</h2>

> 

Defined in raylib.h:

```c
void DetachAudioStreamProcessor(AudioStream stream, AudioCallback processor) 
```

Python wrapper:

```python
def detach_audio_stream_processor(stream: AudioStream, processor: AudioCallback) -> None
```

See also: <a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Clamp"><code>clamp</code> function</h2>

> Clamp float value

Defined in raylib.h:

```c
float Clamp(float value, float min_, float max_) 
```

Python wrapper:

```python
def clamp(value: float, min_: float, max_: float) -> float
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Lerp"><code>lerp</code> function</h2>

> Calculate linear interpolation between two floats

Defined in raylib.h:

```c
float Lerp(float start, float end, float amount) 
```

Python wrapper:

```python
def lerp(start: float, end: float, amount: float) -> float
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Normalize"><code>normalize</code> function</h2>

> Calculate linear interpolation between two floats

Defined in raylib.h:

```c
float Normalize(float value, float start, float end) 
```

Python wrapper:

```python
def normalize(value: float, start: float, end: float) -> float
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Remap"><code>remap</code> function</h2>

> Remap input value within input range to output range

Defined in raylib.h:

```c
float Remap(float value, float input_start, float input_end, float output_start, float output_end) 
```

Python wrapper:

```python
def remap(value: float, input_start: float, input_end: float, output_start: float, output_end: float) -> float
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Wrap"><code>wrap</code> function</h2>

> Wrap input value from min to max

Defined in raylib.h:

```c
float Wrap(float value, float min_, float max_) 
```

Python wrapper:

```python
def wrap(value: float, min_: float, max_: float) -> float
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="FloatEquals"><code>float_equals</code> function</h2>

> Check whether two given floats are almost equal

Defined in raylib.h:

```c
int FloatEquals(float x, float y) 
```

Python wrapper:

```python
def float_equals(x: float, y: float) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Zero"><code>vector2zero</code> function</h2>

> Vector with components value 0.0f

Defined in raylib.h:

```c
Vector2 Vector2Zero() 
```

Python wrapper:

```python
def vector2zero() -> Vector2
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2One"><code>vector2one</code> function</h2>

> Vector with components value 1.0f

Defined in raylib.h:

```c
Vector2 Vector2One() 
```

Python wrapper:

```python
def vector2one() -> Vector2
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Add"><code>vector2add</code> function</h2>

> Add two vectors (v1 + v2)

Defined in raylib.h:

```c
Vector2 Vector2Add(Vector2 v1, Vector2 v2) 
```

Python wrapper:

```python
def vector2add(v1: Vector2, v2: Vector2) -> Vector2
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2AddValue"><code>vector2add_value</code> function</h2>

> Add vector and float value

Defined in raylib.h:

```c
Vector2 Vector2AddValue(Vector2 v, float add) 
```

Python wrapper:

```python
def vector2add_value(v: Vector2, add: float) -> Vector2
```

See also: <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Subtract"><code>vector2subtract</code> function</h2>

> Subtract two vectors (v1 - v2)

Defined in raylib.h:

```c
Vector2 Vector2Subtract(Vector2 v1, Vector2 v2) 
```

Python wrapper:

```python
def vector2subtract(v1: Vector2, v2: Vector2) -> Vector2
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2SubtractValue"><code>vector2subtract_value</code> function</h2>

> Subtract vector by float value

Defined in raylib.h:

```c
Vector2 Vector2SubtractValue(Vector2 v, float sub) 
```

Python wrapper:

```python
def vector2subtract_value(v: Vector2, sub: float) -> Vector2
```

See also: <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Length"><code>vector2length</code> function</h2>

> Calculate vector length

Defined in raylib.h:

```c
float Vector2Length(Vector2 v) 
```

Python wrapper:

```python
def vector2length(v: Vector2) -> float
```

See also: <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2LengthSqr"><code>vector2length_sqr</code> function</h2>

> Calculate vector square length

Defined in raylib.h:

```c
float Vector2LengthSqr(Vector2 v) 
```

Python wrapper:

```python
def vector2length_sqr(v: Vector2) -> float
```

See also: <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2DotProduct"><code>vector2dot_product</code> function</h2>

> Calculate two vectors dot product

Defined in raylib.h:

```c
float Vector2DotProduct(Vector2 v1, Vector2 v2) 
```

Python wrapper:

```python
def vector2dot_product(v1: Vector2, v2: Vector2) -> float
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Distance"><code>vector2distance</code> function</h2>

> Calculate distance between two vectors

Defined in raylib.h:

```c
float Vector2Distance(Vector2 v1, Vector2 v2) 
```

Python wrapper:

```python
def vector2distance(v1: Vector2, v2: Vector2) -> float
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2DistanceSqr"><code>vector2distance_sqr</code> function</h2>

> Calculate square distance between two vectors

Defined in raylib.h:

```c
float Vector2DistanceSqr(Vector2 v1, Vector2 v2) 
```

Python wrapper:

```python
def vector2distance_sqr(v1: Vector2, v2: Vector2) -> float
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Angle"><code>vector2angle</code> function</h2>

> Calculate angle from two vectors

Defined in raylib.h:

```c
float Vector2Angle(Vector2 v1, Vector2 v2) 
```

Python wrapper:

```python
def vector2angle(v1: Vector2, v2: Vector2) -> float
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Scale"><code>vector2scale</code> function</h2>

> Scale vector (multiply by value)

Defined in raylib.h:

```c
Vector2 Vector2Scale(Vector2 v, float scale) 
```

Python wrapper:

```python
def vector2scale(v: Vector2, scale: float) -> Vector2
```

See also: <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Multiply"><code>vector2multiply</code> function</h2>

> Multiply vector by vector

Defined in raylib.h:

```c
Vector2 Vector2Multiply(Vector2 v1, Vector2 v2) 
```

Python wrapper:

```python
def vector2multiply(v1: Vector2, v2: Vector2) -> Vector2
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Negate"><code>vector2negate</code> function</h2>

> Negate vector

Defined in raylib.h:

```c
Vector2 Vector2Negate(Vector2 v) 
```

Python wrapper:

```python
def vector2negate(v: Vector2) -> Vector2
```

See also: <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Divide"><code>vector2divide</code> function</h2>

> Divide vector by vector

Defined in raylib.h:

```c
Vector2 Vector2Divide(Vector2 v1, Vector2 v2) 
```

Python wrapper:

```python
def vector2divide(v1: Vector2, v2: Vector2) -> Vector2
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Normalize"><code>vector2normalize</code> function</h2>

> Normalize provided vector

Defined in raylib.h:

```c
Vector2 Vector2Normalize(Vector2 v) 
```

Python wrapper:

```python
def vector2normalize(v: Vector2) -> Vector2
```

See also: <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Transform"><code>vector2transform</code> function</h2>

> Transforms a Vector2 by a given Matrix

Defined in raylib.h:

```c
Vector2 Vector2Transform(Vector2 v, Matrix mat) 
```

Python wrapper:

```python
def vector2transform(v: Vector2, mat: Matrix) -> Vector2
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Lerp"><code>vector2lerp</code> function</h2>

> Calculate linear interpolation between two vectors

Defined in raylib.h:

```c
Vector2 Vector2Lerp(Vector2 v1, Vector2 v2, float amount) 
```

Python wrapper:

```python
def vector2lerp(v1: Vector2, v2: Vector2, amount: float) -> Vector2
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Reflect"><code>vector2reflect</code> function</h2>

> Calculate reflected vector to normal

Defined in raylib.h:

```c
Vector2 Vector2Reflect(Vector2 v1, Vector2 normal) 
```

Python wrapper:

```python
def vector2reflect(v1: Vector2, normal: Vector2) -> Vector2
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Rotate"><code>vector2rotate</code> function</h2>

> Rotate vector by angle

Defined in raylib.h:

```c
Vector2 Vector2Rotate(Vector2 v1, float angle) 
```

Python wrapper:

```python
def vector2rotate(v1: Vector2, angle: float) -> Vector2
```

See also: <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2MoveTowards"><code>vector2move_towards</code> function</h2>

> Move Vector towards target

Defined in raylib.h:

```c
Vector2 Vector2MoveTowards(Vector2 v1, Vector2 target, float max_distance) 
```

Python wrapper:

```python
def vector2move_towards(v1: Vector2, target: Vector2, max_distance: float) -> Vector2
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Invert"><code>vector2invert</code> function</h2>

> Invert the given vector

Defined in raylib.h:

```c
Vector2 Vector2Invert(Vector2 v) 
```

Python wrapper:

```python
def vector2invert(v: Vector2) -> Vector2
```

See also: <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Clamp"><code>vector2clamp</code> function</h2>

> Clamp the components of the vector between min and max values specified by the given vectors

Defined in raylib.h:

```c
Vector2 Vector2Clamp(Vector2 v, Vector2 min_, Vector2 max_) 
```

Python wrapper:

```python
def vector2clamp(v: Vector2, min_: Vector2, max_: Vector2) -> Vector2
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2ClampValue"><code>vector2clamp_value</code> function</h2>

> Clamp the magnitude of the vector between two min and max values

Defined in raylib.h:

```c
Vector2 Vector2ClampValue(Vector2 v, float min_, float max_) 
```

Python wrapper:

```python
def vector2clamp_value(v: Vector2, min_: float, max_: float) -> Vector2
```

See also: <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Equals"><code>vector2equals</code> function</h2>

> Check whether two given vectors are almost equal

Defined in raylib.h:

```c
int Vector2Equals(Vector2 p, Vector2 q) 
```

Python wrapper:

```python
def vector2equals(p: Vector2, q: Vector2) -> int
```

See also: <a href="#Vector2">Vector2</a>, <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Zero"><code>vector3zero</code> function</h2>

> Vector with components value 0.0f

Defined in raylib.h:

```c
Vector3 Vector3Zero() 
```

Python wrapper:

```python
def vector3zero() -> Vector3
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3One"><code>vector3one</code> function</h2>

> Vector with components value 1.0f

Defined in raylib.h:

```c
Vector3 Vector3One() 
```

Python wrapper:

```python
def vector3one() -> Vector3
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Add"><code>vector3add</code> function</h2>

> Add two vectors

Defined in raylib.h:

```c
Vector3 Vector3Add(Vector3 v1, Vector3 v2) 
```

Python wrapper:

```python
def vector3add(v1: Vector3, v2: Vector3) -> Vector3
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3AddValue"><code>vector3add_value</code> function</h2>

> Add vector and float value

Defined in raylib.h:

```c
Vector3 Vector3AddValue(Vector3 v, float add) 
```

Python wrapper:

```python
def vector3add_value(v: Vector3, add: float) -> Vector3
```

See also: <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Subtract"><code>vector3subtract</code> function</h2>

> Subtract two vectors

Defined in raylib.h:

```c
Vector3 Vector3Subtract(Vector3 v1, Vector3 v2) 
```

Python wrapper:

```python
def vector3subtract(v1: Vector3, v2: Vector3) -> Vector3
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3SubtractValue"><code>vector3subtract_value</code> function</h2>

> Subtract vector and float value

Defined in raylib.h:

```c
Vector3 Vector3SubtractValue(Vector3 v, float sub) 
```

Python wrapper:

```python
def vector3subtract_value(v: Vector3, sub: float) -> Vector3
```

See also: <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Scale"><code>vector3scale</code> function</h2>

> Multiply vector by scalar

Defined in raylib.h:

```c
Vector3 Vector3Scale(Vector3 v, float scalar) 
```

Python wrapper:

```python
def vector3scale(v: Vector3, scalar: float) -> Vector3
```

See also: <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Multiply"><code>vector3multiply</code> function</h2>

> Multiply vector by vector

Defined in raylib.h:

```c
Vector3 Vector3Multiply(Vector3 v1, Vector3 v2) 
```

Python wrapper:

```python
def vector3multiply(v1: Vector3, v2: Vector3) -> Vector3
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3CrossProduct"><code>vector3cross_product</code> function</h2>

> Calculate two vectors cross product

Defined in raylib.h:

```c
float Vector3CrossProduct(Vector3 v1, Vector3 v2) 
```

Python wrapper:

```python
def vector3cross_product(v1: Vector3, v2: Vector3) -> float
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Perpendicular"><code>vector3perpendicular</code> function</h2>

> Calculate one vector perpendicular vector

Defined in raylib.h:

```c
Vector3 Vector3Perpendicular(Vector3 v1) 
```

Python wrapper:

```python
def vector3perpendicular(v1: Vector3) -> Vector3
```

See also: <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Length"><code>vector3length</code> function</h2>

> Calculate vector length

Defined in raylib.h:

```c
float Vector3Length(Vector3 v1) 
```

Python wrapper:

```python
def vector3length(v1: Vector3) -> float
```

See also: <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3LengthSqr"><code>vector3length_sqr</code> function</h2>

> Calculate vector square length

Defined in raylib.h:

```c
float Vector3LengthSqr(Vector3 v1) 
```

Python wrapper:

```python
def vector3length_sqr(v1: Vector3) -> float
```

See also: <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3DotProduct"><code>vector3dot_product</code> function</h2>

> Calculate two vectors dot product

Defined in raylib.h:

```c
float Vector3DotProduct(Vector3 v1, Vector3 v2) 
```

Python wrapper:

```python
def vector3dot_product(v1: Vector3, v2: Vector3) -> float
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Distance"><code>vector3distance</code> function</h2>

> Calculate distance between two vectors

Defined in raylib.h:

```c
float Vector3Distance(Vector3 v1, Vector3 v2) 
```

Python wrapper:

```python
def vector3distance(v1: Vector3, v2: Vector3) -> float
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3DistanceSqr"><code>vector3distance_sqr</code> function</h2>

> Calculate square distance between two vectors

Defined in raylib.h:

```c
float Vector3DistanceSqr(Vector3 v1, Vector3 v2) 
```

Python wrapper:

```python
def vector3distance_sqr(v1: Vector3, v2: Vector3) -> float
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Angle"><code>vector3angle</code> function</h2>

> Calculate angle between two vectors

Defined in raylib.h:

```c
float Vector3Angle(Vector3 v1, Vector3 v2) 
```

Python wrapper:

```python
def vector3angle(v1: Vector3, v2: Vector3) -> float
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Negate"><code>vector3negate</code> function</h2>

> Negate provided vector (invert direction)

Defined in raylib.h:

```c
Vector3 Vector3Negate(Vector3 v) 
```

Python wrapper:

```python
def vector3negate(v: Vector3) -> Vector3
```

See also: <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Divide"><code>vector3divide</code> function</h2>

> Divide vector by vector

Defined in raylib.h:

```c
float Vector3Divide(Vector3 v1, Vector3 v2) 
```

Python wrapper:

```python
def vector3divide(v1: Vector3, v2: Vector3) -> float
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Normalize"><code>vector3normalize</code> function</h2>

> Normalize provided vector

Defined in raylib.h:

```c
Vector3 Vector3Normalize(Vector3 v) 
```

Python wrapper:

```python
def vector3normalize(v: Vector3) -> Vector3
```

See also: <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3OrthoNormalize"><code>vector3ortho_normalize</code> function</h2>

> Makes vectors normalized and orthogonal to each other

Defined in raylib.h:

```c
Vector3 Vector3OrthoNormalize(Vector3 * v1, Vector3 * v2) 
```

Python wrapper:

```python
def vector3ortho_normalize(v1: Vector3Ptr, v2: Vector3Ptr) -> Vector3
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Transform"><code>vector3transform</code> function</h2>

> Transforms a Vector3 by a given Matrix

Defined in raylib.h:

```c
Vector3 Vector3Transform(Vector3 v, Matrix mat) 
```

Python wrapper:

```python
def vector3transform(v: Vector3, mat: Matrix) -> Vector3
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3RotateByQuaternion"><code>vector3rotate_by_quaternion</code> function</h2>

> Transform a vector by quaternion rotation

Defined in raylib.h:

```c
Vector3 Vector3RotateByQuaternion(Vector3 v, Quaternion q) 
```

Python wrapper:

```python
def vector3rotate_by_quaternion(v: Vector3, q: Quaternion) -> Vector3
```

See also: <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3RotateByAxisAngle"><code>vector3rotate_by_axis_angle</code> function</h2>

> Rotates a vector around an axis

Defined in raylib.h:

```c
Vector3 Vector3RotateByAxisAngle(Vector3 v, Vector3 axis, float angle) 
```

Python wrapper:

```python
def vector3rotate_by_axis_angle(v: Vector3, axis: Vector3, angle: float) -> Vector3
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Lerp"><code>vector3lerp</code> function</h2>

> Calculate linear interpolation between two vectors

Defined in raylib.h:

```c
Vector3 Vector3Lerp(Vector3 v1, Vector3 v2, float amount) 
```

Python wrapper:

```python
def vector3lerp(v1: Vector3, v2: Vector3, amount: float) -> Vector3
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Reflect"><code>vector3reflect</code> function</h2>

> Calculate reflected vector to normal

Defined in raylib.h:

```c
Vector3 Vector3Reflect(Vector3 v, Vector3 normal) 
```

Python wrapper:

```python
def vector3reflect(v: Vector3, normal: Vector3) -> Vector3
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Min"><code>vector3min</code> function</h2>

> Get min value for each pair of components

Defined in raylib.h:

```c
Vector3 Vector3Min(Vector3 v1, Vector3 v2) 
```

Python wrapper:

```python
def vector3min(v1: Vector3, v2: Vector3) -> Vector3
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Max"><code>vector3max</code> function</h2>

> Get max value for each pair of components

Defined in raylib.h:

```c
Vector3 Vector3Max(Vector3 v1, Vector3 v2) 
```

Python wrapper:

```python
def vector3max(v1: Vector3, v2: Vector3) -> Vector3
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Barycenter"><code>vector3barycenter</code> function</h2>

> Compute barycenter coordinates (u, v, w) for point p with respect to triangle (a, b, c). Assumes P is on the plane of the triangle

Defined in raylib.h:

```c
Vector3 Vector3Barycenter(Vector3 p, Vector3 a, Vector3 b, Vector3 c) 
```

Python wrapper:

```python
def vector3barycenter(p: Vector3, a: Vector3, b: Vector3, c: Vector3) -> Vector3
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Unproject"><code>vector3unproject</code> function</h2>

> Projects a Vector3 from screen space into object space

Defined in raylib.h:

```c
Vector3 Vector3Unproject(Vector3 source, Matrix projection, Matrix view) 
```

Python wrapper:

```python
def vector3unproject(source: Vector3, projection: Matrix, view: Matrix) -> Vector3
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Matrix">Matrix</a>, <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3ToFloatV"><code>vector3to_float_v</code> function</h2>

> Get Vector3 as float array

Defined in raylib.h:

```c
float[3] Vector3ToFloatV(Vector3 v) 
```

Python wrapper:

```python
def vector3to_float_v(v: Vector3) -> Seq[float]
```

See also: <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Invert"><code>vector3invert</code> function</h2>

> Invert the given vector

Defined in raylib.h:

```c
Vector3 Vector3Invert(Vector3 v) 
```

Python wrapper:

```python
def vector3invert(v: Vector3) -> Vector3
```

See also: <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Clamp"><code>vector3clamp</code> function</h2>

> Clamp the components of the vector between min and max values specified by the given vectors

Defined in raylib.h:

```c
Vector3 Vector3Clamp(Vector3 v, Vector3 min_, Vector3 max_) 
```

Python wrapper:

```python
def vector3clamp(v: Vector3, min_: Vector3, max_: Vector3) -> Vector3
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3ClampValue"><code>vector3clamp_value</code> function</h2>

> Clamp the magnitude of the vector between two values

Defined in raylib.h:

```c
Vector3 Vector3ClampValue(Vector3 v, float min_, float max_) 
```

Python wrapper:

```python
def vector3clamp_value(v: Vector3, min_: float, max_: float) -> Vector3
```

See also: <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Equals"><code>vector3equals</code> function</h2>

> Check whether two given vectors are almost equal

Defined in raylib.h:

```c
int Vector3Equals(Vector3 v, float min_, float max_) 
```

Python wrapper:

```python
def vector3equals(v: Vector3, min_: float, max_: float) -> int
```

See also: <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Refract"><code>vector3refract</code> function</h2>

> Compute the direction of a refracted ray where v specifies the normalized direction of the incoming ray, n specifies the normalized normal vector of the interface of two optical media, and r specifies the ratio of the refractive index of the medium from where the ray comes to the refractive index of the medium on the other side of the surface

Defined in raylib.h:

```c
int Vector3Refract(Vector3 v, Vector3 n, float r) 
```

Python wrapper:

```python
def vector3refract(v: Vector3, n: Vector3, r: float) -> int
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixDeterminant"><code>matrix_determinant</code> function</h2>

> Compute matrix determinant

Defined in raylib.h:

```c
float MatrixDeterminant(Matrix mat) 
```

Python wrapper:

```python
def matrix_determinant(mat: Matrix) -> float
```

See also: <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixTrace"><code>matrix_trace</code> function</h2>

> Get the trace of the matrix (sum of the values along the diagonal)

Defined in raylib.h:

```c
float MatrixTrace(Matrix mat) 
```

Python wrapper:

```python
def matrix_trace(mat: Matrix) -> float
```

See also: <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixTranspose"><code>matrix_transpose</code> function</h2>

> Get the trace of the matrix (sum of the values along the diagonal)

Defined in raylib.h:

```c
Matrix MatrixTranspose(Matrix mat) 
```

Python wrapper:

```python
def matrix_transpose(mat: Matrix) -> Matrix
```

See also: <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixInvert"><code>matrix_invert</code> function</h2>

> Invert provided matrix

Defined in raylib.h:

```c
Matrix MatrixInvert(Matrix mat) 
```

Python wrapper:

```python
def matrix_invert(mat: Matrix) -> Matrix
```

See also: <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixIdentity"><code>matrix_identity</code> function</h2>

> Get identity matrix

Defined in raylib.h:

```c
Matrix MatrixIdentity() 
```

Python wrapper:

```python
def matrix_identity() -> Matrix
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixAdd"><code>matrix_add</code> function</h2>

> Add two matrices

Defined in raylib.h:

```c
Matrix MatrixAdd(Matrix left, Matrix right) 
```

Python wrapper:

```python
def matrix_add(left: Matrix, right: Matrix) -> Matrix
```

See also: <a href="#Matrix">Matrix</a>, <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixSubtract"><code>matrix_subtract</code> function</h2>

> Subtract two matrices (left - right)

Defined in raylib.h:

```c
Matrix MatrixSubtract(Matrix left, Matrix right) 
```

Python wrapper:

```python
def matrix_subtract(left: Matrix, right: Matrix) -> Matrix
```

See also: <a href="#Matrix">Matrix</a>, <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixMultiply"><code>matrix_multiply</code> function</h2>

> Get two matrix multiplication. When multiplying matrices... the order matters!

Defined in raylib.h:

```c
Matrix MatrixMultiply(Matrix left, Matrix right) 
```

Python wrapper:

```python
def matrix_multiply(left: Matrix, right: Matrix) -> Matrix
```

See also: <a href="#Matrix">Matrix</a>, <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixTranslate"><code>matrix_translate</code> function</h2>

> Get translation matrix

Defined in raylib.h:

```c
Matrix MatrixTranslate(float x, float y, float z) 
```

Python wrapper:

```python
def matrix_translate(x: float, y: float, z: float) -> Matrix
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixRotate"><code>matrix_rotate</code> function</h2>

> Create rotation matrix from axis and angle. Angle should be provided in radians

Defined in raylib.h:

```c
Matrix MatrixRotate(Vector3 axis, float angle) 
```

Python wrapper:

```python
def matrix_rotate(axis: Vector3, angle: float) -> Matrix
```

See also: <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixRotateX"><code>matrix_rotate_x</code> function</h2>

> Get x-rotation matrix. Angle must be provided in radians

Defined in raylib.h:

```c
Matrix MatrixRotateX(float angle) 
```

Python wrapper:

```python
def matrix_rotate_x(angle: float) -> Matrix
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixRotateY"><code>matrix_rotate_y</code> function</h2>

> Get y-rotation matrix. Angle must be provided in radians

Defined in raylib.h:

```c
Matrix MatrixRotateY(float angle) 
```

Python wrapper:

```python
def matrix_rotate_y(angle: float) -> Matrix
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixRotateZ"><code>matrix_rotate_z</code> function</h2>

> Get z-rotation matrix. Angle must be provided in radians

Defined in raylib.h:

```c
Matrix MatrixRotateZ(float angle) 
```

Python wrapper:

```python
def matrix_rotate_z(angle: float) -> Matrix
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixRotateXYZ"><code>matrix_rotate_xyz</code> function</h2>

> Get xyz-rotation matrix. Angle must be provided in radians

Defined in raylib.h:

```c
Matrix MatrixRotateXYZ(Vector3 angle) 
```

Python wrapper:

```python
def matrix_rotate_xyz(angle: Vector3) -> Matrix
```

See also: <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixRotateZYX"><code>matrix_rotate_zyx</code> function</h2>

> Get zyx-rotation matrix. Angle must be provided in radians

Defined in raylib.h:

```c
Matrix MatrixRotateZYX(Vector3 angle) 
```

Python wrapper:

```python
def matrix_rotate_zyx(angle: Vector3) -> Matrix
```

See also: <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixScale"><code>matrix_scale</code> function</h2>

> Get scaling matrix

Defined in raylib.h:

```c
Matrix MatrixScale(float x, float y, float z) 
```

Python wrapper:

```python
def matrix_scale(x: float, y: float, z: float) -> Matrix
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixFrustum"><code>matrix_frustum</code> function</h2>

> Get perspective projection matrix

Defined in raylib.h:

```c
Matrix MatrixFrustum(float left, float right, float bottom, float top, float near, float far) 
```

Python wrapper:

```python
def matrix_frustum(left: float, right: float, bottom: float, top: float, near: float, far: float) -> Matrix
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixPerspective"><code>matrix_perspective</code> function</h2>

> Get perspective projection matrix. Fovy angle must be provided in radians

Defined in raylib.h:

```c
Matrix MatrixPerspective(float fovy, float aspect, float near, float far) 
```

Python wrapper:

```python
def matrix_perspective(fovy: float, aspect: float, near: float, far: float) -> Matrix
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixOrtho"><code>matrix_ortho</code> function</h2>

> Get orthographic projection matrix

Defined in raylib.h:

```c
Matrix MatrixOrtho(float left, float right, float bottom, float top, float near, float far) 
```

Python wrapper:

```python
def matrix_ortho(left: float, right: float, bottom: float, top: float, near: float, far: float) -> Matrix
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixLookAt"><code>matrix_look_at</code> function</h2>

> Get camera look-at matrix (view matrix)

Defined in raylib.h:

```c
Matrix MatrixLookAt(Vector3 eye, Vector3 target, Vector3 up) 
```

Python wrapper:

```python
def matrix_look_at(eye: Vector3, target: Vector3, up: Vector3) -> Matrix
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixToFloatV"><code>matrix_to_float_v</code> function</h2>

> Get float array of matrix data

Defined in raylib.h:

```c
float[16] MatrixToFloatV(Matrix mat) 
```

Python wrapper:

```python
def matrix_to_float_v(mat: Matrix) -> Seq[float]
```

See also: <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionAdd"><code>quaternion_add</code> function</h2>

> Add two quaternions

Defined in raylib.h:

```c
Quaternion QuaternionAdd(Quaternion q1, Quaternion q2) 
```

Python wrapper:

```python
def quaternion_add(q1: Quaternion, q2: Quaternion) -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionAddValue"><code>quaternion_add_value</code> function</h2>

> Add quaternion and float value

Defined in raylib.h:

```c
Quaternion QuaternionAddValue(Quaternion q, float add) 
```

Python wrapper:

```python
def quaternion_add_value(q: Quaternion, add: float) -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionSubtract"><code>quaternion_subtract</code> function</h2>

> Subtract two quaternions

Defined in raylib.h:

```c
Quaternion QuaternionSubtract(Quaternion q1, Quaternion q2) 
```

Python wrapper:

```python
def quaternion_subtract(q1: Quaternion, q2: Quaternion) -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionSubtractValue"><code>quaternion_subtract_value</code> function</h2>

> Subtract quaternion and float value

Defined in raylib.h:

```c
Quaternion QuaternionSubtractValue(Quaternion q, float sub) 
```

Python wrapper:

```python
def quaternion_subtract_value(q: Quaternion, sub: float) -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionIdentity"><code>quaternion_identity</code> function</h2>

> Get identity quaternion

Defined in raylib.h:

```c
Quaternion QuaternionIdentity() 
```

Python wrapper:

```python
def quaternion_identity() -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionLength"><code>quaternion_length</code> function</h2>

> Computes the length of a quaternion

Defined in raylib.h:

```c
Quaternion QuaternionLength(Quaternion q) 
```

Python wrapper:

```python
def quaternion_length(q: Quaternion) -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionNormalize"><code>quaternion_normalize</code> function</h2>

> Normalize provided quaternion

Defined in raylib.h:

```c
Quaternion QuaternionNormalize(Quaternion q) 
```

Python wrapper:

```python
def quaternion_normalize(q: Quaternion) -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionInvert"><code>quaternion_invert</code> function</h2>

> Invert provided quaternion

Defined in raylib.h:

```c
Quaternion QuaternionInvert(Quaternion q) 
```

Python wrapper:

```python
def quaternion_invert(q: Quaternion) -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionMultiply"><code>quaternion_multiply</code> function</h2>

> Calculate two quaternion multiplication

Defined in raylib.h:

```c
Quaternion QuaternionMultiply(Quaternion q1, Quaternion q2) 
```

Python wrapper:

```python
def quaternion_multiply(q1: Quaternion, q2: Quaternion) -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionScale"><code>quaternion_scale</code> function</h2>

> Scale quaternion by float value

Defined in raylib.h:

```c
Quaternion QuaternionScale(Quaternion q1, float mul) 
```

Python wrapper:

```python
def quaternion_scale(q1: Quaternion, mul: float) -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionDivide"><code>quaternion_divide</code> function</h2>

> Divide two quaternions

Defined in raylib.h:

```c
Quaternion QuaternionDivide(Quaternion q1, Quaternion q2) 
```

Python wrapper:

```python
def quaternion_divide(q1: Quaternion, q2: Quaternion) -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionNlerp"><code>quaternion_nlerp</code> function</h2>

> Calculate slerp-optimized interpolation between two quaternions

Defined in raylib.h:

```c
Quaternion QuaternionNlerp(Quaternion q1, Quaternion q2, float amount) 
```

Python wrapper:

```python
def quaternion_nlerp(q1: Quaternion, q2: Quaternion, amount: float) -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionSlerp"><code>quaternion_slerp</code> function</h2>

> Calculates spherical linear interpolation between two quaternions

Defined in raylib.h:

```c
Quaternion QuaternionSlerp(Quaternion q1, Quaternion q2, float amount) 
```

Python wrapper:

```python
def quaternion_slerp(q1: Quaternion, q2: Quaternion, amount: float) -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionFromVector3ToVector3"><code>quaternion_from_vector3to_vector3</code> function</h2>

> Calculate quaternion based on the rotation from one vector to another

Defined in raylib.h:

```c
Quaternion QuaternionFromVector3ToVector3(Vector3 from_, Vector3 to) 
```

Python wrapper:

```python
def quaternion_from_vector3to_vector3(from_: Vector3, to: Vector3) -> Quaternion
```

See also: <a href="#Vector3">Vector3</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionToMatrix"><code>quaternion_to_matrix</code> function</h2>

> Get a quaternion for a given rotation matrix

Defined in raylib.h:

```c
Matrix QuaternionToMatrix(Quaternion q) 
```

Python wrapper:

```python
def quaternion_to_matrix(q: Quaternion) -> Matrix
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionFromMatrix"><code>quaternion_from_matrix</code> function</h2>

> Get a quaternion for a given rotation matrix

Defined in raylib.h:

```c
Quaternion QuaternionFromMatrix(Matrix mat) 
```

Python wrapper:

```python
def quaternion_from_matrix(mat: Matrix) -> Quaternion
```

See also: <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionFromAxisAngle"><code>quaternion_from_axis_angle</code> function</h2>

> Get rotation quaternion for an angle and axis. Angle must be provided in radians

Defined in raylib.h:

```c
Quaternion QuaternionFromAxisAngle(Vector3 mat, float angle) 
```

Python wrapper:

```python
def quaternion_from_axis_angle(mat: Vector3, angle: float) -> Quaternion
```

See also: <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionToAxisAngle"><code>quaternion_to_axis_angle</code> function</h2>

> Get the rotation angle and axis for a given quaternion

Defined in raylib.h:

```c
void QuaternionToAxisAngle(Quaternion q, Vector3 * out_axis, float out_angle) 
```

Python wrapper:

```python
def quaternion_to_axis_angle(q: Quaternion, out_axis: Vector3Ptr, out_angle: Union[Seq[float], FloatPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionFromEuler"><code>quaternion_from_euler</code> function</h2>

> Get the quaternion equivalent to Euler angles. Rotation order is ZYX

Defined in raylib.h:

```c
Quaternion QuaternionFromEuler(float pitch, float yaw, float roll) 
```

Python wrapper:

```python
def quaternion_from_euler(pitch: float, yaw: float, roll: float) -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionToEuler"><code>quaternion_to_euler</code> function</h2>

> Get the quaternion equivalent to Euler angles. Rotation order is ZYX

Defined in raylib.h:

```c
Vector3 QuaternionToEuler(Quaternion q) 
```

Python wrapper:

```python
def quaternion_to_euler(q: Quaternion) -> Vector3
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionTransform"><code>quaternion_transform</code> function</h2>

> Transform a quaternion given a transformation matrix

Defined in raylib.h:

```c
Quaternion QuaternionTransform(Quaternion q, Matrix mat) 
```

Python wrapper:

```python
def quaternion_transform(q: Quaternion, mat: Matrix) -> Quaternion
```

See also: <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionEquals"><code>quaternion_equals</code> function</h2>

> Check whether two given quaternions are almost equal

Defined in raylib.h:

```c
int QuaternionEquals(Quaternion p, Quaternion q) 
```

Python wrapper:

```python
def quaternion_equals(p: Quaternion, q: Quaternion) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlMatrixMode"><code>rl_matrix_mode</code> function</h2>

> Choose the current matrix to be transformed

Defined in raylib.h:

```c
void rlMatrixMode(int mode) 
```

Python wrapper:

```python
def rl_matrix_mode(mode: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlPushMatrix"><code>rl_push_matrix</code> function</h2>

> Push the current matrix to stack

Defined in raylib.h:

```c
void rlPushMatrix() 
```

Python wrapper:

```python
def rl_push_matrix() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlPopMatrix"><code>rl_pop_matrix</code> function</h2>

> Pop lattest inserted matrix from stack

Defined in raylib.h:

```c
void rlPopMatrix() 
```

Python wrapper:

```python
def rl_pop_matrix() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadIdentity"><code>rl_load_identity</code> function</h2>

> Reset current matrix to identity matrix

Defined in raylib.h:

```c
void rlLoadIdentity() 
```

Python wrapper:

```python
def rl_load_identity() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlTranslatef"><code>rl_translatef</code> function</h2>

> Multiply the current matrix by a translation matrix

Defined in raylib.h:

```c
void rlTranslatef(float x, float y, float z) 
```

Python wrapper:

```python
def rl_translatef(x: float, y: float, z: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlRotatef"><code>rl_rotatef</code> function</h2>

> Multiply the current matrix by a rotation matrix

Defined in raylib.h:

```c
void rlRotatef(float angle, float x, float y, float z) 
```

Python wrapper:

```python
def rl_rotatef(angle: float, x: float, y: float, z: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlScalef"><code>rl_scalef</code> function</h2>

> Multiply the current matrix by a scaling matrix

Defined in raylib.h:

```c
void rlScalef(float x, float y, float z) 
```

Python wrapper:

```python
def rl_scalef(x: float, y: float, z: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlMultMatrixf"><code>rl_mult_matrixf</code> function</h2>

> Multiply the current matrix by another matrix

Defined in raylib.h:

```c
void rlMultMatrixf(float matf) 
```

Python wrapper:

```python
def rl_mult_matrixf(matf: Union[Seq[float], FloatPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlFrustum"><code>rl_frustum</code> function</h2>

> 

Defined in raylib.h:

```c
void rlFrustum(double left, double right, double bottom, double top, double znear, double zfar) 
```

Python wrapper:

```python
def rl_frustum(left: float, right: float, bottom: float, top: float, znear: float, zfar: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlOrtho"><code>rl_ortho</code> function</h2>

> 

Defined in raylib.h:

```c
void rlOrtho(double left, double right, double bottom, double top, double znear, double zfar) 
```

Python wrapper:

```python
def rl_ortho(left: float, right: float, bottom: float, top: float, znear: float, zfar: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlViewport"><code>rl_viewport</code> function</h2>

> Set the viewport area

Defined in raylib.h:

```c
void rlViewport(int x, int y, int width, int height) 
```

Python wrapper:

```python
def rl_viewport(x: int, y: int, width: int, height: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlBegin"><code>rl_begin</code> function</h2>

> Initialize drawing mode (how to organize vertex)

Defined in raylib.h:

```c
void rlBegin(int mode) 
```

Python wrapper:

```python
def rl_begin(mode: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnd"><code>rl_end</code> function</h2>

> Finish vertex providing

Defined in raylib.h:

```c
void rlEnd() 
```

Python wrapper:

```python
def rl_end() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlVertex2i"><code>rl_vertex2i</code> function</h2>

> Define one vertex (position) - 2 int

Defined in raylib.h:

```c
void rlVertex2i(int x, int y) 
```

Python wrapper:

```python
def rl_vertex2i(x: int, y: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlVertex2f"><code>rl_vertex2f</code> function</h2>

> Define one vertex (position) - 2 float

Defined in raylib.h:

```c
void rlVertex2f(float x, float y) 
```

Python wrapper:

```python
def rl_vertex2f(x: float, y: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlVertex3f"><code>rl_vertex3f</code> function</h2>

> Define one vertex (position) - 3 float

Defined in raylib.h:

```c
void rlVertex3f(float x, float y, float z) 
```

Python wrapper:

```python
def rl_vertex3f(x: float, y: float, z: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlTexCoord2f"><code>rl_tex_coord2f</code> function</h2>

> Define one vertex (texture coordinate) - 2 float

Defined in raylib.h:

```c
void rlTexCoord2f(float x, float y) 
```

Python wrapper:

```python
def rl_tex_coord2f(x: float, y: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlNormal3f"><code>rl_normal3f</code> function</h2>

> Define one vertex (normal) - 3 float

Defined in raylib.h:

```c
void rlNormal3f(float x, float y, float z) 
```

Python wrapper:

```python
def rl_normal3f(x: float, y: float, z: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlColor4ub"><code>rl_color4ub</code> function</h2>

> Define one vertex (color) - 4 byte

Defined in raylib.h:

```c
void rlColor4ub(unsigned char r, unsigned char g, unsigned char b, unsigned char a) 
```

Python wrapper:

```python
def rl_color4ub(r: int, g: int, b: int, a: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlColor3f"><code>rl_color3f</code> function</h2>

> Define one vertex (color) - 3 float

Defined in raylib.h:

```c
void rlColor3f(float x, float y, float z) 
```

Python wrapper:

```python
def rl_color3f(x: float, y: float, z: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlColor4f"><code>rl_color4f</code> function</h2>

> Define one vertex (color) - 4 float

Defined in raylib.h:

```c
void rlColor4f(float x, float y, float z, float w) 
```

Python wrapper:

```python
def rl_color4f(x: float, y: float, z: float, w: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableVertexArray"><code>rl_enable_vertex_array</code> function</h2>

> Enable vertex array (VAO, if supported)

Defined in raylib.h:

```c
bool rlEnableVertexArray(unsigned int vao_id) 
```

Python wrapper:

```python
def rl_enable_vertex_array(vao_id: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableVertexArray"><code>rl_disable_vertex_array</code> function</h2>

> Disable vertex array (VAO, if supported)

Defined in raylib.h:

```c
void rlDisableVertexArray() 
```

Python wrapper:

```python
def rl_disable_vertex_array() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableVertexBuffer"><code>rl_enable_vertex_buffer</code> function</h2>

> Enable vertex buffer (VBO)

Defined in raylib.h:

```c
void rlEnableVertexBuffer(unsigned int id) 
```

Python wrapper:

```python
def rl_enable_vertex_buffer(id: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableVertexBuffer"><code>rl_disable_vertex_buffer</code> function</h2>

> Disable vertex buffer (VBO)

Defined in raylib.h:

```c
void rlDisableVertexBuffer() 
```

Python wrapper:

```python
def rl_disable_vertex_buffer() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableVertexBufferElement"><code>rl_enable_vertex_buffer_element</code> function</h2>

> Enable vertex buffer element (VBO element)

Defined in raylib.h:

```c
void rlEnableVertexBufferElement(unsigned int id) 
```

Python wrapper:

```python
def rl_enable_vertex_buffer_element(id: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableVertexBufferElement"><code>rl_disable_vertex_buffer_element</code> function</h2>

> Disable vertex buffer element (VBO element)

Defined in raylib.h:

```c
void rlDisableVertexBufferElement() 
```

Python wrapper:

```python
def rl_disable_vertex_buffer_element() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableVertexAttribute"><code>rl_enable_vertex_attribute</code> function</h2>

> Enable vertex attribute index

Defined in raylib.h:

```c
void rlEnableVertexAttribute(unsigned int index) 
```

Python wrapper:

```python
def rl_enable_vertex_attribute(index: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableVertexAttribute"><code>rl_disable_vertex_attribute</code> function</h2>

> Disable vertex attribute index

Defined in raylib.h:

```c
void rlDisableVertexAttribute(unsigned int index) 
```

Python wrapper:

```python
def rl_disable_vertex_attribute(index: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlActiveTextureSlot"><code>rl_active_texture_slot</code> function</h2>

> Select and active a texture slot

Defined in raylib.h:

```c
void rlActiveTextureSlot(int slot) 
```

Python wrapper:

```python
def rl_active_texture_slot(slot: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableTexture"><code>rl_enable_texture</code> function</h2>

> Enable texture

Defined in raylib.h:

```c
void rlEnableTexture(unsigned int id) 
```

Python wrapper:

```python
def rl_enable_texture(id: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableTexture"><code>rl_disable_texture</code> function</h2>

> Disable texture

Defined in raylib.h:

```c
void rlDisableTexture() 
```

Python wrapper:

```python
def rl_disable_texture() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableTextureCubemap"><code>rl_enable_texture_cubemap</code> function</h2>

> Enable texture cubemap

Defined in raylib.h:

```c
void rlEnableTextureCubemap(unsigned int id) 
```

Python wrapper:

```python
def rl_enable_texture_cubemap(id: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableTextureCubemap"><code>rl_disable_texture_cubemap</code> function</h2>

> Disable texture cubemap

Defined in raylib.h:

```c
void rlDisableTextureCubemap() 
```

Python wrapper:

```python
def rl_disable_texture_cubemap() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlTextureParameters"><code>rl_texture_parameters</code> function</h2>

> Set texture parameters (filter, wrap)

Defined in raylib.h:

```c
void rlTextureParameters(unsigned int id, int param, int value) 
```

Python wrapper:

```python
def rl_texture_parameters(id: int, param: int, value: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableShader"><code>rl_enable_shader</code> function</h2>

> Enable shader program

Defined in raylib.h:

```c
void rlEnableShader(unsigned int id) 
```

Python wrapper:

```python
def rl_enable_shader(id: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableShader"><code>rl_disable_shader</code> function</h2>

> Disable shader program

Defined in raylib.h:

```c
void rlDisableShader() 
```

Python wrapper:

```python
def rl_disable_shader() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableFramebuffer"><code>rl_enable_framebuffer</code> function</h2>

> Enable render texture (fbo)

Defined in raylib.h:

```c
void rlEnableFramebuffer(unsigned int id) 
```

Python wrapper:

```python
def rl_enable_framebuffer(id: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableFramebuffer"><code>rl_disable_framebuffer</code> function</h2>

> Disable render texture (fbo), return to default framebuffer

Defined in raylib.h:

```c
void rlDisableFramebuffer() 
```

Python wrapper:

```python
def rl_disable_framebuffer() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlActiveDrawBuffers"><code>rl_active_draw_buffers</code> function</h2>

> Activate multiple draw color buffers

Defined in raylib.h:

```c
void rlActiveDrawBuffers(int count) 
```

Python wrapper:

```python
def rl_active_draw_buffers(count: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableColorBlend"><code>rl_enable_color_blend</code> function</h2>

> Enable color blending

Defined in raylib.h:

```c
void rlEnableColorBlend() 
```

Python wrapper:

```python
def rl_enable_color_blend() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableColorBlend"><code>rl_disable_color_blend</code> function</h2>

> Disable color blending

Defined in raylib.h:

```c
void rlDisableColorBlend() 
```

Python wrapper:

```python
def rl_disable_color_blend() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableDepthTest"><code>rl_enable_depth_test</code> function</h2>

> Enable depth test

Defined in raylib.h:

```c
void rlEnableDepthTest() 
```

Python wrapper:

```python
def rl_enable_depth_test() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableDepthTest"><code>rl_disable_depth_test</code> function</h2>

> Disable depth test

Defined in raylib.h:

```c
void rlDisableDepthTest() 
```

Python wrapper:

```python
def rl_disable_depth_test() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableDepthMask"><code>rl_enable_depth_mask</code> function</h2>

> Enable depth write

Defined in raylib.h:

```c
void rlEnableDepthMask() 
```

Python wrapper:

```python
def rl_enable_depth_mask() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableDepthMask"><code>rl_disable_depth_mask</code> function</h2>

> Disable depth write

Defined in raylib.h:

```c
void rlDisableDepthMask() 
```

Python wrapper:

```python
def rl_disable_depth_mask() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableBackfaceCulling"><code>rl_enable_backface_culling</code> function</h2>

> Enable backface culling

Defined in raylib.h:

```c
void rlEnableBackfaceCulling() 
```

Python wrapper:

```python
def rl_enable_backface_culling() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableBackfaceCulling"><code>rl_disable_backface_culling</code> function</h2>

> Disable backface culling

Defined in raylib.h:

```c
void rlDisableBackfaceCulling() 
```

Python wrapper:

```python
def rl_disable_backface_culling() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableScissorTest"><code>rl_enable_scissor_test</code> function</h2>

> Enable scissor test

Defined in raylib.h:

```c
void rlEnableScissorTest() 
```

Python wrapper:

```python
def rl_enable_scissor_test() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableScissorTest"><code>rl_disable_scissor_test</code> function</h2>

> Disable scissor test

Defined in raylib.h:

```c
void rlDisableScissorTest() 
```

Python wrapper:

```python
def rl_disable_scissor_test() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlScissor"><code>rl_scissor</code> function</h2>

> Scissor test

Defined in raylib.h:

```c
void rlScissor(int x, int y, int width, int height) 
```

Python wrapper:

```python
def rl_scissor(x: int, y: int, width: int, height: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableWireMode"><code>rl_enable_wire_mode</code> function</h2>

> Enable wire mode

Defined in raylib.h:

```c
void rlEnableWireMode() 
```

Python wrapper:

```python
def rl_enable_wire_mode() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableWireMode"><code>rl_disable_wire_mode</code> function</h2>

> Disable wire mode

Defined in raylib.h:

```c
void rlDisableWireMode() 
```

Python wrapper:

```python
def rl_disable_wire_mode() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetLineWidth"><code>rl_set_line_width</code> function</h2>

> Set the line drawing width

Defined in raylib.h:

```c
void rlSetLineWidth(float width) 
```

Python wrapper:

```python
def rl_set_line_width(width: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetLineWidth"><code>rl_get_line_width</code> function</h2>

> Get the line drawing width

Defined in raylib.h:

```c
float rlGetLineWidth() 
```

Python wrapper:

```python
def rl_get_line_width() -> float
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableSmoothLines"><code>rl_enable_smooth_lines</code> function</h2>

> Enable line aliasing

Defined in raylib.h:

```c
void rlEnableSmoothLines() 
```

Python wrapper:

```python
def rl_enable_smooth_lines() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableSmoothLines"><code>rl_disable_smooth_lines</code> function</h2>

> Disable line aliasing

Defined in raylib.h:

```c
void rlDisableSmoothLines() 
```

Python wrapper:

```python
def rl_disable_smooth_lines() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableStereoRender"><code>rl_enable_stereo_render</code> function</h2>

> Enable stereo rendering

Defined in raylib.h:

```c
void rlEnableStereoRender() 
```

Python wrapper:

```python
def rl_enable_stereo_render() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableStereoRender"><code>rl_disable_stereo_render</code> function</h2>

> Disable stereo rendering

Defined in raylib.h:

```c
void rlDisableStereoRender() 
```

Python wrapper:

```python
def rl_disable_stereo_render() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlIsStereoRenderEnabled"><code>rl_is_stereo_render_enabled</code> function</h2>

> Check if stereo render is enabled

Defined in raylib.h:

```c
bool rlIsStereoRenderEnabled() 
```

Python wrapper:

```python
def rl_is_stereo_render_enabled() -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlClearColor"><code>rl_clear_color</code> function</h2>

> Clear color buffer with color

Defined in raylib.h:

```c
void rlClearColor(unsigned char r, unsigned char g, unsigned char b, unsigned char a) 
```

Python wrapper:

```python
def rl_clear_color(r: int, g: int, b: int, a: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlClearScreenBuffers"><code>rl_clear_screen_buffers</code> function</h2>

> Clear used screen buffers (color and depth)

Defined in raylib.h:

```c
void rlClearScreenBuffers() 
```

Python wrapper:

```python
def rl_clear_screen_buffers() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlCheckErrors"><code>rl_check_errors</code> function</h2>

> Check and log OpenGL error codes

Defined in raylib.h:

```c
void rlCheckErrors() 
```

Python wrapper:

```python
def rl_check_errors() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetBlendMode"><code>rl_set_blend_mode</code> function</h2>

> Set blending mode

Defined in raylib.h:

```c
void rlSetBlendMode(int mode) 
```

Python wrapper:

```python
def rl_set_blend_mode(mode: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetBlendFactors"><code>rl_set_blend_factors</code> function</h2>

> Set blending mode factor and equation (using OpenGL factors)

Defined in raylib.h:

```c
void rlSetBlendFactors(int gl_src_factor, int gl_dst_factor, int gl_equation) 
```

Python wrapper:

```python
def rl_set_blend_factors(gl_src_factor: int, gl_dst_factor: int, gl_equation: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlglInit"><code>rlgl_init</code> function</h2>

> Initialize rlgl (buffers, shaders, textures, states)

Defined in raylib.h:

```c
void rlglInit(int width, int height) 
```

Python wrapper:

```python
def rlgl_init(width: int, height: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlglClose"><code>rlgl_close</code> function</h2>

> De-inititialize rlgl (buffers, shaders, textures)

Defined in raylib.h:

```c
void rlglClose() 
```

Python wrapper:

```python
def rlgl_close() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadExtensions"><code>rl_load_extensions</code> function</h2>

> Load OpenGL extensions (loader function required)

Defined in raylib.h:

```c
void rlLoadExtensions(void loader) 
```

Python wrapper:

```python
def rl_load_extensions(loader: bytes) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetVersion"><code>rl_get_version</code> function</h2>

> Get current OpenGL version

Defined in raylib.h:

```c
int rlGetVersion() 
```

Python wrapper:

```python
def rl_get_version() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetFramebufferWidth"><code>rl_set_framebuffer_width</code> function</h2>

> Set current framebuffer width

Defined in raylib.h:

```c
void rlSetFramebufferWidth(int width) 
```

Python wrapper:

```python
def rl_set_framebuffer_width(width: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetFramebufferWidth"><code>rl_get_framebuffer_width</code> function</h2>

> Get default framebuffer width

Defined in raylib.h:

```c
int rlGetFramebufferWidth() 
```

Python wrapper:

```python
def rl_get_framebuffer_width() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetFramebufferHeight"><code>rl_set_framebuffer_height</code> function</h2>

> Set current framebuffer height

Defined in raylib.h:

```c
void rlSetFramebufferHeight(int height) 
```

Python wrapper:

```python
def rl_set_framebuffer_height(height: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetFramebufferHeight"><code>rl_get_framebuffer_height</code> function</h2>

> Get default framebuffer height

Defined in raylib.h:

```c
int rlGetFramebufferHeight() 
```

Python wrapper:

```python
def rl_get_framebuffer_height() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetTextureIdDefault"><code>rl_get_texture_id_default</code> function</h2>

> Get default texture id

Defined in raylib.h:

```c
unsigned int rlGetTextureIdDefault() 
```

Python wrapper:

```python
def rl_get_texture_id_default() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetShaderIdDefault"><code>rl_get_shader_id_default</code> function</h2>

> Get default shader id

Defined in raylib.h:

```c
unsigned int rlGetShaderIdDefault() 
```

Python wrapper:

```python
def rl_get_shader_id_default() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetShaderLocsDefault"><code>rl_get_shader_locs_default</code> function</h2>

> Get default shader locations

Defined in raylib.h:

```c
int rlGetShaderLocsDefault() 
```

Python wrapper:

```python
def rl_get_shader_locs_default() -> Union[Seq[int], IntPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadRenderBatch"><code>rl_load_render_batch</code> function</h2>

> Load a render batch system

Defined in raylib.h:

```c
rlRenderBatch rlLoadRenderBatch(int num_buffers, int buffer_elements) 
```

Python wrapper:

```python
def rl_load_render_batch(num_buffers: int, buffer_elements: int) -> rlRenderBatch
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlUnloadRenderBatch"><code>rl_unload_render_batch</code> function</h2>

> Unload render batch system

Defined in raylib.h:

```c
void rlUnloadRenderBatch(rlRenderBatch batch) 
```

Python wrapper:

```python
def rl_unload_render_batch(batch: rlRenderBatch) -> None
```

See also: <a href="#rlRenderBatch">rlRenderBatch</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDrawRenderBatch"><code>rl_draw_render_batch</code> function</h2>

> Draw render batch data (Update->Draw->Reset)

Defined in raylib.h:

```c
void rlDrawRenderBatch(rlRenderBatch * batch) 
```

Python wrapper:

```python
def rl_draw_render_batch(batch: rlRenderBatchPtr) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetRenderBatchActive"><code>rl_set_render_batch_active</code> function</h2>

> Set the active render batch for rlgl (NULL for default internal)

Defined in raylib.h:

```c
void rlSetRenderBatchActive(rlRenderBatch * batch) 
```

Python wrapper:

```python
def rl_set_render_batch_active(batch: rlRenderBatchPtr) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDrawRenderBatchActive"><code>rl_draw_render_batch_active</code> function</h2>

> Update and draw internal render batch

Defined in raylib.h:

```c
void rlDrawRenderBatchActive() 
```

Python wrapper:

```python
def rl_draw_render_batch_active() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlCheckRenderBatchLimit"><code>rl_check_render_batch_limit</code> function</h2>

> Check internal buffer overflow for a given number of vertex

Defined in raylib.h:

```c
bool rlCheckRenderBatchLimit(int v_count) 
```

Python wrapper:

```python
def rl_check_render_batch_limit(v_count: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetTexture"><code>rl_set_texture</code> function</h2>

> Set current texture for render batch and check buffers limits

Defined in raylib.h:

```c
void rlSetTexture(unsigned int id) 
```

Python wrapper:

```python
def rl_set_texture(id: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadVertexArray"><code>rl_load_vertex_array</code> function</h2>

> Load vertex array (vao) if supported

Defined in raylib.h:

```c
unsigned int rlLoadVertexArray() 
```

Python wrapper:

```python
def rl_load_vertex_array() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadVertexBuffer"><code>rl_load_vertex_buffer</code> function</h2>

> Load a vertex buffer attribute

Defined in raylib.h:

```c
unsigned int rlLoadVertexBuffer(void buffer, int size, bool dynamic) 
```

Python wrapper:

```python
def rl_load_vertex_buffer(buffer: bytes, size: int, dynamic: bool) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadVertexBufferElement"><code>rl_load_vertex_buffer_element</code> function</h2>

> Load a new attributes element buffer

Defined in raylib.h:

```c
unsigned int rlLoadVertexBufferElement(void buffer, int size, bool dynamic) 
```

Python wrapper:

```python
def rl_load_vertex_buffer_element(buffer: bytes, size: int, dynamic: bool) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlUpdateVertexBuffer"><code>rl_update_vertex_buffer</code> function</h2>

> Update GPU buffer with new data

Defined in raylib.h:

```c
void rlUpdateVertexBuffer(unsigned int buffer_id, void data, int data_size, int offset) 
```

Python wrapper:

```python
def rl_update_vertex_buffer(buffer_id: int, data: bytes, data_size: int, offset: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlUpdateVertexBufferElements"><code>rl_update_vertex_buffer_elements</code> function</h2>

> Update vertex buffer elements with new data

Defined in raylib.h:

```c
void rlUpdateVertexBufferElements(unsigned int id, void data, int data_size, int offset) 
```

Python wrapper:

```python
def rl_update_vertex_buffer_elements(id: int, data: bytes, data_size: int, offset: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlUnloadVertexArray"><code>rl_unload_vertex_array</code> function</h2>

> 

Defined in raylib.h:

```c
void rlUnloadVertexArray(unsigned int vao_id) 
```

Python wrapper:

```python
def rl_unload_vertex_array(vao_id: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlUnloadVertexBuffer"><code>rl_unload_vertex_buffer</code> function</h2>

> 

Defined in raylib.h:

```c
void rlUnloadVertexBuffer(unsigned int vbo_id) 
```

Python wrapper:

```python
def rl_unload_vertex_buffer(vbo_id: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetVertexAttribute"><code>rl_set_vertex_attribute</code> function</h2>

> 

Defined in raylib.h:

```c
void rlSetVertexAttribute(unsigned int index, int comp_size, int type, bool normalized, int stride, void pointer) 
```

Python wrapper:

```python
def rl_set_vertex_attribute(index: int, comp_size: int, type: int, normalized: bool, stride: int, pointer: bytes) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetVertexAttributeDivisor"><code>rl_set_vertex_attribute_divisor</code> function</h2>

> 

Defined in raylib.h:

```c
void rlSetVertexAttributeDivisor(unsigned int index, int divisor) 
```

Python wrapper:

```python
def rl_set_vertex_attribute_divisor(index: int, divisor: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetVertexAttributeDefault"><code>rl_set_vertex_attribute_default</code> function</h2>

> Set vertex attribute default value

Defined in raylib.h:

```c
void rlSetVertexAttributeDefault(int loc_index, void value, int attrib_type, int count) 
```

Python wrapper:

```python
def rl_set_vertex_attribute_default(loc_index: int, value: bytes, attrib_type: int, count: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDrawVertexArray"><code>rl_draw_vertex_array</code> function</h2>

> 

Defined in raylib.h:

```c
void rlDrawVertexArray(int offset, int count) 
```

Python wrapper:

```python
def rl_draw_vertex_array(offset: int, count: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDrawVertexArrayElements"><code>rl_draw_vertex_array_elements</code> function</h2>

> 

Defined in raylib.h:

```c
void rlDrawVertexArrayElements(int offset, int count, void buffer) 
```

Python wrapper:

```python
def rl_draw_vertex_array_elements(offset: int, count: int, buffer: bytes) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDrawVertexArrayInstanced"><code>rl_draw_vertex_array_instanced</code> function</h2>

> 

Defined in raylib.h:

```c
void rlDrawVertexArrayInstanced(int offset, int count, int instances) 
```

Python wrapper:

```python
def rl_draw_vertex_array_instanced(offset: int, count: int, instances: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDrawVertexArrayElementsInstanced"><code>rl_draw_vertex_array_elements_instanced</code> function</h2>

> 

Defined in raylib.h:

```c
void rlDrawVertexArrayElementsInstanced(int offset, int count, void buffer, int instances) 
```

Python wrapper:

```python
def rl_draw_vertex_array_elements_instanced(offset: int, count: int, buffer: bytes, instances: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadTexture"><code>rl_load_texture</code> function</h2>

> Load texture in GPU

Defined in raylib.h:

```c
unsigned int rlLoadTexture(void data, int width, int height, int format, int mipmap_count) 
```

Python wrapper:

```python
def rl_load_texture(data: bytes, width: int, height: int, format: int, mipmap_count: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadTextureDepth"><code>rl_load_texture_depth</code> function</h2>

> Load depth texture/renderbuffer (to be attached to fbo)

Defined in raylib.h:

```c
unsigned int rlLoadTextureDepth(int width, int height, bool use_render_buffer) 
```

Python wrapper:

```python
def rl_load_texture_depth(width: int, height: int, use_render_buffer: bool) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadTextureCubemap"><code>rl_load_texture_cubemap</code> function</h2>

> Load texture cubemap

Defined in raylib.h:

```c
unsigned int rlLoadTextureCubemap(void data, int size, int format) 
```

Python wrapper:

```python
def rl_load_texture_cubemap(data: bytes, size: int, format: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlUpdateTexture"><code>rl_update_texture</code> function</h2>

> Update GPU texture with new data

Defined in raylib.h:

```c
void rlUpdateTexture(unsigned int id, int offset_x, int offset_y, int width, int height, int format, void data) 
```

Python wrapper:

```python
def rl_update_texture(id: int, offset_x: int, offset_y: int, width: int, height: int, format: int, data: bytes) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetGlTextureFormats"><code>rl_get_gl_texture_formats</code> function</h2>

> Get OpenGL internal formats

Defined in raylib.h:

```c
void rlGetGlTextureFormats(int format, unsigned int gl_internal_format, unsigned int gl_format, unsigned int gl_type) 
```

Python wrapper:

```python
def rl_get_gl_texture_formats(format: int, gl_internal_format: Union[Seq[int], UIntPtr], gl_format: Union[Seq[int], UIntPtr], gl_type: Union[Seq[int], UIntPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetPixelFormatName"><code>rl_get_pixel_format_name</code> function</h2>

> Get name string for pixel format

Defined in raylib.h:

```c
char * rlGetPixelFormatName(unsigned int format) 
```

Python wrapper:

```python
def rl_get_pixel_format_name(format: int) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlUnloadTexture"><code>rl_unload_texture</code> function</h2>

> Unload texture from GPU memory

Defined in raylib.h:

```c
void rlUnloadTexture(unsigned int id) 
```

Python wrapper:

```python
def rl_unload_texture(id: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGenTextureMipmaps"><code>rl_gen_texture_mipmaps</code> function</h2>

> Generate mipmap data for selected texture

Defined in raylib.h:

```c
void rlGenTextureMipmaps(unsigned int id, int width, int height, int format, int mipmaps) 
```

Python wrapper:

```python
def rl_gen_texture_mipmaps(id: int, width: int, height: int, format: int, mipmaps: Union[Seq[int], IntPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlReadTexturePixels"><code>rl_read_texture_pixels</code> function</h2>

> Read texture pixel data

Defined in raylib.h:

```c
void rlReadTexturePixels(unsigned int id, int width, int height, int format) 
```

Python wrapper:

```python
def rl_read_texture_pixels(id: int, width: int, height: int, format: int) -> bytes
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlReadScreenPixels"><code>rl_read_screen_pixels</code> function</h2>

> Read screen pixel data (color buffer)

Defined in raylib.h:

```c
unsigned char * rlReadScreenPixels(int width, int height) 
```

Python wrapper:

```python
def rl_read_screen_pixels(width: int, height: int) -> Union[Seq[int], UCharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadFramebuffer"><code>rl_load_framebuffer</code> function</h2>

> Load an empty framebuffer

Defined in raylib.h:

```c
unsigned int rlLoadFramebuffer(int width, int height) 
```

Python wrapper:

```python
def rl_load_framebuffer(width: int, height: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlFramebufferAttach"><code>rl_framebuffer_attach</code> function</h2>

> Attach texture/renderbuffer to a framebuffer

Defined in raylib.h:

```c
void rlFramebufferAttach(unsigned int fbo_id, unsigned int tex_id, int attach_type, int tex_type, int mip_level) 
```

Python wrapper:

```python
def rl_framebuffer_attach(fbo_id: int, tex_id: int, attach_type: int, tex_type: int, mip_level: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlFramebufferComplete"><code>rl_framebuffer_complete</code> function</h2>

> Verify framebuffer is complete

Defined in raylib.h:

```c
bool rlFramebufferComplete(unsigned int id) 
```

Python wrapper:

```python
def rl_framebuffer_complete(id: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlUnloadFramebuffer"><code>rl_unload_framebuffer</code> function</h2>

> Delete framebuffer from GPU

Defined in raylib.h:

```c
void rlUnloadFramebuffer(unsigned int id) 
```

Python wrapper:

```python
def rl_unload_framebuffer(id: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadShaderCode"><code>rl_load_shader_code</code> function</h2>

> Load shader from code strings

Defined in raylib.h:

```c
unsigned int rlLoadShaderCode(char * vs_code, char * fs_code) 
```

Python wrapper:

```python
def rl_load_shader_code(vs_code: Union[str, CharPtr], fs_code: Union[str, CharPtr]) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlCompileShader"><code>rl_compile_shader</code> function</h2>

> Compile custom shader and return shader id (type: RL_VERTEX_SHADER, RL_FRAGMENT_SHADER, RL_COMPUTE_SHADER)

Defined in raylib.h:

```c
unsigned int rlCompileShader(char * shader_code, int type) 
```

Python wrapper:

```python
def rl_compile_shader(shader_code: Union[str, CharPtr], type: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadShaderProgram"><code>rl_load_shader_program</code> function</h2>

> Load custom shader program

Defined in raylib.h:

```c
unsigned int rlLoadShaderProgram(unsigned int v_shader_id, unsigned int f_shader_id) 
```

Python wrapper:

```python
def rl_load_shader_program(v_shader_id: int, f_shader_id: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlUnloadShaderProgram"><code>rl_unload_shader_program</code> function</h2>

> Unload shader program

Defined in raylib.h:

```c
void rlUnloadShaderProgram(unsigned int id) 
```

Python wrapper:

```python
def rl_unload_shader_program(id: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetLocationUniform"><code>rl_get_location_uniform</code> function</h2>

> Get shader location uniform

Defined in raylib.h:

```c
int rlGetLocationUniform(unsigned int shader_id, char * uniform_name) 
```

Python wrapper:

```python
def rl_get_location_uniform(shader_id: int, uniform_name: Union[str, CharPtr]) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetLocationAttrib"><code>rl_get_location_attrib</code> function</h2>

> Get shader location attribute

Defined in raylib.h:

```c
int rlGetLocationAttrib(unsigned int shader_id, char * attrib_name) 
```

Python wrapper:

```python
def rl_get_location_attrib(shader_id: int, attrib_name: Union[str, CharPtr]) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetUniform"><code>rl_set_uniform</code> function</h2>

> Set shader value uniform

Defined in raylib.h:

```c
void rlSetUniform(int loc_index, void value, int uniform_type, int count) 
```

Python wrapper:

```python
def rl_set_uniform(loc_index: int, value: bytes, uniform_type: int, count: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetUniformMatrix"><code>rl_set_uniform_matrix</code> function</h2>

> Set shader value matrix

Defined in raylib.h:

```c
void rlSetUniformMatrix(int loc_index, Matrix mat) 
```

Python wrapper:

```python
def rl_set_uniform_matrix(loc_index: int, mat: Matrix) -> None
```

See also: <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetUniformSampler"><code>rl_set_uniform_sampler</code> function</h2>

> Set shader value sampler

Defined in raylib.h:

```c
void rlSetUniformSampler(int loc_index, unsigned int texture_id) 
```

Python wrapper:

```python
def rl_set_uniform_sampler(loc_index: int, texture_id: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetShader"><code>rl_set_shader</code> function</h2>

> Set shader currently active (id and locations)

Defined in raylib.h:

```c
void rlSetShader(unsigned int id, int locs) 
```

Python wrapper:

```python
def rl_set_shader(id: int, locs: Union[Seq[int], IntPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadComputeShaderProgram"><code>rl_load_compute_shader_program</code> function</h2>

> Load compute shader program

Defined in raylib.h:

```c
unsigned int rlLoadComputeShaderProgram(unsigned int shader_id) 
```

Python wrapper:

```python
def rl_load_compute_shader_program(shader_id: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlComputeShaderDispatch"><code>rl_compute_shader_dispatch</code> function</h2>

> Dispatch compute shader (equivalent to *draw* for graphics pilepine)

Defined in raylib.h:

```c
void rlComputeShaderDispatch(unsigned int group_x, unsigned int group_y, unsigned int group_z) 
```

Python wrapper:

```python
def rl_compute_shader_dispatch(group_x: int, group_y: int, group_z: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadShaderBuffer"><code>rl_load_shader_buffer</code> function</h2>

> Load shader storage buffer object (SSBO)

Defined in raylib.h:

```c
unsigned int rlLoadShaderBuffer(unsigned long long * size, void data, int usage_hint) 
```

Python wrapper:

```python
def rl_load_shader_buffer(size: int, data: bytes, usage_hint: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlUnloadShaderBuffer"><code>rl_unload_shader_buffer</code> function</h2>

> Unload shader storage buffer object (SSBO)

Defined in raylib.h:

```c
void rlUnloadShaderBuffer(unsigned int ssbo_id) 
```

Python wrapper:

```python
def rl_unload_shader_buffer(ssbo_id: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlUpdateShaderBufferElements"><code>rl_update_shader_buffer_elements</code> function</h2>

> Update SSBO buffer data

Defined in raylib.h:

```c
void rlUpdateShaderBufferElements(unsigned int id, void data, unsigned long long * data_size, unsigned long long * offset) 
```

Python wrapper:

```python
def rl_update_shader_buffer_elements(id: int, data: bytes, data_size: int, offset: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetShaderBufferSize"><code>rl_get_shader_buffer_size</code> function</h2>

> Get SSBO buffer size

Defined in raylib.h:

```c
unsigned long long * rlGetShaderBufferSize(unsigned int id) 
```

Python wrapper:

```python
def rl_get_shader_buffer_size(id: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlReadShaderBufferElements"><code>rl_read_shader_buffer_elements</code> function</h2>

> Bind SSBO buffer

Defined in raylib.h:

```c
void rlReadShaderBufferElements(unsigned int id, void dest, unsigned long long * count, unsigned long long * offset) 
```

Python wrapper:

```python
def rl_read_shader_buffer_elements(id: int, dest: bytes, count: int, offset: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlBindShaderBuffer"><code>rl_bind_shader_buffer</code> function</h2>

> Copy SSBO buffer data

Defined in raylib.h:

```c
void rlBindShaderBuffer(unsigned int id, unsigned int index) 
```

Python wrapper:

```python
def rl_bind_shader_buffer(id: int, index: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlCopyBuffersElements"><code>rl_copy_buffers_elements</code> function</h2>

> Copy SSBO buffer data

Defined in raylib.h:

```c
void rlCopyBuffersElements(unsigned int dest_id, unsigned int src_id, unsigned long long * dest_offset, unsigned long long * src_offset, unsigned long long * count) 
```

Python wrapper:

```python
def rl_copy_buffers_elements(dest_id: int, src_id: int, dest_offset: int, src_offset: int, count: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlBindImageTexture"><code>rl_bind_image_texture</code> function</h2>

> Bind image texture

Defined in raylib.h:

```c
void rlBindImageTexture(unsigned int id, unsigned int index, unsigned int format, int readonly) 
```

Python wrapper:

```python
def rl_bind_image_texture(id: int, index: int, format: int, readonly: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetMatrixModelview"><code>rl_get_matrix_modelview</code> function</h2>

> Get internal modelview matrix

Defined in raylib.h:

```c
Matrix rlGetMatrixModelview() 
```

Python wrapper:

```python
def rl_get_matrix_modelview() -> Matrix
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetMatrixProjection"><code>rl_get_matrix_projection</code> function</h2>

> Get internal projection matrix

Defined in raylib.h:

```c
Matrix rlGetMatrixProjection() 
```

Python wrapper:

```python
def rl_get_matrix_projection() -> Matrix
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetMatrixTransform"><code>rl_get_matrix_transform</code> function</h2>

> Get internal accumulated transform matrix

Defined in raylib.h:

```c
Matrix rlGetMatrixTransform() 
```

Python wrapper:

```python
def rl_get_matrix_transform() -> Matrix
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetMatrixProjectionStereo"><code>rl_get_matrix_projection_stereo</code> function</h2>

> Get internal projection matrix for stereo render (selected eye)

Defined in raylib.h:

```c
Matrix rlGetMatrixProjectionStereo(int eye) 
```

Python wrapper:

```python
def rl_get_matrix_projection_stereo(eye: int) -> Matrix
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetMatrixViewOffsetStereo"><code>rl_get_matrix_view_offset_stereo</code> function</h2>

> Get internal view offset matrix for stereo render (selected eye)

Defined in raylib.h:

```c
Matrix rlGetMatrixViewOffsetStereo(int eye) 
```

Python wrapper:

```python
def rl_get_matrix_view_offset_stereo(eye: int) -> Matrix
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetMatrixProjection"><code>rl_set_matrix_projection</code> function</h2>

> Set a custom projection matrix (replaces internal projection matrix)

Defined in raylib.h:

```c
void rlSetMatrixProjection(Matrix proj) 
```

Python wrapper:

```python
def rl_set_matrix_projection(proj: Matrix) -> None
```

See also: <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetMatrixModelview"><code>rl_set_matrix_modelview</code> function</h2>

> Set a custom modelview matrix (replaces internal modelview matrix)

Defined in raylib.h:

```c
void rlSetMatrixModelview(Matrix view) 
```

Python wrapper:

```python
def rl_set_matrix_modelview(view: Matrix) -> None
```

See also: <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetMatrixProjectionStereo"><code>rl_set_matrix_projection_stereo</code> function</h2>

> Set eyes projection matrices for stereo rendering

Defined in raylib.h:

```c
void rlSetMatrixProjectionStereo(Matrix right, Matrix left) 
```

Python wrapper:

```python
def rl_set_matrix_projection_stereo(right: Matrix, left: Matrix) -> None
```

See also: <a href="#Matrix">Matrix</a>, <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetMatrixViewOffsetStereo"><code>rl_set_matrix_view_offset_stereo</code> function</h2>

> Set eyes view offsets matrices for stereo rendering

Defined in raylib.h:

```c
void rlSetMatrixViewOffsetStereo(Matrix right, Matrix left) 
```

Python wrapper:

```python
def rl_set_matrix_view_offset_stereo(right: Matrix, left: Matrix) -> None
```

See also: <a href="#Matrix">Matrix</a>, <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadDrawCube"><code>rl_load_draw_cube</code> function</h2>

> Load and draw a cube

Defined in raylib.h:

```c
void rlLoadDrawCube() 
```

Python wrapper:

```python
def rl_load_draw_cube() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadDrawQuad"><code>rl_load_draw_quad</code> function</h2>

> Load and draw a quad

Defined in raylib.h:

```c
void rlLoadDrawQuad() 
```

Python wrapper:

```python
def rl_load_draw_quad() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
