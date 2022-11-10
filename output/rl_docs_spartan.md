# Raylib-py API reference

This is an API reference documentation generated for Raylib 4.2.

<h2 id="toc">Table of Contents</h2>

- <a href="#structs">Structures</a>
- <a href="#aliases">Aliases</a>
- <a href="#enums">Enumerations</a>
- <a href="#defines">Constants</a>
- <a href="#funcs">Functions</a>
- <a href="#callbacks">Callbacks</a>
- <a href="#contexts">Context Managers</a>

---

## Helper Types

Many types are aliases to ctypes types. Types suffixed with `Ptr` are pointer types.

To create array types, you can multiply the type to the array length, like below:

```python

# Create an array of 4 floats:
arr = (Float * 4)(1.0, 3.5, -10.0, 0.0)

```

Raylib wrapped structures provide the `array_of()` classmethod for this same purpose:

```python

# Create an array of Vector2:
v_arr = Vector2.array_of([vec1, vec2, vec3, vec4])

```

Alias | Ctypes type
------|-------
`Bool` | `c_bool`
`BoolPtr` | `POINTER(c_bool)`
`Byte` | `c_byte`
`BytePtr` | `POINTER(c_byte)`
`Char` | `c_char`
`CharPtr` | `POINTER(c_char)`
`Short` | `c_short`
`ShortPtr` | `POINTER(c_short)`
`Int` | `c_long`
`IntPtr` | `POINTER(c_long)`
`Long` | `c_long`
`LongPtr` | `POINTER(c_long)`
`LongLong` | `c_longlong`
`LongLongPtr` | `POINTER(c_longlong)`
`UChar` | `c_ubyte`
`UCharPtr` | `POINTER(c_ubyte)`
`UByte` | `c_ubyte`
`UBytePtr` | `POINTER(c_ubyte)`
`UShort` | `c_ushort`
`UShortPtr` | `POINTER(c_ushort)`
`UInt` | `c_ulong`
`UIntPtr` | `POINTER(c_ulong)`
`ULong` | `c_ulong`
`ULongPtr` | `POINTER(c_ulong)`
`ULongLong` | `c_ulonglong`
`ULongLongPtr` | `POINTER(c_ulonglong)`
`Float` | `c_float`
`FloatPtr` | `POINTER(c_float)`
`Double` | `c_double`
`DoublePtr` | `POINTER(c_double)`
`VoidPtr` | `c_void_p`
`VoidPtrPtr` | `POINTER(c_void_p)`
`CharPtr` | `c_char_p`
`CharPtrPtr` | `POINTER(c_char_p)`

<h2 id="structs">Structures</h2>

Item|Item|Item|Item|Item
--------|--------|--------|--------|--------
<a href="#AudioStream">AudioStream</a> | <a href="#BoneInfo">BoneInfo</a> | <a href="#BoundingBox">BoundingBox</a> | <a href="#Camera2D">Camera2D</a> | <a href="#Camera3D">Camera3D</a>
<a href="#Color">Color</a> | <a href="#FilePathList">FilePathList</a> | <a href="#Font">Font</a> | <a href="#GlyphInfo">GlyphInfo</a> | <a href="#Image">Image</a>
<a href="#Material">Material</a> | <a href="#MaterialMap">MaterialMap</a> | <a href="#Matrix">Matrix</a> | <a href="#Matrix">Matrix</a> | <a href="#Mesh">Mesh</a>
<a href="#Model">Model</a> | <a href="#ModelAnimation">ModelAnimation</a> | <a href="#Music">Music</a> | <a href="#NPatchInfo">NPatchInfo</a> | <a href="#Ray">Ray</a>
<a href="#RayCollision">RayCollision</a> | <a href="#Rectangle">Rectangle</a> | <a href="#RenderTexture">RenderTexture</a> | <a href="#Shader">Shader</a> | <a href="#Sound">Sound</a>
<a href="#Texture">Texture</a> | <a href="#Transform">Transform</a> | <a href="#Vector2">Vector2</a> | <a href="#Vector3">Vector3</a> | <a href="#Vector4">Vector4</a>
<a href="#VrDeviceInfo">VrDeviceInfo</a> | <a href="#VrStereoConfig">VrStereoConfig</a> | <a href="#Wave">Wave</a> | <a href="#rlDrawCall">rlDrawCall</a> | <a href="#rlRenderBatch">rlRenderBatch</a>
<a href="#rlVertexBuffer">rlVertexBuffer</a>

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
`.Length` | <a href="#Vector2Length"><code>Vector2Length</code></a>
`.LengthSqr` | <a href="#Vector2LengthSqr"><code>Vector2LengthSqr</code></a>

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, vector2_sequence)` | *n/a*
*classmethod* | `.One()` | <a href="#Vector2One"><code>Vector2One</code></a>
*method* | `.DotProduct(self, v2: 'Vector2')` | <a href="#Vector2DotProduct"><code>Vector2DotProduct</code></a>
*method* | `.Distance(self, v2: 'Vector2')` | <a href="#Vector2Distance"><code>Vector2Distance</code></a>
*method* | `.DistanceSqr(self, v2: 'Vector2')` | <a href="#Vector2DistanceSqr"><code>Vector2DistanceSqr</code></a>
*method* | `.Angle(self, v2: 'Vector2')` | <a href="#Vector2Angle"><code>Vector2Angle</code></a>
*method* | `.Normalize(self)` | <a href="#Vector2Normalize"><code>Vector2Normalize</code></a>
*method* | `.Transform(self, mat: 'Matrix')` | <a href="#Vector2Transform"><code>Vector2Transform</code></a>
*method* | `.Lerp(self, v2: 'Vector2', amount: 'float')` | <a href="#Vector2Lerp"><code>Vector2Lerp</code></a>
*method* | `.Reflect(self, normal: 'Vector2')` | <a href="#Vector2Reflect"><code>Vector2Reflect</code></a>
*method* | `.Rotate(self, angle: 'float')` | <a href="#Vector2Rotate"><code>Vector2Rotate</code></a>
*method* | `.MoveTowards(self, target: 'Vector2', maxDistance: 'float')` | <a href="#Vector2MoveTowards"><code>Vector2MoveTowards</code></a>
*method* | `.Clamp(self, min_: 'Vector2', max_: 'Vector2')` | <a href="#Vector2Clamp"><code>Vector2Clamp</code></a>
*method* | `.ClampValue(self, min_: 'float', max_: 'float')` | <a href="#Vector2ClampValue"><code>Vector2ClampValue</code></a>



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
`.Length` | <a href="#Vector3Length"><code>Vector3Length</code></a>
`.LengthSqr` | <a href="#Vector3LengthSqr"><code>Vector3LengthSqr</code></a>

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, vector3_sequence)` | *n/a*
*classmethod* | `.One()` | <a href="#Vector3One"><code>Vector3One</code></a>
*method* | `.CrossProduct(self, v2: 'Vector3')` | <a href="#Vector3CrossProduct"><code>Vector3CrossProduct</code></a>
*method* | `.Perpendicular(self)` | <a href="#Vector3Perpendicular"><code>Vector3Perpendicular</code></a>
*method* | `.DotProduct(self, v2: 'Vector3')` | <a href="#Vector3DotProduct"><code>Vector3DotProduct</code></a>
*method* | `.Distance(self, v2: 'Vector3')` | <a href="#Vector3Distance"><code>Vector3Distance</code></a>
*method* | `.DistanceSqr(self, v2: 'Vector3')` | <a href="#Vector3DistanceSqr"><code>Vector3DistanceSqr</code></a>
*method* | `.Angle(self, v2: 'Vector3')` | <a href="#Vector3Angle"><code>Vector3Angle</code></a>
*method* | `.Normalize(self)` | <a href="#Vector3Normalize"><code>Vector3Normalize</code></a>
*method* | `.OrthoNormalize(self, v2: 'Vector3Ptr')` | <a href="#Vector3OrthoNormalize"><code>Vector3OrthoNormalize</code></a>
*method* | `.Transform(self, mat: 'Matrix')` | <a href="#Vector3Transform"><code>Vector3Transform</code></a>
*method* | `.RotateByQuaternion(self, q: 'Quaternion')` | <a href="#Vector3RotateByQuaternion"><code>Vector3RotateByQuaternion</code></a>
*method* | `.RotateByAxisAngle(self, axis: 'Vector3', angle: 'float')` | <a href="#Vector3RotateByAxisAngle"><code>Vector3RotateByAxisAngle</code></a>
*method* | `.Lerp(self, v2: 'Vector3', amount: 'float')` | <a href="#Vector3Lerp"><code>Vector3Lerp</code></a>
*method* | `.Reflect(self, normal: 'Vector3')` | <a href="#Vector3Reflect"><code>Vector3Reflect</code></a>
*method* | `.Min(self, v2: 'Vector3')` | <a href="#Vector3Min"><code>Vector3Min</code></a>
*method* | `.Max(self, v2: 'Vector3')` | <a href="#Vector3Max"><code>Vector3Max</code></a>
*method* | `.Barycenter(self, a: 'Vector3', b: 'Vector3', c: 'Vector3')` | <a href="#Vector3Barycenter"><code>Vector3Barycenter</code></a>
*method* | `.Unproject(self, projection: 'Matrix', view: 'Matrix')` | <a href="#Vector3Unproject"><code>Vector3Unproject</code></a>
*method* | `.ToFloatV(self)` | <a href="#Vector3ToFloatV"><code>Vector3ToFloatV</code></a>
*method* | `.Clamp(self, min_: 'Vector3', max_: 'Vector3')` | <a href="#Vector3Clamp"><code>Vector3Clamp</code></a>
*method* | `.ClampValue(self, min_: 'float', max_: 'float')` | <a href="#Vector3ClampValue"><code>Vector3ClampValue</code></a>
*method* | `.Refract(self, n: 'Vector3', r: 'float')` | <a href="#Vector3Refract"><code>Vector3Refract</code></a>



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
*classmethod* | `.Identity()` | <a href="#MatrixIdentity"><code>MatrixIdentity</code></a>
*classmethod* | `.Translate(cls, x: 'float', y: 'float', z: 'float')` | <a href="#MatrixTranslate"><code>MatrixTranslate</code></a>
*classmethod* | `.Rotate(cls, axis: 'Vector3', angle: 'float')` | <a href="#MatrixRotate"><code>MatrixRotate</code></a>
*classmethod* | `.RotateX(cls, angle: 'float')` | <a href="#MatrixRotateX"><code>MatrixRotateX</code></a>
*classmethod* | `.RotateY(cls, angle: 'float')` | <a href="#MatrixRotateY"><code>MatrixRotateY</code></a>
*classmethod* | `.RotateZ(cls, angle: 'float')` | <a href="#MatrixRotateZ"><code>MatrixRotateZ</code></a>
*classmethod* | `.RotateXYZ(cls, angle: 'Vector3')` | <a href="#MatrixRotateXYZ"><code>MatrixRotateXYZ</code></a>
*classmethod* | `.RotateZYX(cls, angle: 'Vector3')` | <a href="#MatrixRotateZYX"><code>MatrixRotateZYX</code></a>
*classmethod* | `.Scale(cls, x: 'float', y: 'float', z: 'float')` | <a href="#MatrixScale"><code>MatrixScale</code></a>
*classmethod* | `.Frustum(cls, left: 'float', right: 'float', bottom: 'float', top: 'float', near: 'float', far: 'float')` | <a href="#MatrixFrustum"><code>MatrixFrustum</code></a>
*classmethod* | `.Perspective(cls, fovy: 'float', aspect: 'float', near: 'float', far: 'float')` | <a href="#MatrixPerspective"><code>MatrixPerspective</code></a>
*classmethod* | `.Ortho(cls, left: 'float', right: 'float', bottom: 'float', top: 'float', near: 'float', far: 'float')` | <a href="#MatrixOrtho"><code>MatrixOrtho</code></a>
*classmethod* | `.LookAt(cls, eye: 'Vector3', target: 'Vector3', up: 'Vector3')` | <a href="#MatrixLookAt"><code>MatrixLookAt</code></a>
*method* | `.Determinant(self)` | <a href="#MatrixDeterminant"><code>MatrixDeterminant</code></a>
*method* | `.Trace(self)` | <a href="#MatrixTrace"><code>MatrixTrace</code></a>
*method* | `.Transpose(self)` | <a href="#MatrixTranspose"><code>MatrixTranspose</code></a>
*method* | `.Invert(self)` | <a href="#MatrixInvert"><code>MatrixInvert</code></a>



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
*method* | `.Fade(self, alpha: 'float')` | <a href="#Fade"><code>Fade</code></a>
*method* | `.ToInt(self)` | <a href="#ColorToInt"><code>ColorToInt</code></a>
*method* | `.ToHSV(self)` | <a href="#ColorToHSV"><code>ColorToHSV</code></a>
*method* | `.FromHSV(self, saturation: 'float', value: 'float')` | <a href="#ColorFromHSV"><code>ColorFromHSV</code></a>
*method* | `.Alpha(self, alpha: 'float')` | <a href="#ColorAlpha"><code>ColorAlpha</code></a>
*method* | `.AlphaBlend(self, src: 'Color', tint: 'Color')` | <a href="#ColorAlphaBlend"><code>ColorAlphaBlend</code></a>



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
*staticmethod* | `.UnloadColors(colors: 'ColorPtr')` | <a href="#UnloadImageColors"><code>UnloadImageColors</code></a>
*staticmethod* | `.UnloadPalette(colors: 'ColorPtr')` | <a href="#UnloadImagePalette"><code>UnloadImagePalette</code></a>
*classmethod* | `.array_of(cls, image_sequence)` | *n/a*
*classmethod* | `.Load(cls, fileName: 'Union[str, CharPtr]')` | <a href="#LoadImage"><code>LoadImage</code></a>
*classmethod* | `.LoadRaw(cls, fileName: 'Union[str, CharPtr]', width: 'int', height: 'int', format: 'int', headerSize: 'int')` | <a href="#LoadImageRaw"><code>LoadImageRaw</code></a>
*classmethod* | `.LoadAnim(cls, fileName: 'Union[str, CharPtr]', frames: 'Union[Seq[int], IntPtr]')` | <a href="#LoadImageAnim"><code>LoadImageAnim</code></a>
*classmethod* | `.LoadFromMemory(cls, fileType: 'Union[str, CharPtr]', fileData: 'Union[Seq[int], UCharPtr]', dataSize: 'int')` | <a href="#LoadImageFromMemory"><code>LoadImageFromMemory</code></a>
*classmethod* | `.LoadFromTexture(cls, texture: 'Texture2D')` | <a href="#LoadImageFromTexture"><code>LoadImageFromTexture</code></a>
*classmethod* | `.LoadFromScreen()` | <a href="#LoadImageFromScreen"><code>LoadImageFromScreen</code></a>
*classmethod* | `.GenColor(cls, width: 'int', height: 'int', color: 'Color')` | <a href="#GenImageColor"><code>GenImageColor</code></a>
*classmethod* | `.GenGradientH(cls, width: 'int', height: 'int', left: 'Color', right: 'Color')` | <a href="#GenImageGradientH"><code>GenImageGradientH</code></a>
*classmethod* | `.GenGradientV(cls, width: 'int', height: 'int', top: 'Color', bottom: 'Color')` | <a href="#GenImageGradientV"><code>GenImageGradientV</code></a>
*classmethod* | `.GenGradientRadial(cls, width: 'int', height: 'int', density: 'float', inner: 'Color', outer: 'Color')` | <a href="#GenImageGradientRadial"><code>GenImageGradientRadial</code></a>
*classmethod* | `.GenChecked(cls, width: 'int', height: 'int', checksX: 'int', checksY: 'int', col1: 'Color', col2: 'Color')` | <a href="#GenImageChecked"><code>GenImageChecked</code></a>
*classmethod* | `.GenWhiteNoise(cls, width: 'int', height: 'int', factor: 'float')` | <a href="#GenImageWhiteNoise"><code>GenImageWhiteNoise</code></a>
*classmethod* | `.GenCellular(cls, width: 'int', height: 'int', tileSize: 'int')` | <a href="#GenImageCellular"><code>GenImageCellular</code></a>
*classmethod* | `.FromImage(cls, image: 'Image', rec: 'Rectangle')` | <a href="#ImageFromImage"><code>ImageFromImage</code></a>
*classmethod* | `.Text(cls, text: 'Union[str, CharPtr]', fontSize: 'int', color: 'Color')` | <a href="#ImageText"><code>ImageText</code></a>
*classmethod* | `.TextEx(cls, font: 'Font', text: 'Union[str, CharPtr]', fontSize: 'float', spacing: 'float', tint: 'Color')` | <a href="#ImageTextEx"><code>ImageTextEx</code></a>
*method* | `.Unload(self)` | <a href="#UnloadImage"><code>UnloadImage</code></a>
*method* | `.Export(self, fileName: 'Union[str, CharPtr]')` | <a href="#ExportImage"><code>ExportImage</code></a>
*method* | `.ExportAsCode(self, fileName: 'Union[str, CharPtr]')` | <a href="#ExportImageAsCode"><code>ExportImageAsCode</code></a>
*method* | `.Copy(self)` | <a href="#ImageCopy"><code>ImageCopy</code></a>
*method* | `.Format(self, newFormat: 'int')` | <a href="#ImageFormat"><code>ImageFormat</code></a>
*method* | `.ToPOT(self, fill: 'Color')` | <a href="#ImageToPOT"><code>ImageToPOT</code></a>
*method* | `.Crop(self, crop: 'Rectangle')` | <a href="#ImageCrop"><code>ImageCrop</code></a>
*method* | `.AlphaCrop(self, threshold: 'float')` | <a href="#ImageAlphaCrop"><code>ImageAlphaCrop</code></a>
*method* | `.AlphaClear(self, color: 'Color', threshold: 'float')` | <a href="#ImageAlphaClear"><code>ImageAlphaClear</code></a>
*method* | `.AlphaMask(self, alphaMask: 'Image')` | <a href="#ImageAlphaMask"><code>ImageAlphaMask</code></a>
*method* | `.AlphaPremultiply(self)` | <a href="#ImageAlphaPremultiply"><code>ImageAlphaPremultiply</code></a>
*method* | `.Resize(self, newWidth: 'int', newHeight: 'int')` | <a href="#ImageResize"><code>ImageResize</code></a>
*method* | `.ResizeNN(self, newWidth: 'int', newHeight: 'int')` | <a href="#ImageResizeNN"><code>ImageResizeNN</code></a>
*method* | `.ResizeCanvas(self, newWidth: 'int', newHeight: 'int', offsetX: 'int', offsetY: 'int', fill: 'Color')` | <a href="#ImageResizeCanvas"><code>ImageResizeCanvas</code></a>
*method* | `.Mipmaps(self)` | <a href="#ImageMipmaps"><code>ImageMipmaps</code></a>
*method* | `.Dither(self, rBpp: 'int', gBpp: 'int', bBpp: 'int', aBpp: 'int')` | <a href="#ImageDither"><code>ImageDither</code></a>
*method* | `.FlipVertical(self)` | <a href="#ImageFlipVertical"><code>ImageFlipVertical</code></a>
*method* | `.FlipHorizontal(self)` | <a href="#ImageFlipHorizontal"><code>ImageFlipHorizontal</code></a>
*method* | `.RotateCW(self)` | <a href="#ImageRotateCW"><code>ImageRotateCW</code></a>
*method* | `.RotateCCW(self)` | <a href="#ImageRotateCCW"><code>ImageRotateCCW</code></a>
*method* | `.ColorTint(self, color: 'Color')` | <a href="#ImageColorTint"><code>ImageColorTint</code></a>
*method* | `.ColorInvert(self)` | <a href="#ImageColorInvert"><code>ImageColorInvert</code></a>
*method* | `.ColorGrayscale(self)` | <a href="#ImageColorGrayscale"><code>ImageColorGrayscale</code></a>
*method* | `.ColorContrast(self, contrast: 'float')` | <a href="#ImageColorContrast"><code>ImageColorContrast</code></a>
*method* | `.ColorBrightness(self, brightness: 'int')` | <a href="#ImageColorBrightness"><code>ImageColorBrightness</code></a>
*method* | `.ColorReplace(self, color: 'Color', replace: 'Color')` | <a href="#ImageColorReplace"><code>ImageColorReplace</code></a>
*method* | `.ClearBackground(self, color: 'Color')` | <a href="#ImageClearBackground"><code>ImageClearBackground</code></a>
*method* | `.DrawPixel(self, posX: 'int', posY: 'int', color: 'Color')` | <a href="#ImageDrawPixel"><code>ImageDrawPixel</code></a>
*method* | `.DrawPixelV(self, position: 'Vector2', color: 'Color')` | <a href="#ImageDrawPixelV"><code>ImageDrawPixelV</code></a>
*method* | `.DrawLine(self, startPosX: 'int', startPosY: 'int', endPosX: 'int', endPosY: 'int', color: 'Color')` | <a href="#ImageDrawLine"><code>ImageDrawLine</code></a>
*method* | `.DrawLineV(self, start: 'Vector2', end: 'Vector2', color: 'Color')` | <a href="#ImageDrawLineV"><code>ImageDrawLineV</code></a>
*method* | `.DrawCircle(self, centerX: 'int', centerY: 'int', radius: 'int', color: 'Color')` | <a href="#ImageDrawCircle"><code>ImageDrawCircle</code></a>
*method* | `.DrawCircleV(self, center: 'Vector2', radius: 'int', color: 'Color')` | <a href="#ImageDrawCircleV"><code>ImageDrawCircleV</code></a>
*method* | `.DrawRectangle(self, posX: 'int', posY: 'int', width: 'int', height: 'int', color: 'Color')` | <a href="#ImageDrawRectangle"><code>ImageDrawRectangle</code></a>
*method* | `.DrawRectangleV(self, position: 'Vector2', size: 'Vector2', color: 'Color')` | <a href="#ImageDrawRectangleV"><code>ImageDrawRectangleV</code></a>
*method* | `.DrawRectangleRec(self, rec: 'Rectangle', color: 'Color')` | <a href="#ImageDrawRectangleRec"><code>ImageDrawRectangleRec</code></a>
*method* | `.DrawRectangleLines(self, rec: 'Rectangle', thick: 'int', color: 'Color')` | <a href="#ImageDrawRectangleLines"><code>ImageDrawRectangleLines</code></a>
*method* | `.Draw(self, src: 'Image', srcRec: 'Rectangle', dstRec: 'Rectangle', tint: 'Color')` | <a href="#ImageDraw"><code>ImageDraw</code></a>
*method* | `.DrawText(self, text: 'Union[str, CharPtr]', posX: 'int', posY: 'int', fontSize: 'int', color: 'Color')` | <a href="#ImageDrawText"><code>ImageDrawText</code></a>
*method* | `.DrawTextEx(self, font: 'Font', text: 'Union[str, CharPtr]', position: 'Vector2', fontSize: 'float', spacing: 'float', tint: 'Color')` | <a href="#ImageDrawTextEx"><code>ImageDrawTextEx</code></a>
*method* | `.LoadColors(self)` | <a href="#LoadImageColors"><code>LoadImageColors</code></a>
*method* | `.LoadPalette(self, maxPaletteSize: 'int')` | <a href="#LoadImagePalette"><code>LoadImagePalette</code></a>
*method* | `.GetAlphaBorder(self, threshold: 'float')` | <a href="#GetImageAlphaBorder"><code>GetImageAlphaBorder</code></a>
*method* | `.GetColor(self, x: 'int', y: 'int')` | <a href="#GetImageColor"><code>GetImageColor</code></a>



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
`offsetX` | `int` | `Int` | `int` | Character offset X when drawing
`offsetY` | `int` | `Int` | `int` | Character offset Y when drawing
`advanceX` | `int` | `Int` | `int` | Character advance position X
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
`baseSize` | `int` | `Int` | `int` | Base size (default chars height)
`glyphCount` | `int` | `Int` | `int` | Number of glyph characters
`glyphPadding` | `int` | `Int` | `int` | Padding around the glyph characters
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
*staticmethod* | `.LoadData(fileData: 'Union[Seq[int], UCharPtr]', dataSize: 'int', fontSize: 'int', fontChars: 'Union[Seq[int], IntPtr]', glyphCount: 'int', type: 'int')` | <a href="#LoadFontData"><code>LoadFontData</code></a>
*staticmethod* | `.UnloadData(chars: 'GlyphInfoPtr', glyphCount: 'int')` | <a href="#UnloadFontData"><code>UnloadFontData</code></a>
*classmethod* | `.array_of(cls, font_sequence)` | *n/a*
*classmethod* | `.Load(cls, fileName: 'Union[str, CharPtr]')` | <a href="#LoadFont"><code>LoadFont</code></a>
*classmethod* | `.LoadEx(cls, fileName: 'Union[str, CharPtr]', fontSize: 'int', fontChars: 'Union[Seq[int], IntPtr]', glyphCount: 'int')` | <a href="#LoadFontEx"><code>LoadFontEx</code></a>
*classmethod* | `.LoadFromImage(cls, image: 'Image', key: 'Color', firstChar: 'int')` | <a href="#LoadFontFromImage"><code>LoadFontFromImage</code></a>
*classmethod* | `.LoadFromMemory(cls, fileType: 'Union[str, CharPtr]', fileData: 'Union[Seq[int], UCharPtr]', dataSize: 'int', fontSize: 'int', fontChars: 'Union[Seq[int], IntPtr]', glyphCount: 'int')` | <a href="#LoadFontFromMemory"><code>LoadFontFromMemory</code></a>
*method* | `.Unload(self)` | <a href="#UnloadFont"><code>UnloadFont</code></a>
*method* | `.DrawTextEx(self, text: 'Union[str, CharPtr]', position: 'Vector2', fontSize: 'float', spacing: 'float', tint: 'Color')` | <a href="#DrawTextEx"><code>DrawTextEx</code></a>
*method* | `.DrawTextPro(self, text: 'Union[str, CharPtr]', position: 'Vector2', origin: 'Vector2', rotation: 'float', fontSize: 'float', spacing: 'float', tint: 'Color')` | <a href="#DrawTextPro"><code>DrawTextPro</code></a>
*method* | `.DrawTextCodepoint(self, codepoint: 'int', position: 'Vector2', fontSize: 'float', tint: 'Color')` | <a href="#DrawTextCodepoint"><code>DrawTextCodepoint</code></a>
*method* | `.DrawTextCodepoints(self, codepoints: 'Union[Seq[int], IntPtr]', position: 'Vector2', fontSize: 'float', spacing: 'float', tint: 'Color')` | <a href="#DrawTextCodepoints"><code>DrawTextCodepoints</code></a>
*method* | `.MeasureTextEx(self, text: 'Union[str, CharPtr]', fontSize: 'float', spacing: 'float')` | <a href="#MeasureTextEx"><code>MeasureTextEx</code></a>
*method* | `.GetGlyphIndex(self, codepoint: 'int')` | <a href="#GetGlyphIndex"><code>GetGlyphIndex</code></a>
*method* | `.GetGlyphInfo(self, codepoint: 'int')` | <a href="#GetGlyphInfo"><code>GetGlyphInfo</code></a>
*method* | `.GetGlyphAtlasRec(self, codepoint: 'int')` | <a href="#GetGlyphAtlasRec"><code>GetGlyphAtlasRec</code></a>



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
*method* | `.SetMode(self, mode: 'int')` | <a href="#SetCameraMode"><code>SetCameraMode</code></a>

### Context Manager

Context | API
--------|----
Enter | BeginMode3D
Leave | EndMode3D



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
Enter | BeginMode2D
Leave | EndMode2D



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Mesh"><code>Mesh</code> structure</h2>

Mesh, vertex data and vao/vbo

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`vertexCount` | `int` | `Int` | `int` | Number of vertices stored in arrays
`triangleCount` | `int` | `Int` | `int` | Number of triangles stored (indexed or not)
`vertices` | `Union[Seq[float], FloatPtr]` | `FloatPtr` | `float` | Vertex position (XYZ - 3 components per vertex) (shader-location = 0)
`texcoords` | `Union[Seq[float], FloatPtr]` | `FloatPtr` | `float` | Vertex texture coordinates (UV - 2 components per vertex) (shader-location = 1)
`texcoords2` | `Union[Seq[float], FloatPtr]` | `FloatPtr` | `float` | Vertex texture second coordinates (UV - 2 components per vertex) (shader-location = 5)
`normals` | `Union[Seq[float], FloatPtr]` | `FloatPtr` | `float` | Vertex normals (XYZ - 3 components per vertex) (shader-location = 2)
`tangents` | `Union[Seq[float], FloatPtr]` | `FloatPtr` | `float` | Vertex tangents (XYZW - 4 components per vertex) (shader-location = 4)
`colors` | `Union[Seq[int], UCharPtr]` | `UCharPtr` | `unsigned char *` | Vertex colors (RGBA - 4 components per vertex) (shader-location = 3)
`indices` | `Union[Seq[int], UShortPtr]` | `UShortPtr` | `unsigned short` | Vertex indices (in case vertex data comes indexed)
`animVertices` | `Union[Seq[float], FloatPtr]` | `FloatPtr` | `float` | Animated vertex positions (after bones transformations)
`animNormals` | `Union[Seq[float], FloatPtr]` | `FloatPtr` | `float` | Animated normals (after bones transformations)
`boneIds` | `Union[Seq[int], UCharPtr]` | `UCharPtr` | `unsigned char *` | Vertex bone ids, max 255 bone ids, up to 4 bones influence by vertex (skinning)
`boneWeights` | `Union[Seq[float], FloatPtr]` | `FloatPtr` | `float` | Vertex bone weight, up to 4 bones influence by vertex (skinning)
`vaoId` | `int` | `UInt` | `unsigned int` | OpenGL Vertex Array Object id
`vboId` | `Union[Seq[int], UIntPtr]` | `UIntPtr` | `unsigned int` | OpenGL Vertex Buffer Objects id (default vertex data)

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, mesh_sequence)` | *n/a*
*classmethod* | `.GenPoly(cls, sides: 'int', radius: 'float')` | <a href="#GenMeshPoly"><code>GenMeshPoly</code></a>
*classmethod* | `.GenPlane(cls, width: 'float', length: 'float', resX: 'int', resZ: 'int')` | <a href="#GenMeshPlane"><code>GenMeshPlane</code></a>
*classmethod* | `.GenCube(cls, width: 'float', height: 'float', length: 'float')` | <a href="#GenMeshCube"><code>GenMeshCube</code></a>
*classmethod* | `.GenSphere(cls, radius: 'float', rings: 'int', slices: 'int')` | <a href="#GenMeshSphere"><code>GenMeshSphere</code></a>
*classmethod* | `.GenHemiSphere(cls, radius: 'float', rings: 'int', slices: 'int')` | <a href="#GenMeshHemiSphere"><code>GenMeshHemiSphere</code></a>
*classmethod* | `.GenCylinder(cls, radius: 'float', height: 'float', slices: 'int')` | <a href="#GenMeshCylinder"><code>GenMeshCylinder</code></a>
*classmethod* | `.GenCone(cls, radius: 'float', height: 'float', slices: 'int')` | <a href="#GenMeshCone"><code>GenMeshCone</code></a>
*classmethod* | `.GenTorus(cls, radius: 'float', size: 'float', radSeg: 'int', sides: 'int')` | <a href="#GenMeshTorus"><code>GenMeshTorus</code></a>
*classmethod* | `.GenKnot(cls, radius: 'float', size: 'float', radSeg: 'int', sides: 'int')` | <a href="#GenMeshKnot"><code>GenMeshKnot</code></a>
*classmethod* | `.GenHeightmap(cls, heightmap: 'Image', size: 'Vector3')` | <a href="#GenMeshHeightmap"><code>GenMeshHeightmap</code></a>
*classmethod* | `.GenCubicmap(cls, cubicmap: 'Image', cubeSize: 'Vector3')` | <a href="#GenMeshCubicmap"><code>GenMeshCubicmap</code></a>
*method* | `.Upload(self, dynamic: 'bool')` | <a href="#UploadMesh"><code>UploadMesh</code></a>
*method* | `.UpdateBuffer(self, index: 'int', data: 'bytes', dataSize: 'int', offset: 'int')` | <a href="#UpdateMeshBuffer"><code>UpdateMeshBuffer</code></a>
*method* | `.Unload(self)` | <a href="#UnloadMesh"><code>UnloadMesh</code></a>
*method* | `.Draw(self, material: 'Material', transform: 'Matrix')` | <a href="#DrawMesh"><code>DrawMesh</code></a>
*method* | `.DrawInstanced(self, material: 'Material', transforms: 'MatrixPtr', instances: 'int')` | <a href="#DrawMeshInstanced"><code>DrawMeshInstanced</code></a>
*method* | `.Export(self, fileName: 'Union[str, CharPtr]')` | <a href="#ExportMesh"><code>ExportMesh</code></a>
*method* | `.GetBoundingBox(self)` | <a href="#GetMeshBoundingBox"><code>GetMeshBoundingBox</code></a>
*method* | `.GenTangents(self)` | <a href="#GenMeshTangents"><code>GenMeshTangents</code></a>



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
*classmethod* | `.Load(cls, vsFileName: 'Union[str, CharPtr]', fsFileName: 'Union[str, CharPtr]')` | <a href="#LoadShader"><code>LoadShader</code></a>
*classmethod* | `.LoadFromMemory(cls, vsCode: 'Union[str, CharPtr]', fsCode: 'Union[str, CharPtr]')` | <a href="#LoadShaderFromMemory"><code>LoadShaderFromMemory</code></a>
*method* | `.GetLocation(self, uniformName: 'Union[str, CharPtr]')` | <a href="#GetShaderLocation"><code>GetShaderLocation</code></a>
*method* | `.GetLocationAttrib(self, attribName: 'Union[str, CharPtr]')` | <a href="#GetShaderLocationAttrib"><code>GetShaderLocationAttrib</code></a>
*method* | `.SetValue(self, locIndex: 'int', value: 'bytes', uniformType: 'int')` | <a href="#SetShaderValue"><code>SetShaderValue</code></a>
*method* | `.SetValueV(self, locIndex: 'int', value: 'bytes', uniformType: 'int', count: 'int')` | <a href="#SetShaderValueV"><code>SetShaderValueV</code></a>
*method* | `.SetValueMatrix(self, locIndex: 'int', mat: 'Matrix')` | <a href="#SetShaderValueMatrix"><code>SetShaderValueMatrix</code></a>
*method* | `.SetValueTexture(self, locIndex: 'int', texture: 'Texture2D')` | <a href="#SetShaderValueTexture"><code>SetShaderValueTexture</code></a>
*method* | `.Unload(self)` | <a href="#UnloadShader"><code>UnloadShader</code></a>

### Context Manager

Context | API
--------|----
Enter | BeginShaderMode
Leave | EndShaderMode



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
*classmethod* | `.LoadMaterials(cls, fileName: 'Union[str, CharPtr]')` | <a href="#LoadMaterials"><code>LoadMaterials</code></a>
*classmethod* | `.LoadDefault()` | <a href="#LoadMaterialDefault"><code>LoadMaterialDefault</code></a>
*method* | `.Unload(self)` | <a href="#UnloadMaterial"><code>UnloadMaterial</code></a>
*method* | `.SetTexture(self, mapType: 'int', texture: 'Texture2D')` | <a href="#SetMaterialTexture"><code>SetMaterialTexture</code></a>



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
`meshCount` | `int` | `Int` | `int` | Number of meshes
`materialCount` | `int` | `Int` | `int` | Number of materials
`meshes` | `MeshPtr` | `MeshPtr` | `Mesh *` | Meshes array
`materials` | `MaterialPtr` | `MaterialPtr` | `Material *` | Materials array
`meshMaterial` | `Union[Seq[int], IntPtr]` | `IntPtr` | `int` | Mesh material number
`boneCount` | `int` | `Int` | `int` | Number of bones
`bones` | `BoneInfoPtr` | `BoneInfoPtr` | `BoneInfo *` | Bones information (skeleton)
`bindPose` | `TransformPtr` | `TransformPtr` | `Transform *` | Bones base transformation (pose)

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, model_sequence)` | *n/a*
*classmethod* | `.Load(cls, fileName: 'Union[str, CharPtr]')` | <a href="#LoadModel"><code>LoadModel</code></a>
*classmethod* | `.LoadFromMesh(cls, mesh: 'Mesh')` | <a href="#LoadModelFromMesh"><code>LoadModelFromMesh</code></a>
*method* | `.IsAnimationValid(self, anim: 'ModelAnimation')` | <a href="#IsModelAnimationValid"><code>IsModelAnimationValid</code></a>
*method* | `.UpdateAnimation(self, anim: 'ModelAnimation', frame: 'int')` | <a href="#UpdateModelAnimation"><code>UpdateModelAnimation</code></a>
*method* | `.SetMeshMaterial(self, meshId: 'int', materialId: 'int')` | <a href="#SetModelMeshMaterial"><code>SetModelMeshMaterial</code></a>
*method* | `.Unload(self)` | <a href="#UnloadModel"><code>UnloadModel</code></a>
*method* | `.UnloadKeepMeshes(self)` | <a href="#UnloadModelKeepMeshes"><code>UnloadModelKeepMeshes</code></a>
*method* | `.GetBoundingBox(self)` | <a href="#GetModelBoundingBox"><code>GetModelBoundingBox</code></a>
*method* | `.Draw(self, position: 'Vector3', scale: 'float', tint: 'Color')` | <a href="#DrawModel"><code>DrawModel</code></a>
*method* | `.DrawEx(self, position: 'Vector3', rotationAxis: 'Vector3', rotationAngle: 'float', scale: 'Vector3', tint: 'Color')` | <a href="#DrawModelEx"><code>DrawModelEx</code></a>
*method* | `.DrawWires(self, position: 'Vector3', scale: 'float', tint: 'Color')` | <a href="#DrawModelWires"><code>DrawModelWires</code></a>
*method* | `.DrawWiresEx(self, position: 'Vector3', rotationAxis: 'Vector3', rotationAngle: 'float', scale: 'Vector3', tint: 'Color')` | <a href="#DrawModelWiresEx"><code>DrawModelWiresEx</code></a>



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ModelAnimation"><code>ModelAnimation</code> structure</h2>

ModelAnimation

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`boneCount` | `int` | `Int` | `int` | Number of bones
`frameCount` | `int` | `Int` | `int` | Number of animation frames
`bones` | `BoneInfoPtr` | `BoneInfoPtr` | `BoneInfo *` | Bones information (skeleton)
`framePoses` | `TransformPtr` | `TransformPtr` | `Transform **` | Poses array by frame

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
`frameCount` | `int` | `UInt` | `unsigned int` | Total number of frames (considering channels)
`sampleRate` | `int` | `UInt` | `unsigned int` | Frequency (samples per second)
`sampleSize` | `int` | `UInt` | `unsigned int` | Bit depth (bits per sample): 8, 16, 32 (24 not supported)
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
*classmethod* | `.Load(cls, fileName: 'Union[str, CharPtr]')` | <a href="#LoadWave"><code>LoadWave</code></a>
*classmethod* | `.LoadFromMemory(cls, fileType: 'Union[str, CharPtr]', fileData: 'Union[Seq[int], UCharPtr]', dataSize: 'int')` | <a href="#LoadWaveFromMemory"><code>LoadWaveFromMemory</code></a>
*method* | `.Copy(self)` | <a href="#WaveCopy"><code>WaveCopy</code></a>
*method* | `.Crop(self, initSample: 'int', finalSample: 'int')` | <a href="#WaveCrop"><code>WaveCrop</code></a>
*method* | `.Format(self, sampleRate: 'int', sampleSize: 'int', channels: 'int')` | <a href="#WaveFormat"><code>WaveFormat</code></a>
*method* | `.Format(self)` | <a href="#LoadWaveSamples"><code>LoadWaveSamples</code></a>
*method* | `.Export(self, fileName: 'Union[str, CharPtr]')` | <a href="#ExportWave"><code>ExportWave</code></a>
*method* | `.ExportAsCode(self, fileName: 'Union[str, CharPtr]')` | <a href="#ExportWaveAsCode"><code>ExportWaveAsCode</code></a>
*method* | `.Unload(self)` | <a href="#UnloadWave"><code>UnloadWave</code></a>
*method* | `.UnloadSamples(self)` | <a href="#UnloadWaveSamples"><code>UnloadWaveSamples</code></a>



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="AudioStream"><code>AudioStream</code> structure</h2>

AudioStream, custom audio stream

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`buffer` | `rAudioBufferPtr` | `rAudioBufferPtr` | `rAudioBuffer *` | Pointer to internal data used by the audio system
`processor` | `rAudioProcessorPtr` | `rAudioProcessorPtr` | `rAudioProcessor *` | Pointer to internal data processor, useful for audio effects
`sampleRate` | `int` | `UInt` | `unsigned int` | Frequency (samples per second)
`sampleSize` | `int` | `UInt` | `unsigned int` | Bit depth (bits per sample): 8, 16, 32 (24 not supported)
`channels` | `int` | `UInt` | `unsigned int` | Number of channels (1-mono, 2-stereo, ...)

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*classmethod* | `.array_of(cls, audio_stream_sequence)` | *n/a*
*classmethod* | `.Load(cls, sampleRate: 'int', sampleSize: 'int', channels: 'int')` | <a href="#LoadAudioStream"><code>LoadAudioStream</code></a>
*method* | `.Unload(self)` | <a href="#UnloadAudioStream"><code>UnloadAudioStream</code></a>
*method* | `.Update(self, data: 'bytes', frameCount: 'int')` | <a href="#UpdateAudioStream"><code>UpdateAudioStream</code></a>
*method* | `.IsProcessed(self)` | <a href="#IsAudioStreamProcessed"><code>IsAudioStreamProcessed</code></a>
*method* | `.Play(self)` | <a href="#PlayAudioStream"><code>PlayAudioStream</code></a>
*method* | `.Pause(self)` | <a href="#PauseAudioStream"><code>PauseAudioStream</code></a>
*method* | `.Resume(self)` | <a href="#ResumeAudioStream"><code>ResumeAudioStream</code></a>
*method* | `.IsPlaying(self)` | <a href="#IsAudioStreamPlaying"><code>IsAudioStreamPlaying</code></a>
*method* | `.Stop(self)` | <a href="#StopAudioStream"><code>StopAudioStream</code></a>
*method* | `.SetVolume(self, volume: 'float')` | <a href="#SetAudioStreamVolume"><code>SetAudioStreamVolume</code></a>
*method* | `.SetPitch(self, pitch: 'float')` | <a href="#SetAudioStreamPitch"><code>SetAudioStreamPitch</code></a>
*method* | `.SetPan(self, pan: 'float')` | <a href="#SetAudioStreamPan"><code>SetAudioStreamPan</code></a>
*method* | `.SetBufferSizeDefault(self)` | <a href="#SetAudioStreamBufferSizeDefault"><code>SetAudioStreamBufferSizeDefault</code></a>
*method* | `.SetCallback(self, callback: 'AudioCallback')` | <a href="#SetAudioStreamCallback"><code>SetAudioStreamCallback</code></a>
*method* | `.AttachProcessor(self, processor: 'AudioCallback')` | <a href="#AttachAudioStreamProcessor"><code>AttachAudioStreamProcessor</code></a>
*method* | `.DetachProcessor(self, processor: 'AudioCallback')` | <a href="#DetachAudioStreamProcessor"><code>DetachAudioStreamProcessor</code></a>



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Sound"><code>Sound</code> structure</h2>

Sound

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`stream` | `AudioStream` | `AudioStream` | `AudioStream` | Audio stream
`frameCount` | `int` | `UInt` | `unsigned int` | Total number of frames (considering channels)

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*staticmethod* | `.GetSoundsPlaying()` | <a href="#GetSoundsPlaying"><code>GetSoundsPlaying</code></a>
*staticmethod* | `.StopMulti()` | <a href="#StopSoundMulti"><code>StopSoundMulti</code></a>
*classmethod* | `.array_of(cls, sound_sequence)` | *n/a*
*classmethod* | `.Load(cls, fileName: 'Union[str, CharPtr]')` | <a href="#LoadSound"><code>LoadSound</code></a>
*classmethod* | `.LoadFromWave(cls, wave: 'Wave')` | <a href="#LoadSoundFromWave"><code>LoadSoundFromWave</code></a>
*method* | `.Play(self)` | <a href="#PlaySound"><code>PlaySound</code></a>
*method* | `.Stop(self)` | <a href="#StopSound"><code>StopSound</code></a>
*method* | `.Pause(self)` | <a href="#PauseSound"><code>PauseSound</code></a>
*method* | `.Resume(self)` | <a href="#ResumeSound"><code>ResumeSound</code></a>
*method* | `.PlayMulti(self)` | <a href="#PlaySoundMulti"><code>PlaySoundMulti</code></a>
*method* | `.IsPlaying(self)` | <a href="#IsSoundPlaying"><code>IsSoundPlaying</code></a>
*method* | `.SetVolume(self, volume: 'float')` | <a href="#SetSoundVolume"><code>SetSoundVolume</code></a>
*method* | `.SetPitch(self, pitch: 'float')` | <a href="#SetSoundPitch"><code>SetSoundPitch</code></a>
*method* | `.SetPan(self, pan: 'float')` | <a href="#SetSoundPan"><code>SetSoundPan</code></a>
*method* | `.Unload(self)` | <a href="#UnloadSound"><code>UnloadSound</code></a>
*method* | `.Update(self, data: 'bytes', sampleCount: 'int')` | <a href="#UpdateSound"><code>UpdateSound</code></a>



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Music"><code>Music</code> structure</h2>

Music, audio stream, anything longer than ~10 seconds should be streamed

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`stream` | `AudioStream` | `AudioStream` | `AudioStream` | Audio stream
`frameCount` | `int` | `UInt` | `unsigned int` | Total number of frames (considering channels)
`looping` | `bool` | `Bool` | `bool` | Music looping enable
`ctxType` | `int` | `Int` | `int` | Type of music context (audio filetype)
`ctxData` | `bytes` | `VoidPtr` | `void` | Audio context data, depends on type

### Properties

Name | API
-----|----
`.byref` | *n/a*

### Methods

Bound as | Name | API
---------|------|----
*staticmethod* | `.Load(fileName: 'Union[str, CharPtr]')` | <a href="#LoadMusicStream"><code>LoadMusicStream</code></a>
*staticmethod* | `.LoadFromMemory(fileType: 'Union[str, CharPtr]', data: 'Union[Seq[int], UCharPtr]', dataSize: 'int')` | <a href="#LoadMusicStreamFromMemory"><code>LoadMusicStreamFromMemory</code></a>
*classmethod* | `.array_of(cls, music_sequence)` | *n/a*
*method* | `.Play(self)` | <a href="#PlayMusicStream"><code>PlayMusicStream</code></a>
*method* | `.IsPlaying(self)` | <a href="#IsMusicStreamPlaying"><code>IsMusicStreamPlaying</code></a>
*method* | `.Update(self)` | <a href="#UpdateMusicStream"><code>UpdateMusicStream</code></a>
*method* | `.Stop(self)` | <a href="#StopMusicStream"><code>StopMusicStream</code></a>
*method* | `.Pause(self)` | <a href="#PauseMusicStream"><code>PauseMusicStream</code></a>
*method* | `.Resume(self)` | <a href="#ResumeMusicStream"><code>ResumeMusicStream</code></a>
*method* | `.Seek(self, position: 'float')` | <a href="#SeekMusicStream"><code>SeekMusicStream</code></a>
*method* | `.SetVolume(self, volume: 'float')` | <a href="#SetMusicVolume"><code>SetMusicVolume</code></a>
*method* | `.SetPitch(self, pitch: 'float')` | <a href="#SetMusicPitch"><code>SetMusicPitch</code></a>
*method* | `.SetPan(self, pan: 'float')` | <a href="#SetMusicPan"><code>SetMusicPan</code></a>
*method* | `.GetTimeLength(self)` | <a href="#GetMusicTimeLength"><code>GetMusicTimeLength</code></a>
*method* | `.GetTimePlayed(self)` | <a href="#GetMusicTimePlayed"><code>GetMusicTimePlayed</code></a>



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="VrDeviceInfo"><code>VrDeviceInfo</code> structure</h2>

VrDeviceInfo, Head-Mounted-Display device parameters

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
`hResolution` | `int` | `Int` | `int` | Horizontal resolution in pixels
`vResolution` | `int` | `Int` | `int` | Vertical resolution in pixels
`hScreenSize` | `float` | `Float` | `float` | Horizontal size in meters
`vScreenSize` | `float` | `Float` | `float` | Vertical size in meters
`vScreenCenter` | `float` | `Float` | `float` | Screen center in meters
`eyeToScreenDistance` | `float` | `Float` | `float` | Distance between eye and display in meters
`lensSeparationDistance` | `float` | `Float` | `float` | Lens separation distance in meters
`interpupillaryDistance` | `float` | `Float` | `float` | IPD (distance between pupils) in meters
`lensDistortionValues` | `Seq[float]` | `Float * 4` | `float[4]` | Lens distortion constant parameters
`chromaAbCorrection` | `Seq[float]` | `Float * 4` | `float[4]` | Chromatic aberration correction parameters

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
`viewOffset` | `Seq[Matrix]` | `Matrix * 2` | `Matrix[2]` | VR view offset matrices (per eye)
`leftLensCenter` | `Seq[float]` | `Float * 2` | `float[2]` | VR left lens center
`rightLensCenter` | `Seq[float]` | `Float * 2` | `float[2]` | VR right lens center
`leftScreenCenter` | `Seq[float]` | `Float * 2` | `float[2]` | VR left screen center
`rightScreenCenter` | `Seq[float]` | `Float * 2` | `float[2]` | VR right screen center
`scale` | `Seq[float]` | `Float * 2` | `float[2]` | VR distortion scale
`scaleIn` | `Seq[float]` | `Float * 2` | `float[2]` | VR distortion scale in

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
Enter | BeginVrStereoMode
Leave | EndVrStereoMode



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
`elementCount` | `int` | `Int` | `int` | Number of elements in the buffer (QUADS)
`vertices` | `Union[Seq[float], FloatPtr]` | `FloatPtr` | `float` | Vertex position (XYZ - 3 components per vertex) (shader-location = 0)
`texcoords` | `Union[Seq[float], FloatPtr]` | `FloatPtr` | `float` | Vertex texture coordinates (UV - 2 components per vertex) (shader-location = 1)
`colors` | `Union[Seq[int], UCharPtr]` | `UCharPtr` | `unsigned char *` | Vertex colors (RGBA - 4 components per vertex) (shader-location = 3)
`indices` | `Union[Seq[int], UIntPtr]` | `UIntPtr` | `unsigned int` | Vertex indices (in case vertex data comes indexed) (6 indices per quad)
`vaoId` | `int` | `UInt` | `unsigned int` | OpenGL Vertex Array Object id
`vboId` | `Seq[int]` | `Int * 4` | `unsigned int[4]` | OpenGL Vertex Buffer Objects id (4 types of vertex data)

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
`vertexCount` | `int` | `Int` | `int` | Number of vertex of the draw
`vertexAlignment` | `int` | `Int` | `int` | Number of vertex required for index alignment (LINES, TRIANGLES)
`textureId` | `int` | `UInt` | `unsigned int` | Texture id to be used on the draw -> Use to create new draw call if changes

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
`bufferCount` | `int` | `Int` | `int` | Number of vertex buffers (multi-buffering support)
`currentBuffer` | `int` | `Int` | `int` | Current buffer tracking in case of multi-buffering
`vertexBuffer` | `rlVertexBufferPtr` | `rlVertexBufferPtr` | `rlVertexBuffer *` | Dynamic buffer(s) for vertex data
`draws` | `rlDrawCallPtr` | `rlDrawCallPtr` | `rlDrawCall *` | Draw calls array, depends on textureId
`drawCounter` | `int` | `Int` | `int` | Draw calls counter
`currentDepth` | `float` | `Float` | `float` | Current depth value for next draw

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
*classmethod* | `.Identity()` | <a href="#MatrixIdentity"><code>MatrixIdentity</code></a>
*classmethod* | `.Translate(cls, x: 'float', y: 'float', z: 'float')` | <a href="#MatrixTranslate"><code>MatrixTranslate</code></a>
*classmethod* | `.Rotate(cls, axis: 'Vector3', angle: 'float')` | <a href="#MatrixRotate"><code>MatrixRotate</code></a>
*classmethod* | `.RotateX(cls, angle: 'float')` | <a href="#MatrixRotateX"><code>MatrixRotateX</code></a>
*classmethod* | `.RotateY(cls, angle: 'float')` | <a href="#MatrixRotateY"><code>MatrixRotateY</code></a>
*classmethod* | `.RotateZ(cls, angle: 'float')` | <a href="#MatrixRotateZ"><code>MatrixRotateZ</code></a>
*classmethod* | `.RotateXYZ(cls, angle: 'Vector3')` | <a href="#MatrixRotateXYZ"><code>MatrixRotateXYZ</code></a>
*classmethod* | `.RotateZYX(cls, angle: 'Vector3')` | <a href="#MatrixRotateZYX"><code>MatrixRotateZYX</code></a>
*classmethod* | `.Scale(cls, x: 'float', y: 'float', z: 'float')` | <a href="#MatrixScale"><code>MatrixScale</code></a>
*classmethod* | `.Frustum(cls, left: 'float', right: 'float', bottom: 'float', top: 'float', near: 'float', far: 'float')` | <a href="#MatrixFrustum"><code>MatrixFrustum</code></a>
*classmethod* | `.Perspective(cls, fovy: 'float', aspect: 'float', near: 'float', far: 'float')` | <a href="#MatrixPerspective"><code>MatrixPerspective</code></a>
*classmethod* | `.Ortho(cls, left: 'float', right: 'float', bottom: 'float', top: 'float', near: 'float', far: 'float')` | <a href="#MatrixOrtho"><code>MatrixOrtho</code></a>
*classmethod* | `.LookAt(cls, eye: 'Vector3', target: 'Vector3', up: 'Vector3')` | <a href="#MatrixLookAt"><code>MatrixLookAt</code></a>
*method* | `.Determinant(self)` | <a href="#MatrixDeterminant"><code>MatrixDeterminant</code></a>
*method* | `.Trace(self)` | <a href="#MatrixTrace"><code>MatrixTrace</code></a>
*method* | `.Transpose(self)` | <a href="#MatrixTranspose"><code>MatrixTranspose</code></a>
*method* | `.Invert(self)` | <a href="#MatrixInvert"><code>MatrixInvert</code></a>



[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="aliases">Aliases</h2>

Alias Name | Type | Description
-----------|------|------------
`Quaternion` | `<a href="#Vector4">Vector4</a>` | Quaternion, 4 components (Vector4 alias)
`Texture2D` | `<a href="#Texture">Texture</a>` | Texture2D, same as Texture
`TextureCubemap` | `<a href="#Texture">Texture</a>` | TextureCubemap, same as Texture
`RenderTexture2D` | `<a href="#RenderTexture">RenderTexture</a>` | RenderTexture2D, same as RenderTexture
`Camera` | `<a href="#Camera3D">Camera3D</a>` | Camera type fallback, defaults to Camera3D

[ <a href="#toc">ToC</a> ]

<h2 id="enums">Enumerations</h2>

Item|Item|Item|Item|Item
--------|--------|--------|--------|--------
<a href="#BlendMode">BlendMode</a> | <a href="#CameraMode">CameraMode</a> | <a href="#CameraProjection">CameraProjection</a> | <a href="#ConfigFlags">ConfigFlags</a> | <a href="#CubemapLayout">CubemapLayout</a>
<a href="#FontType">FontType</a> | <a href="#GamepadAxis">GamepadAxis</a> | <a href="#GamepadButton">GamepadButton</a> | <a href="#Gesture">Gesture</a> | <a href="#KeyboardKey">KeyboardKey</a>
<a href="#MaterialMapIndex">MaterialMapIndex</a> | <a href="#MouseButton">MouseButton</a> | <a href="#MouseCursor">MouseCursor</a> | <a href="#NPatchLayout">NPatchLayout</a> | <a href="#PixelFormat">PixelFormat</a>
<a href="#ShaderAttributeDataType">ShaderAttributeDataType</a> | <a href="#ShaderLocationIndex">ShaderLocationIndex</a> | <a href="#ShaderUniformDataType">ShaderUniformDataType</a> | <a href="#TextureFilter">TextureFilter</a> | <a href="#TextureWrap">TextureWrap</a>
<a href="#TraceLogLevel">TraceLogLevel</a> | <a href="#rlBlendMode">rlBlendMode</a> | <a href="#rlFramebufferAttachTextureType">rlFramebufferAttachTextureType</a> | <a href="#rlFramebufferAttachType">rlFramebufferAttachType</a> | <a href="#rlGlVersion">rlGlVersion</a>
<a href="#rlPixelFormat">rlPixelFormat</a> | <a href="#rlShaderAttributeDataType">rlShaderAttributeDataType</a> | <a href="#rlShaderLocationIndex">rlShaderLocationIndex</a> | <a href="#rlShaderUniformDataType">rlShaderUniformDataType</a> | <a href="#rlTextureFilter">rlTextureFilter</a>
<a href="#rlTraceLogLevel">rlTraceLogLevel</a>

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
<h2 id="defines">Constants</h2>

Name | Value | Description
-----|-------|------------
`RAYLIB_VERSION` | `'4.2'` | *n/a*
`PI` | `3.141592653589793` | *n/a*
`DEG2RAD` | `(PI / 180.0)` | *n/a*
`RAD2DEG` | `(180.0 / PI)` | *n/a*
`LIGHTGRAY` | `Color(200, 200, 200, 255)` |  <span style="color:rgba(200, 200, 200, 255);">█████</span> Light Gray
`GRAY` | `Color(130, 130, 130, 255)` |  <span style="color:rgba(130, 130, 130, 255);">█████</span> Gray
`DARKGRAY` | `Color(80, 80, 80, 255)` |  <span style="color:rgba(80, 80, 80, 255);">█████</span> Dark Gray
`YELLOW` | `Color(253, 249, 0, 255)` |  <span style="color:rgba(253, 249, 0, 255);">█████</span> Yellow
`GOLD` | `Color(255, 203, 0, 255)` |  <span style="color:rgba(255, 203, 0, 255);">█████</span> Gold
`ORANGE` | `Color(255, 161, 0, 255)` |  <span style="color:rgba(255, 161, 0, 255);">█████</span> Orange
`PINK` | `Color(255, 109, 194, 255)` |  <span style="color:rgba(255, 109, 194, 255);">█████</span> Pink
`RED` | `Color(230, 41, 55, 255)` |  <span style="color:rgba(230, 41, 55, 255);">█████</span> Red
`MAROON` | `Color(190, 33, 55, 255)` |  <span style="color:rgba(190, 33, 55, 255);">█████</span> Maroon
`GREEN` | `Color(0, 228, 48, 255)` |  <span style="color:rgba(0, 228, 48, 255);">█████</span> Green
`LIME` | `Color(0, 158, 47, 255)` |  <span style="color:rgba(0, 158, 47, 255);">█████</span> Lime
`DARKGREEN` | `Color(0, 117, 44, 255)` |  <span style="color:rgba(0, 117, 44, 255);">█████</span> Dark Green
`SKYBLUE` | `Color(102, 191, 255, 255)` |  <span style="color:rgba(102, 191, 255, 255);">█████</span> Sky Blue
`BLUE` | `Color(0, 121, 241, 255)` |  <span style="color:rgba(0, 121, 241, 255);">█████</span> Blue
`DARKBLUE` | `Color(0, 82, 172, 255)` |  <span style="color:rgba(0, 82, 172, 255);">█████</span> Dark Blue
`PURPLE` | `Color(200, 122, 255, 255)` |  <span style="color:rgba(200, 122, 255, 255);">█████</span> Purple
`VIOLET` | `Color(135, 60, 190, 255)` |  <span style="color:rgba(135, 60, 190, 255);">█████</span> Violet
`DARKPURPLE` | `Color(112, 31, 126, 255)` |  <span style="color:rgba(112, 31, 126, 255);">█████</span> Dark Purple
`BEIGE` | `Color(211, 176, 131, 255)` |  <span style="color:rgba(211, 176, 131, 255);">█████</span> Beige
`BROWN` | `Color(127, 106, 79, 255)` |  <span style="color:rgba(127, 106, 79, 255);">█████</span> Brown
`DARKBROWN` | `Color(76, 63, 47, 255)` |  <span style="color:rgba(76, 63, 47, 255);">█████</span> Dark Brown
`WHITE` | `Color(255, 255, 255, 255)` |  <span style="color:rgba(255, 255, 255, 255);">█████</span> White
`BLACK` | `Color(0, 0, 0, 255)` |  <span style="color:rgba(0, 0, 0, 255);">█████</span> Black
`BLANK` | `Color(0, 0, 0, 0)` |  <span style="color:rgba(0, 0, 0, 0);">█████</span> Blank (Transparent)
`MAGENTA` | `Color(255, 0, 255, 255)` |  <span style="color:rgba(255, 0, 255, 255);">█████</span> Magenta
`RAYWHITE` | `Color(245, 245, 245, 255)` |  <span style="color:rgba(245, 245, 245, 255);">█████</span> My own White (raylib logo)
`RLGL_VERSION` | `'4.0'` | *n/a*
`RL_DEFAULT_BATCH_BUFFER_ELEMENTS` | `8192` | *n/a*
`RL_DEFAULT_BATCH_BUFFERS` | `1` | Default number of batch buffers (multi-buffering)
`RL_DEFAULT_BATCH_DRAWCALLS` | `256` | Default number of batch draw calls (by state changes: mode, texture)
`RL_DEFAULT_BATCH_MAX_TEXTURE_UNITS` | `4` | Maximum number of textures units that can be activated on batch drawing (SetShaderValueTexture())
`RL_MAX_MATRIX_STACK_SIZE` | `32` | Maximum size of Matrix stack
`RL_MAX_SHADER_LOCATIONS` | `32` | Maximum number of shader locations supported
`RL_CULL_DISTANCE_NEAR` | `0.01` | Default near cull distance
`RL_CULL_DISTANCE_FAR` | `1000.0` | Default far cull distance
`RL_TEXTURE_WRAP_S` | `10242` | GL_TEXTURE_WRAP_S
`RL_TEXTURE_WRAP_T` | `10243` | GL_TEXTURE_WRAP_T
`RL_TEXTURE_MAG_FILTER` | `10240` | GL_TEXTURE_MAG_FILTER
`RL_TEXTURE_MIN_FILTER` | `10241` | GL_TEXTURE_MIN_FILTER
`RL_TEXTURE_FILTER_NEAREST` | `9728` | GL_NEAREST
`RL_TEXTURE_FILTER_LINEAR` | `9729` | GL_LINEAR
`RL_TEXTURE_FILTER_MIP_NEAREST` | `9984` | GL_NEAREST_MIPMAP_NEAREST
`RL_TEXTURE_FILTER_NEAREST_MIP_LINEAR` | `9986` | GL_NEAREST_MIPMAP_LINEAR
`RL_TEXTURE_FILTER_LINEAR_MIP_NEAREST` | `9985` | GL_LINEAR_MIPMAP_NEAREST
`RL_TEXTURE_FILTER_MIP_LINEAR` | `9987` | GL_LINEAR_MIPMAP_LINEAR
`RL_TEXTURE_FILTER_ANISOTROPIC` | `12288` | Anisotropic filter (custom identifier)
`RL_TEXTURE_WRAP_REPEAT` | `10497` | GL_REPEAT
`RL_TEXTURE_WRAP_CLAMP` | `33071` | GL_CLAMP_TO_EDGE
`RL_TEXTURE_WRAP_MIRROR_REPEAT` | `33648` | GL_MIRRORED_REPEAT
`RL_TEXTURE_WRAP_MIRROR_CLAMP` | `34626` | GL_MIRROR_CLAMP_EXT
`RL_MODELVIEW` | `5888` | GL_MODELVIEW
`RL_PROJECTION` | `5889` | GL_PROJECTION
`RL_TEXTURE` | `5890` | GL_TEXTURE
`RL_LINES` | `1` | GL_LINES
`RL_TRIANGLES` | `4` | GL_TRIANGLES
`RL_QUADS` | `7` | GL_QUADS
`RL_UNSIGNED_BYTE` | `5121` | GL_UNSIGNED_BYTE
`RL_FLOAT` | `5126` | GL_FLOAT
`RL_STREAM_DRAW` | `35040` | GL_STREAM_DRAW
`RL_STREAM_READ` | `35041` | GL_STREAM_READ
`RL_STREAM_COPY` | `35042` | GL_STREAM_COPY
`RL_STATIC_DRAW` | `35044` | GL_STATIC_DRAW
`RL_STATIC_READ` | `35045` | GL_STATIC_READ
`RL_STATIC_COPY` | `35046` | GL_STATIC_COPY
`RL_DYNAMIC_DRAW` | `35048` | GL_DYNAMIC_DRAW
`RL_DYNAMIC_READ` | `35049` | GL_DYNAMIC_READ
`RL_DYNAMIC_COPY` | `35050` | GL_DYNAMIC_COPY
`RL_FRAGMENT_SHADER` | `35632` | GL_FRAGMENT_SHADER
`RL_VERTEX_SHADER` | `35633` | GL_VERTEX_SHADER
`RL_COMPUTE_SHADER` | `37305` | GL_COMPUTE_SHADER

[ <a href="#toc">ToC</a> ]

<h2 id="callbacks">Callbacks</h2>

To define and use your own callbacks, you can do like below:

```python
# defines a callback function decorating it with the AudioCallback CFUNCTYPE
@AudioCallback
def my_callback(data, frames):
    # TODO: some logic
    pass

# then, somewhere ahead in the code
set_audio_stream_callback(some_stream, my_callback)

```

Name | Signature | Description
-----|-----------|------------
`TraceLogCallback` | `(logLevel: 'int', text: 'Union[str, CharPtr]', args: 'bytes') -> None` | Logging: Redirect trace log messages
`LoadFileDataCallback` | `(fileName: 'Union[str, CharPtr]', bytesRead: 'Union[Seq[int], UIntPtr]') -> Union[Seq[int], UCharPtr]` | FileIO: Load binary data
`SaveFileDataCallback` | `(fileName: 'Union[str, CharPtr]', data: 'bytes', bytesToWrite: 'int') -> bool` | FileIO: Save binary data
`LoadFileTextCallback` | `(fileName: 'Union[str, CharPtr]') -> Union[str, CharPtr]` | FileIO: Load text data
`SaveFileTextCallback` | `(fileName: 'Union[str, CharPtr]', text: 'Union[str, CharPtr]') -> bool` | FileIO: Save text data
`AudioCallback` | `(bufferData: 'bytes', frames: 'int') -> None` | *n/a*

[ <a href="#toc">ToC</a> ]

<h2 id="funcs">Functions</h2>

Item|Item|Item|Item|Item
--------|--------|--------|--------|--------
<a href="#AttachAudioStreamProcessor">AttachAudioStreamProcessor</a> | <a href="#BeginBlendMode">BeginBlendMode</a> | <a href="#BeginDrawing">BeginDrawing</a> | <a href="#BeginMode2D">BeginMode2D</a> | <a href="#BeginMode3D">BeginMode3D</a>
<a href="#BeginScissorMode">BeginScissorMode</a> | <a href="#BeginShaderMode">BeginShaderMode</a> | <a href="#BeginTextureMode">BeginTextureMode</a> | <a href="#BeginVrStereoMode">BeginVrStereoMode</a> | <a href="#ChangeDirectory">ChangeDirectory</a>
<a href="#CheckCollisionBoxSphere">CheckCollisionBoxSphere</a> | <a href="#CheckCollisionBoxes">CheckCollisionBoxes</a> | <a href="#CheckCollisionCircleRec">CheckCollisionCircleRec</a> | <a href="#CheckCollisionCircles">CheckCollisionCircles</a> | <a href="#CheckCollisionLines">CheckCollisionLines</a>
<a href="#CheckCollisionPointCircle">CheckCollisionPointCircle</a> | <a href="#CheckCollisionPointLine">CheckCollisionPointLine</a> | <a href="#CheckCollisionPointRec">CheckCollisionPointRec</a> | <a href="#CheckCollisionPointTriangle">CheckCollisionPointTriangle</a> | <a href="#CheckCollisionRecs">CheckCollisionRecs</a>
<a href="#CheckCollisionSpheres">CheckCollisionSpheres</a> | <a href="#Clamp">Clamp</a> | <a href="#ClearBackground">ClearBackground</a> | <a href="#ClearWindowState">ClearWindowState</a> | <a href="#CloseAudioDevice">CloseAudioDevice</a>
<a href="#CloseWindow">CloseWindow</a> | <a href="#CodepointToUTF8">CodepointToUTF8</a> | <a href="#ColorAlpha">ColorAlpha</a> | <a href="#ColorAlphaBlend">ColorAlphaBlend</a> | <a href="#ColorFromHSV">ColorFromHSV</a>
<a href="#ColorFromNormalized">ColorFromNormalized</a> | <a href="#ColorNormalize">ColorNormalize</a> | <a href="#ColorToHSV">ColorToHSV</a> | <a href="#ColorToInt">ColorToInt</a> | <a href="#CompressData">CompressData</a>
<a href="#DecodeDataBase64">DecodeDataBase64</a> | <a href="#DecompressData">DecompressData</a> | <a href="#DetachAudioStreamProcessor">DetachAudioStreamProcessor</a> | <a href="#DirectoryExists">DirectoryExists</a> | <a href="#DisableCursor">DisableCursor</a>
<a href="#DisableEventWaiting">DisableEventWaiting</a> | <a href="#DrawBillboard">DrawBillboard</a> | <a href="#DrawBillboardPro">DrawBillboardPro</a> | <a href="#DrawBillboardRec">DrawBillboardRec</a> | <a href="#DrawBoundingBox">DrawBoundingBox</a>
<a href="#DrawCircle">DrawCircle</a> | <a href="#DrawCircle3D">DrawCircle3D</a> | <a href="#DrawCircleGradient">DrawCircleGradient</a> | <a href="#DrawCircleLines">DrawCircleLines</a> | <a href="#DrawCircleSector">DrawCircleSector</a>
<a href="#DrawCircleSectorLines">DrawCircleSectorLines</a> | <a href="#DrawCircleV">DrawCircleV</a> | <a href="#DrawCube">DrawCube</a> | <a href="#DrawCubeTexture">DrawCubeTexture</a> | <a href="#DrawCubeTextureRec">DrawCubeTextureRec</a>
<a href="#DrawCubeV">DrawCubeV</a> | <a href="#DrawCubeWires">DrawCubeWires</a> | <a href="#DrawCubeWiresV">DrawCubeWiresV</a> | <a href="#DrawCylinder">DrawCylinder</a> | <a href="#DrawCylinderEx">DrawCylinderEx</a>
<a href="#DrawCylinderWires">DrawCylinderWires</a> | <a href="#DrawCylinderWiresEx">DrawCylinderWiresEx</a> | <a href="#DrawEllipse">DrawEllipse</a> | <a href="#DrawEllipseLines">DrawEllipseLines</a> | <a href="#DrawFPS">DrawFPS</a>
<a href="#DrawGrid">DrawGrid</a> | <a href="#DrawLine">DrawLine</a> | <a href="#DrawLine3D">DrawLine3D</a> | <a href="#DrawLineBezier">DrawLineBezier</a> | <a href="#DrawLineBezierCubic">DrawLineBezierCubic</a>
<a href="#DrawLineBezierQuad">DrawLineBezierQuad</a> | <a href="#DrawLineEx">DrawLineEx</a> | <a href="#DrawLineStrip">DrawLineStrip</a> | <a href="#DrawLineV">DrawLineV</a> | <a href="#DrawMesh">DrawMesh</a>
<a href="#DrawMeshInstanced">DrawMeshInstanced</a> | <a href="#DrawModel">DrawModel</a> | <a href="#DrawModelEx">DrawModelEx</a> | <a href="#DrawModelWires">DrawModelWires</a> | <a href="#DrawModelWiresEx">DrawModelWiresEx</a>
<a href="#DrawPixel">DrawPixel</a> | <a href="#DrawPixelV">DrawPixelV</a> | <a href="#DrawPlane">DrawPlane</a> | <a href="#DrawPoint3D">DrawPoint3D</a> | <a href="#DrawPoly">DrawPoly</a>
<a href="#DrawPolyLines">DrawPolyLines</a> | <a href="#DrawPolyLinesEx">DrawPolyLinesEx</a> | <a href="#DrawRay">DrawRay</a> | <a href="#DrawRectangle">DrawRectangle</a> | <a href="#DrawRectangleGradientEx">DrawRectangleGradientEx</a>
<a href="#DrawRectangleGradientH">DrawRectangleGradientH</a> | <a href="#DrawRectangleGradientV">DrawRectangleGradientV</a> | <a href="#DrawRectangleLines">DrawRectangleLines</a> | <a href="#DrawRectangleLinesEx">DrawRectangleLinesEx</a> | <a href="#DrawRectanglePro">DrawRectanglePro</a>
<a href="#DrawRectangleRec">DrawRectangleRec</a> | <a href="#DrawRectangleRounded">DrawRectangleRounded</a> | <a href="#DrawRectangleRoundedLines">DrawRectangleRoundedLines</a> | <a href="#DrawRectangleV">DrawRectangleV</a> | <a href="#DrawRing">DrawRing</a>
<a href="#DrawRingLines">DrawRingLines</a> | <a href="#DrawSphere">DrawSphere</a> | <a href="#DrawSphereEx">DrawSphereEx</a> | <a href="#DrawSphereWires">DrawSphereWires</a> | <a href="#DrawText">DrawText</a>
<a href="#DrawTextCodepoint">DrawTextCodepoint</a> | <a href="#DrawTextCodepoints">DrawTextCodepoints</a> | <a href="#DrawTextEx">DrawTextEx</a> | <a href="#DrawTextPro">DrawTextPro</a> | <a href="#DrawTexture">DrawTexture</a>
<a href="#DrawTextureEx">DrawTextureEx</a> | <a href="#DrawTextureNPatch">DrawTextureNPatch</a> | <a href="#DrawTexturePoly">DrawTexturePoly</a> | <a href="#DrawTexturePro">DrawTexturePro</a> | <a href="#DrawTextureQuad">DrawTextureQuad</a>
<a href="#DrawTextureRec">DrawTextureRec</a> | <a href="#DrawTextureTiled">DrawTextureTiled</a> | <a href="#DrawTextureV">DrawTextureV</a> | <a href="#DrawTriangle">DrawTriangle</a> | <a href="#DrawTriangle3D">DrawTriangle3D</a>
<a href="#DrawTriangleFan">DrawTriangleFan</a> | <a href="#DrawTriangleLines">DrawTriangleLines</a> | <a href="#DrawTriangleStrip">DrawTriangleStrip</a> | <a href="#DrawTriangleStrip3D">DrawTriangleStrip3D</a> | <a href="#EnableCursor">EnableCursor</a>
<a href="#EnableEventWaiting">EnableEventWaiting</a> | <a href="#EncodeDataBase64">EncodeDataBase64</a> | <a href="#EndBlendMode">EndBlendMode</a> | <a href="#EndDrawing">EndDrawing</a> | <a href="#EndMode2D">EndMode2D</a>
<a href="#EndMode3D">EndMode3D</a> | <a href="#EndScissorMode">EndScissorMode</a> | <a href="#EndShaderMode">EndShaderMode</a> | <a href="#EndTextureMode">EndTextureMode</a> | <a href="#EndVrStereoMode">EndVrStereoMode</a>
<a href="#ExportDataAsCode">ExportDataAsCode</a> | <a href="#ExportFontAsCode">ExportFontAsCode</a> | <a href="#ExportImage">ExportImage</a> | <a href="#ExportImageAsCode">ExportImageAsCode</a> | <a href="#ExportMesh">ExportMesh</a>
<a href="#ExportWave">ExportWave</a> | <a href="#ExportWaveAsCode">ExportWaveAsCode</a> | <a href="#Fade">Fade</a> | <a href="#FileExists">FileExists</a> | <a href="#FloatEquals">FloatEquals</a>
<a href="#GenImageCellular">GenImageCellular</a> | <a href="#GenImageChecked">GenImageChecked</a> | <a href="#GenImageColor">GenImageColor</a> | <a href="#GenImageFontAtlas">GenImageFontAtlas</a> | <a href="#GenImageGradientH">GenImageGradientH</a>
<a href="#GenImageGradientRadial">GenImageGradientRadial</a> | <a href="#GenImageGradientV">GenImageGradientV</a> | <a href="#GenImageWhiteNoise">GenImageWhiteNoise</a> | <a href="#GenMeshCone">GenMeshCone</a> | <a href="#GenMeshCube">GenMeshCube</a>
<a href="#GenMeshCubicmap">GenMeshCubicmap</a> | <a href="#GenMeshCylinder">GenMeshCylinder</a> | <a href="#GenMeshHeightmap">GenMeshHeightmap</a> | <a href="#GenMeshHemiSphere">GenMeshHemiSphere</a> | <a href="#GenMeshKnot">GenMeshKnot</a>
<a href="#GenMeshPlane">GenMeshPlane</a> | <a href="#GenMeshPoly">GenMeshPoly</a> | <a href="#GenMeshSphere">GenMeshSphere</a> | <a href="#GenMeshTangents">GenMeshTangents</a> | <a href="#GenMeshTorus">GenMeshTorus</a>
<a href="#GenTextureMipmaps">GenTextureMipmaps</a> | <a href="#GetApplicationDirectory">GetApplicationDirectory</a> | <a href="#GetCameraMatrix">GetCameraMatrix</a> | <a href="#GetCameraMatrix2D">GetCameraMatrix2D</a> | <a href="#GetCharPressed">GetCharPressed</a>
<a href="#GetClipboardText">GetClipboardText</a> | <a href="#GetCodepoint">GetCodepoint</a> | <a href="#GetCodepointCount">GetCodepointCount</a> | <a href="#GetCollisionRec">GetCollisionRec</a> | <a href="#GetColor">GetColor</a>
<a href="#GetCurrentMonitor">GetCurrentMonitor</a> | <a href="#GetDirectoryPath">GetDirectoryPath</a> | <a href="#GetFPS">GetFPS</a> | <a href="#GetFileExtension">GetFileExtension</a> | <a href="#GetFileLength">GetFileLength</a>
<a href="#GetFileModTime">GetFileModTime</a> | <a href="#GetFileName">GetFileName</a> | <a href="#GetFileNameWithoutExt">GetFileNameWithoutExt</a> | <a href="#GetFontDefault">GetFontDefault</a> | <a href="#GetFrameTime">GetFrameTime</a>
<a href="#GetGamepadAxisCount">GetGamepadAxisCount</a> | <a href="#GetGamepadAxisMovement">GetGamepadAxisMovement</a> | <a href="#GetGamepadButtonPressed">GetGamepadButtonPressed</a> | <a href="#GetGamepadName">GetGamepadName</a> | <a href="#GetGestureDetected">GetGestureDetected</a>
<a href="#GetGestureDragAngle">GetGestureDragAngle</a> | <a href="#GetGestureDragVector">GetGestureDragVector</a> | <a href="#GetGestureHoldDuration">GetGestureHoldDuration</a> | <a href="#GetGesturePinchAngle">GetGesturePinchAngle</a> | <a href="#GetGesturePinchVector">GetGesturePinchVector</a>
<a href="#GetGlyphAtlasRec">GetGlyphAtlasRec</a> | <a href="#GetGlyphIndex">GetGlyphIndex</a> | <a href="#GetGlyphInfo">GetGlyphInfo</a> | <a href="#GetImageAlphaBorder">GetImageAlphaBorder</a> | <a href="#GetImageColor">GetImageColor</a>
<a href="#GetKeyPressed">GetKeyPressed</a> | <a href="#GetMeshBoundingBox">GetMeshBoundingBox</a> | <a href="#GetModelBoundingBox">GetModelBoundingBox</a> | <a href="#GetMonitorCount">GetMonitorCount</a> | <a href="#GetMonitorHeight">GetMonitorHeight</a>
<a href="#GetMonitorName">GetMonitorName</a> | <a href="#GetMonitorPhysicalHeight">GetMonitorPhysicalHeight</a> | <a href="#GetMonitorPhysicalWidth">GetMonitorPhysicalWidth</a> | <a href="#GetMonitorPosition">GetMonitorPosition</a> | <a href="#GetMonitorRefreshRate">GetMonitorRefreshRate</a>
<a href="#GetMonitorWidth">GetMonitorWidth</a> | <a href="#GetMouseDelta">GetMouseDelta</a> | <a href="#GetMousePosition">GetMousePosition</a> | <a href="#GetMouseRay">GetMouseRay</a> | <a href="#GetMouseWheelMove">GetMouseWheelMove</a>
<a href="#GetMouseWheelMoveV">GetMouseWheelMoveV</a> | <a href="#GetMouseX">GetMouseX</a> | <a href="#GetMouseY">GetMouseY</a> | <a href="#GetMusicTimeLength">GetMusicTimeLength</a> | <a href="#GetMusicTimePlayed">GetMusicTimePlayed</a>
<a href="#GetPixelColor">GetPixelColor</a> | <a href="#GetPixelDataSize">GetPixelDataSize</a> | <a href="#GetPrevDirectoryPath">GetPrevDirectoryPath</a> | <a href="#GetRandomValue">GetRandomValue</a> | <a href="#GetRayCollisionBox">GetRayCollisionBox</a>
<a href="#GetRayCollisionMesh">GetRayCollisionMesh</a> | <a href="#GetRayCollisionQuad">GetRayCollisionQuad</a> | <a href="#GetRayCollisionSphere">GetRayCollisionSphere</a> | <a href="#GetRayCollisionTriangle">GetRayCollisionTriangle</a> | <a href="#GetRenderHeight">GetRenderHeight</a>
<a href="#GetRenderWidth">GetRenderWidth</a> | <a href="#GetScreenHeight">GetScreenHeight</a> | <a href="#GetScreenToWorld2D">GetScreenToWorld2D</a> | <a href="#GetScreenWidth">GetScreenWidth</a> | <a href="#GetShaderLocation">GetShaderLocation</a>
<a href="#GetShaderLocationAttrib">GetShaderLocationAttrib</a> | <a href="#GetSoundsPlaying">GetSoundsPlaying</a> | <a href="#GetTime">GetTime</a> | <a href="#GetTouchPointCount">GetTouchPointCount</a> | <a href="#GetTouchPointId">GetTouchPointId</a>
<a href="#GetTouchPosition">GetTouchPosition</a> | <a href="#GetTouchX">GetTouchX</a> | <a href="#GetTouchY">GetTouchY</a> | <a href="#GetWindowHandle">GetWindowHandle</a> | <a href="#GetWindowPosition">GetWindowPosition</a>
<a href="#GetWindowScaleDPI">GetWindowScaleDPI</a> | <a href="#GetWorkingDirectory">GetWorkingDirectory</a> | <a href="#GetWorldToScreen">GetWorldToScreen</a> | <a href="#GetWorldToScreen2D">GetWorldToScreen2D</a> | <a href="#GetWorldToScreenEx">GetWorldToScreenEx</a>
<a href="#HideCursor">HideCursor</a> | <a href="#ImageAlphaClear">ImageAlphaClear</a> | <a href="#ImageAlphaCrop">ImageAlphaCrop</a> | <a href="#ImageAlphaMask">ImageAlphaMask</a> | <a href="#ImageAlphaPremultiply">ImageAlphaPremultiply</a>
<a href="#ImageClearBackground">ImageClearBackground</a> | <a href="#ImageColorBrightness">ImageColorBrightness</a> | <a href="#ImageColorContrast">ImageColorContrast</a> | <a href="#ImageColorGrayscale">ImageColorGrayscale</a> | <a href="#ImageColorInvert">ImageColorInvert</a>
<a href="#ImageColorReplace">ImageColorReplace</a> | <a href="#ImageColorTint">ImageColorTint</a> | <a href="#ImageCopy">ImageCopy</a> | <a href="#ImageCrop">ImageCrop</a> | <a href="#ImageDither">ImageDither</a>
<a href="#ImageDraw">ImageDraw</a> | <a href="#ImageDrawCircle">ImageDrawCircle</a> | <a href="#ImageDrawCircleV">ImageDrawCircleV</a> | <a href="#ImageDrawLine">ImageDrawLine</a> | <a href="#ImageDrawLineV">ImageDrawLineV</a>
<a href="#ImageDrawPixel">ImageDrawPixel</a> | <a href="#ImageDrawPixelV">ImageDrawPixelV</a> | <a href="#ImageDrawRectangle">ImageDrawRectangle</a> | <a href="#ImageDrawRectangleLines">ImageDrawRectangleLines</a> | <a href="#ImageDrawRectangleRec">ImageDrawRectangleRec</a>
<a href="#ImageDrawRectangleV">ImageDrawRectangleV</a> | <a href="#ImageDrawText">ImageDrawText</a> | <a href="#ImageDrawTextEx">ImageDrawTextEx</a> | <a href="#ImageFlipHorizontal">ImageFlipHorizontal</a> | <a href="#ImageFlipVertical">ImageFlipVertical</a>
<a href="#ImageFormat">ImageFormat</a> | <a href="#ImageFromImage">ImageFromImage</a> | <a href="#ImageMipmaps">ImageMipmaps</a> | <a href="#ImageResize">ImageResize</a> | <a href="#ImageResizeCanvas">ImageResizeCanvas</a>
<a href="#ImageResizeNN">ImageResizeNN</a> | <a href="#ImageRotateCCW">ImageRotateCCW</a> | <a href="#ImageRotateCW">ImageRotateCW</a> | <a href="#ImageText">ImageText</a> | <a href="#ImageTextEx">ImageTextEx</a>
<a href="#ImageToPOT">ImageToPOT</a> | <a href="#InitAudioDevice">InitAudioDevice</a> | <a href="#InitWindow">InitWindow</a> | <a href="#IsAudioDeviceReady">IsAudioDeviceReady</a> | <a href="#IsAudioStreamPlaying">IsAudioStreamPlaying</a>
<a href="#IsAudioStreamProcessed">IsAudioStreamProcessed</a> | <a href="#IsCursorHidden">IsCursorHidden</a> | <a href="#IsCursorOnScreen">IsCursorOnScreen</a> | <a href="#IsFileDropped">IsFileDropped</a> | <a href="#IsFileExtension">IsFileExtension</a>
<a href="#IsGamepadAvailable">IsGamepadAvailable</a> | <a href="#IsGamepadButtonDown">IsGamepadButtonDown</a> | <a href="#IsGamepadButtonPressed">IsGamepadButtonPressed</a> | <a href="#IsGamepadButtonReleased">IsGamepadButtonReleased</a> | <a href="#IsGamepadButtonUp">IsGamepadButtonUp</a>
<a href="#IsGestureDetected">IsGestureDetected</a> | <a href="#IsKeyDown">IsKeyDown</a> | <a href="#IsKeyPressed">IsKeyPressed</a> | <a href="#IsKeyReleased">IsKeyReleased</a> | <a href="#IsKeyUp">IsKeyUp</a>
<a href="#IsModelAnimationValid">IsModelAnimationValid</a> | <a href="#IsMouseButtonDown">IsMouseButtonDown</a> | <a href="#IsMouseButtonPressed">IsMouseButtonPressed</a> | <a href="#IsMouseButtonReleased">IsMouseButtonReleased</a> | <a href="#IsMouseButtonUp">IsMouseButtonUp</a>
<a href="#IsMusicStreamPlaying">IsMusicStreamPlaying</a> | <a href="#IsPathFile">IsPathFile</a> | <a href="#IsSoundPlaying">IsSoundPlaying</a> | <a href="#IsWindowFocused">IsWindowFocused</a> | <a href="#IsWindowFullscreen">IsWindowFullscreen</a>
<a href="#IsWindowHidden">IsWindowHidden</a> | <a href="#IsWindowMaximized">IsWindowMaximized</a> | <a href="#IsWindowMinimized">IsWindowMinimized</a> | <a href="#IsWindowReady">IsWindowReady</a> | <a href="#IsWindowResized">IsWindowResized</a>
<a href="#IsWindowState">IsWindowState</a> | <a href="#Lerp">Lerp</a> | <a href="#LoadAudioStream">LoadAudioStream</a> | <a href="#LoadCodepoints">LoadCodepoints</a> | <a href="#LoadDirectoryFiles">LoadDirectoryFiles</a>
<a href="#LoadDirectoryFilesEx">LoadDirectoryFilesEx</a> | <a href="#LoadDroppedFiles">LoadDroppedFiles</a> | <a href="#LoadFileData">LoadFileData</a> | <a href="#LoadFileText">LoadFileText</a> | <a href="#LoadFont">LoadFont</a>
<a href="#LoadFontData">LoadFontData</a> | <a href="#LoadFontEx">LoadFontEx</a> | <a href="#LoadFontFromImage">LoadFontFromImage</a> | <a href="#LoadFontFromMemory">LoadFontFromMemory</a> | <a href="#LoadImage">LoadImage</a>
<a href="#LoadImageAnim">LoadImageAnim</a> | <a href="#LoadImageColors">LoadImageColors</a> | <a href="#LoadImageFromMemory">LoadImageFromMemory</a> | <a href="#LoadImageFromScreen">LoadImageFromScreen</a> | <a href="#LoadImageFromTexture">LoadImageFromTexture</a>
<a href="#LoadImagePalette">LoadImagePalette</a> | <a href="#LoadImageRaw">LoadImageRaw</a> | <a href="#LoadMaterialDefault">LoadMaterialDefault</a> | <a href="#LoadMaterials">LoadMaterials</a> | <a href="#LoadModel">LoadModel</a>
<a href="#LoadModelAnimations">LoadModelAnimations</a> | <a href="#LoadModelFromMesh">LoadModelFromMesh</a> | <a href="#LoadMusicStream">LoadMusicStream</a> | <a href="#LoadMusicStreamFromMemory">LoadMusicStreamFromMemory</a> | <a href="#LoadRenderTexture">LoadRenderTexture</a>
<a href="#LoadShader">LoadShader</a> | <a href="#LoadShaderFromMemory">LoadShaderFromMemory</a> | <a href="#LoadSound">LoadSound</a> | <a href="#LoadSoundFromWave">LoadSoundFromWave</a> | <a href="#LoadTexture">LoadTexture</a>
<a href="#LoadTextureCubemap">LoadTextureCubemap</a> | <a href="#LoadTextureFromImage">LoadTextureFromImage</a> | <a href="#LoadVrStereoConfig">LoadVrStereoConfig</a> | <a href="#LoadWave">LoadWave</a> | <a href="#LoadWaveFromMemory">LoadWaveFromMemory</a>
<a href="#LoadWaveSamples">LoadWaveSamples</a> | <a href="#MatrixAdd">MatrixAdd</a> | <a href="#MatrixDeterminant">MatrixDeterminant</a> | <a href="#MatrixFrustum">MatrixFrustum</a> | <a href="#MatrixIdentity">MatrixIdentity</a>
<a href="#MatrixInvert">MatrixInvert</a> | <a href="#MatrixLookAt">MatrixLookAt</a> | <a href="#MatrixMultiply">MatrixMultiply</a> | <a href="#MatrixOrtho">MatrixOrtho</a> | <a href="#MatrixPerspective">MatrixPerspective</a>
<a href="#MatrixRotate">MatrixRotate</a> | <a href="#MatrixRotateX">MatrixRotateX</a> | <a href="#MatrixRotateXYZ">MatrixRotateXYZ</a> | <a href="#MatrixRotateY">MatrixRotateY</a> | <a href="#MatrixRotateZ">MatrixRotateZ</a>
<a href="#MatrixRotateZYX">MatrixRotateZYX</a> | <a href="#MatrixScale">MatrixScale</a> | <a href="#MatrixSubtract">MatrixSubtract</a> | <a href="#MatrixToFloatV">MatrixToFloatV</a> | <a href="#MatrixTrace">MatrixTrace</a>
<a href="#MatrixTranslate">MatrixTranslate</a> | <a href="#MatrixTranspose">MatrixTranspose</a> | <a href="#MaximizeWindow">MaximizeWindow</a> | <a href="#MeasureText">MeasureText</a> | <a href="#MeasureTextEx">MeasureTextEx</a>
<a href="#MemAlloc">MemAlloc</a> | <a href="#MemFree">MemFree</a> | <a href="#MemRealloc">MemRealloc</a> | <a href="#MinimizeWindow">MinimizeWindow</a> | <a href="#Normalize">Normalize</a>
<a href="#OpenURL">OpenURL</a> | <a href="#PauseAudioStream">PauseAudioStream</a> | <a href="#PauseMusicStream">PauseMusicStream</a> | <a href="#PauseSound">PauseSound</a> | <a href="#PlayAudioStream">PlayAudioStream</a>
<a href="#PlayMusicStream">PlayMusicStream</a> | <a href="#PlaySound">PlaySound</a> | <a href="#PlaySoundMulti">PlaySoundMulti</a> | <a href="#PollInputEvents">PollInputEvents</a> | <a href="#QuaternionAdd">QuaternionAdd</a>
<a href="#QuaternionAddValue">QuaternionAddValue</a> | <a href="#QuaternionDivide">QuaternionDivide</a> | <a href="#QuaternionEquals">QuaternionEquals</a> | <a href="#QuaternionFromAxisAngle">QuaternionFromAxisAngle</a> | <a href="#QuaternionFromEuler">QuaternionFromEuler</a>
<a href="#QuaternionFromMatrix">QuaternionFromMatrix</a> | <a href="#QuaternionFromVector3ToVector3">QuaternionFromVector3ToVector3</a> | <a href="#QuaternionIdentity">QuaternionIdentity</a> | <a href="#QuaternionInvert">QuaternionInvert</a> | <a href="#QuaternionLength">QuaternionLength</a>
<a href="#QuaternionMultiply">QuaternionMultiply</a> | <a href="#QuaternionNlerp">QuaternionNlerp</a> | <a href="#QuaternionNormalize">QuaternionNormalize</a> | <a href="#QuaternionScale">QuaternionScale</a> | <a href="#QuaternionSlerp">QuaternionSlerp</a>
<a href="#QuaternionSubtract">QuaternionSubtract</a> | <a href="#QuaternionSubtractValue">QuaternionSubtractValue</a> | <a href="#QuaternionToAxisAngle">QuaternionToAxisAngle</a> | <a href="#QuaternionToEuler">QuaternionToEuler</a> | <a href="#QuaternionToMatrix">QuaternionToMatrix</a>
<a href="#QuaternionTransform">QuaternionTransform</a> | <a href="#Remap">Remap</a> | <a href="#RestoreWindow">RestoreWindow</a> | <a href="#ResumeAudioStream">ResumeAudioStream</a> | <a href="#ResumeMusicStream">ResumeMusicStream</a>
<a href="#ResumeSound">ResumeSound</a> | <a href="#SaveFileData">SaveFileData</a> | <a href="#SaveFileText">SaveFileText</a> | <a href="#SeekMusicStream">SeekMusicStream</a> | <a href="#SetAudioStreamBufferSizeDefault">SetAudioStreamBufferSizeDefault</a>
<a href="#SetAudioStreamCallback">SetAudioStreamCallback</a> | <a href="#SetAudioStreamPan">SetAudioStreamPan</a> | <a href="#SetAudioStreamPitch">SetAudioStreamPitch</a> | <a href="#SetAudioStreamVolume">SetAudioStreamVolume</a> | <a href="#SetCameraAltControl">SetCameraAltControl</a>
<a href="#SetCameraMode">SetCameraMode</a> | <a href="#SetCameraMoveControls">SetCameraMoveControls</a> | <a href="#SetCameraPanControl">SetCameraPanControl</a> | <a href="#SetCameraSmoothZoomControl">SetCameraSmoothZoomControl</a> | <a href="#SetClipboardText">SetClipboardText</a>
<a href="#SetConfigFlags">SetConfigFlags</a> | <a href="#SetExitKey">SetExitKey</a> | <a href="#SetGamepadMappings">SetGamepadMappings</a> | <a href="#SetGesturesEnabled">SetGesturesEnabled</a> | <a href="#SetLoadFileDataCallback">SetLoadFileDataCallback</a>
<a href="#SetLoadFileTextCallback">SetLoadFileTextCallback</a> | <a href="#SetMasterVolume">SetMasterVolume</a> | <a href="#SetMaterialTexture">SetMaterialTexture</a> | <a href="#SetModelMeshMaterial">SetModelMeshMaterial</a> | <a href="#SetMouseCursor">SetMouseCursor</a>
<a href="#SetMouseOffset">SetMouseOffset</a> | <a href="#SetMousePosition">SetMousePosition</a> | <a href="#SetMouseScale">SetMouseScale</a> | <a href="#SetMusicPan">SetMusicPan</a> | <a href="#SetMusicPitch">SetMusicPitch</a>
<a href="#SetMusicVolume">SetMusicVolume</a> | <a href="#SetPixelColor">SetPixelColor</a> | <a href="#SetRandomSeed">SetRandomSeed</a> | <a href="#SetSaveFileDataCallback">SetSaveFileDataCallback</a> | <a href="#SetSaveFileTextCallback">SetSaveFileTextCallback</a>
<a href="#SetShaderValue">SetShaderValue</a> | <a href="#SetShaderValueMatrix">SetShaderValueMatrix</a> | <a href="#SetShaderValueTexture">SetShaderValueTexture</a> | <a href="#SetShaderValueV">SetShaderValueV</a> | <a href="#SetShapesTexture">SetShapesTexture</a>
<a href="#SetSoundPan">SetSoundPan</a> | <a href="#SetSoundPitch">SetSoundPitch</a> | <a href="#SetSoundVolume">SetSoundVolume</a> | <a href="#SetTargetFPS">SetTargetFPS</a> | <a href="#SetTextureFilter">SetTextureFilter</a>
<a href="#SetTextureWrap">SetTextureWrap</a> | <a href="#SetTraceLogCallback">SetTraceLogCallback</a> | <a href="#SetTraceLogLevel">SetTraceLogLevel</a> | <a href="#SetWindowIcon">SetWindowIcon</a> | <a href="#SetWindowMinSize">SetWindowMinSize</a>
<a href="#SetWindowMonitor">SetWindowMonitor</a> | <a href="#SetWindowOpacity">SetWindowOpacity</a> | <a href="#SetWindowPosition">SetWindowPosition</a> | <a href="#SetWindowSize">SetWindowSize</a> | <a href="#SetWindowState">SetWindowState</a>
<a href="#SetWindowTitle">SetWindowTitle</a> | <a href="#ShowCursor">ShowCursor</a> | <a href="#StopAudioStream">StopAudioStream</a> | <a href="#StopMusicStream">StopMusicStream</a> | <a href="#StopSound">StopSound</a>
<a href="#StopSoundMulti">StopSoundMulti</a> | <a href="#SwapScreenBuffer">SwapScreenBuffer</a> | <a href="#TakeScreenshot">TakeScreenshot</a> | <a href="#TextAppend">TextAppend</a> | <a href="#TextCodepointsToUTF8">TextCodepointsToUTF8</a>
<a href="#TextCopy">TextCopy</a> | <a href="#TextFindIndex">TextFindIndex</a> | <a href="#TextFormat">TextFormat</a> | <a href="#TextInsert">TextInsert</a> | <a href="#TextIsEqual">TextIsEqual</a>
<a href="#TextJoin">TextJoin</a> | <a href="#TextLength">TextLength</a> | <a href="#TextReplace">TextReplace</a> | <a href="#TextSplit">TextSplit</a> | <a href="#TextSubtext">TextSubtext</a>
<a href="#TextToInteger">TextToInteger</a> | <a href="#TextToLower">TextToLower</a> | <a href="#TextToPascal">TextToPascal</a> | <a href="#TextToUpper">TextToUpper</a> | <a href="#ToggleFullscreen">ToggleFullscreen</a>
<a href="#TraceLog">TraceLog</a> | <a href="#UnloadAudioStream">UnloadAudioStream</a> | <a href="#UnloadCodepoints">UnloadCodepoints</a> | <a href="#UnloadDirectoryFiles">UnloadDirectoryFiles</a> | <a href="#UnloadDroppedFiles">UnloadDroppedFiles</a>
<a href="#UnloadFileData">UnloadFileData</a> | <a href="#UnloadFileText">UnloadFileText</a> | <a href="#UnloadFont">UnloadFont</a> | <a href="#UnloadFontData">UnloadFontData</a> | <a href="#UnloadImage">UnloadImage</a>
<a href="#UnloadImageColors">UnloadImageColors</a> | <a href="#UnloadImagePalette">UnloadImagePalette</a> | <a href="#UnloadMaterial">UnloadMaterial</a> | <a href="#UnloadMesh">UnloadMesh</a> | <a href="#UnloadModel">UnloadModel</a>
<a href="#UnloadModelAnimation">UnloadModelAnimation</a> | <a href="#UnloadModelAnimations">UnloadModelAnimations</a> | <a href="#UnloadModelKeepMeshes">UnloadModelKeepMeshes</a> | <a href="#UnloadMusicStream">UnloadMusicStream</a> | <a href="#UnloadRenderTexture">UnloadRenderTexture</a>
<a href="#UnloadShader">UnloadShader</a> | <a href="#UnloadSound">UnloadSound</a> | <a href="#UnloadTexture">UnloadTexture</a> | <a href="#UnloadVrStereoConfig">UnloadVrStereoConfig</a> | <a href="#UnloadWave">UnloadWave</a>
<a href="#UnloadWaveSamples">UnloadWaveSamples</a> | <a href="#UpdateAudioStream">UpdateAudioStream</a> | <a href="#UpdateCamera">UpdateCamera</a> | <a href="#UpdateMeshBuffer">UpdateMeshBuffer</a> | <a href="#UpdateModelAnimation">UpdateModelAnimation</a>
<a href="#UpdateMusicStream">UpdateMusicStream</a> | <a href="#UpdateSound">UpdateSound</a> | <a href="#UpdateTexture">UpdateTexture</a> | <a href="#UpdateTextureRec">UpdateTextureRec</a> | <a href="#UploadMesh">UploadMesh</a>
<a href="#Vector2Add">Vector2Add</a> | <a href="#Vector2AddValue">Vector2AddValue</a> | <a href="#Vector2Angle">Vector2Angle</a> | <a href="#Vector2Clamp">Vector2Clamp</a> | <a href="#Vector2ClampValue">Vector2ClampValue</a>
<a href="#Vector2Distance">Vector2Distance</a> | <a href="#Vector2DistanceSqr">Vector2DistanceSqr</a> | <a href="#Vector2Divide">Vector2Divide</a> | <a href="#Vector2DotProduct">Vector2DotProduct</a> | <a href="#Vector2Equals">Vector2Equals</a>
<a href="#Vector2Invert">Vector2Invert</a> | <a href="#Vector2Length">Vector2Length</a> | <a href="#Vector2LengthSqr">Vector2LengthSqr</a> | <a href="#Vector2Lerp">Vector2Lerp</a> | <a href="#Vector2MoveTowards">Vector2MoveTowards</a>
<a href="#Vector2Multiply">Vector2Multiply</a> | <a href="#Vector2Negate">Vector2Negate</a> | <a href="#Vector2Normalize">Vector2Normalize</a> | <a href="#Vector2One">Vector2One</a> | <a href="#Vector2Reflect">Vector2Reflect</a>
<a href="#Vector2Rotate">Vector2Rotate</a> | <a href="#Vector2Scale">Vector2Scale</a> | <a href="#Vector2Subtract">Vector2Subtract</a> | <a href="#Vector2SubtractValue">Vector2SubtractValue</a> | <a href="#Vector2Transform">Vector2Transform</a>
<a href="#Vector2Zero">Vector2Zero</a> | <a href="#Vector3Add">Vector3Add</a> | <a href="#Vector3AddValue">Vector3AddValue</a> | <a href="#Vector3Angle">Vector3Angle</a> | <a href="#Vector3Barycenter">Vector3Barycenter</a>
<a href="#Vector3Clamp">Vector3Clamp</a> | <a href="#Vector3ClampValue">Vector3ClampValue</a> | <a href="#Vector3CrossProduct">Vector3CrossProduct</a> | <a href="#Vector3Distance">Vector3Distance</a> | <a href="#Vector3DistanceSqr">Vector3DistanceSqr</a>
<a href="#Vector3Divide">Vector3Divide</a> | <a href="#Vector3DotProduct">Vector3DotProduct</a> | <a href="#Vector3Equals">Vector3Equals</a> | <a href="#Vector3Invert">Vector3Invert</a> | <a href="#Vector3Length">Vector3Length</a>
<a href="#Vector3LengthSqr">Vector3LengthSqr</a> | <a href="#Vector3Lerp">Vector3Lerp</a> | <a href="#Vector3Max">Vector3Max</a> | <a href="#Vector3Min">Vector3Min</a> | <a href="#Vector3Multiply">Vector3Multiply</a>
<a href="#Vector3Negate">Vector3Negate</a> | <a href="#Vector3Normalize">Vector3Normalize</a> | <a href="#Vector3One">Vector3One</a> | <a href="#Vector3OrthoNormalize">Vector3OrthoNormalize</a> | <a href="#Vector3Perpendicular">Vector3Perpendicular</a>
<a href="#Vector3Reflect">Vector3Reflect</a> | <a href="#Vector3Refract">Vector3Refract</a> | <a href="#Vector3RotateByAxisAngle">Vector3RotateByAxisAngle</a> | <a href="#Vector3RotateByQuaternion">Vector3RotateByQuaternion</a> | <a href="#Vector3Scale">Vector3Scale</a>
<a href="#Vector3Subtract">Vector3Subtract</a> | <a href="#Vector3SubtractValue">Vector3SubtractValue</a> | <a href="#Vector3ToFloatV">Vector3ToFloatV</a> | <a href="#Vector3Transform">Vector3Transform</a> | <a href="#Vector3Unproject">Vector3Unproject</a>
<a href="#Vector3Zero">Vector3Zero</a> | <a href="#WaitTime">WaitTime</a> | <a href="#WaveCopy">WaveCopy</a> | <a href="#WaveCrop">WaveCrop</a> | <a href="#WaveFormat">WaveFormat</a>
<a href="#WindowShouldClose">WindowShouldClose</a> | <a href="#Wrap">Wrap</a> | <a href="#rlActiveDrawBuffers">rlActiveDrawBuffers</a> | <a href="#rlActiveTextureSlot">rlActiveTextureSlot</a> | <a href="#rlBegin">rlBegin</a>
<a href="#rlBindImageTexture">rlBindImageTexture</a> | <a href="#rlBindShaderBuffer">rlBindShaderBuffer</a> | <a href="#rlCheckErrors">rlCheckErrors</a> | <a href="#rlCheckRenderBatchLimit">rlCheckRenderBatchLimit</a> | <a href="#rlClearColor">rlClearColor</a>
<a href="#rlClearScreenBuffers">rlClearScreenBuffers</a> | <a href="#rlColor3f">rlColor3f</a> | <a href="#rlColor4f">rlColor4f</a> | <a href="#rlColor4ub">rlColor4ub</a> | <a href="#rlCompileShader">rlCompileShader</a>
<a href="#rlComputeShaderDispatch">rlComputeShaderDispatch</a> | <a href="#rlCopyBuffersElements">rlCopyBuffersElements</a> | <a href="#rlDisableBackfaceCulling">rlDisableBackfaceCulling</a> | <a href="#rlDisableColorBlend">rlDisableColorBlend</a> | <a href="#rlDisableDepthMask">rlDisableDepthMask</a>
<a href="#rlDisableDepthTest">rlDisableDepthTest</a> | <a href="#rlDisableFramebuffer">rlDisableFramebuffer</a> | <a href="#rlDisableScissorTest">rlDisableScissorTest</a> | <a href="#rlDisableShader">rlDisableShader</a> | <a href="#rlDisableSmoothLines">rlDisableSmoothLines</a>
<a href="#rlDisableStereoRender">rlDisableStereoRender</a> | <a href="#rlDisableTexture">rlDisableTexture</a> | <a href="#rlDisableTextureCubemap">rlDisableTextureCubemap</a> | <a href="#rlDisableVertexArray">rlDisableVertexArray</a> | <a href="#rlDisableVertexAttribute">rlDisableVertexAttribute</a>
<a href="#rlDisableVertexBuffer">rlDisableVertexBuffer</a> | <a href="#rlDisableVertexBufferElement">rlDisableVertexBufferElement</a> | <a href="#rlDisableWireMode">rlDisableWireMode</a> | <a href="#rlDrawRenderBatch">rlDrawRenderBatch</a> | <a href="#rlDrawRenderBatchActive">rlDrawRenderBatchActive</a>
<a href="#rlDrawVertexArray">rlDrawVertexArray</a> | <a href="#rlDrawVertexArrayElements">rlDrawVertexArrayElements</a> | <a href="#rlDrawVertexArrayElementsInstanced">rlDrawVertexArrayElementsInstanced</a> | <a href="#rlDrawVertexArrayInstanced">rlDrawVertexArrayInstanced</a> | <a href="#rlEnableBackfaceCulling">rlEnableBackfaceCulling</a>
<a href="#rlEnableColorBlend">rlEnableColorBlend</a> | <a href="#rlEnableDepthMask">rlEnableDepthMask</a> | <a href="#rlEnableDepthTest">rlEnableDepthTest</a> | <a href="#rlEnableFramebuffer">rlEnableFramebuffer</a> | <a href="#rlEnableScissorTest">rlEnableScissorTest</a>
<a href="#rlEnableShader">rlEnableShader</a> | <a href="#rlEnableSmoothLines">rlEnableSmoothLines</a> | <a href="#rlEnableStereoRender">rlEnableStereoRender</a> | <a href="#rlEnableTexture">rlEnableTexture</a> | <a href="#rlEnableTextureCubemap">rlEnableTextureCubemap</a>
<a href="#rlEnableVertexArray">rlEnableVertexArray</a> | <a href="#rlEnableVertexAttribute">rlEnableVertexAttribute</a> | <a href="#rlEnableVertexBuffer">rlEnableVertexBuffer</a> | <a href="#rlEnableVertexBufferElement">rlEnableVertexBufferElement</a> | <a href="#rlEnableWireMode">rlEnableWireMode</a>
<a href="#rlEnd">rlEnd</a> | <a href="#rlFramebufferAttach">rlFramebufferAttach</a> | <a href="#rlFramebufferComplete">rlFramebufferComplete</a> | <a href="#rlFrustum">rlFrustum</a> | <a href="#rlGenTextureMipmaps">rlGenTextureMipmaps</a>
<a href="#rlGetFramebufferHeight">rlGetFramebufferHeight</a> | <a href="#rlGetFramebufferWidth">rlGetFramebufferWidth</a> | <a href="#rlGetGlTextureFormats">rlGetGlTextureFormats</a> | <a href="#rlGetLineWidth">rlGetLineWidth</a> | <a href="#rlGetLocationAttrib">rlGetLocationAttrib</a>
<a href="#rlGetLocationUniform">rlGetLocationUniform</a> | <a href="#rlGetMatrixModelview">rlGetMatrixModelview</a> | <a href="#rlGetMatrixProjection">rlGetMatrixProjection</a> | <a href="#rlGetMatrixProjectionStereo">rlGetMatrixProjectionStereo</a> | <a href="#rlGetMatrixTransform">rlGetMatrixTransform</a>
<a href="#rlGetMatrixViewOffsetStereo">rlGetMatrixViewOffsetStereo</a> | <a href="#rlGetPixelFormatName">rlGetPixelFormatName</a> | <a href="#rlGetShaderBufferSize">rlGetShaderBufferSize</a> | <a href="#rlGetShaderIdDefault">rlGetShaderIdDefault</a> | <a href="#rlGetShaderLocsDefault">rlGetShaderLocsDefault</a>
<a href="#rlGetTextureIdDefault">rlGetTextureIdDefault</a> | <a href="#rlGetVersion">rlGetVersion</a> | <a href="#rlIsStereoRenderEnabled">rlIsStereoRenderEnabled</a> | <a href="#rlLoadComputeShaderProgram">rlLoadComputeShaderProgram</a> | <a href="#rlLoadDrawCube">rlLoadDrawCube</a>
<a href="#rlLoadDrawQuad">rlLoadDrawQuad</a> | <a href="#rlLoadExtensions">rlLoadExtensions</a> | <a href="#rlLoadFramebuffer">rlLoadFramebuffer</a> | <a href="#rlLoadIdentity">rlLoadIdentity</a> | <a href="#rlLoadRenderBatch">rlLoadRenderBatch</a>
<a href="#rlLoadShaderBuffer">rlLoadShaderBuffer</a> | <a href="#rlLoadShaderCode">rlLoadShaderCode</a> | <a href="#rlLoadShaderProgram">rlLoadShaderProgram</a> | <a href="#rlLoadTexture">rlLoadTexture</a> | <a href="#rlLoadTextureCubemap">rlLoadTextureCubemap</a>
<a href="#rlLoadTextureDepth">rlLoadTextureDepth</a> | <a href="#rlLoadVertexArray">rlLoadVertexArray</a> | <a href="#rlLoadVertexBuffer">rlLoadVertexBuffer</a> | <a href="#rlLoadVertexBufferElement">rlLoadVertexBufferElement</a> | <a href="#rlMatrixMode">rlMatrixMode</a>
<a href="#rlMultMatrixf">rlMultMatrixf</a> | <a href="#rlNormal3f">rlNormal3f</a> | <a href="#rlOrtho">rlOrtho</a> | <a href="#rlPopMatrix">rlPopMatrix</a> | <a href="#rlPushMatrix">rlPushMatrix</a>
<a href="#rlReadScreenPixels">rlReadScreenPixels</a> | <a href="#rlReadShaderBufferElements">rlReadShaderBufferElements</a> | <a href="#rlReadTexturePixels">rlReadTexturePixels</a> | <a href="#rlRotatef">rlRotatef</a> | <a href="#rlScalef">rlScalef</a>
<a href="#rlScissor">rlScissor</a> | <a href="#rlSetBlendFactors">rlSetBlendFactors</a> | <a href="#rlSetBlendMode">rlSetBlendMode</a> | <a href="#rlSetFramebufferHeight">rlSetFramebufferHeight</a> | <a href="#rlSetFramebufferWidth">rlSetFramebufferWidth</a>
<a href="#rlSetLineWidth">rlSetLineWidth</a> | <a href="#rlSetMatrixModelview">rlSetMatrixModelview</a> | <a href="#rlSetMatrixProjection">rlSetMatrixProjection</a> | <a href="#rlSetMatrixProjectionStereo">rlSetMatrixProjectionStereo</a> | <a href="#rlSetMatrixViewOffsetStereo">rlSetMatrixViewOffsetStereo</a>
<a href="#rlSetRenderBatchActive">rlSetRenderBatchActive</a> | <a href="#rlSetShader">rlSetShader</a> | <a href="#rlSetTexture">rlSetTexture</a> | <a href="#rlSetUniform">rlSetUniform</a> | <a href="#rlSetUniformMatrix">rlSetUniformMatrix</a>
<a href="#rlSetUniformSampler">rlSetUniformSampler</a> | <a href="#rlSetVertexAttribute">rlSetVertexAttribute</a> | <a href="#rlSetVertexAttributeDefault">rlSetVertexAttributeDefault</a> | <a href="#rlSetVertexAttributeDivisor">rlSetVertexAttributeDivisor</a> | <a href="#rlTexCoord2f">rlTexCoord2f</a>
<a href="#rlTextureParameters">rlTextureParameters</a> | <a href="#rlTranslatef">rlTranslatef</a> | <a href="#rlUnloadFramebuffer">rlUnloadFramebuffer</a> | <a href="#rlUnloadRenderBatch">rlUnloadRenderBatch</a> | <a href="#rlUnloadShaderBuffer">rlUnloadShaderBuffer</a>
<a href="#rlUnloadShaderProgram">rlUnloadShaderProgram</a> | <a href="#rlUnloadTexture">rlUnloadTexture</a> | <a href="#rlUnloadVertexArray">rlUnloadVertexArray</a> | <a href="#rlUnloadVertexBuffer">rlUnloadVertexBuffer</a> | <a href="#rlUpdateShaderBufferElements">rlUpdateShaderBufferElements</a>
<a href="#rlUpdateTexture">rlUpdateTexture</a> | <a href="#rlUpdateVertexBuffer">rlUpdateVertexBuffer</a> | <a href="#rlUpdateVertexBufferElements">rlUpdateVertexBufferElements</a> | <a href="#rlVertex2f">rlVertex2f</a> | <a href="#rlVertex2i">rlVertex2i</a>
<a href="#rlVertex3f">rlVertex3f</a> | <a href="#rlViewport">rlViewport</a> | <a href="#rlglClose">rlglClose</a> | <a href="#rlglInit">rlglInit</a>

[ <a href="#toc">ToC</a> ]

<h2 id="InitWindow"><code>InitWindow</code> function</h2>

> Initialize window and OpenGL context

Defined in raylib.h:

```c
void InitWindow(int width, int height, char * title) 
```

Python wrapper:

```python
def InitWindow(width: int, height: int, title: Union[str, CharPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="WindowShouldClose"><code>WindowShouldClose</code> function</h2>

> Check if KEY_ESCAPE pressed or Close icon pressed

Defined in raylib.h:

```c
bool WindowShouldClose() 
```

Python wrapper:

```python
def WindowShouldClose() -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CloseWindow"><code>CloseWindow</code> function</h2>

> Close window and unload OpenGL context

Defined in raylib.h:

```c
void CloseWindow() 
```

Python wrapper:

```python
def CloseWindow() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsWindowReady"><code>IsWindowReady</code> function</h2>

> Check if window has been initialized successfully

Defined in raylib.h:

```c
bool IsWindowReady() 
```

Python wrapper:

```python
def IsWindowReady() -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsWindowFullscreen"><code>IsWindowFullscreen</code> function</h2>

> Check if window is currently fullscreen

Defined in raylib.h:

```c
bool IsWindowFullscreen() 
```

Python wrapper:

```python
def IsWindowFullscreen() -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsWindowHidden"><code>IsWindowHidden</code> function</h2>

> Check if window is currently hidden (only PLATFORM_DESKTOP)

Defined in raylib.h:

```c
bool IsWindowHidden() 
```

Python wrapper:

```python
def IsWindowHidden() -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsWindowMinimized"><code>IsWindowMinimized</code> function</h2>

> Check if window is currently minimized (only PLATFORM_DESKTOP)

Defined in raylib.h:

```c
bool IsWindowMinimized() 
```

Python wrapper:

```python
def IsWindowMinimized() -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsWindowMaximized"><code>IsWindowMaximized</code> function</h2>

> Check if window is currently maximized (only PLATFORM_DESKTOP)

Defined in raylib.h:

```c
bool IsWindowMaximized() 
```

Python wrapper:

```python
def IsWindowMaximized() -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsWindowFocused"><code>IsWindowFocused</code> function</h2>

> Check if window is currently focused (only PLATFORM_DESKTOP)

Defined in raylib.h:

```c
bool IsWindowFocused() 
```

Python wrapper:

```python
def IsWindowFocused() -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsWindowResized"><code>IsWindowResized</code> function</h2>

> Check if window has been resized last frame

Defined in raylib.h:

```c
bool IsWindowResized() 
```

Python wrapper:

```python
def IsWindowResized() -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsWindowState"><code>IsWindowState</code> function</h2>

> Check if one specific window flag is enabled

Defined in raylib.h:

```c
bool IsWindowState(unsigned int flag) 
```

Python wrapper:

```python
def IsWindowState(flag: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetWindowState"><code>SetWindowState</code> function</h2>

> Set window configuration state using flags (only PLATFORM_DESKTOP)

Defined in raylib.h:

```c
void SetWindowState(unsigned int flags) 
```

Python wrapper:

```python
def SetWindowState(flags: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ClearWindowState"><code>ClearWindowState</code> function</h2>

> Clear window configuration state flags

Defined in raylib.h:

```c
void ClearWindowState(unsigned int flags) 
```

Python wrapper:

```python
def ClearWindowState(flags: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ToggleFullscreen"><code>ToggleFullscreen</code> function</h2>

> Toggle window state: fullscreen/windowed (only PLATFORM_DESKTOP)

Defined in raylib.h:

```c
void ToggleFullscreen() 
```

Python wrapper:

```python
def ToggleFullscreen() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MaximizeWindow"><code>MaximizeWindow</code> function</h2>

> Set window state: maximized, if resizable (only PLATFORM_DESKTOP)

Defined in raylib.h:

```c
void MaximizeWindow() 
```

Python wrapper:

```python
def MaximizeWindow() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MinimizeWindow"><code>MinimizeWindow</code> function</h2>

> Set window state: minimized, if resizable (only PLATFORM_DESKTOP)

Defined in raylib.h:

```c
void MinimizeWindow() 
```

Python wrapper:

```python
def MinimizeWindow() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="RestoreWindow"><code>RestoreWindow</code> function</h2>

> Set window state: not minimized/maximized (only PLATFORM_DESKTOP)

Defined in raylib.h:

```c
void RestoreWindow() 
```

Python wrapper:

```python
def RestoreWindow() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetWindowIcon"><code>SetWindowIcon</code> function</h2>

> Set icon for window (only PLATFORM_DESKTOP)

Defined in raylib.h:

```c
void SetWindowIcon(Image image) 
```

Python wrapper:

```python
def SetWindowIcon(image: Image) -> None
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetWindowTitle"><code>SetWindowTitle</code> function</h2>

> Set title for window (only PLATFORM_DESKTOP)

Defined in raylib.h:

```c
void SetWindowTitle(char * title) 
```

Python wrapper:

```python
def SetWindowTitle(title: Union[str, CharPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetWindowPosition"><code>SetWindowPosition</code> function</h2>

> Set window position on screen (only PLATFORM_DESKTOP)

Defined in raylib.h:

```c
void SetWindowPosition(int x, int y) 
```

Python wrapper:

```python
def SetWindowPosition(x: int, y: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetWindowMonitor"><code>SetWindowMonitor</code> function</h2>

> Set monitor for the current window (fullscreen mode)

Defined in raylib.h:

```c
void SetWindowMonitor(int monitor) 
```

Python wrapper:

```python
def SetWindowMonitor(monitor: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetWindowMinSize"><code>SetWindowMinSize</code> function</h2>

> Set window minimum dimensions (for FLAG_WINDOW_RESIZABLE)

Defined in raylib.h:

```c
void SetWindowMinSize(int width, int height) 
```

Python wrapper:

```python
def SetWindowMinSize(width: int, height: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetWindowSize"><code>SetWindowSize</code> function</h2>

> Set window dimensions

Defined in raylib.h:

```c
void SetWindowSize(int width, int height) 
```

Python wrapper:

```python
def SetWindowSize(width: int, height: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetWindowOpacity"><code>SetWindowOpacity</code> function</h2>

> Set window opacity [0.0f..1.0f] (only PLATFORM_DESKTOP)

Defined in raylib.h:

```c
void SetWindowOpacity(float opacity) 
```

Python wrapper:

```python
def SetWindowOpacity(opacity: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetWindowHandle"><code>GetWindowHandle</code> function</h2>

> Get native window handle

Defined in raylib.h:

```c
void GetWindowHandle() 
```

Python wrapper:

```python
def GetWindowHandle() -> bytes
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetScreenWidth"><code>GetScreenWidth</code> function</h2>

> Get current screen width

Defined in raylib.h:

```c
int GetScreenWidth() 
```

Python wrapper:

```python
def GetScreenWidth() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetScreenHeight"><code>GetScreenHeight</code> function</h2>

> Get current screen height

Defined in raylib.h:

```c
int GetScreenHeight() 
```

Python wrapper:

```python
def GetScreenHeight() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetRenderWidth"><code>GetRenderWidth</code> function</h2>

> Get current render width (it considers HiDPI)

Defined in raylib.h:

```c
int GetRenderWidth() 
```

Python wrapper:

```python
def GetRenderWidth() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetRenderHeight"><code>GetRenderHeight</code> function</h2>

> Get current render height (it considers HiDPI)

Defined in raylib.h:

```c
int GetRenderHeight() 
```

Python wrapper:

```python
def GetRenderHeight() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMonitorCount"><code>GetMonitorCount</code> function</h2>

> Get number of connected monitors

Defined in raylib.h:

```c
int GetMonitorCount() 
```

Python wrapper:

```python
def GetMonitorCount() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetCurrentMonitor"><code>GetCurrentMonitor</code> function</h2>

> Get current connected monitor

Defined in raylib.h:

```c
int GetCurrentMonitor() 
```

Python wrapper:

```python
def GetCurrentMonitor() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMonitorPosition"><code>GetMonitorPosition</code> function</h2>

> Get specified monitor position

Defined in raylib.h:

```c
Vector2 GetMonitorPosition(int monitor) 
```

Python wrapper:

```python
def GetMonitorPosition(monitor: int) -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMonitorWidth"><code>GetMonitorWidth</code> function</h2>

> Get specified monitor width (current video mode used by monitor)

Defined in raylib.h:

```c
int GetMonitorWidth(int monitor) 
```

Python wrapper:

```python
def GetMonitorWidth(monitor: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMonitorHeight"><code>GetMonitorHeight</code> function</h2>

> Get specified monitor height (current video mode used by monitor)

Defined in raylib.h:

```c
int GetMonitorHeight(int monitor) 
```

Python wrapper:

```python
def GetMonitorHeight(monitor: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMonitorPhysicalWidth"><code>GetMonitorPhysicalWidth</code> function</h2>

> Get specified monitor physical width in millimetres

Defined in raylib.h:

```c
int GetMonitorPhysicalWidth(int monitor) 
```

Python wrapper:

```python
def GetMonitorPhysicalWidth(monitor: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMonitorPhysicalHeight"><code>GetMonitorPhysicalHeight</code> function</h2>

> Get specified monitor physical height in millimetres

Defined in raylib.h:

```c
int GetMonitorPhysicalHeight(int monitor) 
```

Python wrapper:

```python
def GetMonitorPhysicalHeight(monitor: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMonitorRefreshRate"><code>GetMonitorRefreshRate</code> function</h2>

> Get specified monitor refresh rate

Defined in raylib.h:

```c
int GetMonitorRefreshRate(int monitor) 
```

Python wrapper:

```python
def GetMonitorRefreshRate(monitor: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetWindowPosition"><code>GetWindowPosition</code> function</h2>

> Get window position XY on monitor

Defined in raylib.h:

```c
Vector2 GetWindowPosition() 
```

Python wrapper:

```python
def GetWindowPosition() -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetWindowScaleDPI"><code>GetWindowScaleDPI</code> function</h2>

> Get window scale DPI factor

Defined in raylib.h:

```c
Vector2 GetWindowScaleDPI() 
```

Python wrapper:

```python
def GetWindowScaleDPI() -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMonitorName"><code>GetMonitorName</code> function</h2>

> Get the human-readable, UTF-8 encoded name of the primary monitor

Defined in raylib.h:

```c
char * GetMonitorName(int monitor) 
```

Python wrapper:

```python
def GetMonitorName(monitor: int) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetClipboardText"><code>SetClipboardText</code> function</h2>

> Set clipboard text content

Defined in raylib.h:

```c
void SetClipboardText(char * text) 
```

Python wrapper:

```python
def SetClipboardText(text: Union[str, CharPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetClipboardText"><code>GetClipboardText</code> function</h2>

> Get clipboard text content

Defined in raylib.h:

```c
char * GetClipboardText() 
```

Python wrapper:

```python
def GetClipboardText() -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="EnableEventWaiting"><code>EnableEventWaiting</code> function</h2>

> Enable waiting for events on EndDrawing(), no automatic event polling

Defined in raylib.h:

```c
void EnableEventWaiting() 
```

Python wrapper:

```python
def EnableEventWaiting() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DisableEventWaiting"><code>DisableEventWaiting</code> function</h2>

> Disable waiting for events on EndDrawing(), automatic events polling

Defined in raylib.h:

```c
void DisableEventWaiting() 
```

Python wrapper:

```python
def DisableEventWaiting() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SwapScreenBuffer"><code>SwapScreenBuffer</code> function</h2>

> Swap back buffer with front buffer (screen drawing)

Defined in raylib.h:

```c
void SwapScreenBuffer() 
```

Python wrapper:

```python
def SwapScreenBuffer() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="PollInputEvents"><code>PollInputEvents</code> function</h2>

> Register all input events

Defined in raylib.h:

```c
void PollInputEvents() 
```

Python wrapper:

```python
def PollInputEvents() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="WaitTime"><code>WaitTime</code> function</h2>

> Wait for some time (halt program execution)

Defined in raylib.h:

```c
void WaitTime(double seconds) 
```

Python wrapper:

```python
def WaitTime(seconds: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ShowCursor"><code>ShowCursor</code> function</h2>

> Shows cursor

Defined in raylib.h:

```c
void ShowCursor() 
```

Python wrapper:

```python
def ShowCursor() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="HideCursor"><code>HideCursor</code> function</h2>

> Hides cursor

Defined in raylib.h:

```c
void HideCursor() 
```

Python wrapper:

```python
def HideCursor() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsCursorHidden"><code>IsCursorHidden</code> function</h2>

> Check if cursor is not visible

Defined in raylib.h:

```c
bool IsCursorHidden() 
```

Python wrapper:

```python
def IsCursorHidden() -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="EnableCursor"><code>EnableCursor</code> function</h2>

> Enables cursor (unlock cursor)

Defined in raylib.h:

```c
void EnableCursor() 
```

Python wrapper:

```python
def EnableCursor() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DisableCursor"><code>DisableCursor</code> function</h2>

> Disables cursor (lock cursor)

Defined in raylib.h:

```c
void DisableCursor() 
```

Python wrapper:

```python
def DisableCursor() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsCursorOnScreen"><code>IsCursorOnScreen</code> function</h2>

> Check if cursor is on the screen

Defined in raylib.h:

```c
bool IsCursorOnScreen() 
```

Python wrapper:

```python
def IsCursorOnScreen() -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ClearBackground"><code>ClearBackground</code> function</h2>

> Set background color (framebuffer clear color)

Defined in raylib.h:

```c
void ClearBackground(Color color) 
```

Python wrapper:

```python
def ClearBackground(color: Color) -> None
```

See also:
<a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="BeginDrawing"><code>BeginDrawing</code> function</h2>

> Setup canvas (framebuffer) to start drawing

Defined in raylib.h:

```c
void BeginDrawing() 
```

Python wrapper:

```python
def BeginDrawing() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="EndDrawing"><code>EndDrawing</code> function</h2>

> End canvas drawing and swap buffers (double buffering)

Defined in raylib.h:

```c
void EndDrawing() 
```

Python wrapper:

```python
def EndDrawing() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="BeginMode2D"><code>BeginMode2D</code> function</h2>

> Begin 2D mode with custom camera (2D)

Defined in raylib.h:

```c
void BeginMode2D(Camera2D camera) 
```

Python wrapper:

```python
def BeginMode2D(camera: Camera2D) -> None
```

See also:
<a href="#Camera2D">Camera2D</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="EndMode2D"><code>EndMode2D</code> function</h2>

> Ends 2D mode with custom camera

Defined in raylib.h:

```c
void EndMode2D() 
```

Python wrapper:

```python
def EndMode2D() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="BeginMode3D"><code>BeginMode3D</code> function</h2>

> Begin 3D mode with custom camera (3D)

Defined in raylib.h:

```c
void BeginMode3D(Camera3D camera) 
```

Python wrapper:

```python
def BeginMode3D(camera: Camera3D) -> None
```

See also:
<a href="#Camera3D">Camera3D</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="EndMode3D"><code>EndMode3D</code> function</h2>

> Ends 3D mode and returns to default 2D orthographic mode

Defined in raylib.h:

```c
void EndMode3D() 
```

Python wrapper:

```python
def EndMode3D() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="BeginTextureMode"><code>BeginTextureMode</code> function</h2>

> Begin drawing to render texture

Defined in raylib.h:

```c
void BeginTextureMode(RenderTexture2D target) 
```

Python wrapper:

```python
def BeginTextureMode(target: RenderTexture2D) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="EndTextureMode"><code>EndTextureMode</code> function</h2>

> Ends drawing to render texture

Defined in raylib.h:

```c
void EndTextureMode() 
```

Python wrapper:

```python
def EndTextureMode() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="BeginShaderMode"><code>BeginShaderMode</code> function</h2>

> Begin custom shader drawing

Defined in raylib.h:

```c
void BeginShaderMode(Shader shader) 
```

Python wrapper:

```python
def BeginShaderMode(shader: Shader) -> None
```

See also:
<a href="#Shader">Shader</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="EndShaderMode"><code>EndShaderMode</code> function</h2>

> End custom shader drawing (use default shader)

Defined in raylib.h:

```c
void EndShaderMode() 
```

Python wrapper:

```python
def EndShaderMode() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="BeginBlendMode"><code>BeginBlendMode</code> function</h2>

> Begin blending mode (alpha, additive, multiplied, subtract, custom)

Defined in raylib.h:

```c
void BeginBlendMode(int mode) 
```

Python wrapper:

```python
def BeginBlendMode(mode: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="EndBlendMode"><code>EndBlendMode</code> function</h2>

> End blending mode (reset to default: alpha blending)

Defined in raylib.h:

```c
void EndBlendMode() 
```

Python wrapper:

```python
def EndBlendMode() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="BeginScissorMode"><code>BeginScissorMode</code> function</h2>

> Begin scissor mode (define screen area for following drawing)

Defined in raylib.h:

```c
void BeginScissorMode(int x, int y, int width, int height) 
```

Python wrapper:

```python
def BeginScissorMode(x: int, y: int, width: int, height: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="EndScissorMode"><code>EndScissorMode</code> function</h2>

> End scissor mode

Defined in raylib.h:

```c
void EndScissorMode() 
```

Python wrapper:

```python
def EndScissorMode() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="BeginVrStereoMode"><code>BeginVrStereoMode</code> function</h2>

> Begin stereo rendering (requires VR simulator)

Defined in raylib.h:

```c
void BeginVrStereoMode(VrStereoConfig config) 
```

Python wrapper:

```python
def BeginVrStereoMode(config: VrStereoConfig) -> None
```

See also:
<a href="#VrStereoConfig">VrStereoConfig</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="EndVrStereoMode"><code>EndVrStereoMode</code> function</h2>

> End stereo rendering (requires VR simulator)

Defined in raylib.h:

```c
void EndVrStereoMode() 
```

Python wrapper:

```python
def EndVrStereoMode() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadVrStereoConfig"><code>LoadVrStereoConfig</code> function</h2>

> Load VR stereo config for VR simulator device parameters

Defined in raylib.h:

```c
VrStereoConfig LoadVrStereoConfig(VrDeviceInfo device) 
```

Python wrapper:

```python
def LoadVrStereoConfig(device: VrDeviceInfo) -> VrStereoConfig
```

See also:
<a href="#VrDeviceInfo">VrDeviceInfo</a>, <a href="#VrStereoConfig">VrStereoConfig</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadVrStereoConfig"><code>UnloadVrStereoConfig</code> function</h2>

> Unload VR stereo config

Defined in raylib.h:

```c
void UnloadVrStereoConfig(VrStereoConfig config) 
```

Python wrapper:

```python
def UnloadVrStereoConfig(config: VrStereoConfig) -> None
```

See also:
<a href="#VrStereoConfig">VrStereoConfig</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadShader"><code>LoadShader</code> function</h2>

> Load shader from files and bind default locations

Defined in raylib.h:

```c
Shader LoadShader(char * vsFileName, char * fsFileName) 
```

Python wrapper:

```python
def LoadShader(vsFileName: Union[str, CharPtr], fsFileName: Union[str, CharPtr]) -> Shader
```

See also:
<a href="#Shader">Shader</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadShaderFromMemory"><code>LoadShaderFromMemory</code> function</h2>

> Load shader from code strings and bind default locations

Defined in raylib.h:

```c
Shader LoadShaderFromMemory(char * vsCode, char * fsCode) 
```

Python wrapper:

```python
def LoadShaderFromMemory(vsCode: Union[str, CharPtr], fsCode: Union[str, CharPtr]) -> Shader
```

See also:
<a href="#Shader">Shader</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetShaderLocation"><code>GetShaderLocation</code> function</h2>

> Get shader uniform location

Defined in raylib.h:

```c
int GetShaderLocation(Shader shader, char * uniformName) 
```

Python wrapper:

```python
def GetShaderLocation(shader: Shader, uniformName: Union[str, CharPtr]) -> int
```

See also:
<a href="#Shader">Shader</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetShaderLocationAttrib"><code>GetShaderLocationAttrib</code> function</h2>

> Get shader attribute location

Defined in raylib.h:

```c
int GetShaderLocationAttrib(Shader shader, char * attribName) 
```

Python wrapper:

```python
def GetShaderLocationAttrib(shader: Shader, attribName: Union[str, CharPtr]) -> int
```

See also:
<a href="#Shader">Shader</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetShaderValue"><code>SetShaderValue</code> function</h2>

> Set shader uniform value

Defined in raylib.h:

```c
void SetShaderValue(Shader shader, int locIndex, void value, int uniformType) 
```

Python wrapper:

```python
def SetShaderValue(shader: Shader, locIndex: int, value: bytes, uniformType: int) -> None
```

See also:
<a href="#Shader">Shader</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetShaderValueV"><code>SetShaderValueV</code> function</h2>

> Set shader uniform value vector

Defined in raylib.h:

```c
void SetShaderValueV(Shader shader, int locIndex, void value, int uniformType, int count) 
```

Python wrapper:

```python
def SetShaderValueV(shader: Shader, locIndex: int, value: bytes, uniformType: int, count: int) -> None
```

See also:
<a href="#Shader">Shader</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetShaderValueMatrix"><code>SetShaderValueMatrix</code> function</h2>

> Set shader uniform value (matrix 4x4)

Defined in raylib.h:

```c
void SetShaderValueMatrix(Shader shader, int locIndex, Matrix mat) 
```

Python wrapper:

```python
def SetShaderValueMatrix(shader: Shader, locIndex: int, mat: Matrix) -> None
```

See also:
<a href="#Shader">Shader</a>, <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetShaderValueTexture"><code>SetShaderValueTexture</code> function</h2>

> Set shader uniform value for texture (sampler2d)

Defined in raylib.h:

```c
void SetShaderValueTexture(Shader shader, int locIndex, Texture2D texture) 
```

Python wrapper:

```python
def SetShaderValueTexture(shader: Shader, locIndex: int, texture: Texture2D) -> None
```

See also:
<a href="#Shader">Shader</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadShader"><code>UnloadShader</code> function</h2>

> Unload shader from GPU memory (VRAM)

Defined in raylib.h:

```c
void UnloadShader(Shader shader) 
```

Python wrapper:

```python
def UnloadShader(shader: Shader) -> None
```

See also:
<a href="#Shader">Shader</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMouseRay"><code>GetMouseRay</code> function</h2>

> Get a ray trace from mouse position

Defined in raylib.h:

```c
Ray GetMouseRay(Vector2 mousePosition, Camera camera) 
```

Python wrapper:

```python
def GetMouseRay(mousePosition: Vector2, camera: Camera) -> Ray
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Ray">Ray</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetCameraMatrix"><code>GetCameraMatrix</code> function</h2>

> Get camera transform matrix (view matrix)

Defined in raylib.h:

```c
Matrix GetCameraMatrix(Camera camera) 
```

Python wrapper:

```python
def GetCameraMatrix(camera: Camera) -> Matrix
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetCameraMatrix2D"><code>GetCameraMatrix2D</code> function</h2>

> Get camera 2d transform matrix

Defined in raylib.h:

```c
Matrix GetCameraMatrix2D(Camera2D camera) 
```

Python wrapper:

```python
def GetCameraMatrix2D(camera: Camera2D) -> Matrix
```

See also:
<a href="#Camera2D">Camera2D</a>, <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetWorldToScreen"><code>GetWorldToScreen</code> function</h2>

> Get the screen space position for a 3d world space position

Defined in raylib.h:

```c
Vector2 GetWorldToScreen(Vector3 position, Camera camera) 
```

Python wrapper:

```python
def GetWorldToScreen(position: Vector3, camera: Camera) -> Vector2
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetScreenToWorld2D"><code>GetScreenToWorld2D</code> function</h2>

> Get the world space position for a 2d camera screen space position

Defined in raylib.h:

```c
Vector2 GetScreenToWorld2D(Vector2 position, Camera2D camera) 
```

Python wrapper:

```python
def GetScreenToWorld2D(position: Vector2, camera: Camera2D) -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Camera2D">Camera2D</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetWorldToScreenEx"><code>GetWorldToScreenEx</code> function</h2>

> Get size position for a 3d world space position

Defined in raylib.h:

```c
Vector2 GetWorldToScreenEx(Vector3 position, Camera camera, int width, int height) 
```

Python wrapper:

```python
def GetWorldToScreenEx(position: Vector3, camera: Camera, width: int, height: int) -> Vector2
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetWorldToScreen2D"><code>GetWorldToScreen2D</code> function</h2>

> Get the screen space position for a 2d camera world space position

Defined in raylib.h:

```c
Vector2 GetWorldToScreen2D(Vector2 position, Camera2D camera) 
```

Python wrapper:

```python
def GetWorldToScreen2D(position: Vector2, camera: Camera2D) -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Camera2D">Camera2D</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetTargetFPS"><code>SetTargetFPS</code> function</h2>

> Set target FPS (maximum)

Defined in raylib.h:

```c
void SetTargetFPS(int fps) 
```

Python wrapper:

```python
def SetTargetFPS(fps: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetFPS"><code>GetFPS</code> function</h2>

> Get current FPS

Defined in raylib.h:

```c
int GetFPS() 
```

Python wrapper:

```python
def GetFPS() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetFrameTime"><code>GetFrameTime</code> function</h2>

> Get time in seconds for last frame drawn (delta time)

Defined in raylib.h:

```c
float GetFrameTime() 
```

Python wrapper:

```python
def GetFrameTime() -> float
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetTime"><code>GetTime</code> function</h2>

> Get elapsed time in seconds since InitWindow()

Defined in raylib.h:

```c
double GetTime() 
```

Python wrapper:

```python
def GetTime() -> float
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetRandomValue"><code>GetRandomValue</code> function</h2>

> Get a random value between min and max (both included)

Defined in raylib.h:

```c
int GetRandomValue(int min, int max) 
```

Python wrapper:

```python
def GetRandomValue(min: int, max: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetRandomSeed"><code>SetRandomSeed</code> function</h2>

> Set the seed for the random number generator

Defined in raylib.h:

```c
void SetRandomSeed(unsigned int seed) 
```

Python wrapper:

```python
def SetRandomSeed(seed: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TakeScreenshot"><code>TakeScreenshot</code> function</h2>

> Takes a screenshot of current screen (filename extension defines format)

Defined in raylib.h:

```c
void TakeScreenshot(char * fileName) 
```

Python wrapper:

```python
def TakeScreenshot(fileName: Union[str, CharPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetConfigFlags"><code>SetConfigFlags</code> function</h2>

> Setup init configuration flags (view FLAGS)

Defined in raylib.h:

```c
void SetConfigFlags(unsigned int flags) 
```

Python wrapper:

```python
def SetConfigFlags(flags: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TraceLog"><code>TraceLog</code> function</h2>

> Show trace log messages (LOG_DEBUG, LOG_INFO, LOG_WARNING, LOG_ERROR...)

Defined in raylib.h:

```c
void TraceLog(int logLevel, char * text, va_list args) 
```

Python wrapper:

```python
def TraceLog(logLevel: int, text: Union[str, CharPtr], args: bytes) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetTraceLogLevel"><code>SetTraceLogLevel</code> function</h2>

> Set the current threshold (minimum) log level

Defined in raylib.h:

```c
void SetTraceLogLevel(int logLevel) 
```

Python wrapper:

```python
def SetTraceLogLevel(logLevel: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MemAlloc"><code>MemAlloc</code> function</h2>

> Internal memory allocator

Defined in raylib.h:

```c
void MemAlloc(int size) 
```

Python wrapper:

```python
def MemAlloc(size: int) -> bytes
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MemRealloc"><code>MemRealloc</code> function</h2>

> Internal memory reallocator

Defined in raylib.h:

```c
void MemRealloc(void ptr, int size) 
```

Python wrapper:

```python
def MemRealloc(ptr: bytes, size: int) -> bytes
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MemFree"><code>MemFree</code> function</h2>

> Internal memory free

Defined in raylib.h:

```c
void MemFree(void ptr) 
```

Python wrapper:

```python
def MemFree(ptr: bytes) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="OpenURL"><code>OpenURL</code> function</h2>

> Open URL with default system browser (if available)

Defined in raylib.h:

```c
void OpenURL(char * url) 
```

Python wrapper:

```python
def OpenURL(url: Union[str, CharPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetTraceLogCallback"><code>SetTraceLogCallback</code> function</h2>

> Set custom trace log

Defined in raylib.h:

```c
void SetTraceLogCallback(TraceLogCallback callback) 
```

Python wrapper:

```python
def SetTraceLogCallback(callback: TraceLogCallback) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetLoadFileDataCallback"><code>SetLoadFileDataCallback</code> function</h2>

> Set custom file binary data loader

Defined in raylib.h:

```c
void SetLoadFileDataCallback(LoadFileDataCallback callback) 
```

Python wrapper:

```python
def SetLoadFileDataCallback(callback: LoadFileDataCallback) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetSaveFileDataCallback"><code>SetSaveFileDataCallback</code> function</h2>

> Set custom file binary data saver

Defined in raylib.h:

```c
void SetSaveFileDataCallback(SaveFileDataCallback callback) 
```

Python wrapper:

```python
def SetSaveFileDataCallback(callback: SaveFileDataCallback) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetLoadFileTextCallback"><code>SetLoadFileTextCallback</code> function</h2>

> Set custom file text data loader

Defined in raylib.h:

```c
void SetLoadFileTextCallback(LoadFileTextCallback callback) 
```

Python wrapper:

```python
def SetLoadFileTextCallback(callback: LoadFileTextCallback) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetSaveFileTextCallback"><code>SetSaveFileTextCallback</code> function</h2>

> Set custom file text data saver

Defined in raylib.h:

```c
void SetSaveFileTextCallback(SaveFileTextCallback callback) 
```

Python wrapper:

```python
def SetSaveFileTextCallback(callback: SaveFileTextCallback) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadFileData"><code>LoadFileData</code> function</h2>

> Load file data as byte array (read)

Defined in raylib.h:

```c
unsigned char * LoadFileData(char * fileName, unsigned int bytesRead) 
```

Python wrapper:

```python
def LoadFileData(fileName: Union[str, CharPtr], bytesRead: Union[Seq[int], UIntPtr]) -> Union[Seq[int], UCharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadFileData"><code>UnloadFileData</code> function</h2>

> Unload file data allocated by LoadFileData()

Defined in raylib.h:

```c
void UnloadFileData(unsigned char * data) 
```

Python wrapper:

```python
def UnloadFileData(data: Union[Seq[int], UCharPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SaveFileData"><code>SaveFileData</code> function</h2>

> Save data to file from byte array (write), returns true on success

Defined in raylib.h:

```c
bool SaveFileData(char * fileName, void data, unsigned int bytesToWrite) 
```

Python wrapper:

```python
def SaveFileData(fileName: Union[str, CharPtr], data: bytes, bytesToWrite: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ExportDataAsCode"><code>ExportDataAsCode</code> function</h2>

> Export data to code (.h), returns true on success

Defined in raylib.h:

```c
bool ExportDataAsCode(char * data, unsigned int size, char * fileName) 
```

Python wrapper:

```python
def ExportDataAsCode(data: Union[str, CharPtr], size: int, fileName: Union[str, CharPtr]) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadFileText"><code>LoadFileText</code> function</h2>

> Load text data from file (read), returns a '\0' terminated string

Defined in raylib.h:

```c
char * LoadFileText(char * fileName) 
```

Python wrapper:

```python
def LoadFileText(fileName: Union[str, CharPtr]) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadFileText"><code>UnloadFileText</code> function</h2>

> Unload file text data allocated by LoadFileText()

Defined in raylib.h:

```c
void UnloadFileText(char * text) 
```

Python wrapper:

```python
def UnloadFileText(text: Union[str, CharPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SaveFileText"><code>SaveFileText</code> function</h2>

> Save text data to file (write), string must be '\0' terminated, returns true on success

Defined in raylib.h:

```c
bool SaveFileText(char * fileName, char * text) 
```

Python wrapper:

```python
def SaveFileText(fileName: Union[str, CharPtr], text: Union[str, CharPtr]) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="FileExists"><code>FileExists</code> function</h2>

> Check if file exists

Defined in raylib.h:

```c
bool FileExists(char * fileName) 
```

Python wrapper:

```python
def FileExists(fileName: Union[str, CharPtr]) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DirectoryExists"><code>DirectoryExists</code> function</h2>

> Check if a directory path exists

Defined in raylib.h:

```c
bool DirectoryExists(char * dirPath) 
```

Python wrapper:

```python
def DirectoryExists(dirPath: Union[str, CharPtr]) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsFileExtension"><code>IsFileExtension</code> function</h2>

> Check file extension (including point: .png, .wav)

Defined in raylib.h:

```c
bool IsFileExtension(char * fileName, char * ext) 
```

Python wrapper:

```python
def IsFileExtension(fileName: Union[str, CharPtr], ext: Union[str, CharPtr]) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetFileLength"><code>GetFileLength</code> function</h2>

> Get file length in bytes (NOTE: GetFileSize() conflicts with windows.h)

Defined in raylib.h:

```c
int GetFileLength(char * fileName) 
```

Python wrapper:

```python
def GetFileLength(fileName: Union[str, CharPtr]) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetFileExtension"><code>GetFileExtension</code> function</h2>

> Get pointer to extension for a filename string (includes dot: '.png')

Defined in raylib.h:

```c
char * GetFileExtension(char * fileName) 
```

Python wrapper:

```python
def GetFileExtension(fileName: Union[str, CharPtr]) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetFileName"><code>GetFileName</code> function</h2>

> Get pointer to filename for a path string

Defined in raylib.h:

```c
char * GetFileName(char * filePath) 
```

Python wrapper:

```python
def GetFileName(filePath: Union[str, CharPtr]) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetFileNameWithoutExt"><code>GetFileNameWithoutExt</code> function</h2>

> Get filename string without extension (uses static string)

Defined in raylib.h:

```c
char * GetFileNameWithoutExt(char * filePath) 
```

Python wrapper:

```python
def GetFileNameWithoutExt(filePath: Union[str, CharPtr]) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetDirectoryPath"><code>GetDirectoryPath</code> function</h2>

> Get full path for a given fileName with path (uses static string)

Defined in raylib.h:

```c
char * GetDirectoryPath(char * filePath) 
```

Python wrapper:

```python
def GetDirectoryPath(filePath: Union[str, CharPtr]) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetPrevDirectoryPath"><code>GetPrevDirectoryPath</code> function</h2>

> Get previous directory path for a given path (uses static string)

Defined in raylib.h:

```c
char * GetPrevDirectoryPath(char * dirPath) 
```

Python wrapper:

```python
def GetPrevDirectoryPath(dirPath: Union[str, CharPtr]) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetWorkingDirectory"><code>GetWorkingDirectory</code> function</h2>

> Get current working directory (uses static string)

Defined in raylib.h:

```c
char * GetWorkingDirectory() 
```

Python wrapper:

```python
def GetWorkingDirectory() -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetApplicationDirectory"><code>GetApplicationDirectory</code> function</h2>

> Get the directory if the running application (uses static string)

Defined in raylib.h:

```c
char * GetApplicationDirectory() 
```

Python wrapper:

```python
def GetApplicationDirectory() -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ChangeDirectory"><code>ChangeDirectory</code> function</h2>

> Change working directory, return true on success

Defined in raylib.h:

```c
bool ChangeDirectory(char * dir) 
```

Python wrapper:

```python
def ChangeDirectory(dir: Union[str, CharPtr]) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsPathFile"><code>IsPathFile</code> function</h2>

> Check if a given path is a file or a directory

Defined in raylib.h:

```c
bool IsPathFile(char * path) 
```

Python wrapper:

```python
def IsPathFile(path: Union[str, CharPtr]) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadDirectoryFiles"><code>LoadDirectoryFiles</code> function</h2>

> Load directory filepaths

Defined in raylib.h:

```c
FilePathList LoadDirectoryFiles(char * dirPath) 
```

Python wrapper:

```python
def LoadDirectoryFiles(dirPath: Union[str, CharPtr]) -> FilePathList
```

See also:
<a href="#FilePathList">FilePathList</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadDirectoryFilesEx"><code>LoadDirectoryFilesEx</code> function</h2>

> Load directory filepaths with extension filtering and recursive directory scan

Defined in raylib.h:

```c
FilePathList LoadDirectoryFilesEx(char * basePath, char * filter, bool scanSubdirs) 
```

Python wrapper:

```python
def LoadDirectoryFilesEx(basePath: Union[str, CharPtr], filter: Union[str, CharPtr], scanSubdirs: bool) -> FilePathList
```

See also:
<a href="#FilePathList">FilePathList</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadDirectoryFiles"><code>UnloadDirectoryFiles</code> function</h2>

> Unload filepaths

Defined in raylib.h:

```c
void UnloadDirectoryFiles(FilePathList files) 
```

Python wrapper:

```python
def UnloadDirectoryFiles(files: FilePathList) -> None
```

See also:
<a href="#FilePathList">FilePathList</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsFileDropped"><code>IsFileDropped</code> function</h2>

> Check if a file has been dropped into window

Defined in raylib.h:

```c
bool IsFileDropped() 
```

Python wrapper:

```python
def IsFileDropped() -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadDroppedFiles"><code>LoadDroppedFiles</code> function</h2>

> Load dropped filepaths

Defined in raylib.h:

```c
FilePathList LoadDroppedFiles() 
```

Python wrapper:

```python
def LoadDroppedFiles() -> FilePathList
```

See also:
<a href="#FilePathList">FilePathList</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadDroppedFiles"><code>UnloadDroppedFiles</code> function</h2>

> Unload dropped filepaths

Defined in raylib.h:

```c
void UnloadDroppedFiles(FilePathList files) 
```

Python wrapper:

```python
def UnloadDroppedFiles(files: FilePathList) -> None
```

See also:
<a href="#FilePathList">FilePathList</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetFileModTime"><code>GetFileModTime</code> function</h2>

> Get file modification time (last write time)

Defined in raylib.h:

```c
long GetFileModTime(char * fileName) 
```

Python wrapper:

```python
def GetFileModTime(fileName: Union[str, CharPtr]) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CompressData"><code>CompressData</code> function</h2>

> Compress data (DEFLATE algorithm), memory must be MemFree()

Defined in raylib.h:

```c
unsigned char * CompressData(unsigned char * data, int dataSize, int compDataSize) 
```

Python wrapper:

```python
def CompressData(data: Union[Seq[int], UCharPtr], dataSize: int, compDataSize: Union[Seq[int], IntPtr]) -> Union[Seq[int], UCharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DecompressData"><code>DecompressData</code> function</h2>

> Decompress data (DEFLATE algorithm), memory must be MemFree()

Defined in raylib.h:

```c
unsigned char * DecompressData(unsigned char * compData, int compDataSize, int dataSize) 
```

Python wrapper:

```python
def DecompressData(compData: Union[Seq[int], UCharPtr], compDataSize: int, dataSize: Union[Seq[int], IntPtr]) -> Union[Seq[int], UCharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="EncodeDataBase64"><code>EncodeDataBase64</code> function</h2>

> Encode data to Base64 string, memory must be MemFree()

Defined in raylib.h:

```c
char * EncodeDataBase64(unsigned char * data, int dataSize, int outputSize) 
```

Python wrapper:

```python
def EncodeDataBase64(data: Union[Seq[int], UCharPtr], dataSize: int, outputSize: Union[Seq[int], IntPtr]) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DecodeDataBase64"><code>DecodeDataBase64</code> function</h2>

> Decode Base64 string data, memory must be MemFree()

Defined in raylib.h:

```c
unsigned char * DecodeDataBase64(unsigned char * data, int outputSize) 
```

Python wrapper:

```python
def DecodeDataBase64(data: Union[Seq[int], UCharPtr], outputSize: Union[Seq[int], IntPtr]) -> Union[Seq[int], UCharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsKeyPressed"><code>IsKeyPressed</code> function</h2>

> Check if a key has been pressed once

Defined in raylib.h:

```c
bool IsKeyPressed(int key) 
```

Python wrapper:

```python
def IsKeyPressed(key: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsKeyDown"><code>IsKeyDown</code> function</h2>

> Check if a key is being pressed

Defined in raylib.h:

```c
bool IsKeyDown(int key) 
```

Python wrapper:

```python
def IsKeyDown(key: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsKeyReleased"><code>IsKeyReleased</code> function</h2>

> Check if a key has been released once

Defined in raylib.h:

```c
bool IsKeyReleased(int key) 
```

Python wrapper:

```python
def IsKeyReleased(key: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsKeyUp"><code>IsKeyUp</code> function</h2>

> Check if a key is NOT being pressed

Defined in raylib.h:

```c
bool IsKeyUp(int key) 
```

Python wrapper:

```python
def IsKeyUp(key: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetExitKey"><code>SetExitKey</code> function</h2>

> Set a custom key to exit program (default is ESC)

Defined in raylib.h:

```c
void SetExitKey(int key) 
```

Python wrapper:

```python
def SetExitKey(key: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetKeyPressed"><code>GetKeyPressed</code> function</h2>

> Get key pressed (keycode), call it multiple times for keys queued, returns 0 when the queue is empty

Defined in raylib.h:

```c
int GetKeyPressed() 
```

Python wrapper:

```python
def GetKeyPressed() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetCharPressed"><code>GetCharPressed</code> function</h2>

> Get char pressed (unicode), call it multiple times for chars queued, returns 0 when the queue is empty

Defined in raylib.h:

```c
int GetCharPressed() 
```

Python wrapper:

```python
def GetCharPressed() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsGamepadAvailable"><code>IsGamepadAvailable</code> function</h2>

> Check if a gamepad is available

Defined in raylib.h:

```c
bool IsGamepadAvailable(int gamepad) 
```

Python wrapper:

```python
def IsGamepadAvailable(gamepad: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetGamepadName"><code>GetGamepadName</code> function</h2>

> Get gamepad internal name id

Defined in raylib.h:

```c
char * GetGamepadName(int gamepad) 
```

Python wrapper:

```python
def GetGamepadName(gamepad: int) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsGamepadButtonPressed"><code>IsGamepadButtonPressed</code> function</h2>

> Check if a gamepad button has been pressed once

Defined in raylib.h:

```c
bool IsGamepadButtonPressed(int gamepad, int button) 
```

Python wrapper:

```python
def IsGamepadButtonPressed(gamepad: int, button: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsGamepadButtonDown"><code>IsGamepadButtonDown</code> function</h2>

> Check if a gamepad button is being pressed

Defined in raylib.h:

```c
bool IsGamepadButtonDown(int gamepad, int button) 
```

Python wrapper:

```python
def IsGamepadButtonDown(gamepad: int, button: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsGamepadButtonReleased"><code>IsGamepadButtonReleased</code> function</h2>

> Check if a gamepad button has been released once

Defined in raylib.h:

```c
bool IsGamepadButtonReleased(int gamepad, int button) 
```

Python wrapper:

```python
def IsGamepadButtonReleased(gamepad: int, button: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsGamepadButtonUp"><code>IsGamepadButtonUp</code> function</h2>

> Check if a gamepad button is NOT being pressed

Defined in raylib.h:

```c
bool IsGamepadButtonUp(int gamepad, int button) 
```

Python wrapper:

```python
def IsGamepadButtonUp(gamepad: int, button: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetGamepadButtonPressed"><code>GetGamepadButtonPressed</code> function</h2>

> Get the last gamepad button pressed

Defined in raylib.h:

```c
int GetGamepadButtonPressed() 
```

Python wrapper:

```python
def GetGamepadButtonPressed() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetGamepadAxisCount"><code>GetGamepadAxisCount</code> function</h2>

> Get gamepad axis count for a gamepad

Defined in raylib.h:

```c
int GetGamepadAxisCount(int gamepad) 
```

Python wrapper:

```python
def GetGamepadAxisCount(gamepad: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetGamepadAxisMovement"><code>GetGamepadAxisMovement</code> function</h2>

> Get axis movement value for a gamepad axis

Defined in raylib.h:

```c
float GetGamepadAxisMovement(int gamepad, int axis) 
```

Python wrapper:

```python
def GetGamepadAxisMovement(gamepad: int, axis: int) -> float
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetGamepadMappings"><code>SetGamepadMappings</code> function</h2>

> Set internal gamepad mappings (SDL_GameControllerDB)

Defined in raylib.h:

```c
int SetGamepadMappings(char * mappings) 
```

Python wrapper:

```python
def SetGamepadMappings(mappings: Union[str, CharPtr]) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsMouseButtonPressed"><code>IsMouseButtonPressed</code> function</h2>

> Check if a mouse button has been pressed once

Defined in raylib.h:

```c
bool IsMouseButtonPressed(int button) 
```

Python wrapper:

```python
def IsMouseButtonPressed(button: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsMouseButtonDown"><code>IsMouseButtonDown</code> function</h2>

> Check if a mouse button is being pressed

Defined in raylib.h:

```c
bool IsMouseButtonDown(int button) 
```

Python wrapper:

```python
def IsMouseButtonDown(button: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsMouseButtonReleased"><code>IsMouseButtonReleased</code> function</h2>

> Check if a mouse button has been released once

Defined in raylib.h:

```c
bool IsMouseButtonReleased(int button) 
```

Python wrapper:

```python
def IsMouseButtonReleased(button: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsMouseButtonUp"><code>IsMouseButtonUp</code> function</h2>

> Check if a mouse button is NOT being pressed

Defined in raylib.h:

```c
bool IsMouseButtonUp(int button) 
```

Python wrapper:

```python
def IsMouseButtonUp(button: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMouseX"><code>GetMouseX</code> function</h2>

> Get mouse position X

Defined in raylib.h:

```c
int GetMouseX() 
```

Python wrapper:

```python
def GetMouseX() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMouseY"><code>GetMouseY</code> function</h2>

> Get mouse position Y

Defined in raylib.h:

```c
int GetMouseY() 
```

Python wrapper:

```python
def GetMouseY() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMousePosition"><code>GetMousePosition</code> function</h2>

> Get mouse position XY

Defined in raylib.h:

```c
Vector2 GetMousePosition() 
```

Python wrapper:

```python
def GetMousePosition() -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMouseDelta"><code>GetMouseDelta</code> function</h2>

> Get mouse delta between frames

Defined in raylib.h:

```c
Vector2 GetMouseDelta() 
```

Python wrapper:

```python
def GetMouseDelta() -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetMousePosition"><code>SetMousePosition</code> function</h2>

> Set mouse position XY

Defined in raylib.h:

```c
void SetMousePosition(int x, int y) 
```

Python wrapper:

```python
def SetMousePosition(x: int, y: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetMouseOffset"><code>SetMouseOffset</code> function</h2>

> Set mouse offset

Defined in raylib.h:

```c
void SetMouseOffset(int offsetX, int offsetY) 
```

Python wrapper:

```python
def SetMouseOffset(offsetX: int, offsetY: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetMouseScale"><code>SetMouseScale</code> function</h2>

> Set mouse scaling

Defined in raylib.h:

```c
void SetMouseScale(float scaleX, float scaleY) 
```

Python wrapper:

```python
def SetMouseScale(scaleX: float, scaleY: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMouseWheelMove"><code>GetMouseWheelMove</code> function</h2>

> Get mouse wheel movement for X or Y, whichever is larger

Defined in raylib.h:

```c
float GetMouseWheelMove() 
```

Python wrapper:

```python
def GetMouseWheelMove() -> float
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMouseWheelMoveV"><code>GetMouseWheelMoveV</code> function</h2>

> Get mouse wheel movement for both X and Y

Defined in raylib.h:

```c
Vector2 GetMouseWheelMoveV() 
```

Python wrapper:

```python
def GetMouseWheelMoveV() -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetMouseCursor"><code>SetMouseCursor</code> function</h2>

> Set mouse cursor

Defined in raylib.h:

```c
void SetMouseCursor(int cursor) 
```

Python wrapper:

```python
def SetMouseCursor(cursor: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetTouchX"><code>GetTouchX</code> function</h2>

> Get touch position X for touch point 0 (relative to screen size)

Defined in raylib.h:

```c
int GetTouchX() 
```

Python wrapper:

```python
def GetTouchX() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetTouchY"><code>GetTouchY</code> function</h2>

> Get touch position Y for touch point 0 (relative to screen size)

Defined in raylib.h:

```c
int GetTouchY() 
```

Python wrapper:

```python
def GetTouchY() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetTouchPosition"><code>GetTouchPosition</code> function</h2>

> Get touch position XY for a touch point index (relative to screen size)

Defined in raylib.h:

```c
Vector2 GetTouchPosition(int index) 
```

Python wrapper:

```python
def GetTouchPosition(index: int) -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetTouchPointId"><code>GetTouchPointId</code> function</h2>

> Get touch point identifier for given index

Defined in raylib.h:

```c
int GetTouchPointId(int index) 
```

Python wrapper:

```python
def GetTouchPointId(index: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetTouchPointCount"><code>GetTouchPointCount</code> function</h2>

> Get number of touch points

Defined in raylib.h:

```c
int GetTouchPointCount() 
```

Python wrapper:

```python
def GetTouchPointCount() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetGesturesEnabled"><code>SetGesturesEnabled</code> function</h2>

> Enable a set of gestures using flags

Defined in raylib.h:

```c
void SetGesturesEnabled(unsigned int flags) 
```

Python wrapper:

```python
def SetGesturesEnabled(flags: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsGestureDetected"><code>IsGestureDetected</code> function</h2>

> Check if a gesture have been detected

Defined in raylib.h:

```c
bool IsGestureDetected(int gesture) 
```

Python wrapper:

```python
def IsGestureDetected(gesture: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetGestureDetected"><code>GetGestureDetected</code> function</h2>

> Get latest detected gesture

Defined in raylib.h:

```c
int GetGestureDetected() 
```

Python wrapper:

```python
def GetGestureDetected() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetGestureHoldDuration"><code>GetGestureHoldDuration</code> function</h2>

> Get gesture hold time in milliseconds

Defined in raylib.h:

```c
float GetGestureHoldDuration() 
```

Python wrapper:

```python
def GetGestureHoldDuration() -> float
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetGestureDragVector"><code>GetGestureDragVector</code> function</h2>

> Get gesture drag vector

Defined in raylib.h:

```c
Vector2 GetGestureDragVector() 
```

Python wrapper:

```python
def GetGestureDragVector() -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetGestureDragAngle"><code>GetGestureDragAngle</code> function</h2>

> Get gesture drag angle

Defined in raylib.h:

```c
float GetGestureDragAngle() 
```

Python wrapper:

```python
def GetGestureDragAngle() -> float
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetGesturePinchVector"><code>GetGesturePinchVector</code> function</h2>

> Get gesture pinch delta

Defined in raylib.h:

```c
Vector2 GetGesturePinchVector() 
```

Python wrapper:

```python
def GetGesturePinchVector() -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetGesturePinchAngle"><code>GetGesturePinchAngle</code> function</h2>

> Get gesture pinch angle

Defined in raylib.h:

```c
float GetGesturePinchAngle() 
```

Python wrapper:

```python
def GetGesturePinchAngle() -> float
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetCameraMode"><code>SetCameraMode</code> function</h2>

> Set camera mode (multiple camera modes available)

Defined in raylib.h:

```c
void SetCameraMode(Camera camera, int mode) 
```

Python wrapper:

```python
def SetCameraMode(camera: Camera, mode: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UpdateCamera"><code>UpdateCamera</code> function</h2>

> Update camera position for selected mode

Defined in raylib.h:

```c
void UpdateCamera(Camera * camera) 
```

Python wrapper:

```python
def UpdateCamera(camera: CameraPtr) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetCameraPanControl"><code>SetCameraPanControl</code> function</h2>

> Set camera pan key to combine with mouse movement (free camera)

Defined in raylib.h:

```c
void SetCameraPanControl(int keyPan) 
```

Python wrapper:

```python
def SetCameraPanControl(keyPan: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetCameraAltControl"><code>SetCameraAltControl</code> function</h2>

> Set camera alt key to combine with mouse movement (free camera)

Defined in raylib.h:

```c
void SetCameraAltControl(int keyAlt) 
```

Python wrapper:

```python
def SetCameraAltControl(keyAlt: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetCameraSmoothZoomControl"><code>SetCameraSmoothZoomControl</code> function</h2>

> Set camera smooth zoom key to combine with mouse (free camera)

Defined in raylib.h:

```c
void SetCameraSmoothZoomControl(int keySmoothZoom) 
```

Python wrapper:

```python
def SetCameraSmoothZoomControl(keySmoothZoom: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetCameraMoveControls"><code>SetCameraMoveControls</code> function</h2>

> Set camera move controls (1st person and 3rd person cameras)

Defined in raylib.h:

```c
void SetCameraMoveControls(int keyFront, int keyBack, int keyRight, int keyLeft, int keyUp, int keyDown) 
```

Python wrapper:

```python
def SetCameraMoveControls(keyFront: int, keyBack: int, keyRight: int, keyLeft: int, keyUp: int, keyDown: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetShapesTexture"><code>SetShapesTexture</code> function</h2>

> Set texture and rectangle to be used on shapes drawing

Defined in raylib.h:

```c
void SetShapesTexture(Texture2D texture, Rectangle source) 
```

Python wrapper:

```python
def SetShapesTexture(texture: Texture2D, source: Rectangle) -> None
```

See also:
<a href="#Rectangle">Rectangle</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawPixel"><code>DrawPixel</code> function</h2>

> Draw a pixel

Defined in raylib.h:

```c
void DrawPixel(int posX, int posY, Color color) 
```

Python wrapper:

```python
def DrawPixel(posX: int, posY: int, color: Color) -> None
```

See also:
<a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawPixelV"><code>DrawPixelV</code> function</h2>

> Draw a pixel (Vector version)

Defined in raylib.h:

```c
void DrawPixelV(Vector2 position, Color color) 
```

Python wrapper:

```python
def DrawPixelV(position: Vector2, color: Color) -> None
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawLine"><code>DrawLine</code> function</h2>

> Draw a line

Defined in raylib.h:

```c
void DrawLine(int startPosX, int startPosY, int endPosX, int endPosY, Color color) 
```

Python wrapper:

```python
def DrawLine(startPosX: int, startPosY: int, endPosX: int, endPosY: int, color: Color) -> None
```

See also:
<a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawLineV"><code>DrawLineV</code> function</h2>

> Draw a line (Vector version)

Defined in raylib.h:

```c
void DrawLineV(Vector2 startPos, Vector2 endPos, Color color) 
```

Python wrapper:

```python
def DrawLineV(startPos: Vector2, endPos: Vector2, color: Color) -> None
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawLineEx"><code>DrawLineEx</code> function</h2>

> Draw a line defining thickness

Defined in raylib.h:

```c
void DrawLineEx(Vector2 startPos, Vector2 endPos, float thick, Color color) 
```

Python wrapper:

```python
def DrawLineEx(startPos: Vector2, endPos: Vector2, thick: float, color: Color) -> None
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawLineBezier"><code>DrawLineBezier</code> function</h2>

> Draw a line using cubic-bezier curves in-out

Defined in raylib.h:

```c
void DrawLineBezier(Vector2 startPos, Vector2 endPos, float thick, Color color) 
```

Python wrapper:

```python
def DrawLineBezier(startPos: Vector2, endPos: Vector2, thick: float, color: Color) -> None
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawLineBezierQuad"><code>DrawLineBezierQuad</code> function</h2>

> Draw line using quadratic bezier curves with a control point

Defined in raylib.h:

```c
void DrawLineBezierQuad(Vector2 startPos, Vector2 endPos, Vector2 controlPos, float thick, Color color) 
```

Python wrapper:

```python
def DrawLineBezierQuad(startPos: Vector2, endPos: Vector2, controlPos: Vector2, thick: float, color: Color) -> None
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawLineBezierCubic"><code>DrawLineBezierCubic</code> function</h2>

> Draw line using cubic bezier curves with 2 control points

Defined in raylib.h:

```c
void DrawLineBezierCubic(Vector2 startPos, Vector2 endPos, Vector2 startControlPos, Vector2 endControlPos, float thick, Color color) 
```

Python wrapper:

```python
def DrawLineBezierCubic(startPos: Vector2, endPos: Vector2, startControlPos: Vector2, endControlPos: Vector2, thick: float, color: Color) -> None
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawLineStrip"><code>DrawLineStrip</code> function</h2>

> Draw lines sequence

Defined in raylib.h:

```c
void DrawLineStrip(Vector2 * points, int pointCount, Color color) 
```

Python wrapper:

```python
def DrawLineStrip(points: Vector2Ptr, pointCount: int, color: Color) -> None
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCircle"><code>DrawCircle</code> function</h2>

> Draw a color-filled circle

Defined in raylib.h:

```c
void DrawCircle(int centerX, int centerY, float radius, Color color) 
```

Python wrapper:

```python
def DrawCircle(centerX: int, centerY: int, radius: float, color: Color) -> None
```

See also:
<a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCircleSector"><code>DrawCircleSector</code> function</h2>

> Draw a piece of a circle

Defined in raylib.h:

```c
void DrawCircleSector(Vector2 center, float radius, float startAngle, float endAngle, int segments, Color color) 
```

Python wrapper:

```python
def DrawCircleSector(center: Vector2, radius: float, startAngle: float, endAngle: float, segments: int, color: Color) -> None
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCircleSectorLines"><code>DrawCircleSectorLines</code> function</h2>

> Draw circle sector outline

Defined in raylib.h:

```c
void DrawCircleSectorLines(Vector2 center, float radius, float startAngle, float endAngle, int segments, Color color) 
```

Python wrapper:

```python
def DrawCircleSectorLines(center: Vector2, radius: float, startAngle: float, endAngle: float, segments: int, color: Color) -> None
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCircleGradient"><code>DrawCircleGradient</code> function</h2>

> Draw a gradient-filled circle

Defined in raylib.h:

```c
void DrawCircleGradient(int centerX, int centerY, float radius, Color color1, Color color2) 
```

Python wrapper:

```python
def DrawCircleGradient(centerX: int, centerY: int, radius: float, color1: Color, color2: Color) -> None
```

See also:
<a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCircleV"><code>DrawCircleV</code> function</h2>

> Draw a color-filled circle (Vector version)

Defined in raylib.h:

```c
void DrawCircleV(Vector2 center, float radius, Color color) 
```

Python wrapper:

```python
def DrawCircleV(center: Vector2, radius: float, color: Color) -> None
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCircleLines"><code>DrawCircleLines</code> function</h2>

> Draw circle outline

Defined in raylib.h:

```c
void DrawCircleLines(int centerX, int centerY, float radius, Color color) 
```

Python wrapper:

```python
def DrawCircleLines(centerX: int, centerY: int, radius: float, color: Color) -> None
```

See also:
<a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawEllipse"><code>DrawEllipse</code> function</h2>

> Draw ellipse

Defined in raylib.h:

```c
void DrawEllipse(int centerX, int centerY, float radiusH, float radiusV, Color color) 
```

Python wrapper:

```python
def DrawEllipse(centerX: int, centerY: int, radiusH: float, radiusV: float, color: Color) -> None
```

See also:
<a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawEllipseLines"><code>DrawEllipseLines</code> function</h2>

> Draw ellipse outline

Defined in raylib.h:

```c
void DrawEllipseLines(int centerX, int centerY, float radiusH, float radiusV, Color color) 
```

Python wrapper:

```python
def DrawEllipseLines(centerX: int, centerY: int, radiusH: float, radiusV: float, color: Color) -> None
```

See also:
<a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRing"><code>DrawRing</code> function</h2>

> Draw ring

Defined in raylib.h:

```c
void DrawRing(Vector2 center, float innerRadius, float outerRadius, float startAngle, float endAngle, int segments, Color color) 
```

Python wrapper:

```python
def DrawRing(center: Vector2, innerRadius: float, outerRadius: float, startAngle: float, endAngle: float, segments: int, color: Color) -> None
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRingLines"><code>DrawRingLines</code> function</h2>

> Draw ring outline

Defined in raylib.h:

```c
void DrawRingLines(Vector2 center, float innerRadius, float outerRadius, float startAngle, float endAngle, int segments, Color color) 
```

Python wrapper:

```python
def DrawRingLines(center: Vector2, innerRadius: float, outerRadius: float, startAngle: float, endAngle: float, segments: int, color: Color) -> None
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRectangle"><code>DrawRectangle</code> function</h2>

> Draw a color-filled rectangle

Defined in raylib.h:

```c
void DrawRectangle(int posX, int posY, int width, int height, Color color) 
```

Python wrapper:

```python
def DrawRectangle(posX: int, posY: int, width: int, height: int, color: Color) -> None
```

See also:
<a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRectangleV"><code>DrawRectangleV</code> function</h2>

> Draw a color-filled rectangle (Vector version)

Defined in raylib.h:

```c
void DrawRectangleV(Vector2 position, Vector2 size, Color color) 
```

Python wrapper:

```python
def DrawRectangleV(position: Vector2, size: Vector2, color: Color) -> None
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRectangleRec"><code>DrawRectangleRec</code> function</h2>

> Draw a color-filled rectangle

Defined in raylib.h:

```c
void DrawRectangleRec(Rectangle rec, Color color) 
```

Python wrapper:

```python
def DrawRectangleRec(rec: Rectangle, color: Color) -> None
```

See also:
<a href="#Rectangle">Rectangle</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRectanglePro"><code>DrawRectanglePro</code> function</h2>

> Draw a color-filled rectangle with pro parameters

Defined in raylib.h:

```c
void DrawRectanglePro(Rectangle rec, Vector2 origin, float rotation, Color color) 
```

Python wrapper:

```python
def DrawRectanglePro(rec: Rectangle, origin: Vector2, rotation: float, color: Color) -> None
```

See also:
<a href="#Rectangle">Rectangle</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRectangleGradientV"><code>DrawRectangleGradientV</code> function</h2>

> Draw a vertical-gradient-filled rectangle

Defined in raylib.h:

```c
void DrawRectangleGradientV(int posX, int posY, int width, int height, Color color1, Color color2) 
```

Python wrapper:

```python
def DrawRectangleGradientV(posX: int, posY: int, width: int, height: int, color1: Color, color2: Color) -> None
```

See also:
<a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRectangleGradientH"><code>DrawRectangleGradientH</code> function</h2>

> Draw a horizontal-gradient-filled rectangle

Defined in raylib.h:

```c
void DrawRectangleGradientH(int posX, int posY, int width, int height, Color color1, Color color2) 
```

Python wrapper:

```python
def DrawRectangleGradientH(posX: int, posY: int, width: int, height: int, color1: Color, color2: Color) -> None
```

See also:
<a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRectangleGradientEx"><code>DrawRectangleGradientEx</code> function</h2>

> Draw a gradient-filled rectangle with custom vertex colors

Defined in raylib.h:

```c
void DrawRectangleGradientEx(Rectangle rec, Color col1, Color col2, Color col3, Color col4) 
```

Python wrapper:

```python
def DrawRectangleGradientEx(rec: Rectangle, col1: Color, col2: Color, col3: Color, col4: Color) -> None
```

See also:
<a href="#Rectangle">Rectangle</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRectangleLines"><code>DrawRectangleLines</code> function</h2>

> Draw rectangle outline

Defined in raylib.h:

```c
void DrawRectangleLines(int posX, int posY, int width, int height, Color color) 
```

Python wrapper:

```python
def DrawRectangleLines(posX: int, posY: int, width: int, height: int, color: Color) -> None
```

See also:
<a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRectangleLinesEx"><code>DrawRectangleLinesEx</code> function</h2>

> Draw rectangle outline with extended parameters

Defined in raylib.h:

```c
void DrawRectangleLinesEx(Rectangle rec, float lineThick, Color color) 
```

Python wrapper:

```python
def DrawRectangleLinesEx(rec: Rectangle, lineThick: float, color: Color) -> None
```

See also:
<a href="#Rectangle">Rectangle</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRectangleRounded"><code>DrawRectangleRounded</code> function</h2>

> Draw rectangle with rounded edges

Defined in raylib.h:

```c
void DrawRectangleRounded(Rectangle rec, float roundness, int segments, Color color) 
```

Python wrapper:

```python
def DrawRectangleRounded(rec: Rectangle, roundness: float, segments: int, color: Color) -> None
```

See also:
<a href="#Rectangle">Rectangle</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRectangleRoundedLines"><code>DrawRectangleRoundedLines</code> function</h2>

> Draw rectangle with rounded edges outline

Defined in raylib.h:

```c
void DrawRectangleRoundedLines(Rectangle rec, float roundness, int segments, float lineThick, Color color) 
```

Python wrapper:

```python
def DrawRectangleRoundedLines(rec: Rectangle, roundness: float, segments: int, lineThick: float, color: Color) -> None
```

See also:
<a href="#Rectangle">Rectangle</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTriangle"><code>DrawTriangle</code> function</h2>

> Draw a color-filled triangle (vertex in counter-clockwise order!)

Defined in raylib.h:

```c
void DrawTriangle(Vector2 v1, Vector2 v2, Vector2 v3, Color color) 
```

Python wrapper:

```python
def DrawTriangle(v1: Vector2, v2: Vector2, v3: Vector2, color: Color) -> None
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTriangleLines"><code>DrawTriangleLines</code> function</h2>

> Draw triangle outline (vertex in counter-clockwise order!)

Defined in raylib.h:

```c
void DrawTriangleLines(Vector2 v1, Vector2 v2, Vector2 v3, Color color) 
```

Python wrapper:

```python
def DrawTriangleLines(v1: Vector2, v2: Vector2, v3: Vector2, color: Color) -> None
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTriangleFan"><code>DrawTriangleFan</code> function</h2>

> Draw a triangle fan defined by points (first vertex is the center)

Defined in raylib.h:

```c
void DrawTriangleFan(Vector2 * points, int pointCount, Color color) 
```

Python wrapper:

```python
def DrawTriangleFan(points: Vector2Ptr, pointCount: int, color: Color) -> None
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTriangleStrip"><code>DrawTriangleStrip</code> function</h2>

> Draw a triangle strip defined by points

Defined in raylib.h:

```c
void DrawTriangleStrip(Vector2 * points, int pointCount, Color color) 
```

Python wrapper:

```python
def DrawTriangleStrip(points: Vector2Ptr, pointCount: int, color: Color) -> None
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawPoly"><code>DrawPoly</code> function</h2>

> Draw a regular polygon (Vector version)

Defined in raylib.h:

```c
void DrawPoly(Vector2 center, int sides, float radius, float rotation, Color color) 
```

Python wrapper:

```python
def DrawPoly(center: Vector2, sides: int, radius: float, rotation: float, color: Color) -> None
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawPolyLines"><code>DrawPolyLines</code> function</h2>

> Draw a polygon outline of n sides

Defined in raylib.h:

```c
void DrawPolyLines(Vector2 center, int sides, float radius, float rotation, Color color) 
```

Python wrapper:

```python
def DrawPolyLines(center: Vector2, sides: int, radius: float, rotation: float, color: Color) -> None
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawPolyLinesEx"><code>DrawPolyLinesEx</code> function</h2>

> Draw a polygon outline of n sides with extended parameters

Defined in raylib.h:

```c
void DrawPolyLinesEx(Vector2 center, int sides, float radius, float rotation, float lineThick, Color color) 
```

Python wrapper:

```python
def DrawPolyLinesEx(center: Vector2, sides: int, radius: float, rotation: float, lineThick: float, color: Color) -> None
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CheckCollisionRecs"><code>CheckCollisionRecs</code> function</h2>

> Check collision between two rectangles

Defined in raylib.h:

```c
bool CheckCollisionRecs(Rectangle rec1, Rectangle rec2) 
```

Python wrapper:

```python
def CheckCollisionRecs(rec1: Rectangle, rec2: Rectangle) -> bool
```

See also:
<a href="#Rectangle">Rectangle</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CheckCollisionCircles"><code>CheckCollisionCircles</code> function</h2>

> Check collision between two circles

Defined in raylib.h:

```c
bool CheckCollisionCircles(Vector2 center1, float radius1, Vector2 center2, float radius2) 
```

Python wrapper:

```python
def CheckCollisionCircles(center1: Vector2, radius1: float, center2: Vector2, radius2: float) -> bool
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CheckCollisionCircleRec"><code>CheckCollisionCircleRec</code> function</h2>

> Check collision between circle and rectangle

Defined in raylib.h:

```c
bool CheckCollisionCircleRec(Vector2 center, float radius, Rectangle rec) 
```

Python wrapper:

```python
def CheckCollisionCircleRec(center: Vector2, radius: float, rec: Rectangle) -> bool
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Rectangle">Rectangle</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CheckCollisionPointRec"><code>CheckCollisionPointRec</code> function</h2>

> Check if point is inside rectangle

Defined in raylib.h:

```c
bool CheckCollisionPointRec(Vector2 point, Rectangle rec) 
```

Python wrapper:

```python
def CheckCollisionPointRec(point: Vector2, rec: Rectangle) -> bool
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Rectangle">Rectangle</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CheckCollisionPointCircle"><code>CheckCollisionPointCircle</code> function</h2>

> Check if point is inside circle

Defined in raylib.h:

```c
bool CheckCollisionPointCircle(Vector2 point, Vector2 center, float radius) 
```

Python wrapper:

```python
def CheckCollisionPointCircle(point: Vector2, center: Vector2, radius: float) -> bool
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CheckCollisionPointTriangle"><code>CheckCollisionPointTriangle</code> function</h2>

> Check if point is inside a triangle

Defined in raylib.h:

```c
bool CheckCollisionPointTriangle(Vector2 point, Vector2 p1, Vector2 p2, Vector2 p3) 
```

Python wrapper:

```python
def CheckCollisionPointTriangle(point: Vector2, p1: Vector2, p2: Vector2, p3: Vector2) -> bool
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CheckCollisionLines"><code>CheckCollisionLines</code> function</h2>

> Check the collision between two lines defined by two points each, returns collision point by reference

Defined in raylib.h:

```c
bool CheckCollisionLines(Vector2 startPos1, Vector2 endPos1, Vector2 startPos2, Vector2 endPos2, Vector2 * collisionPoint) 
```

Python wrapper:

```python
def CheckCollisionLines(startPos1: Vector2, endPos1: Vector2, startPos2: Vector2, endPos2: Vector2, collisionPoint: Vector2Ptr) -> bool
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CheckCollisionPointLine"><code>CheckCollisionPointLine</code> function</h2>

> Check if point belongs to line created between two points [p1] and [p2] with defined margin in pixels [threshold]

Defined in raylib.h:

```c
bool CheckCollisionPointLine(Vector2 point, Vector2 p1, Vector2 p2, int threshold) 
```

Python wrapper:

```python
def CheckCollisionPointLine(point: Vector2, p1: Vector2, p2: Vector2, threshold: int) -> bool
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetCollisionRec"><code>GetCollisionRec</code> function</h2>

> Get collision rectangle for two rectangles collision

Defined in raylib.h:

```c
Rectangle GetCollisionRec(Rectangle rec1, Rectangle rec2) 
```

Python wrapper:

```python
def GetCollisionRec(rec1: Rectangle, rec2: Rectangle) -> Rectangle
```

See also:
<a href="#Rectangle">Rectangle</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadImage"><code>LoadImage</code> function</h2>

> Load image from file into CPU memory (RAM)

Defined in raylib.h:

```c
Image LoadImage(char * fileName) 
```

Python wrapper:

```python
def LoadImage(fileName: Union[str, CharPtr]) -> Image
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadImageRaw"><code>LoadImageRaw</code> function</h2>

> Load image from RAW file data

Defined in raylib.h:

```c
Image LoadImageRaw(char * fileName, int width, int height, int format, int headerSize) 
```

Python wrapper:

```python
def LoadImageRaw(fileName: Union[str, CharPtr], width: int, height: int, format: int, headerSize: int) -> Image
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadImageAnim"><code>LoadImageAnim</code> function</h2>

> Load image sequence from file (frames appended to image.data)

Defined in raylib.h:

```c
Image LoadImageAnim(char * fileName, int frames) 
```

Python wrapper:

```python
def LoadImageAnim(fileName: Union[str, CharPtr], frames: Union[Seq[int], IntPtr]) -> Image
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadImageFromMemory"><code>LoadImageFromMemory</code> function</h2>

> Load image from memory buffer, fileType refers to extension: i.e. '.png'

Defined in raylib.h:

```c
Image LoadImageFromMemory(char * fileType, unsigned char * fileData, int dataSize) 
```

Python wrapper:

```python
def LoadImageFromMemory(fileType: Union[str, CharPtr], fileData: Union[Seq[int], UCharPtr], dataSize: int) -> Image
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadImageFromTexture"><code>LoadImageFromTexture</code> function</h2>

> Load image from GPU texture data

Defined in raylib.h:

```c
Image LoadImageFromTexture(Texture2D texture) 
```

Python wrapper:

```python
def LoadImageFromTexture(texture: Texture2D) -> Image
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadImageFromScreen"><code>LoadImageFromScreen</code> function</h2>

> Load image from screen buffer and (screenshot)

Defined in raylib.h:

```c
Image LoadImageFromScreen() 
```

Python wrapper:

```python
def LoadImageFromScreen() -> Image
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadImage"><code>UnloadImage</code> function</h2>

> Unload image from CPU memory (RAM)

Defined in raylib.h:

```c
void UnloadImage(Image image) 
```

Python wrapper:

```python
def UnloadImage(image: Image) -> None
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ExportImage"><code>ExportImage</code> function</h2>

> Export image data to file, returns true on success

Defined in raylib.h:

```c
bool ExportImage(Image image, char * fileName) 
```

Python wrapper:

```python
def ExportImage(image: Image, fileName: Union[str, CharPtr]) -> bool
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ExportImageAsCode"><code>ExportImageAsCode</code> function</h2>

> Export image as code file defining an array of bytes, returns true on success

Defined in raylib.h:

```c
bool ExportImageAsCode(Image image, char * fileName) 
```

Python wrapper:

```python
def ExportImageAsCode(image: Image, fileName: Union[str, CharPtr]) -> bool
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenImageColor"><code>GenImageColor</code> function</h2>

> Generate image: plain color

Defined in raylib.h:

```c
Image GenImageColor(int width, int height, Color color) 
```

Python wrapper:

```python
def GenImageColor(width: int, height: int, color: Color) -> Image
```

See also:
<a href="#Color">Color</a>, <a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenImageGradientV"><code>GenImageGradientV</code> function</h2>

> Generate image: vertical gradient

Defined in raylib.h:

```c
Image GenImageGradientV(int width, int height, Color top, Color bottom) 
```

Python wrapper:

```python
def GenImageGradientV(width: int, height: int, top: Color, bottom: Color) -> Image
```

See also:
<a href="#Color">Color</a>, <a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenImageGradientH"><code>GenImageGradientH</code> function</h2>

> Generate image: horizontal gradient

Defined in raylib.h:

```c
Image GenImageGradientH(int width, int height, Color left, Color right) 
```

Python wrapper:

```python
def GenImageGradientH(width: int, height: int, left: Color, right: Color) -> Image
```

See also:
<a href="#Color">Color</a>, <a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenImageGradientRadial"><code>GenImageGradientRadial</code> function</h2>

> Generate image: radial gradient

Defined in raylib.h:

```c
Image GenImageGradientRadial(int width, int height, float density, Color inner, Color outer) 
```

Python wrapper:

```python
def GenImageGradientRadial(width: int, height: int, density: float, inner: Color, outer: Color) -> Image
```

See also:
<a href="#Color">Color</a>, <a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenImageChecked"><code>GenImageChecked</code> function</h2>

> Generate image: checked

Defined in raylib.h:

```c
Image GenImageChecked(int width, int height, int checksX, int checksY, Color col1, Color col2) 
```

Python wrapper:

```python
def GenImageChecked(width: int, height: int, checksX: int, checksY: int, col1: Color, col2: Color) -> Image
```

See also:
<a href="#Color">Color</a>, <a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenImageWhiteNoise"><code>GenImageWhiteNoise</code> function</h2>

> Generate image: white noise

Defined in raylib.h:

```c
Image GenImageWhiteNoise(int width, int height, float factor) 
```

Python wrapper:

```python
def GenImageWhiteNoise(width: int, height: int, factor: float) -> Image
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenImageCellular"><code>GenImageCellular</code> function</h2>

> Generate image: cellular algorithm, bigger tileSize means bigger cells

Defined in raylib.h:

```c
Image GenImageCellular(int width, int height, int tileSize) 
```

Python wrapper:

```python
def GenImageCellular(width: int, height: int, tileSize: int) -> Image
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageCopy"><code>ImageCopy</code> function</h2>

> Create an image duplicate (useful for transformations)

Defined in raylib.h:

```c
Image ImageCopy(Image image) 
```

Python wrapper:

```python
def ImageCopy(image: Image) -> Image
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageFromImage"><code>ImageFromImage</code> function</h2>

> Create an image from another image piece

Defined in raylib.h:

```c
Image ImageFromImage(Image image, Rectangle rec) 
```

Python wrapper:

```python
def ImageFromImage(image: Image, rec: Rectangle) -> Image
```

See also:
<a href="#Image">Image</a>, <a href="#Rectangle">Rectangle</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageText"><code>ImageText</code> function</h2>

> Create an image from text (default font)

Defined in raylib.h:

```c
Image ImageText(char * text, int fontSize, Color color) 
```

Python wrapper:

```python
def ImageText(text: Union[str, CharPtr], fontSize: int, color: Color) -> Image
```

See also:
<a href="#Color">Color</a>, <a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageTextEx"><code>ImageTextEx</code> function</h2>

> Create an image from text (custom sprite font)

Defined in raylib.h:

```c
Image ImageTextEx(Font font, char * text, float fontSize, float spacing, Color tint) 
```

Python wrapper:

```python
def ImageTextEx(font: Font, text: Union[str, CharPtr], fontSize: float, spacing: float, tint: Color) -> Image
```

See also:
<a href="#Font">Font</a>, <a href="#Color">Color</a>, <a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageFormat"><code>ImageFormat</code> function</h2>

> Convert image data to desired format

Defined in raylib.h:

```c
void ImageFormat(Image * image, int newFormat) 
```

Python wrapper:

```python
def ImageFormat(image: ImagePtr, newFormat: int) -> None
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageToPOT"><code>ImageToPOT</code> function</h2>

> Convert image to POT (power-of-two)

Defined in raylib.h:

```c
void ImageToPOT(Image * image, Color fill) 
```

Python wrapper:

```python
def ImageToPOT(image: ImagePtr, fill: Color) -> None
```

See also:
<a href="#Image">Image</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageCrop"><code>ImageCrop</code> function</h2>

> Crop an image to a defined rectangle

Defined in raylib.h:

```c
void ImageCrop(Image * image, Rectangle crop) 
```

Python wrapper:

```python
def ImageCrop(image: ImagePtr, crop: Rectangle) -> None
```

See also:
<a href="#Image">Image</a>, <a href="#Rectangle">Rectangle</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageAlphaCrop"><code>ImageAlphaCrop</code> function</h2>

> Crop image depending on alpha value

Defined in raylib.h:

```c
void ImageAlphaCrop(Image * image, float threshold) 
```

Python wrapper:

```python
def ImageAlphaCrop(image: ImagePtr, threshold: float) -> None
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageAlphaClear"><code>ImageAlphaClear</code> function</h2>

> Clear alpha channel to desired color

Defined in raylib.h:

```c
void ImageAlphaClear(Image * image, Color color, float threshold) 
```

Python wrapper:

```python
def ImageAlphaClear(image: ImagePtr, color: Color, threshold: float) -> None
```

See also:
<a href="#Image">Image</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageAlphaMask"><code>ImageAlphaMask</code> function</h2>

> Apply alpha mask to image

Defined in raylib.h:

```c
void ImageAlphaMask(Image * image, Image alphaMask) 
```

Python wrapper:

```python
def ImageAlphaMask(image: ImagePtr, alphaMask: Image) -> None
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageAlphaPremultiply"><code>ImageAlphaPremultiply</code> function</h2>

> Premultiply alpha channel

Defined in raylib.h:

```c
void ImageAlphaPremultiply(Image * image) 
```

Python wrapper:

```python
def ImageAlphaPremultiply(image: ImagePtr) -> None
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageResize"><code>ImageResize</code> function</h2>

> Resize image (Bicubic scaling algorithm)

Defined in raylib.h:

```c
void ImageResize(Image * image, int newWidth, int newHeight) 
```

Python wrapper:

```python
def ImageResize(image: ImagePtr, newWidth: int, newHeight: int) -> None
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageResizeNN"><code>ImageResizeNN</code> function</h2>

> Resize image (Nearest-Neighbor scaling algorithm)

Defined in raylib.h:

```c
void ImageResizeNN(Image * image, int newWidth, int newHeight) 
```

Python wrapper:

```python
def ImageResizeNN(image: ImagePtr, newWidth: int, newHeight: int) -> None
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageResizeCanvas"><code>ImageResizeCanvas</code> function</h2>

> Resize canvas and fill with color

Defined in raylib.h:

```c
void ImageResizeCanvas(Image * image, int newWidth, int newHeight, int offsetX, int offsetY, Color fill) 
```

Python wrapper:

```python
def ImageResizeCanvas(image: ImagePtr, newWidth: int, newHeight: int, offsetX: int, offsetY: int, fill: Color) -> None
```

See also:
<a href="#Image">Image</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageMipmaps"><code>ImageMipmaps</code> function</h2>

> Compute all mipmap levels for a provided image

Defined in raylib.h:

```c
void ImageMipmaps(Image * image) 
```

Python wrapper:

```python
def ImageMipmaps(image: ImagePtr) -> None
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDither"><code>ImageDither</code> function</h2>

> Dither image data to 16bpp or lower (Floyd-Steinberg dithering)

Defined in raylib.h:

```c
void ImageDither(Image * image, int rBpp, int gBpp, int bBpp, int aBpp) 
```

Python wrapper:

```python
def ImageDither(image: ImagePtr, rBpp: int, gBpp: int, bBpp: int, aBpp: int) -> None
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageFlipVertical"><code>ImageFlipVertical</code> function</h2>

> Flip image vertically

Defined in raylib.h:

```c
void ImageFlipVertical(Image * image) 
```

Python wrapper:

```python
def ImageFlipVertical(image: ImagePtr) -> None
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageFlipHorizontal"><code>ImageFlipHorizontal</code> function</h2>

> Flip image horizontally

Defined in raylib.h:

```c
void ImageFlipHorizontal(Image * image) 
```

Python wrapper:

```python
def ImageFlipHorizontal(image: ImagePtr) -> None
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageRotateCW"><code>ImageRotateCW</code> function</h2>

> Rotate image clockwise 90deg

Defined in raylib.h:

```c
void ImageRotateCW(Image * image) 
```

Python wrapper:

```python
def ImageRotateCW(image: ImagePtr) -> None
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageRotateCCW"><code>ImageRotateCCW</code> function</h2>

> Rotate image counter-clockwise 90deg

Defined in raylib.h:

```c
void ImageRotateCCW(Image * image) 
```

Python wrapper:

```python
def ImageRotateCCW(image: ImagePtr) -> None
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageColorTint"><code>ImageColorTint</code> function</h2>

> Modify image color: tint

Defined in raylib.h:

```c
void ImageColorTint(Image * image, Color color) 
```

Python wrapper:

```python
def ImageColorTint(image: ImagePtr, color: Color) -> None
```

See also:
<a href="#Image">Image</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageColorInvert"><code>ImageColorInvert</code> function</h2>

> Modify image color: invert

Defined in raylib.h:

```c
void ImageColorInvert(Image * image) 
```

Python wrapper:

```python
def ImageColorInvert(image: ImagePtr) -> None
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageColorGrayscale"><code>ImageColorGrayscale</code> function</h2>

> Modify image color: grayscale

Defined in raylib.h:

```c
void ImageColorGrayscale(Image * image) 
```

Python wrapper:

```python
def ImageColorGrayscale(image: ImagePtr) -> None
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageColorContrast"><code>ImageColorContrast</code> function</h2>

> Modify image color: contrast (-100 to 100)

Defined in raylib.h:

```c
void ImageColorContrast(Image * image, float contrast) 
```

Python wrapper:

```python
def ImageColorContrast(image: ImagePtr, contrast: float) -> None
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageColorBrightness"><code>ImageColorBrightness</code> function</h2>

> Modify image color: brightness (-255 to 255)

Defined in raylib.h:

```c
void ImageColorBrightness(Image * image, int brightness) 
```

Python wrapper:

```python
def ImageColorBrightness(image: ImagePtr, brightness: int) -> None
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageColorReplace"><code>ImageColorReplace</code> function</h2>

> Modify image color: replace color

Defined in raylib.h:

```c
void ImageColorReplace(Image * image, Color color, Color replace) 
```

Python wrapper:

```python
def ImageColorReplace(image: ImagePtr, color: Color, replace: Color) -> None
```

See also:
<a href="#Image">Image</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadImageColors"><code>LoadImageColors</code> function</h2>

> Load color data from image as a Color array (RGBA - 32bit)

Defined in raylib.h:

```c
Color * LoadImageColors(Image image) 
```

Python wrapper:

```python
def LoadImageColors(image: Image) -> ColorPtr
```

See also:
<a href="#Image">Image</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadImagePalette"><code>LoadImagePalette</code> function</h2>

> Load colors palette from image as a Color array (RGBA - 32bit)

Defined in raylib.h:

```c
Color * LoadImagePalette(Image image, int maxPaletteSize, int colorCount) 
```

Python wrapper:

```python
def LoadImagePalette(image: Image, maxPaletteSize: int, colorCount: Union[Seq[int], IntPtr]) -> ColorPtr
```

See also:
<a href="#Image">Image</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadImageColors"><code>UnloadImageColors</code> function</h2>

> Unload color data loaded with LoadImageColors()

Defined in raylib.h:

```c
void UnloadImageColors(Color * colors) 
```

Python wrapper:

```python
def UnloadImageColors(colors: ColorPtr) -> None
```

See also:
<a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadImagePalette"><code>UnloadImagePalette</code> function</h2>

> Unload colors palette loaded with LoadImagePalette()

Defined in raylib.h:

```c
void UnloadImagePalette(Color * colors) 
```

Python wrapper:

```python
def UnloadImagePalette(colors: ColorPtr) -> None
```

See also:
<a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetImageAlphaBorder"><code>GetImageAlphaBorder</code> function</h2>

> Get image alpha border rectangle

Defined in raylib.h:

```c
Rectangle GetImageAlphaBorder(Image image, float threshold) 
```

Python wrapper:

```python
def GetImageAlphaBorder(image: Image, threshold: float) -> Rectangle
```

See also:
<a href="#Image">Image</a>, <a href="#Rectangle">Rectangle</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetImageColor"><code>GetImageColor</code> function</h2>

> Get image pixel color at (x, y) position

Defined in raylib.h:

```c
Color GetImageColor(Image image, int x, int y) 
```

Python wrapper:

```python
def GetImageColor(image: Image, x: int, y: int) -> Color
```

See also:
<a href="#Image">Image</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageClearBackground"><code>ImageClearBackground</code> function</h2>

> Clear image background with given color

Defined in raylib.h:

```c
void ImageClearBackground(Image * dst, Color color) 
```

Python wrapper:

```python
def ImageClearBackground(dst: ImagePtr, color: Color) -> None
```

See also:
<a href="#Image">Image</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDrawPixel"><code>ImageDrawPixel</code> function</h2>

> Draw pixel within an image

Defined in raylib.h:

```c
void ImageDrawPixel(Image * dst, int posX, int posY, Color color) 
```

Python wrapper:

```python
def ImageDrawPixel(dst: ImagePtr, posX: int, posY: int, color: Color) -> None
```

See also:
<a href="#Image">Image</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDrawPixelV"><code>ImageDrawPixelV</code> function</h2>

> Draw pixel within an image (Vector version)

Defined in raylib.h:

```c
void ImageDrawPixelV(Image * dst, Vector2 position, Color color) 
```

Python wrapper:

```python
def ImageDrawPixelV(dst: ImagePtr, position: Vector2, color: Color) -> None
```

See also:
<a href="#Image">Image</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDrawLine"><code>ImageDrawLine</code> function</h2>

> Draw line within an image

Defined in raylib.h:

```c
void ImageDrawLine(Image * dst, int startPosX, int startPosY, int endPosX, int endPosY, Color color) 
```

Python wrapper:

```python
def ImageDrawLine(dst: ImagePtr, startPosX: int, startPosY: int, endPosX: int, endPosY: int, color: Color) -> None
```

See also:
<a href="#Image">Image</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDrawLineV"><code>ImageDrawLineV</code> function</h2>

> Draw line within an image (Vector version)

Defined in raylib.h:

```c
void ImageDrawLineV(Image * dst, Vector2 start, Vector2 end, Color color) 
```

Python wrapper:

```python
def ImageDrawLineV(dst: ImagePtr, start: Vector2, end: Vector2, color: Color) -> None
```

See also:
<a href="#Image">Image</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDrawCircle"><code>ImageDrawCircle</code> function</h2>

> Draw circle within an image

Defined in raylib.h:

```c
void ImageDrawCircle(Image * dst, int centerX, int centerY, int radius, Color color) 
```

Python wrapper:

```python
def ImageDrawCircle(dst: ImagePtr, centerX: int, centerY: int, radius: int, color: Color) -> None
```

See also:
<a href="#Image">Image</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDrawCircleV"><code>ImageDrawCircleV</code> function</h2>

> Draw circle within an image (Vector version)

Defined in raylib.h:

```c
void ImageDrawCircleV(Image * dst, Vector2 center, int radius, Color color) 
```

Python wrapper:

```python
def ImageDrawCircleV(dst: ImagePtr, center: Vector2, radius: int, color: Color) -> None
```

See also:
<a href="#Image">Image</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDrawRectangle"><code>ImageDrawRectangle</code> function</h2>

> Draw rectangle within an image

Defined in raylib.h:

```c
void ImageDrawRectangle(Image * dst, int posX, int posY, int width, int height, Color color) 
```

Python wrapper:

```python
def ImageDrawRectangle(dst: ImagePtr, posX: int, posY: int, width: int, height: int, color: Color) -> None
```

See also:
<a href="#Image">Image</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDrawRectangleV"><code>ImageDrawRectangleV</code> function</h2>

> Draw rectangle within an image (Vector version)

Defined in raylib.h:

```c
void ImageDrawRectangleV(Image * dst, Vector2 position, Vector2 size, Color color) 
```

Python wrapper:

```python
def ImageDrawRectangleV(dst: ImagePtr, position: Vector2, size: Vector2, color: Color) -> None
```

See also:
<a href="#Image">Image</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDrawRectangleRec"><code>ImageDrawRectangleRec</code> function</h2>

> Draw rectangle within an image

Defined in raylib.h:

```c
void ImageDrawRectangleRec(Image * dst, Rectangle rec, Color color) 
```

Python wrapper:

```python
def ImageDrawRectangleRec(dst: ImagePtr, rec: Rectangle, color: Color) -> None
```

See also:
<a href="#Image">Image</a>, <a href="#Rectangle">Rectangle</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDrawRectangleLines"><code>ImageDrawRectangleLines</code> function</h2>

> Draw rectangle lines within an image

Defined in raylib.h:

```c
void ImageDrawRectangleLines(Image * dst, Rectangle rec, int thick, Color color) 
```

Python wrapper:

```python
def ImageDrawRectangleLines(dst: ImagePtr, rec: Rectangle, thick: int, color: Color) -> None
```

See also:
<a href="#Image">Image</a>, <a href="#Rectangle">Rectangle</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDraw"><code>ImageDraw</code> function</h2>

> Draw a source image within a destination image (tint applied to source)

Defined in raylib.h:

```c
void ImageDraw(Image * dst, Image src, Rectangle srcRec, Rectangle dstRec, Color tint) 
```

Python wrapper:

```python
def ImageDraw(dst: ImagePtr, src: Image, srcRec: Rectangle, dstRec: Rectangle, tint: Color) -> None
```

See also:
<a href="#Image">Image</a>, <a href="#Rectangle">Rectangle</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDrawText"><code>ImageDrawText</code> function</h2>

> Draw text (using default font) within an image (destination)

Defined in raylib.h:

```c
void ImageDrawText(Image * dst, char * text, int posX, int posY, int fontSize, Color color) 
```

Python wrapper:

```python
def ImageDrawText(dst: ImagePtr, text: Union[str, CharPtr], posX: int, posY: int, fontSize: int, color: Color) -> None
```

See also:
<a href="#Image">Image</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ImageDrawTextEx"><code>ImageDrawTextEx</code> function</h2>

> Draw text (custom sprite font) within an image (destination)

Defined in raylib.h:

```c
void ImageDrawTextEx(Image * dst, Font font, char * text, Vector2 position, float fontSize, float spacing, Color tint) 
```

Python wrapper:

```python
def ImageDrawTextEx(dst: ImagePtr, font: Font, text: Union[str, CharPtr], position: Vector2, fontSize: float, spacing: float, tint: Color) -> None
```

See also:
<a href="#Image">Image</a>, <a href="#Font">Font</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadTexture"><code>LoadTexture</code> function</h2>

> Load texture from file into GPU memory (VRAM)

Defined in raylib.h:

```c
Texture2D LoadTexture(char * fileName) 
```

Python wrapper:

```python
def LoadTexture(fileName: Union[str, CharPtr]) -> Texture2D
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadTextureFromImage"><code>LoadTextureFromImage</code> function</h2>

> Load texture from image data

Defined in raylib.h:

```c
Texture2D LoadTextureFromImage(Image image) 
```

Python wrapper:

```python
def LoadTextureFromImage(image: Image) -> Texture2D
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadTextureCubemap"><code>LoadTextureCubemap</code> function</h2>

> Load cubemap from image, multiple image cubemap layouts supported

Defined in raylib.h:

```c
TextureCubemap LoadTextureCubemap(Image image, int layout) 
```

Python wrapper:

```python
def LoadTextureCubemap(image: Image, layout: int) -> TextureCubemap
```

See also:
<a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadRenderTexture"><code>LoadRenderTexture</code> function</h2>

> Load texture for rendering (framebuffer)

Defined in raylib.h:

```c
RenderTexture2D LoadRenderTexture(int width, int height) 
```

Python wrapper:

```python
def LoadRenderTexture(width: int, height: int) -> RenderTexture2D
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadTexture"><code>UnloadTexture</code> function</h2>

> Unload texture from GPU memory (VRAM)

Defined in raylib.h:

```c
void UnloadTexture(Texture2D texture) 
```

Python wrapper:

```python
def UnloadTexture(texture: Texture2D) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadRenderTexture"><code>UnloadRenderTexture</code> function</h2>

> Unload render texture from GPU memory (VRAM)

Defined in raylib.h:

```c
void UnloadRenderTexture(RenderTexture2D target) 
```

Python wrapper:

```python
def UnloadRenderTexture(target: RenderTexture2D) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UpdateTexture"><code>UpdateTexture</code> function</h2>

> Update GPU texture with new data

Defined in raylib.h:

```c
void UpdateTexture(Texture2D texture, void pixels) 
```

Python wrapper:

```python
def UpdateTexture(texture: Texture2D, pixels: bytes) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UpdateTextureRec"><code>UpdateTextureRec</code> function</h2>

> Update GPU texture rectangle with new data

Defined in raylib.h:

```c
void UpdateTextureRec(Texture2D texture, Rectangle rec, void pixels) 
```

Python wrapper:

```python
def UpdateTextureRec(texture: Texture2D, rec: Rectangle, pixels: bytes) -> None
```

See also:
<a href="#Rectangle">Rectangle</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenTextureMipmaps"><code>GenTextureMipmaps</code> function</h2>

> Generate GPU mipmaps for a texture

Defined in raylib.h:

```c
void GenTextureMipmaps(Texture2D * texture) 
```

Python wrapper:

```python
def GenTextureMipmaps(texture: Texture2DPtr) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetTextureFilter"><code>SetTextureFilter</code> function</h2>

> Set texture scaling filter mode

Defined in raylib.h:

```c
void SetTextureFilter(Texture2D texture, int filter) 
```

Python wrapper:

```python
def SetTextureFilter(texture: Texture2D, filter: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetTextureWrap"><code>SetTextureWrap</code> function</h2>

> Set texture wrapping mode

Defined in raylib.h:

```c
void SetTextureWrap(Texture2D texture, int wrap) 
```

Python wrapper:

```python
def SetTextureWrap(texture: Texture2D, wrap: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTexture"><code>DrawTexture</code> function</h2>

> Draw a Texture2D

Defined in raylib.h:

```c
void DrawTexture(Texture2D texture, int posX, int posY, Color tint) 
```

Python wrapper:

```python
def DrawTexture(texture: Texture2D, posX: int, posY: int, tint: Color) -> None
```

See also:
<a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTextureV"><code>DrawTextureV</code> function</h2>

> Draw a Texture2D with position defined as Vector2

Defined in raylib.h:

```c
void DrawTextureV(Texture2D texture, Vector2 position, Color tint) 
```

Python wrapper:

```python
def DrawTextureV(texture: Texture2D, position: Vector2, tint: Color) -> None
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTextureEx"><code>DrawTextureEx</code> function</h2>

> Draw a Texture2D with extended parameters

Defined in raylib.h:

```c
void DrawTextureEx(Texture2D texture, Vector2 position, float rotation, float scale, Color tint) 
```

Python wrapper:

```python
def DrawTextureEx(texture: Texture2D, position: Vector2, rotation: float, scale: float, tint: Color) -> None
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTextureRec"><code>DrawTextureRec</code> function</h2>

> Draw a part of a texture defined by a rectangle

Defined in raylib.h:

```c
void DrawTextureRec(Texture2D texture, Rectangle source, Vector2 position, Color tint) 
```

Python wrapper:

```python
def DrawTextureRec(texture: Texture2D, source: Rectangle, position: Vector2, tint: Color) -> None
```

See also:
<a href="#Rectangle">Rectangle</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTextureQuad"><code>DrawTextureQuad</code> function</h2>

> Draw texture quad with tiling and offset parameters

Defined in raylib.h:

```c
void DrawTextureQuad(Texture2D texture, Vector2 tiling, Vector2 offset, Rectangle quad, Color tint) 
```

Python wrapper:

```python
def DrawTextureQuad(texture: Texture2D, tiling: Vector2, offset: Vector2, quad: Rectangle, tint: Color) -> None
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Rectangle">Rectangle</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTextureTiled"><code>DrawTextureTiled</code> function</h2>

> Draw part of a texture (defined by a rectangle) with rotation and scale tiled into dest.

Defined in raylib.h:

```c
void DrawTextureTiled(Texture2D texture, Rectangle source, Rectangle dest, Vector2 origin, float rotation, float scale, Color tint) 
```

Python wrapper:

```python
def DrawTextureTiled(texture: Texture2D, source: Rectangle, dest: Rectangle, origin: Vector2, rotation: float, scale: float, tint: Color) -> None
```

See also:
<a href="#Rectangle">Rectangle</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTexturePro"><code>DrawTexturePro</code> function</h2>

> Draw a part of a texture defined by a rectangle with 'pro' parameters

Defined in raylib.h:

```c
void DrawTexturePro(Texture2D texture, Rectangle source, Rectangle dest, Vector2 origin, float rotation, Color tint) 
```

Python wrapper:

```python
def DrawTexturePro(texture: Texture2D, source: Rectangle, dest: Rectangle, origin: Vector2, rotation: float, tint: Color) -> None
```

See also:
<a href="#Rectangle">Rectangle</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTextureNPatch"><code>DrawTextureNPatch</code> function</h2>

> Draws a texture (or part of it) that stretches or shrinks nicely

Defined in raylib.h:

```c
void DrawTextureNPatch(Texture2D texture, NPatchInfo nPatchInfo, Rectangle dest, Vector2 origin, float rotation, Color tint) 
```

Python wrapper:

```python
def DrawTextureNPatch(texture: Texture2D, nPatchInfo: NPatchInfo, dest: Rectangle, origin: Vector2, rotation: float, tint: Color) -> None
```

See also:
<a href="#NPatchInfo">NPatchInfo</a>, <a href="#Rectangle">Rectangle</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTexturePoly"><code>DrawTexturePoly</code> function</h2>

> Draw a textured polygon

Defined in raylib.h:

```c
void DrawTexturePoly(Texture2D texture, Vector2 center, Vector2 * points, Vector2 * texcoords, int pointCount, Color tint) 
```

Python wrapper:

```python
def DrawTexturePoly(texture: Texture2D, center: Vector2, points: Vector2Ptr, texcoords: Vector2Ptr, pointCount: int, tint: Color) -> None
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Fade"><code>Fade</code> function</h2>

> Get color with alpha applied, alpha goes from 0.0f to 1.0f

Defined in raylib.h:

```c
Color Fade(Color color, float alpha) 
```

Python wrapper:

```python
def Fade(color: Color, alpha: float) -> Color
```

See also:
<a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ColorToInt"><code>ColorToInt</code> function</h2>

> Get hexadecimal value for a Color

Defined in raylib.h:

```c
int ColorToInt(Color color) 
```

Python wrapper:

```python
def ColorToInt(color: Color) -> int
```

See also:
<a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ColorNormalize"><code>ColorNormalize</code> function</h2>

> Get Color normalized as float [0..1]

Defined in raylib.h:

```c
Vector4 ColorNormalize(Color color) 
```

Python wrapper:

```python
def ColorNormalize(color: Color) -> Vector4
```

See also:
<a href="#Color">Color</a>, <a href="#Vector4">Vector4</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ColorFromNormalized"><code>ColorFromNormalized</code> function</h2>

> Get Color from normalized values [0..1]

Defined in raylib.h:

```c
Color ColorFromNormalized(Vector4 normalized) 
```

Python wrapper:

```python
def ColorFromNormalized(normalized: Vector4) -> Color
```

See also:
<a href="#Vector4">Vector4</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ColorToHSV"><code>ColorToHSV</code> function</h2>

> Get HSV values for a Color, hue [0..360], saturation/value [0..1]

Defined in raylib.h:

```c
Vector3 ColorToHSV(Color color) 
```

Python wrapper:

```python
def ColorToHSV(color: Color) -> Vector3
```

See also:
<a href="#Color">Color</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ColorFromHSV"><code>ColorFromHSV</code> function</h2>

> Get a Color from HSV values, hue [0..360], saturation/value [0..1]

Defined in raylib.h:

```c
Color ColorFromHSV(float hue, float saturation, float value) 
```

Python wrapper:

```python
def ColorFromHSV(hue: float, saturation: float, value: float) -> Color
```

See also:
<a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ColorAlpha"><code>ColorAlpha</code> function</h2>

> Get color with alpha applied, alpha goes from 0.0f to 1.0f

Defined in raylib.h:

```c
Color ColorAlpha(Color color, float alpha) 
```

Python wrapper:

```python
def ColorAlpha(color: Color, alpha: float) -> Color
```

See also:
<a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ColorAlphaBlend"><code>ColorAlphaBlend</code> function</h2>

> Get src alpha-blended into dst color with tint

Defined in raylib.h:

```c
Color ColorAlphaBlend(Color dst, Color src, Color tint) 
```

Python wrapper:

```python
def ColorAlphaBlend(dst: Color, src: Color, tint: Color) -> Color
```

See also:
<a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetColor"><code>GetColor</code> function</h2>

> Get Color structure from hexadecimal value

Defined in raylib.h:

```c
Color GetColor(unsigned int hexValue) 
```

Python wrapper:

```python
def GetColor(hexValue: int) -> Color
```

See also:
<a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetPixelColor"><code>GetPixelColor</code> function</h2>

> Get Color from a source pixel pointer of certain format

Defined in raylib.h:

```c
Color GetPixelColor(void srcPtr, int format) 
```

Python wrapper:

```python
def GetPixelColor(srcPtr: bytes, format: int) -> Color
```

See also:
<a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetPixelColor"><code>SetPixelColor</code> function</h2>

> Set color formatted into destination pixel pointer

Defined in raylib.h:

```c
void SetPixelColor(void dstPtr, Color color, int format) 
```

Python wrapper:

```python
def SetPixelColor(dstPtr: bytes, color: Color, format: int) -> None
```

See also:
<a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetPixelDataSize"><code>GetPixelDataSize</code> function</h2>

> Get pixel data size in bytes for certain format

Defined in raylib.h:

```c
int GetPixelDataSize(int width, int height, int format) 
```

Python wrapper:

```python
def GetPixelDataSize(width: int, height: int, format: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetFontDefault"><code>GetFontDefault</code> function</h2>

> Get the default Font

Defined in raylib.h:

```c
Font GetFontDefault() 
```

Python wrapper:

```python
def GetFontDefault() -> Font
```

See also:
<a href="#Font">Font</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadFont"><code>LoadFont</code> function</h2>

> Load font from file into GPU memory (VRAM)

Defined in raylib.h:

```c
Font LoadFont(char * fileName) 
```

Python wrapper:

```python
def LoadFont(fileName: Union[str, CharPtr]) -> Font
```

See also:
<a href="#Font">Font</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadFontEx"><code>LoadFontEx</code> function</h2>

> Load font from file with extended parameters, use NULL for fontChars and 0 for glyphCount to load the default character set

Defined in raylib.h:

```c
Font LoadFontEx(char * fileName, int fontSize, int fontChars, int glyphCount) 
```

Python wrapper:

```python
def LoadFontEx(fileName: Union[str, CharPtr], fontSize: int, fontChars: Union[Seq[int], IntPtr], glyphCount: int) -> Font
```

See also:
<a href="#Font">Font</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadFontFromImage"><code>LoadFontFromImage</code> function</h2>

> Load font from Image (XNA style)

Defined in raylib.h:

```c
Font LoadFontFromImage(Image image, Color key, int firstChar) 
```

Python wrapper:

```python
def LoadFontFromImage(image: Image, key: Color, firstChar: int) -> Font
```

See also:
<a href="#Image">Image</a>, <a href="#Color">Color</a>, <a href="#Font">Font</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadFontFromMemory"><code>LoadFontFromMemory</code> function</h2>

> Load font from memory buffer, fileType refers to extension: i.e. '.ttf'

Defined in raylib.h:

```c
Font LoadFontFromMemory(char * fileType, unsigned char * fileData, int dataSize, int fontSize, int fontChars, int glyphCount) 
```

Python wrapper:

```python
def LoadFontFromMemory(fileType: Union[str, CharPtr], fileData: Union[Seq[int], UCharPtr], dataSize: int, fontSize: int, fontChars: Union[Seq[int], IntPtr], glyphCount: int) -> Font
```

See also:
<a href="#Font">Font</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadFontData"><code>LoadFontData</code> function</h2>

> Load font data for further use

Defined in raylib.h:

```c
GlyphInfo * LoadFontData(unsigned char * fileData, int dataSize, int fontSize, int fontChars, int glyphCount, int type) 
```

Python wrapper:

```python
def LoadFontData(fileData: Union[Seq[int], UCharPtr], dataSize: int, fontSize: int, fontChars: Union[Seq[int], IntPtr], glyphCount: int, type: int) -> GlyphInfoPtr
```

See also:
<a href="#GlyphInfo">GlyphInfo</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenImageFontAtlas"><code>GenImageFontAtlas</code> function</h2>

> Generate image font atlas using chars info

Defined in raylib.h:

```c
Image GenImageFontAtlas(GlyphInfo * chars, Rectangle ** recs, int glyphCount, int fontSize, int padding, int packMethod) 
```

Python wrapper:

```python
def GenImageFontAtlas(chars: GlyphInfoPtr, recs: RectanglePtr, glyphCount: int, fontSize: int, padding: int, packMethod: int) -> Image
```

See also:
<a href="#GlyphInfo">GlyphInfo</a>, <a href="#Rectangle">Rectangle</a>, <a href="#Image">Image</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadFontData"><code>UnloadFontData</code> function</h2>

> Unload font chars info data (RAM)

Defined in raylib.h:

```c
void UnloadFontData(GlyphInfo * chars, int glyphCount) 
```

Python wrapper:

```python
def UnloadFontData(chars: GlyphInfoPtr, glyphCount: int) -> None
```

See also:
<a href="#GlyphInfo">GlyphInfo</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadFont"><code>UnloadFont</code> function</h2>

> Unload font from GPU memory (VRAM)

Defined in raylib.h:

```c
void UnloadFont(Font font) 
```

Python wrapper:

```python
def UnloadFont(font: Font) -> None
```

See also:
<a href="#Font">Font</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ExportFontAsCode"><code>ExportFontAsCode</code> function</h2>

> Export font as code file, returns true on success

Defined in raylib.h:

```c
bool ExportFontAsCode(Font font, char * fileName) 
```

Python wrapper:

```python
def ExportFontAsCode(font: Font, fileName: Union[str, CharPtr]) -> bool
```

See also:
<a href="#Font">Font</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawFPS"><code>DrawFPS</code> function</h2>

> Draw current FPS

Defined in raylib.h:

```c
void DrawFPS(int posX, int posY) 
```

Python wrapper:

```python
def DrawFPS(posX: int, posY: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawText"><code>DrawText</code> function</h2>

> Draw text (using default font)

Defined in raylib.h:

```c
void DrawText(char * text, int posX, int posY, int fontSize, Color color) 
```

Python wrapper:

```python
def DrawText(text: Union[str, CharPtr], posX: int, posY: int, fontSize: int, color: Color) -> None
```

See also:
<a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTextEx"><code>DrawTextEx</code> function</h2>

> Draw text using font and additional parameters

Defined in raylib.h:

```c
void DrawTextEx(Font font, char * text, Vector2 position, float fontSize, float spacing, Color tint) 
```

Python wrapper:

```python
def DrawTextEx(font: Font, text: Union[str, CharPtr], position: Vector2, fontSize: float, spacing: float, tint: Color) -> None
```

See also:
<a href="#Font">Font</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTextPro"><code>DrawTextPro</code> function</h2>

> Draw text using Font and pro parameters (rotation)

Defined in raylib.h:

```c
void DrawTextPro(Font font, char * text, Vector2 position, Vector2 origin, float rotation, float fontSize, float spacing, Color tint) 
```

Python wrapper:

```python
def DrawTextPro(font: Font, text: Union[str, CharPtr], position: Vector2, origin: Vector2, rotation: float, fontSize: float, spacing: float, tint: Color) -> None
```

See also:
<a href="#Font">Font</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTextCodepoint"><code>DrawTextCodepoint</code> function</h2>

> Draw one character (codepoint)

Defined in raylib.h:

```c
void DrawTextCodepoint(Font font, int codepoint, Vector2 position, float fontSize, Color tint) 
```

Python wrapper:

```python
def DrawTextCodepoint(font: Font, codepoint: int, position: Vector2, fontSize: float, tint: Color) -> None
```

See also:
<a href="#Font">Font</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTextCodepoints"><code>DrawTextCodepoints</code> function</h2>

> Draw multiple character (codepoint)

Defined in raylib.h:

```c
void DrawTextCodepoints(Font font, int codepoints, int count, Vector2 position, float fontSize, float spacing, Color tint) 
```

Python wrapper:

```python
def DrawTextCodepoints(font: Font, codepoints: Union[Seq[int], IntPtr], count: int, position: Vector2, fontSize: float, spacing: float, tint: Color) -> None
```

See also:
<a href="#Font">Font</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MeasureText"><code>MeasureText</code> function</h2>

> Measure string width for default font

Defined in raylib.h:

```c
int MeasureText(char * text, int fontSize) 
```

Python wrapper:

```python
def MeasureText(text: Union[str, CharPtr], fontSize: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MeasureTextEx"><code>MeasureTextEx</code> function</h2>

> Measure string size for Font

Defined in raylib.h:

```c
Vector2 MeasureTextEx(Font font, char * text, float fontSize, float spacing) 
```

Python wrapper:

```python
def MeasureTextEx(font: Font, text: Union[str, CharPtr], fontSize: float, spacing: float) -> Vector2
```

See also:
<a href="#Font">Font</a>, <a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetGlyphIndex"><code>GetGlyphIndex</code> function</h2>

> Get glyph index position in font for a codepoint (unicode character), fallback to '?' if not found

Defined in raylib.h:

```c
int GetGlyphIndex(Font font, int codepoint) 
```

Python wrapper:

```python
def GetGlyphIndex(font: Font, codepoint: int) -> int
```

See also:
<a href="#Font">Font</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetGlyphInfo"><code>GetGlyphInfo</code> function</h2>

> Get glyph font info data for a codepoint (unicode character), fallback to '?' if not found

Defined in raylib.h:

```c
GlyphInfo GetGlyphInfo(Font font, int codepoint) 
```

Python wrapper:

```python
def GetGlyphInfo(font: Font, codepoint: int) -> GlyphInfo
```

See also:
<a href="#Font">Font</a>, <a href="#GlyphInfo">GlyphInfo</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetGlyphAtlasRec"><code>GetGlyphAtlasRec</code> function</h2>

> Get glyph rectangle in font atlas for a codepoint (unicode character), fallback to '?' if not found

Defined in raylib.h:

```c
Rectangle GetGlyphAtlasRec(Font font, int codepoint) 
```

Python wrapper:

```python
def GetGlyphAtlasRec(font: Font, codepoint: int) -> Rectangle
```

See also:
<a href="#Font">Font</a>, <a href="#Rectangle">Rectangle</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadCodepoints"><code>LoadCodepoints</code> function</h2>

> Load all codepoints from a UTF-8 text string, codepoints count returned by parameter

Defined in raylib.h:

```c
int LoadCodepoints(char * text, int count) 
```

Python wrapper:

```python
def LoadCodepoints(text: Union[str, CharPtr], count: Union[Seq[int], IntPtr]) -> Union[Seq[int], IntPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadCodepoints"><code>UnloadCodepoints</code> function</h2>

> Unload codepoints data from memory

Defined in raylib.h:

```c
void UnloadCodepoints(int codepoints) 
```

Python wrapper:

```python
def UnloadCodepoints(codepoints: Union[Seq[int], IntPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetCodepointCount"><code>GetCodepointCount</code> function</h2>

> Get total number of codepoints in a UTF-8 encoded string

Defined in raylib.h:

```c
int GetCodepointCount(char * text) 
```

Python wrapper:

```python
def GetCodepointCount(text: Union[str, CharPtr]) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetCodepoint"><code>GetCodepoint</code> function</h2>

> Get next codepoint in a UTF-8 encoded string, 0x3f('?') is returned on failure

Defined in raylib.h:

```c
int GetCodepoint(char * text, int bytesProcessed) 
```

Python wrapper:

```python
def GetCodepoint(text: Union[str, CharPtr], bytesProcessed: Union[Seq[int], IntPtr]) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CodepointToUTF8"><code>CodepointToUTF8</code> function</h2>

> Encode one codepoint into UTF-8 byte array (array length returned as parameter)

Defined in raylib.h:

```c
char * CodepointToUTF8(int codepoint, int byteSize) 
```

Python wrapper:

```python
def CodepointToUTF8(codepoint: int, byteSize: Union[Seq[int], IntPtr]) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextCodepointsToUTF8"><code>TextCodepointsToUTF8</code> function</h2>

> Encode text as codepoints array into UTF-8 text string (WARNING: memory must be freed!)

Defined in raylib.h:

```c
char * TextCodepointsToUTF8(int codepoints, int length) 
```

Python wrapper:

```python
def TextCodepointsToUTF8(codepoints: Union[Seq[int], IntPtr], length: int) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextCopy"><code>TextCopy</code> function</h2>

> Copy one string to another, returns bytes copied

Defined in raylib.h:

```c
int TextCopy(char * dst, char * src) 
```

Python wrapper:

```python
def TextCopy(dst: Union[str, CharPtr], src: Union[str, CharPtr]) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextIsEqual"><code>TextIsEqual</code> function</h2>

> Check if two text string are equal

Defined in raylib.h:

```c
bool TextIsEqual(char * text1, char * text2) 
```

Python wrapper:

```python
def TextIsEqual(text1: Union[str, CharPtr], text2: Union[str, CharPtr]) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextLength"><code>TextLength</code> function</h2>

> Get text length, checks for '\0' ending

Defined in raylib.h:

```c
unsigned int TextLength(char * text) 
```

Python wrapper:

```python
def TextLength(text: Union[str, CharPtr]) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextFormat"><code>TextFormat</code> function</h2>

> Text formatting with variables (sprintf() style)

Defined in raylib.h:

```c
char * TextFormat(char * text, va_list args) 
```

Python wrapper:

```python
def TextFormat(text: Union[str, CharPtr], args: bytes) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextSubtext"><code>TextSubtext</code> function</h2>

> Get a piece of a text string

Defined in raylib.h:

```c
char * TextSubtext(char * text, int position, int length) 
```

Python wrapper:

```python
def TextSubtext(text: Union[str, CharPtr], position: int, length: int) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextReplace"><code>TextReplace</code> function</h2>

> Replace text string (WARNING: memory must be freed!)

Defined in raylib.h:

```c
char * TextReplace(char * text, char * replace, char * by) 
```

Python wrapper:

```python
def TextReplace(text: Union[str, CharPtr], replace: Union[str, CharPtr], by: Union[str, CharPtr]) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextInsert"><code>TextInsert</code> function</h2>

> Insert text in a position (WARNING: memory must be freed!)

Defined in raylib.h:

```c
char * TextInsert(char * text, char * insert, int position) 
```

Python wrapper:

```python
def TextInsert(text: Union[str, CharPtr], insert: Union[str, CharPtr], position: int) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextJoin"><code>TextJoin</code> function</h2>

> Join text strings with delimiter

Defined in raylib.h:

```c
char * TextJoin(char ** textList, int count, char * delimiter) 
```

Python wrapper:

```python
def TextJoin(textList: Seq[Union[str, CharPtr]], count: int, delimiter: Union[str, CharPtr]) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextSplit"><code>TextSplit</code> function</h2>

> Split text into multiple strings

Defined in raylib.h:

```c
char ** TextSplit(char * text, char delimiter, int count) 
```

Python wrapper:

```python
def TextSplit(text: Union[str, CharPtr], delimiter: int, count: Union[Seq[int], IntPtr]) -> Seq[Union[str, CharPtr]]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextAppend"><code>TextAppend</code> function</h2>

> Append text at specific position and move cursor!

Defined in raylib.h:

```c
void TextAppend(char * text, char * append, int position) 
```

Python wrapper:

```python
def TextAppend(text: Union[str, CharPtr], append: Union[str, CharPtr], position: Union[Seq[int], IntPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextFindIndex"><code>TextFindIndex</code> function</h2>

> Find first text occurrence within a string

Defined in raylib.h:

```c
int TextFindIndex(char * text, char * find) 
```

Python wrapper:

```python
def TextFindIndex(text: Union[str, CharPtr], find: Union[str, CharPtr]) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextToUpper"><code>TextToUpper</code> function</h2>

> Get upper case version of provided string

Defined in raylib.h:

```c
char * TextToUpper(char * text) 
```

Python wrapper:

```python
def TextToUpper(text: Union[str, CharPtr]) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextToLower"><code>TextToLower</code> function</h2>

> Get lower case version of provided string

Defined in raylib.h:

```c
char * TextToLower(char * text) 
```

Python wrapper:

```python
def TextToLower(text: Union[str, CharPtr]) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextToPascal"><code>TextToPascal</code> function</h2>

> Get Pascal case notation version of provided string

Defined in raylib.h:

```c
char * TextToPascal(char * text) 
```

Python wrapper:

```python
def TextToPascal(text: Union[str, CharPtr]) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextToInteger"><code>TextToInteger</code> function</h2>

> Get integer value from text (negative values not supported)

Defined in raylib.h:

```c
int TextToInteger(char * text) 
```

Python wrapper:

```python
def TextToInteger(text: Union[str, CharPtr]) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawLine3D"><code>DrawLine3D</code> function</h2>

> Draw a line in 3D world space

Defined in raylib.h:

```c
void DrawLine3D(Vector3 startPos, Vector3 endPos, Color color) 
```

Python wrapper:

```python
def DrawLine3D(startPos: Vector3, endPos: Vector3, color: Color) -> None
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawPoint3D"><code>DrawPoint3D</code> function</h2>

> Draw a point in 3D space, actually a small line

Defined in raylib.h:

```c
void DrawPoint3D(Vector3 position, Color color) 
```

Python wrapper:

```python
def DrawPoint3D(position: Vector3, color: Color) -> None
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCircle3D"><code>DrawCircle3D</code> function</h2>

> Draw a circle in 3D world space

Defined in raylib.h:

```c
void DrawCircle3D(Vector3 center, float radius, Vector3 rotationAxis, float rotationAngle, Color color) 
```

Python wrapper:

```python
def DrawCircle3D(center: Vector3, radius: float, rotationAxis: Vector3, rotationAngle: float, color: Color) -> None
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTriangle3D"><code>DrawTriangle3D</code> function</h2>

> Draw a color-filled triangle (vertex in counter-clockwise order!)

Defined in raylib.h:

```c
void DrawTriangle3D(Vector3 v1, Vector3 v2, Vector3 v3, Color color) 
```

Python wrapper:

```python
def DrawTriangle3D(v1: Vector3, v2: Vector3, v3: Vector3, color: Color) -> None
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawTriangleStrip3D"><code>DrawTriangleStrip3D</code> function</h2>

> Draw a triangle strip defined by points

Defined in raylib.h:

```c
void DrawTriangleStrip3D(Vector3 * points, int pointCount, Color color) 
```

Python wrapper:

```python
def DrawTriangleStrip3D(points: Vector3Ptr, pointCount: int, color: Color) -> None
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCube"><code>DrawCube</code> function</h2>

> Draw cube

Defined in raylib.h:

```c
void DrawCube(Vector3 position, float width, float height, float length, Color color) 
```

Python wrapper:

```python
def DrawCube(position: Vector3, width: float, height: float, length: float, color: Color) -> None
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCubeV"><code>DrawCubeV</code> function</h2>

> Draw cube (Vector version)

Defined in raylib.h:

```c
void DrawCubeV(Vector3 position, Vector3 size, Color color) 
```

Python wrapper:

```python
def DrawCubeV(position: Vector3, size: Vector3, color: Color) -> None
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCubeWires"><code>DrawCubeWires</code> function</h2>

> Draw cube wires

Defined in raylib.h:

```c
void DrawCubeWires(Vector3 position, float width, float height, float length, Color color) 
```

Python wrapper:

```python
def DrawCubeWires(position: Vector3, width: float, height: float, length: float, color: Color) -> None
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCubeWiresV"><code>DrawCubeWiresV</code> function</h2>

> Draw cube wires (Vector version)

Defined in raylib.h:

```c
void DrawCubeWiresV(Vector3 position, Vector3 size, Color color) 
```

Python wrapper:

```python
def DrawCubeWiresV(position: Vector3, size: Vector3, color: Color) -> None
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCubeTexture"><code>DrawCubeTexture</code> function</h2>

> Draw cube textured

Defined in raylib.h:

```c
void DrawCubeTexture(Texture2D texture, Vector3 position, float width, float height, float length, Color color) 
```

Python wrapper:

```python
def DrawCubeTexture(texture: Texture2D, position: Vector3, width: float, height: float, length: float, color: Color) -> None
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCubeTextureRec"><code>DrawCubeTextureRec</code> function</h2>

> Draw cube with a region of a texture

Defined in raylib.h:

```c
void DrawCubeTextureRec(Texture2D texture, Rectangle source, Vector3 position, float width, float height, float length, Color color) 
```

Python wrapper:

```python
def DrawCubeTextureRec(texture: Texture2D, source: Rectangle, position: Vector3, width: float, height: float, length: float, color: Color) -> None
```

See also:
<a href="#Rectangle">Rectangle</a>, <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawSphere"><code>DrawSphere</code> function</h2>

> Draw sphere

Defined in raylib.h:

```c
void DrawSphere(Vector3 centerPos, float radius, Color color) 
```

Python wrapper:

```python
def DrawSphere(centerPos: Vector3, radius: float, color: Color) -> None
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawSphereEx"><code>DrawSphereEx</code> function</h2>

> Draw sphere with extended parameters

Defined in raylib.h:

```c
void DrawSphereEx(Vector3 centerPos, float radius, int rings, int slices, Color color) 
```

Python wrapper:

```python
def DrawSphereEx(centerPos: Vector3, radius: float, rings: int, slices: int, color: Color) -> None
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawSphereWires"><code>DrawSphereWires</code> function</h2>

> Draw sphere wires

Defined in raylib.h:

```c
void DrawSphereWires(Vector3 centerPos, float radius, int rings, int slices, Color color) 
```

Python wrapper:

```python
def DrawSphereWires(centerPos: Vector3, radius: float, rings: int, slices: int, color: Color) -> None
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCylinder"><code>DrawCylinder</code> function</h2>

> Draw a cylinder/cone

Defined in raylib.h:

```c
void DrawCylinder(Vector3 position, float radiusTop, float radiusBottom, float height, int slices, Color color) 
```

Python wrapper:

```python
def DrawCylinder(position: Vector3, radiusTop: float, radiusBottom: float, height: float, slices: int, color: Color) -> None
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCylinderEx"><code>DrawCylinderEx</code> function</h2>

> Draw a cylinder with base at startPos and top at endPos

Defined in raylib.h:

```c
void DrawCylinderEx(Vector3 startPos, Vector3 endPos, float startRadius, float endRadius, int sides, Color color) 
```

Python wrapper:

```python
def DrawCylinderEx(startPos: Vector3, endPos: Vector3, startRadius: float, endRadius: float, sides: int, color: Color) -> None
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCylinderWires"><code>DrawCylinderWires</code> function</h2>

> Draw a cylinder/cone wires

Defined in raylib.h:

```c
void DrawCylinderWires(Vector3 position, float radiusTop, float radiusBottom, float height, int slices, Color color) 
```

Python wrapper:

```python
def DrawCylinderWires(position: Vector3, radiusTop: float, radiusBottom: float, height: float, slices: int, color: Color) -> None
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawCylinderWiresEx"><code>DrawCylinderWiresEx</code> function</h2>

> Draw a cylinder wires with base at startPos and top at endPos

Defined in raylib.h:

```c
void DrawCylinderWiresEx(Vector3 startPos, Vector3 endPos, float startRadius, float endRadius, int sides, Color color) 
```

Python wrapper:

```python
def DrawCylinderWiresEx(startPos: Vector3, endPos: Vector3, startRadius: float, endRadius: float, sides: int, color: Color) -> None
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawPlane"><code>DrawPlane</code> function</h2>

> Draw a plane XZ

Defined in raylib.h:

```c
void DrawPlane(Vector3 centerPos, Vector2 size, Color color) 
```

Python wrapper:

```python
def DrawPlane(centerPos: Vector3, size: Vector2, color: Color) -> None
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawRay"><code>DrawRay</code> function</h2>

> Draw a ray line

Defined in raylib.h:

```c
void DrawRay(Ray ray, Color color) 
```

Python wrapper:

```python
def DrawRay(ray: Ray, color: Color) -> None
```

See also:
<a href="#Ray">Ray</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawGrid"><code>DrawGrid</code> function</h2>

> Draw a grid (centered at (0, 0, 0))

Defined in raylib.h:

```c
void DrawGrid(int slices, float spacing) 
```

Python wrapper:

```python
def DrawGrid(slices: int, spacing: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadModel"><code>LoadModel</code> function</h2>

> Load model from files (meshes and materials)

Defined in raylib.h:

```c
Model LoadModel(char * fileName) 
```

Python wrapper:

```python
def LoadModel(fileName: Union[str, CharPtr]) -> Model
```

See also:
<a href="#Model">Model</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadModelFromMesh"><code>LoadModelFromMesh</code> function</h2>

> Load model from generated mesh (default material)

Defined in raylib.h:

```c
Model LoadModelFromMesh(Mesh mesh) 
```

Python wrapper:

```python
def LoadModelFromMesh(mesh: Mesh) -> Model
```

See also:
<a href="#Mesh">Mesh</a>, <a href="#Model">Model</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadModel"><code>UnloadModel</code> function</h2>

> Unload model (including meshes) from memory (RAM and/or VRAM)

Defined in raylib.h:

```c
void UnloadModel(Model model) 
```

Python wrapper:

```python
def UnloadModel(model: Model) -> None
```

See also:
<a href="#Model">Model</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadModelKeepMeshes"><code>UnloadModelKeepMeshes</code> function</h2>

> Unload model (but not meshes) from memory (RAM and/or VRAM)

Defined in raylib.h:

```c
void UnloadModelKeepMeshes(Model model) 
```

Python wrapper:

```python
def UnloadModelKeepMeshes(model: Model) -> None
```

See also:
<a href="#Model">Model</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetModelBoundingBox"><code>GetModelBoundingBox</code> function</h2>

> Compute model bounding box limits (considers all meshes)

Defined in raylib.h:

```c
BoundingBox GetModelBoundingBox(Model model) 
```

Python wrapper:

```python
def GetModelBoundingBox(model: Model) -> BoundingBox
```

See also:
<a href="#Model">Model</a>, <a href="#BoundingBox">BoundingBox</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawModel"><code>DrawModel</code> function</h2>

> Draw a model (with texture if set)

Defined in raylib.h:

```c
void DrawModel(Model model, Vector3 position, float scale, Color tint) 
```

Python wrapper:

```python
def DrawModel(model: Model, position: Vector3, scale: float, tint: Color) -> None
```

See also:
<a href="#Model">Model</a>, <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawModelEx"><code>DrawModelEx</code> function</h2>

> Draw a model with extended parameters

Defined in raylib.h:

```c
void DrawModelEx(Model model, Vector3 position, Vector3 rotationAxis, float rotationAngle, Vector3 scale, Color tint) 
```

Python wrapper:

```python
def DrawModelEx(model: Model, position: Vector3, rotationAxis: Vector3, rotationAngle: float, scale: Vector3, tint: Color) -> None
```

See also:
<a href="#Model">Model</a>, <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawModelWires"><code>DrawModelWires</code> function</h2>

> Draw a model wires (with texture if set)

Defined in raylib.h:

```c
void DrawModelWires(Model model, Vector3 position, float scale, Color tint) 
```

Python wrapper:

```python
def DrawModelWires(model: Model, position: Vector3, scale: float, tint: Color) -> None
```

See also:
<a href="#Model">Model</a>, <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawModelWiresEx"><code>DrawModelWiresEx</code> function</h2>

> Draw a model wires (with texture if set) with extended parameters

Defined in raylib.h:

```c
void DrawModelWiresEx(Model model, Vector3 position, Vector3 rotationAxis, float rotationAngle, Vector3 scale, Color tint) 
```

Python wrapper:

```python
def DrawModelWiresEx(model: Model, position: Vector3, rotationAxis: Vector3, rotationAngle: float, scale: Vector3, tint: Color) -> None
```

See also:
<a href="#Model">Model</a>, <a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawBoundingBox"><code>DrawBoundingBox</code> function</h2>

> Draw bounding box (wires)

Defined in raylib.h:

```c
void DrawBoundingBox(BoundingBox box, Color color) 
```

Python wrapper:

```python
def DrawBoundingBox(box: BoundingBox, color: Color) -> None
```

See also:
<a href="#BoundingBox">BoundingBox</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawBillboard"><code>DrawBillboard</code> function</h2>

> Draw a billboard texture

Defined in raylib.h:

```c
void DrawBillboard(Camera camera, Texture2D texture, Vector3 position, float size, Color tint) 
```

Python wrapper:

```python
def DrawBillboard(camera: Camera, texture: Texture2D, position: Vector3, size: float, tint: Color) -> None
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawBillboardRec"><code>DrawBillboardRec</code> function</h2>

> Draw a billboard texture defined by source

Defined in raylib.h:

```c
void DrawBillboardRec(Camera camera, Texture2D texture, Rectangle source, Vector3 position, Vector2 size, Color tint) 
```

Python wrapper:

```python
def DrawBillboardRec(camera: Camera, texture: Texture2D, source: Rectangle, position: Vector3, size: Vector2, tint: Color) -> None
```

See also:
<a href="#Rectangle">Rectangle</a>, <a href="#Vector3">Vector3</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawBillboardPro"><code>DrawBillboardPro</code> function</h2>

> Draw a billboard texture defined by source and rotation

Defined in raylib.h:

```c
void DrawBillboardPro(Camera camera, Texture2D texture, Rectangle source, Vector3 position, Vector3 up, Vector2 size, Vector2 origin, float rotation, Color tint) 
```

Python wrapper:

```python
def DrawBillboardPro(camera: Camera, texture: Texture2D, source: Rectangle, position: Vector3, up: Vector3, size: Vector2, origin: Vector2, rotation: float, tint: Color) -> None
```

See also:
<a href="#Rectangle">Rectangle</a>, <a href="#Vector3">Vector3</a>, <a href="#Vector2">Vector2</a>, <a href="#Color">Color</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UploadMesh"><code>UploadMesh</code> function</h2>

> Upload mesh vertex data in GPU and provide VAO/VBO ids

Defined in raylib.h:

```c
void UploadMesh(Mesh * mesh, bool dynamic) 
```

Python wrapper:

```python
def UploadMesh(mesh: MeshPtr, dynamic: bool) -> None
```

See also:
<a href="#Mesh">Mesh</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UpdateMeshBuffer"><code>UpdateMeshBuffer</code> function</h2>

> Update mesh vertex data in GPU for a specific buffer index

Defined in raylib.h:

```c
void UpdateMeshBuffer(Mesh mesh, int index, void data, int dataSize, int offset) 
```

Python wrapper:

```python
def UpdateMeshBuffer(mesh: Mesh, index: int, data: bytes, dataSize: int, offset: int) -> None
```

See also:
<a href="#Mesh">Mesh</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadMesh"><code>UnloadMesh</code> function</h2>

> Unload mesh data from CPU and GPU

Defined in raylib.h:

```c
void UnloadMesh(Mesh mesh) 
```

Python wrapper:

```python
def UnloadMesh(mesh: Mesh) -> None
```

See also:
<a href="#Mesh">Mesh</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawMesh"><code>DrawMesh</code> function</h2>

> Draw a 3d mesh with material and transform

Defined in raylib.h:

```c
void DrawMesh(Mesh mesh, Material material, Matrix transform) 
```

Python wrapper:

```python
def DrawMesh(mesh: Mesh, material: Material, transform: Matrix) -> None
```

See also:
<a href="#Mesh">Mesh</a>, <a href="#Material">Material</a>, <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DrawMeshInstanced"><code>DrawMeshInstanced</code> function</h2>

> Draw multiple mesh instances with material and different transforms

Defined in raylib.h:

```c
void DrawMeshInstanced(Mesh mesh, Material material, Matrix * transforms, int instances) 
```

Python wrapper:

```python
def DrawMeshInstanced(mesh: Mesh, material: Material, transforms: MatrixPtr, instances: int) -> None
```

See also:
<a href="#Mesh">Mesh</a>, <a href="#Material">Material</a>, <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ExportMesh"><code>ExportMesh</code> function</h2>

> Export mesh data to file, returns true on success

Defined in raylib.h:

```c
bool ExportMesh(Mesh mesh, char * fileName) 
```

Python wrapper:

```python
def ExportMesh(mesh: Mesh, fileName: Union[str, CharPtr]) -> bool
```

See also:
<a href="#Mesh">Mesh</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMeshBoundingBox"><code>GetMeshBoundingBox</code> function</h2>

> Compute mesh bounding box limits

Defined in raylib.h:

```c
BoundingBox GetMeshBoundingBox(Mesh mesh) 
```

Python wrapper:

```python
def GetMeshBoundingBox(mesh: Mesh) -> BoundingBox
```

See also:
<a href="#Mesh">Mesh</a>, <a href="#BoundingBox">BoundingBox</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenMeshTangents"><code>GenMeshTangents</code> function</h2>

> Compute mesh tangents

Defined in raylib.h:

```c
void GenMeshTangents(Mesh * mesh) 
```

Python wrapper:

```python
def GenMeshTangents(mesh: MeshPtr) -> None
```

See also:
<a href="#Mesh">Mesh</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenMeshPoly"><code>GenMeshPoly</code> function</h2>

> Generate polygonal mesh

Defined in raylib.h:

```c
Mesh GenMeshPoly(int sides, float radius) 
```

Python wrapper:

```python
def GenMeshPoly(sides: int, radius: float) -> Mesh
```

See also:
<a href="#Mesh">Mesh</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenMeshPlane"><code>GenMeshPlane</code> function</h2>

> Generate plane mesh (with subdivisions)

Defined in raylib.h:

```c
Mesh GenMeshPlane(float width, float length, int resX, int resZ) 
```

Python wrapper:

```python
def GenMeshPlane(width: float, length: float, resX: int, resZ: int) -> Mesh
```

See also:
<a href="#Mesh">Mesh</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenMeshCube"><code>GenMeshCube</code> function</h2>

> Generate cuboid mesh

Defined in raylib.h:

```c
Mesh GenMeshCube(float width, float height, float length) 
```

Python wrapper:

```python
def GenMeshCube(width: float, height: float, length: float) -> Mesh
```

See also:
<a href="#Mesh">Mesh</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenMeshSphere"><code>GenMeshSphere</code> function</h2>

> Generate sphere mesh (standard sphere)

Defined in raylib.h:

```c
Mesh GenMeshSphere(float radius, int rings, int slices) 
```

Python wrapper:

```python
def GenMeshSphere(radius: float, rings: int, slices: int) -> Mesh
```

See also:
<a href="#Mesh">Mesh</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenMeshHemiSphere"><code>GenMeshHemiSphere</code> function</h2>

> Generate half-sphere mesh (no bottom cap)

Defined in raylib.h:

```c
Mesh GenMeshHemiSphere(float radius, int rings, int slices) 
```

Python wrapper:

```python
def GenMeshHemiSphere(radius: float, rings: int, slices: int) -> Mesh
```

See also:
<a href="#Mesh">Mesh</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenMeshCylinder"><code>GenMeshCylinder</code> function</h2>

> Generate cylinder mesh

Defined in raylib.h:

```c
Mesh GenMeshCylinder(float radius, float height, int slices) 
```

Python wrapper:

```python
def GenMeshCylinder(radius: float, height: float, slices: int) -> Mesh
```

See also:
<a href="#Mesh">Mesh</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenMeshCone"><code>GenMeshCone</code> function</h2>

> Generate cone/pyramid mesh

Defined in raylib.h:

```c
Mesh GenMeshCone(float radius, float height, int slices) 
```

Python wrapper:

```python
def GenMeshCone(radius: float, height: float, slices: int) -> Mesh
```

See also:
<a href="#Mesh">Mesh</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenMeshTorus"><code>GenMeshTorus</code> function</h2>

> Generate torus mesh

Defined in raylib.h:

```c
Mesh GenMeshTorus(float radius, float size, int radSeg, int sides) 
```

Python wrapper:

```python
def GenMeshTorus(radius: float, size: float, radSeg: int, sides: int) -> Mesh
```

See also:
<a href="#Mesh">Mesh</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenMeshKnot"><code>GenMeshKnot</code> function</h2>

> Generate trefoil knot mesh

Defined in raylib.h:

```c
Mesh GenMeshKnot(float radius, float size, int radSeg, int sides) 
```

Python wrapper:

```python
def GenMeshKnot(radius: float, size: float, radSeg: int, sides: int) -> Mesh
```

See also:
<a href="#Mesh">Mesh</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenMeshHeightmap"><code>GenMeshHeightmap</code> function</h2>

> Generate heightmap mesh from image data

Defined in raylib.h:

```c
Mesh GenMeshHeightmap(Image heightmap, Vector3 size) 
```

Python wrapper:

```python
def GenMeshHeightmap(heightmap: Image, size: Vector3) -> Mesh
```

See also:
<a href="#Image">Image</a>, <a href="#Vector3">Vector3</a>, <a href="#Mesh">Mesh</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GenMeshCubicmap"><code>GenMeshCubicmap</code> function</h2>

> Generate cubes-based map mesh from image data

Defined in raylib.h:

```c
Mesh GenMeshCubicmap(Image cubicmap, Vector3 cubeSize) 
```

Python wrapper:

```python
def GenMeshCubicmap(cubicmap: Image, cubeSize: Vector3) -> Mesh
```

See also:
<a href="#Image">Image</a>, <a href="#Vector3">Vector3</a>, <a href="#Mesh">Mesh</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadMaterials"><code>LoadMaterials</code> function</h2>

> Load materials from model file

Defined in raylib.h:

```c
Material * LoadMaterials(char * fileName, int materialCount) 
```

Python wrapper:

```python
def LoadMaterials(fileName: Union[str, CharPtr], materialCount: Union[Seq[int], IntPtr]) -> MaterialPtr
```

See also:
<a href="#Material">Material</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadMaterialDefault"><code>LoadMaterialDefault</code> function</h2>

> Load default material (Supports: DIFFUSE, SPECULAR, NORMAL maps)

Defined in raylib.h:

```c
Material LoadMaterialDefault() 
```

Python wrapper:

```python
def LoadMaterialDefault() -> Material
```

See also:
<a href="#Material">Material</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadMaterial"><code>UnloadMaterial</code> function</h2>

> Unload material from GPU memory (VRAM)

Defined in raylib.h:

```c
void UnloadMaterial(Material material) 
```

Python wrapper:

```python
def UnloadMaterial(material: Material) -> None
```

See also:
<a href="#Material">Material</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetMaterialTexture"><code>SetMaterialTexture</code> function</h2>

> Set texture for a material map type (MATERIAL_MAP_DIFFUSE, MATERIAL_MAP_SPECULAR...)

Defined in raylib.h:

```c
void SetMaterialTexture(Material * material, int mapType, Texture2D texture) 
```

Python wrapper:

```python
def SetMaterialTexture(material: MaterialPtr, mapType: int, texture: Texture2D) -> None
```

See also:
<a href="#Material">Material</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetModelMeshMaterial"><code>SetModelMeshMaterial</code> function</h2>

> Set material for a mesh

Defined in raylib.h:

```c
void SetModelMeshMaterial(Model * model, int meshId, int materialId) 
```

Python wrapper:

```python
def SetModelMeshMaterial(model: ModelPtr, meshId: int, materialId: int) -> None
```

See also:
<a href="#Model">Model</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadModelAnimations"><code>LoadModelAnimations</code> function</h2>

> Load model animations from file

Defined in raylib.h:

```c
ModelAnimation * LoadModelAnimations(char * fileName, unsigned int animCount) 
```

Python wrapper:

```python
def LoadModelAnimations(fileName: Union[str, CharPtr], animCount: Union[Seq[int], UIntPtr]) -> ModelAnimationPtr
```

See also:
<a href="#ModelAnimation">ModelAnimation</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UpdateModelAnimation"><code>UpdateModelAnimation</code> function</h2>

> Update model animation pose

Defined in raylib.h:

```c
void UpdateModelAnimation(Model model, ModelAnimation anim, int frame) 
```

Python wrapper:

```python
def UpdateModelAnimation(model: Model, anim: ModelAnimation, frame: int) -> None
```

See also:
<a href="#Model">Model</a>, <a href="#ModelAnimation">ModelAnimation</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadModelAnimation"><code>UnloadModelAnimation</code> function</h2>

> Unload animation data

Defined in raylib.h:

```c
void UnloadModelAnimation(ModelAnimation anim) 
```

Python wrapper:

```python
def UnloadModelAnimation(anim: ModelAnimation) -> None
```

See also:
<a href="#ModelAnimation">ModelAnimation</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadModelAnimations"><code>UnloadModelAnimations</code> function</h2>

> Unload animation array data

Defined in raylib.h:

```c
void UnloadModelAnimations(ModelAnimation * animations, unsigned int count) 
```

Python wrapper:

```python
def UnloadModelAnimations(animations: ModelAnimationPtr, count: int) -> None
```

See also:
<a href="#ModelAnimation">ModelAnimation</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsModelAnimationValid"><code>IsModelAnimationValid</code> function</h2>

> Check model animation skeleton match

Defined in raylib.h:

```c
bool IsModelAnimationValid(Model model, ModelAnimation anim) 
```

Python wrapper:

```python
def IsModelAnimationValid(model: Model, anim: ModelAnimation) -> bool
```

See also:
<a href="#Model">Model</a>, <a href="#ModelAnimation">ModelAnimation</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CheckCollisionSpheres"><code>CheckCollisionSpheres</code> function</h2>

> Check collision between two spheres

Defined in raylib.h:

```c
bool CheckCollisionSpheres(Vector3 center1, float radius1, Vector3 center2, float radius2) 
```

Python wrapper:

```python
def CheckCollisionSpheres(center1: Vector3, radius1: float, center2: Vector3, radius2: float) -> bool
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CheckCollisionBoxes"><code>CheckCollisionBoxes</code> function</h2>

> Check collision between two bounding boxes

Defined in raylib.h:

```c
bool CheckCollisionBoxes(BoundingBox box1, BoundingBox box2) 
```

Python wrapper:

```python
def CheckCollisionBoxes(box1: BoundingBox, box2: BoundingBox) -> bool
```

See also:
<a href="#BoundingBox">BoundingBox</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CheckCollisionBoxSphere"><code>CheckCollisionBoxSphere</code> function</h2>

> Check collision between box and sphere

Defined in raylib.h:

```c
bool CheckCollisionBoxSphere(BoundingBox box, Vector3 center, float radius) 
```

Python wrapper:

```python
def CheckCollisionBoxSphere(box: BoundingBox, center: Vector3, radius: float) -> bool
```

See also:
<a href="#BoundingBox">BoundingBox</a>, <a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetRayCollisionSphere"><code>GetRayCollisionSphere</code> function</h2>

> Get collision info between ray and sphere

Defined in raylib.h:

```c
RayCollision GetRayCollisionSphere(Ray ray, Vector3 center, float radius) 
```

Python wrapper:

```python
def GetRayCollisionSphere(ray: Ray, center: Vector3, radius: float) -> RayCollision
```

See also:
<a href="#Ray">Ray</a>, <a href="#Vector3">Vector3</a>, <a href="#RayCollision">RayCollision</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetRayCollisionBox"><code>GetRayCollisionBox</code> function</h2>

> Get collision info between ray and box

Defined in raylib.h:

```c
RayCollision GetRayCollisionBox(Ray ray, BoundingBox box) 
```

Python wrapper:

```python
def GetRayCollisionBox(ray: Ray, box: BoundingBox) -> RayCollision
```

See also:
<a href="#Ray">Ray</a>, <a href="#BoundingBox">BoundingBox</a>, <a href="#RayCollision">RayCollision</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetRayCollisionMesh"><code>GetRayCollisionMesh</code> function</h2>

> Get collision info between ray and mesh

Defined in raylib.h:

```c
RayCollision GetRayCollisionMesh(Ray ray, Mesh mesh, Matrix transform) 
```

Python wrapper:

```python
def GetRayCollisionMesh(ray: Ray, mesh: Mesh, transform: Matrix) -> RayCollision
```

See also:
<a href="#Ray">Ray</a>, <a href="#Mesh">Mesh</a>, <a href="#Matrix">Matrix</a>, <a href="#RayCollision">RayCollision</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetRayCollisionTriangle"><code>GetRayCollisionTriangle</code> function</h2>

> Get collision info between ray and triangle

Defined in raylib.h:

```c
RayCollision GetRayCollisionTriangle(Ray ray, Vector3 p1, Vector3 p2, Vector3 p3) 
```

Python wrapper:

```python
def GetRayCollisionTriangle(ray: Ray, p1: Vector3, p2: Vector3, p3: Vector3) -> RayCollision
```

See also:
<a href="#Ray">Ray</a>, <a href="#Vector3">Vector3</a>, <a href="#RayCollision">RayCollision</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetRayCollisionQuad"><code>GetRayCollisionQuad</code> function</h2>

> Get collision info between ray and quad

Defined in raylib.h:

```c
RayCollision GetRayCollisionQuad(Ray ray, Vector3 p1, Vector3 p2, Vector3 p3, Vector3 p4) 
```

Python wrapper:

```python
def GetRayCollisionQuad(ray: Ray, p1: Vector3, p2: Vector3, p3: Vector3, p4: Vector3) -> RayCollision
```

See also:
<a href="#Ray">Ray</a>, <a href="#Vector3">Vector3</a>, <a href="#RayCollision">RayCollision</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="InitAudioDevice"><code>InitAudioDevice</code> function</h2>

> Initialize audio device and context

Defined in raylib.h:

```c
void InitAudioDevice() 
```

Python wrapper:

```python
def InitAudioDevice() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="CloseAudioDevice"><code>CloseAudioDevice</code> function</h2>

> Close the audio device and context

Defined in raylib.h:

```c
void CloseAudioDevice() 
```

Python wrapper:

```python
def CloseAudioDevice() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsAudioDeviceReady"><code>IsAudioDeviceReady</code> function</h2>

> Check if audio device has been initialized successfully

Defined in raylib.h:

```c
bool IsAudioDeviceReady() 
```

Python wrapper:

```python
def IsAudioDeviceReady() -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetMasterVolume"><code>SetMasterVolume</code> function</h2>

> Set master volume (listener)

Defined in raylib.h:

```c
void SetMasterVolume(float volume) 
```

Python wrapper:

```python
def SetMasterVolume(volume: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadWave"><code>LoadWave</code> function</h2>

> Load wave data from file

Defined in raylib.h:

```c
Wave LoadWave(char * fileName) 
```

Python wrapper:

```python
def LoadWave(fileName: Union[str, CharPtr]) -> Wave
```

See also:
<a href="#Wave">Wave</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadWaveFromMemory"><code>LoadWaveFromMemory</code> function</h2>

> Load wave from memory buffer, fileType refers to extension: i.e. '.wav'

Defined in raylib.h:

```c
Wave LoadWaveFromMemory(char * fileType, unsigned char * fileData, int dataSize) 
```

Python wrapper:

```python
def LoadWaveFromMemory(fileType: Union[str, CharPtr], fileData: Union[Seq[int], UCharPtr], dataSize: int) -> Wave
```

See also:
<a href="#Wave">Wave</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadSound"><code>LoadSound</code> function</h2>

> Load sound from file

Defined in raylib.h:

```c
Sound LoadSound(char * fileName) 
```

Python wrapper:

```python
def LoadSound(fileName: Union[str, CharPtr]) -> Sound
```

See also:
<a href="#Sound">Sound</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadSoundFromWave"><code>LoadSoundFromWave</code> function</h2>

> Load sound from wave data

Defined in raylib.h:

```c
Sound LoadSoundFromWave(Wave wave) 
```

Python wrapper:

```python
def LoadSoundFromWave(wave: Wave) -> Sound
```

See also:
<a href="#Wave">Wave</a>, <a href="#Sound">Sound</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UpdateSound"><code>UpdateSound</code> function</h2>

> Update sound buffer with new data

Defined in raylib.h:

```c
void UpdateSound(Sound sound, void data, int sampleCount) 
```

Python wrapper:

```python
def UpdateSound(sound: Sound, data: bytes, sampleCount: int) -> None
```

See also:
<a href="#Sound">Sound</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadWave"><code>UnloadWave</code> function</h2>

> Unload wave data

Defined in raylib.h:

```c
void UnloadWave(Wave wave) 
```

Python wrapper:

```python
def UnloadWave(wave: Wave) -> None
```

See also:
<a href="#Wave">Wave</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadSound"><code>UnloadSound</code> function</h2>

> Unload sound

Defined in raylib.h:

```c
void UnloadSound(Sound sound) 
```

Python wrapper:

```python
def UnloadSound(sound: Sound) -> None
```

See also:
<a href="#Sound">Sound</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ExportWave"><code>ExportWave</code> function</h2>

> Export wave data to file, returns true on success

Defined in raylib.h:

```c
bool ExportWave(Wave wave, char * fileName) 
```

Python wrapper:

```python
def ExportWave(wave: Wave, fileName: Union[str, CharPtr]) -> bool
```

See also:
<a href="#Wave">Wave</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ExportWaveAsCode"><code>ExportWaveAsCode</code> function</h2>

> Export wave sample data to code (.h), returns true on success

Defined in raylib.h:

```c
bool ExportWaveAsCode(Wave wave, char * fileName) 
```

Python wrapper:

```python
def ExportWaveAsCode(wave: Wave, fileName: Union[str, CharPtr]) -> bool
```

See also:
<a href="#Wave">Wave</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="PlaySound"><code>PlaySound</code> function</h2>

> Play a sound

Defined in raylib.h:

```c
void PlaySound(Sound sound) 
```

Python wrapper:

```python
def PlaySound(sound: Sound) -> None
```

See also:
<a href="#Sound">Sound</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="StopSound"><code>StopSound</code> function</h2>

> Stop playing a sound

Defined in raylib.h:

```c
void StopSound(Sound sound) 
```

Python wrapper:

```python
def StopSound(sound: Sound) -> None
```

See also:
<a href="#Sound">Sound</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="PauseSound"><code>PauseSound</code> function</h2>

> Pause a sound

Defined in raylib.h:

```c
void PauseSound(Sound sound) 
```

Python wrapper:

```python
def PauseSound(sound: Sound) -> None
```

See also:
<a href="#Sound">Sound</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ResumeSound"><code>ResumeSound</code> function</h2>

> Resume a paused sound

Defined in raylib.h:

```c
void ResumeSound(Sound sound) 
```

Python wrapper:

```python
def ResumeSound(sound: Sound) -> None
```

See also:
<a href="#Sound">Sound</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="PlaySoundMulti"><code>PlaySoundMulti</code> function</h2>

> Play a sound (using multichannel buffer pool)

Defined in raylib.h:

```c
void PlaySoundMulti(Sound sound) 
```

Python wrapper:

```python
def PlaySoundMulti(sound: Sound) -> None
```

See also:
<a href="#Sound">Sound</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="StopSoundMulti"><code>StopSoundMulti</code> function</h2>

> Stop any sound playing (using multichannel buffer pool)

Defined in raylib.h:

```c
void StopSoundMulti() 
```

Python wrapper:

```python
def StopSoundMulti() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetSoundsPlaying"><code>GetSoundsPlaying</code> function</h2>

> Get number of sounds playing in the multichannel

Defined in raylib.h:

```c
int GetSoundsPlaying() 
```

Python wrapper:

```python
def GetSoundsPlaying() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsSoundPlaying"><code>IsSoundPlaying</code> function</h2>

> Check if a sound is currently playing

Defined in raylib.h:

```c
bool IsSoundPlaying(Sound sound) 
```

Python wrapper:

```python
def IsSoundPlaying(sound: Sound) -> bool
```

See also:
<a href="#Sound">Sound</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetSoundVolume"><code>SetSoundVolume</code> function</h2>

> Set volume for a sound (1.0 is max level)

Defined in raylib.h:

```c
void SetSoundVolume(Sound sound, float volume) 
```

Python wrapper:

```python
def SetSoundVolume(sound: Sound, volume: float) -> None
```

See also:
<a href="#Sound">Sound</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetSoundPitch"><code>SetSoundPitch</code> function</h2>

> Set pitch for a sound (1.0 is base level)

Defined in raylib.h:

```c
void SetSoundPitch(Sound sound, float pitch) 
```

Python wrapper:

```python
def SetSoundPitch(sound: Sound, pitch: float) -> None
```

See also:
<a href="#Sound">Sound</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetSoundPan"><code>SetSoundPan</code> function</h2>

> Set pan for a sound (0.5 is center)

Defined in raylib.h:

```c
void SetSoundPan(Sound sound, float pan) 
```

Python wrapper:

```python
def SetSoundPan(sound: Sound, pan: float) -> None
```

See also:
<a href="#Sound">Sound</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="WaveCopy"><code>WaveCopy</code> function</h2>

> Copy a wave to a new wave

Defined in raylib.h:

```c
Wave WaveCopy(Wave wave) 
```

Python wrapper:

```python
def WaveCopy(wave: Wave) -> Wave
```

See also:
<a href="#Wave">Wave</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="WaveCrop"><code>WaveCrop</code> function</h2>

> Crop a wave to defined samples range

Defined in raylib.h:

```c
void WaveCrop(Wave * wave, int initSample, int finalSample) 
```

Python wrapper:

```python
def WaveCrop(wave: WavePtr, initSample: int, finalSample: int) -> None
```

See also:
<a href="#Wave">Wave</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="WaveFormat"><code>WaveFormat</code> function</h2>

> Convert wave data to desired format

Defined in raylib.h:

```c
void WaveFormat(Wave * wave, int sampleRate, int sampleSize, int channels) 
```

Python wrapper:

```python
def WaveFormat(wave: WavePtr, sampleRate: int, sampleSize: int, channels: int) -> None
```

See also:
<a href="#Wave">Wave</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadWaveSamples"><code>LoadWaveSamples</code> function</h2>

> Load samples data from wave as a 32bit float data array

Defined in raylib.h:

```c
float LoadWaveSamples(Wave wave) 
```

Python wrapper:

```python
def LoadWaveSamples(wave: Wave) -> Union[Seq[float], FloatPtr]
```

See also:
<a href="#Wave">Wave</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadWaveSamples"><code>UnloadWaveSamples</code> function</h2>

> Unload samples data loaded with LoadWaveSamples()

Defined in raylib.h:

```c
void UnloadWaveSamples(float samples) 
```

Python wrapper:

```python
def UnloadWaveSamples(samples: Union[Seq[float], FloatPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadMusicStream"><code>LoadMusicStream</code> function</h2>

> Load music stream from file

Defined in raylib.h:

```c
Music LoadMusicStream(char * fileName) 
```

Python wrapper:

```python
def LoadMusicStream(fileName: Union[str, CharPtr]) -> Music
```

See also:
<a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadMusicStreamFromMemory"><code>LoadMusicStreamFromMemory</code> function</h2>

> Load music stream from data

Defined in raylib.h:

```c
Music LoadMusicStreamFromMemory(char * fileType, unsigned char * data, int dataSize) 
```

Python wrapper:

```python
def LoadMusicStreamFromMemory(fileType: Union[str, CharPtr], data: Union[Seq[int], UCharPtr], dataSize: int) -> Music
```

See also:
<a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadMusicStream"><code>UnloadMusicStream</code> function</h2>

> Unload music stream

Defined in raylib.h:

```c
void UnloadMusicStream(Music music) 
```

Python wrapper:

```python
def UnloadMusicStream(music: Music) -> None
```

See also:
<a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="PlayMusicStream"><code>PlayMusicStream</code> function</h2>

> Start music playing

Defined in raylib.h:

```c
void PlayMusicStream(Music music) 
```

Python wrapper:

```python
def PlayMusicStream(music: Music) -> None
```

See also:
<a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsMusicStreamPlaying"><code>IsMusicStreamPlaying</code> function</h2>

> Check if music is playing

Defined in raylib.h:

```c
bool IsMusicStreamPlaying(Music music) 
```

Python wrapper:

```python
def IsMusicStreamPlaying(music: Music) -> bool
```

See also:
<a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UpdateMusicStream"><code>UpdateMusicStream</code> function</h2>

> Updates buffers for music streaming

Defined in raylib.h:

```c
void UpdateMusicStream(Music music) 
```

Python wrapper:

```python
def UpdateMusicStream(music: Music) -> None
```

See also:
<a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="StopMusicStream"><code>StopMusicStream</code> function</h2>

> Stop music playing

Defined in raylib.h:

```c
void StopMusicStream(Music music) 
```

Python wrapper:

```python
def StopMusicStream(music: Music) -> None
```

See also:
<a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="PauseMusicStream"><code>PauseMusicStream</code> function</h2>

> Pause music playing

Defined in raylib.h:

```c
void PauseMusicStream(Music music) 
```

Python wrapper:

```python
def PauseMusicStream(music: Music) -> None
```

See also:
<a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ResumeMusicStream"><code>ResumeMusicStream</code> function</h2>

> Resume playing paused music

Defined in raylib.h:

```c
void ResumeMusicStream(Music music) 
```

Python wrapper:

```python
def ResumeMusicStream(music: Music) -> None
```

See also:
<a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SeekMusicStream"><code>SeekMusicStream</code> function</h2>

> Seek music to a position (in seconds)

Defined in raylib.h:

```c
void SeekMusicStream(Music music, float position) 
```

Python wrapper:

```python
def SeekMusicStream(music: Music, position: float) -> None
```

See also:
<a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetMusicVolume"><code>SetMusicVolume</code> function</h2>

> Set volume for music (1.0 is max level)

Defined in raylib.h:

```c
void SetMusicVolume(Music music, float volume) 
```

Python wrapper:

```python
def SetMusicVolume(music: Music, volume: float) -> None
```

See also:
<a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetMusicPitch"><code>SetMusicPitch</code> function</h2>

> Set pitch for a music (1.0 is base level)

Defined in raylib.h:

```c
void SetMusicPitch(Music music, float pitch) 
```

Python wrapper:

```python
def SetMusicPitch(music: Music, pitch: float) -> None
```

See also:
<a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetMusicPan"><code>SetMusicPan</code> function</h2>

> Set pan for a music (0.5 is center)

Defined in raylib.h:

```c
void SetMusicPan(Music music, float pan) 
```

Python wrapper:

```python
def SetMusicPan(music: Music, pan: float) -> None
```

See also:
<a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMusicTimeLength"><code>GetMusicTimeLength</code> function</h2>

> Get music time length (in seconds)

Defined in raylib.h:

```c
float GetMusicTimeLength(Music music) 
```

Python wrapper:

```python
def GetMusicTimeLength(music: Music) -> float
```

See also:
<a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="GetMusicTimePlayed"><code>GetMusicTimePlayed</code> function</h2>

> Get current music time played (in seconds)

Defined in raylib.h:

```c
float GetMusicTimePlayed(Music music) 
```

Python wrapper:

```python
def GetMusicTimePlayed(music: Music) -> float
```

See also:
<a href="#Music">Music</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="LoadAudioStream"><code>LoadAudioStream</code> function</h2>

> Load audio stream (to stream raw audio pcm data)

Defined in raylib.h:

```c
AudioStream LoadAudioStream(unsigned int sampleRate, unsigned int sampleSize, unsigned int channels) 
```

Python wrapper:

```python
def LoadAudioStream(sampleRate: int, sampleSize: int, channels: int) -> AudioStream
```

See also:
<a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UnloadAudioStream"><code>UnloadAudioStream</code> function</h2>

> Unload audio stream and free memory

Defined in raylib.h:

```c
void UnloadAudioStream(AudioStream stream) 
```

Python wrapper:

```python
def UnloadAudioStream(stream: AudioStream) -> None
```

See also:
<a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="UpdateAudioStream"><code>UpdateAudioStream</code> function</h2>

> Update audio stream buffers with data

Defined in raylib.h:

```c
void UpdateAudioStream(AudioStream stream, void data, int frameCount) 
```

Python wrapper:

```python
def UpdateAudioStream(stream: AudioStream, data: bytes, frameCount: int) -> None
```

See also:
<a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsAudioStreamProcessed"><code>IsAudioStreamProcessed</code> function</h2>

> Check if any audio stream buffers requires refill

Defined in raylib.h:

```c
bool IsAudioStreamProcessed(AudioStream stream) 
```

Python wrapper:

```python
def IsAudioStreamProcessed(stream: AudioStream) -> bool
```

See also:
<a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="PlayAudioStream"><code>PlayAudioStream</code> function</h2>

> Play audio stream

Defined in raylib.h:

```c
void PlayAudioStream(AudioStream stream) 
```

Python wrapper:

```python
def PlayAudioStream(stream: AudioStream) -> None
```

See also:
<a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="PauseAudioStream"><code>PauseAudioStream</code> function</h2>

> Pause audio stream

Defined in raylib.h:

```c
void PauseAudioStream(AudioStream stream) 
```

Python wrapper:

```python
def PauseAudioStream(stream: AudioStream) -> None
```

See also:
<a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ResumeAudioStream"><code>ResumeAudioStream</code> function</h2>

> Resume audio stream

Defined in raylib.h:

```c
void ResumeAudioStream(AudioStream stream) 
```

Python wrapper:

```python
def ResumeAudioStream(stream: AudioStream) -> None
```

See also:
<a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="IsAudioStreamPlaying"><code>IsAudioStreamPlaying</code> function</h2>

> Check if audio stream is playing

Defined in raylib.h:

```c
bool IsAudioStreamPlaying(AudioStream stream) 
```

Python wrapper:

```python
def IsAudioStreamPlaying(stream: AudioStream) -> bool
```

See also:
<a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="StopAudioStream"><code>StopAudioStream</code> function</h2>

> Stop audio stream

Defined in raylib.h:

```c
void StopAudioStream(AudioStream stream) 
```

Python wrapper:

```python
def StopAudioStream(stream: AudioStream) -> None
```

See also:
<a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetAudioStreamVolume"><code>SetAudioStreamVolume</code> function</h2>

> Set volume for audio stream (1.0 is max level)

Defined in raylib.h:

```c
void SetAudioStreamVolume(AudioStream stream, float volume) 
```

Python wrapper:

```python
def SetAudioStreamVolume(stream: AudioStream, volume: float) -> None
```

See also:
<a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetAudioStreamPitch"><code>SetAudioStreamPitch</code> function</h2>

> Set pitch for audio stream (1.0 is base level)

Defined in raylib.h:

```c
void SetAudioStreamPitch(AudioStream stream, float pitch) 
```

Python wrapper:

```python
def SetAudioStreamPitch(stream: AudioStream, pitch: float) -> None
```

See also:
<a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetAudioStreamPan"><code>SetAudioStreamPan</code> function</h2>

> Set pan for audio stream (0.5 is centered)

Defined in raylib.h:

```c
void SetAudioStreamPan(AudioStream stream, float pan) 
```

Python wrapper:

```python
def SetAudioStreamPan(stream: AudioStream, pan: float) -> None
```

See also:
<a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetAudioStreamBufferSizeDefault"><code>SetAudioStreamBufferSizeDefault</code> function</h2>

> Default size for new audio streams

Defined in raylib.h:

```c
void SetAudioStreamBufferSizeDefault(int size) 
```

Python wrapper:

```python
def SetAudioStreamBufferSizeDefault(size: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="SetAudioStreamCallback"><code>SetAudioStreamCallback</code> function</h2>

> Audio thread callback to request new data

Defined in raylib.h:

```c
void SetAudioStreamCallback(AudioStream stream, AudioCallback callback) 
```

Python wrapper:

```python
def SetAudioStreamCallback(stream: AudioStream, callback: AudioCallback) -> None
```

See also:
<a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="AttachAudioStreamProcessor"><code>AttachAudioStreamProcessor</code> function</h2>

> 

Defined in raylib.h:

```c
void AttachAudioStreamProcessor(AudioStream stream, AudioCallback processor) 
```

Python wrapper:

```python
def AttachAudioStreamProcessor(stream: AudioStream, processor: AudioCallback) -> None
```

See also:
<a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="DetachAudioStreamProcessor"><code>DetachAudioStreamProcessor</code> function</h2>

> 

Defined in raylib.h:

```c
void DetachAudioStreamProcessor(AudioStream stream, AudioCallback processor) 
```

Python wrapper:

```python
def DetachAudioStreamProcessor(stream: AudioStream, processor: AudioCallback) -> None
```

See also:
<a href="#AudioStream">AudioStream</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Clamp"><code>Clamp</code> function</h2>

> Clamp float value

Defined in raylib.h:

```c
float Clamp(float value, float min_, float max_) 
```

Python wrapper:

```python
def Clamp(value: float, min_: float, max_: float) -> float
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Lerp"><code>Lerp</code> function</h2>

> Calculate linear interpolation between two floats

Defined in raylib.h:

```c
float Lerp(float start, float end, float amount) 
```

Python wrapper:

```python
def Lerp(start: float, end: float, amount: float) -> float
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Normalize"><code>Normalize</code> function</h2>

> Calculate linear interpolation between two floats

Defined in raylib.h:

```c
float Normalize(float value, float start, float end) 
```

Python wrapper:

```python
def Normalize(value: float, start: float, end: float) -> float
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Remap"><code>Remap</code> function</h2>

> Remap input value within input range to output range

Defined in raylib.h:

```c
float Remap(float value, float inputStart, float inputEnd, float outputStart, float outputEnd) 
```

Python wrapper:

```python
def Remap(value: float, inputStart: float, inputEnd: float, outputStart: float, outputEnd: float) -> float
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Wrap"><code>Wrap</code> function</h2>

> Wrap input value from min to max

Defined in raylib.h:

```c
float Wrap(float value, float min_, float max_) 
```

Python wrapper:

```python
def Wrap(value: float, min_: float, max_: float) -> float
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="FloatEquals"><code>FloatEquals</code> function</h2>

> Check whether two given floats are almost equal

Defined in raylib.h:

```c
int FloatEquals(float x, float y) 
```

Python wrapper:

```python
def FloatEquals(x: float, y: float) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Zero"><code>Vector2Zero</code> function</h2>

> Vector with components value 0.0f

Defined in raylib.h:

```c
Vector2 Vector2Zero() 
```

Python wrapper:

```python
def Vector2Zero() -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2One"><code>Vector2One</code> function</h2>

> Vector with components value 1.0f

Defined in raylib.h:

```c
Vector2 Vector2One() 
```

Python wrapper:

```python
def Vector2One() -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Add"><code>Vector2Add</code> function</h2>

> Add two vectors (v1 + v2)

Defined in raylib.h:

```c
Vector2 Vector2Add(Vector2 v1, Vector2 v2) 
```

Python wrapper:

```python
def Vector2Add(v1: Vector2, v2: Vector2) -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2AddValue"><code>Vector2AddValue</code> function</h2>

> Add vector and float value

Defined in raylib.h:

```c
Vector2 Vector2AddValue(Vector2 v, float add) 
```

Python wrapper:

```python
def Vector2AddValue(v: Vector2, add: float) -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Subtract"><code>Vector2Subtract</code> function</h2>

> Subtract two vectors (v1 - v2)

Defined in raylib.h:

```c
Vector2 Vector2Subtract(Vector2 v1, Vector2 v2) 
```

Python wrapper:

```python
def Vector2Subtract(v1: Vector2, v2: Vector2) -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2SubtractValue"><code>Vector2SubtractValue</code> function</h2>

> Subtract vector by float value

Defined in raylib.h:

```c
Vector2 Vector2SubtractValue(Vector2 v, float sub) 
```

Python wrapper:

```python
def Vector2SubtractValue(v: Vector2, sub: float) -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Length"><code>Vector2Length</code> function</h2>

> Calculate vector length

Defined in raylib.h:

```c
float Vector2Length(Vector2 v) 
```

Python wrapper:

```python
def Vector2Length(v: Vector2) -> float
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2LengthSqr"><code>Vector2LengthSqr</code> function</h2>

> Calculate vector square length

Defined in raylib.h:

```c
float Vector2LengthSqr(Vector2 v) 
```

Python wrapper:

```python
def Vector2LengthSqr(v: Vector2) -> float
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2DotProduct"><code>Vector2DotProduct</code> function</h2>

> Calculate two vectors dot product

Defined in raylib.h:

```c
float Vector2DotProduct(Vector2 v1, Vector2 v2) 
```

Python wrapper:

```python
def Vector2DotProduct(v1: Vector2, v2: Vector2) -> float
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Distance"><code>Vector2Distance</code> function</h2>

> Calculate distance between two vectors

Defined in raylib.h:

```c
float Vector2Distance(Vector2 v1, Vector2 v2) 
```

Python wrapper:

```python
def Vector2Distance(v1: Vector2, v2: Vector2) -> float
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2DistanceSqr"><code>Vector2DistanceSqr</code> function</h2>

> Calculate square distance between two vectors

Defined in raylib.h:

```c
float Vector2DistanceSqr(Vector2 v1, Vector2 v2) 
```

Python wrapper:

```python
def Vector2DistanceSqr(v1: Vector2, v2: Vector2) -> float
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Angle"><code>Vector2Angle</code> function</h2>

> Calculate angle from two vectors

Defined in raylib.h:

```c
float Vector2Angle(Vector2 v1, Vector2 v2) 
```

Python wrapper:

```python
def Vector2Angle(v1: Vector2, v2: Vector2) -> float
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Scale"><code>Vector2Scale</code> function</h2>

> Scale vector (multiply by value)

Defined in raylib.h:

```c
Vector2 Vector2Scale(Vector2 v, float scale) 
```

Python wrapper:

```python
def Vector2Scale(v: Vector2, scale: float) -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Multiply"><code>Vector2Multiply</code> function</h2>

> Multiply vector by vector

Defined in raylib.h:

```c
Vector2 Vector2Multiply(Vector2 v1, Vector2 v2) 
```

Python wrapper:

```python
def Vector2Multiply(v1: Vector2, v2: Vector2) -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Negate"><code>Vector2Negate</code> function</h2>

> Negate vector

Defined in raylib.h:

```c
Vector2 Vector2Negate(Vector2 v) 
```

Python wrapper:

```python
def Vector2Negate(v: Vector2) -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Divide"><code>Vector2Divide</code> function</h2>

> Divide vector by vector

Defined in raylib.h:

```c
Vector2 Vector2Divide(Vector2 v1, Vector2 v2) 
```

Python wrapper:

```python
def Vector2Divide(v1: Vector2, v2: Vector2) -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Normalize"><code>Vector2Normalize</code> function</h2>

> Normalize provided vector

Defined in raylib.h:

```c
Vector2 Vector2Normalize(Vector2 v) 
```

Python wrapper:

```python
def Vector2Normalize(v: Vector2) -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Transform"><code>Vector2Transform</code> function</h2>

> Transforms a Vector2 by a given Matrix

Defined in raylib.h:

```c
Vector2 Vector2Transform(Vector2 v, Matrix mat) 
```

Python wrapper:

```python
def Vector2Transform(v: Vector2, mat: Matrix) -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>, <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Lerp"><code>Vector2Lerp</code> function</h2>

> Calculate linear interpolation between two vectors

Defined in raylib.h:

```c
Vector2 Vector2Lerp(Vector2 v1, Vector2 v2, float amount) 
```

Python wrapper:

```python
def Vector2Lerp(v1: Vector2, v2: Vector2, amount: float) -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Reflect"><code>Vector2Reflect</code> function</h2>

> Calculate reflected vector to normal

Defined in raylib.h:

```c
Vector2 Vector2Reflect(Vector2 v1, Vector2 normal) 
```

Python wrapper:

```python
def Vector2Reflect(v1: Vector2, normal: Vector2) -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Rotate"><code>Vector2Rotate</code> function</h2>

> Rotate vector by angle

Defined in raylib.h:

```c
Vector2 Vector2Rotate(Vector2 v1, float angle) 
```

Python wrapper:

```python
def Vector2Rotate(v1: Vector2, angle: float) -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2MoveTowards"><code>Vector2MoveTowards</code> function</h2>

> Move Vector towards target

Defined in raylib.h:

```c
Vector2 Vector2MoveTowards(Vector2 v1, Vector2 target, float maxDistance) 
```

Python wrapper:

```python
def Vector2MoveTowards(v1: Vector2, target: Vector2, maxDistance: float) -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Invert"><code>Vector2Invert</code> function</h2>

> Invert the given vector

Defined in raylib.h:

```c
Vector2 Vector2Invert(Vector2 v) 
```

Python wrapper:

```python
def Vector2Invert(v: Vector2) -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Clamp"><code>Vector2Clamp</code> function</h2>

> Clamp the components of the vector between min and max values specified by the given vectors

Defined in raylib.h:

```c
Vector2 Vector2Clamp(Vector2 v, Vector2 min_, Vector2 max_) 
```

Python wrapper:

```python
def Vector2Clamp(v: Vector2, min_: Vector2, max_: Vector2) -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2ClampValue"><code>Vector2ClampValue</code> function</h2>

> Clamp the magnitude of the vector between two min and max values

Defined in raylib.h:

```c
Vector2 Vector2ClampValue(Vector2 v, float min_, float max_) 
```

Python wrapper:

```python
def Vector2ClampValue(v: Vector2, min_: float, max_: float) -> Vector2
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector2Equals"><code>Vector2Equals</code> function</h2>

> Check whether two given vectors are almost equal

Defined in raylib.h:

```c
int Vector2Equals(Vector2 p, Vector2 q) 
```

Python wrapper:

```python
def Vector2Equals(p: Vector2, q: Vector2) -> int
```

See also:
<a href="#Vector2">Vector2</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Zero"><code>Vector3Zero</code> function</h2>

> Vector with components value 0.0f

Defined in raylib.h:

```c
Vector3 Vector3Zero() 
```

Python wrapper:

```python
def Vector3Zero() -> Vector3
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3One"><code>Vector3One</code> function</h2>

> Vector with components value 1.0f

Defined in raylib.h:

```c
Vector3 Vector3One() 
```

Python wrapper:

```python
def Vector3One() -> Vector3
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Add"><code>Vector3Add</code> function</h2>

> Add two vectors

Defined in raylib.h:

```c
Vector3 Vector3Add(Vector3 v1, Vector3 v2) 
```

Python wrapper:

```python
def Vector3Add(v1: Vector3, v2: Vector3) -> Vector3
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3AddValue"><code>Vector3AddValue</code> function</h2>

> Add vector and float value

Defined in raylib.h:

```c
Vector3 Vector3AddValue(Vector3 v, float add) 
```

Python wrapper:

```python
def Vector3AddValue(v: Vector3, add: float) -> Vector3
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Subtract"><code>Vector3Subtract</code> function</h2>

> Subtract two vectors

Defined in raylib.h:

```c
Vector3 Vector3Subtract(Vector3 v1, Vector3 v2) 
```

Python wrapper:

```python
def Vector3Subtract(v1: Vector3, v2: Vector3) -> Vector3
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3SubtractValue"><code>Vector3SubtractValue</code> function</h2>

> Subtract vector and float value

Defined in raylib.h:

```c
Vector3 Vector3SubtractValue(Vector3 v, float sub) 
```

Python wrapper:

```python
def Vector3SubtractValue(v: Vector3, sub: float) -> Vector3
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Scale"><code>Vector3Scale</code> function</h2>

> Multiply vector by scalar

Defined in raylib.h:

```c
Vector3 Vector3Scale(Vector3 v, float scalar) 
```

Python wrapper:

```python
def Vector3Scale(v: Vector3, scalar: float) -> Vector3
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Multiply"><code>Vector3Multiply</code> function</h2>

> Multiply vector by vector

Defined in raylib.h:

```c
Vector3 Vector3Multiply(Vector3 v1, Vector3 v2) 
```

Python wrapper:

```python
def Vector3Multiply(v1: Vector3, v2: Vector3) -> Vector3
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3CrossProduct"><code>Vector3CrossProduct</code> function</h2>

> Calculate two vectors cross product

Defined in raylib.h:

```c
float Vector3CrossProduct(Vector3 v1, Vector3 v2) 
```

Python wrapper:

```python
def Vector3CrossProduct(v1: Vector3, v2: Vector3) -> float
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Perpendicular"><code>Vector3Perpendicular</code> function</h2>

> Calculate one vector perpendicular vector

Defined in raylib.h:

```c
Vector3 Vector3Perpendicular(Vector3 v1) 
```

Python wrapper:

```python
def Vector3Perpendicular(v1: Vector3) -> Vector3
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Length"><code>Vector3Length</code> function</h2>

> Calculate vector length

Defined in raylib.h:

```c
float Vector3Length(Vector3 v1) 
```

Python wrapper:

```python
def Vector3Length(v1: Vector3) -> float
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3LengthSqr"><code>Vector3LengthSqr</code> function</h2>

> Calculate vector square length

Defined in raylib.h:

```c
float Vector3LengthSqr(Vector3 v1) 
```

Python wrapper:

```python
def Vector3LengthSqr(v1: Vector3) -> float
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3DotProduct"><code>Vector3DotProduct</code> function</h2>

> Calculate two vectors dot product

Defined in raylib.h:

```c
float Vector3DotProduct(Vector3 v1, Vector3 v2) 
```

Python wrapper:

```python
def Vector3DotProduct(v1: Vector3, v2: Vector3) -> float
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Distance"><code>Vector3Distance</code> function</h2>

> Calculate distance between two vectors

Defined in raylib.h:

```c
float Vector3Distance(Vector3 v1, Vector3 v2) 
```

Python wrapper:

```python
def Vector3Distance(v1: Vector3, v2: Vector3) -> float
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3DistanceSqr"><code>Vector3DistanceSqr</code> function</h2>

> Calculate square distance between two vectors

Defined in raylib.h:

```c
float Vector3DistanceSqr(Vector3 v1, Vector3 v2) 
```

Python wrapper:

```python
def Vector3DistanceSqr(v1: Vector3, v2: Vector3) -> float
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Angle"><code>Vector3Angle</code> function</h2>

> Calculate angle between two vectors

Defined in raylib.h:

```c
float Vector3Angle(Vector3 v1, Vector3 v2) 
```

Python wrapper:

```python
def Vector3Angle(v1: Vector3, v2: Vector3) -> float
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Negate"><code>Vector3Negate</code> function</h2>

> Negate provided vector (invert direction)

Defined in raylib.h:

```c
Vector3 Vector3Negate(Vector3 v) 
```

Python wrapper:

```python
def Vector3Negate(v: Vector3) -> Vector3
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Divide"><code>Vector3Divide</code> function</h2>

> Divide vector by vector

Defined in raylib.h:

```c
float Vector3Divide(Vector3 v1, Vector3 v2) 
```

Python wrapper:

```python
def Vector3Divide(v1: Vector3, v2: Vector3) -> float
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Normalize"><code>Vector3Normalize</code> function</h2>

> Normalize provided vector

Defined in raylib.h:

```c
Vector3 Vector3Normalize(Vector3 v) 
```

Python wrapper:

```python
def Vector3Normalize(v: Vector3) -> Vector3
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3OrthoNormalize"><code>Vector3OrthoNormalize</code> function</h2>

> Makes vectors normalized and orthogonal to each other

Defined in raylib.h:

```c
Vector3 Vector3OrthoNormalize(Vector3 * v1, Vector3 * v2) 
```

Python wrapper:

```python
def Vector3OrthoNormalize(v1: Vector3Ptr, v2: Vector3Ptr) -> Vector3
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Transform"><code>Vector3Transform</code> function</h2>

> Transforms a Vector3 by a given Matrix

Defined in raylib.h:

```c
Vector3 Vector3Transform(Vector3 v, Matrix mat) 
```

Python wrapper:

```python
def Vector3Transform(v: Vector3, mat: Matrix) -> Vector3
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3RotateByQuaternion"><code>Vector3RotateByQuaternion</code> function</h2>

> Transform a vector by quaternion rotation

Defined in raylib.h:

```c
Vector3 Vector3RotateByQuaternion(Vector3 v, Quaternion q) 
```

Python wrapper:

```python
def Vector3RotateByQuaternion(v: Vector3, q: Quaternion) -> Vector3
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3RotateByAxisAngle"><code>Vector3RotateByAxisAngle</code> function</h2>

> Rotates a vector around an axis

Defined in raylib.h:

```c
Vector3 Vector3RotateByAxisAngle(Vector3 v, Vector3 axis, float angle) 
```

Python wrapper:

```python
def Vector3RotateByAxisAngle(v: Vector3, axis: Vector3, angle: float) -> Vector3
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Lerp"><code>Vector3Lerp</code> function</h2>

> Calculate linear interpolation between two vectors

Defined in raylib.h:

```c
Vector3 Vector3Lerp(Vector3 v1, Vector3 v2, float amount) 
```

Python wrapper:

```python
def Vector3Lerp(v1: Vector3, v2: Vector3, amount: float) -> Vector3
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Reflect"><code>Vector3Reflect</code> function</h2>

> Calculate reflected vector to normal

Defined in raylib.h:

```c
Vector3 Vector3Reflect(Vector3 v, Vector3 normal) 
```

Python wrapper:

```python
def Vector3Reflect(v: Vector3, normal: Vector3) -> Vector3
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Min"><code>Vector3Min</code> function</h2>

> Get min value for each pair of components

Defined in raylib.h:

```c
Vector3 Vector3Min(Vector3 v1, Vector3 v2) 
```

Python wrapper:

```python
def Vector3Min(v1: Vector3, v2: Vector3) -> Vector3
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Max"><code>Vector3Max</code> function</h2>

> Get max value for each pair of components

Defined in raylib.h:

```c
Vector3 Vector3Max(Vector3 v1, Vector3 v2) 
```

Python wrapper:

```python
def Vector3Max(v1: Vector3, v2: Vector3) -> Vector3
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Barycenter"><code>Vector3Barycenter</code> function</h2>

> Compute barycenter coordinates (u, v, w) for point p with respect to triangle (a, b, c). Assumes P is on the plane of the triangle

Defined in raylib.h:

```c
Vector3 Vector3Barycenter(Vector3 p, Vector3 a, Vector3 b, Vector3 c) 
```

Python wrapper:

```python
def Vector3Barycenter(p: Vector3, a: Vector3, b: Vector3, c: Vector3) -> Vector3
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Unproject"><code>Vector3Unproject</code> function</h2>

> Projects a Vector3 from screen space into object space

Defined in raylib.h:

```c
Vector3 Vector3Unproject(Vector3 source, Matrix projection, Matrix view) 
```

Python wrapper:

```python
def Vector3Unproject(source: Vector3, projection: Matrix, view: Matrix) -> Vector3
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3ToFloatV"><code>Vector3ToFloatV</code> function</h2>

> Get Vector3 as float array

Defined in raylib.h:

```c
float[3] Vector3ToFloatV(Vector3 v) 
```

Python wrapper:

```python
def Vector3ToFloatV(v: Vector3) -> Seq[float]
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Invert"><code>Vector3Invert</code> function</h2>

> Invert the given vector

Defined in raylib.h:

```c
Vector3 Vector3Invert(Vector3 v) 
```

Python wrapper:

```python
def Vector3Invert(v: Vector3) -> Vector3
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Clamp"><code>Vector3Clamp</code> function</h2>

> Clamp the components of the vector between min and max values specified by the given vectors

Defined in raylib.h:

```c
Vector3 Vector3Clamp(Vector3 v, Vector3 min_, Vector3 max_) 
```

Python wrapper:

```python
def Vector3Clamp(v: Vector3, min_: Vector3, max_: Vector3) -> Vector3
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3ClampValue"><code>Vector3ClampValue</code> function</h2>

> Clamp the magnitude of the vector between two values

Defined in raylib.h:

```c
Vector3 Vector3ClampValue(Vector3 v, float min_, float max_) 
```

Python wrapper:

```python
def Vector3ClampValue(v: Vector3, min_: float, max_: float) -> Vector3
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Equals"><code>Vector3Equals</code> function</h2>

> Check whether two given vectors are almost equal

Defined in raylib.h:

```c
int Vector3Equals(Vector3 v, float min_, float max_) 
```

Python wrapper:

```python
def Vector3Equals(v: Vector3, min_: float, max_: float) -> int
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Vector3Refract"><code>Vector3Refract</code> function</h2>

> Compute the direction of a refracted ray where v specifies the normalized direction of the incoming ray, n specifies the normalized normal vector of the interface of two optical media, and r specifies the ratio of the refractive index of the medium from where the ray comes to the refractive index of the medium on the other side of the surface

Defined in raylib.h:

```c
int Vector3Refract(Vector3 v, Vector3 n, float r) 
```

Python wrapper:

```python
def Vector3Refract(v: Vector3, n: Vector3, r: float) -> int
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixDeterminant"><code>MatrixDeterminant</code> function</h2>

> Compute matrix determinant

Defined in raylib.h:

```c
float MatrixDeterminant(Matrix mat) 
```

Python wrapper:

```python
def MatrixDeterminant(mat: Matrix) -> float
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixTrace"><code>MatrixTrace</code> function</h2>

> Get the trace of the matrix (sum of the values along the diagonal)

Defined in raylib.h:

```c
float MatrixTrace(Matrix mat) 
```

Python wrapper:

```python
def MatrixTrace(mat: Matrix) -> float
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixTranspose"><code>MatrixTranspose</code> function</h2>

> Get the trace of the matrix (sum of the values along the diagonal)

Defined in raylib.h:

```c
Matrix MatrixTranspose(Matrix mat) 
```

Python wrapper:

```python
def MatrixTranspose(mat: Matrix) -> Matrix
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixInvert"><code>MatrixInvert</code> function</h2>

> Invert provided matrix

Defined in raylib.h:

```c
Matrix MatrixInvert(Matrix mat) 
```

Python wrapper:

```python
def MatrixInvert(mat: Matrix) -> Matrix
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixIdentity"><code>MatrixIdentity</code> function</h2>

> Get identity matrix

Defined in raylib.h:

```c
Matrix MatrixIdentity() 
```

Python wrapper:

```python
def MatrixIdentity() -> Matrix
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixAdd"><code>MatrixAdd</code> function</h2>

> Add two matrices

Defined in raylib.h:

```c
Matrix MatrixAdd(Matrix left, Matrix right) 
```

Python wrapper:

```python
def MatrixAdd(left: Matrix, right: Matrix) -> Matrix
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixSubtract"><code>MatrixSubtract</code> function</h2>

> Subtract two matrices (left - right)

Defined in raylib.h:

```c
Matrix MatrixSubtract(Matrix left, Matrix right) 
```

Python wrapper:

```python
def MatrixSubtract(left: Matrix, right: Matrix) -> Matrix
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixMultiply"><code>MatrixMultiply</code> function</h2>

> Get two matrix multiplication. When multiplying matrices... the order matters!

Defined in raylib.h:

```c
Matrix MatrixMultiply(Matrix left, Matrix right) 
```

Python wrapper:

```python
def MatrixMultiply(left: Matrix, right: Matrix) -> Matrix
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixTranslate"><code>MatrixTranslate</code> function</h2>

> Get translation matrix

Defined in raylib.h:

```c
Matrix MatrixTranslate(float x, float y, float z) 
```

Python wrapper:

```python
def MatrixTranslate(x: float, y: float, z: float) -> Matrix
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixRotate"><code>MatrixRotate</code> function</h2>

> Create rotation matrix from axis and angle. Angle should be provided in radians

Defined in raylib.h:

```c
Matrix MatrixRotate(Vector3 axis, float angle) 
```

Python wrapper:

```python
def MatrixRotate(axis: Vector3, angle: float) -> Matrix
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixRotateX"><code>MatrixRotateX</code> function</h2>

> Get x-rotation matrix. Angle must be provided in radians

Defined in raylib.h:

```c
Matrix MatrixRotateX(float angle) 
```

Python wrapper:

```python
def MatrixRotateX(angle: float) -> Matrix
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixRotateY"><code>MatrixRotateY</code> function</h2>

> Get y-rotation matrix. Angle must be provided in radians

Defined in raylib.h:

```c
Matrix MatrixRotateY(float angle) 
```

Python wrapper:

```python
def MatrixRotateY(angle: float) -> Matrix
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixRotateZ"><code>MatrixRotateZ</code> function</h2>

> Get z-rotation matrix. Angle must be provided in radians

Defined in raylib.h:

```c
Matrix MatrixRotateZ(float angle) 
```

Python wrapper:

```python
def MatrixRotateZ(angle: float) -> Matrix
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixRotateXYZ"><code>MatrixRotateXYZ</code> function</h2>

> Get xyz-rotation matrix. Angle must be provided in radians

Defined in raylib.h:

```c
Matrix MatrixRotateXYZ(Vector3 angle) 
```

Python wrapper:

```python
def MatrixRotateXYZ(angle: Vector3) -> Matrix
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixRotateZYX"><code>MatrixRotateZYX</code> function</h2>

> Get zyx-rotation matrix. Angle must be provided in radians

Defined in raylib.h:

```c
Matrix MatrixRotateZYX(Vector3 angle) 
```

Python wrapper:

```python
def MatrixRotateZYX(angle: Vector3) -> Matrix
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixScale"><code>MatrixScale</code> function</h2>

> Get scaling matrix

Defined in raylib.h:

```c
Matrix MatrixScale(float x, float y, float z) 
```

Python wrapper:

```python
def MatrixScale(x: float, y: float, z: float) -> Matrix
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixFrustum"><code>MatrixFrustum</code> function</h2>

> Get perspective projection matrix

Defined in raylib.h:

```c
Matrix MatrixFrustum(float left, float right, float bottom, float top, float near, float far) 
```

Python wrapper:

```python
def MatrixFrustum(left: float, right: float, bottom: float, top: float, near: float, far: float) -> Matrix
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixPerspective"><code>MatrixPerspective</code> function</h2>

> Get perspective projection matrix. Fovy angle must be provided in radians

Defined in raylib.h:

```c
Matrix MatrixPerspective(float fovy, float aspect, float near, float far) 
```

Python wrapper:

```python
def MatrixPerspective(fovy: float, aspect: float, near: float, far: float) -> Matrix
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixOrtho"><code>MatrixOrtho</code> function</h2>

> Get orthographic projection matrix

Defined in raylib.h:

```c
Matrix MatrixOrtho(float left, float right, float bottom, float top, float near, float far) 
```

Python wrapper:

```python
def MatrixOrtho(left: float, right: float, bottom: float, top: float, near: float, far: float) -> Matrix
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixLookAt"><code>MatrixLookAt</code> function</h2>

> Get camera look-at matrix (view matrix)

Defined in raylib.h:

```c
Matrix MatrixLookAt(Vector3 eye, Vector3 target, Vector3 up) 
```

Python wrapper:

```python
def MatrixLookAt(eye: Vector3, target: Vector3, up: Vector3) -> Matrix
```

See also:
<a href="#Vector3">Vector3</a>, <a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="MatrixToFloatV"><code>MatrixToFloatV</code> function</h2>

> Get float array of matrix data

Defined in raylib.h:

```c
float[16] MatrixToFloatV(Matrix mat) 
```

Python wrapper:

```python
def MatrixToFloatV(mat: Matrix) -> Seq[float]
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionAdd"><code>QuaternionAdd</code> function</h2>

> Add two quaternions

Defined in raylib.h:

```c
Quaternion QuaternionAdd(Quaternion q1, Quaternion q2) 
```

Python wrapper:

```python
def QuaternionAdd(q1: Quaternion, q2: Quaternion) -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionAddValue"><code>QuaternionAddValue</code> function</h2>

> Add quaternion and float value

Defined in raylib.h:

```c
Quaternion QuaternionAddValue(Quaternion q, float add) 
```

Python wrapper:

```python
def QuaternionAddValue(q: Quaternion, add: float) -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionSubtract"><code>QuaternionSubtract</code> function</h2>

> Subtract two quaternions

Defined in raylib.h:

```c
Quaternion QuaternionSubtract(Quaternion q1, Quaternion q2) 
```

Python wrapper:

```python
def QuaternionSubtract(q1: Quaternion, q2: Quaternion) -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionSubtractValue"><code>QuaternionSubtractValue</code> function</h2>

> Subtract quaternion and float value

Defined in raylib.h:

```c
Quaternion QuaternionSubtractValue(Quaternion q, float sub) 
```

Python wrapper:

```python
def QuaternionSubtractValue(q: Quaternion, sub: float) -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionIdentity"><code>QuaternionIdentity</code> function</h2>

> Get identity quaternion

Defined in raylib.h:

```c
Quaternion QuaternionIdentity() 
```

Python wrapper:

```python
def QuaternionIdentity() -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionLength"><code>QuaternionLength</code> function</h2>

> Computes the length of a quaternion

Defined in raylib.h:

```c
Quaternion QuaternionLength(Quaternion q) 
```

Python wrapper:

```python
def QuaternionLength(q: Quaternion) -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionNormalize"><code>QuaternionNormalize</code> function</h2>

> Normalize provided quaternion

Defined in raylib.h:

```c
Quaternion QuaternionNormalize(Quaternion q) 
```

Python wrapper:

```python
def QuaternionNormalize(q: Quaternion) -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionInvert"><code>QuaternionInvert</code> function</h2>

> Invert provided quaternion

Defined in raylib.h:

```c
Quaternion QuaternionInvert(Quaternion q) 
```

Python wrapper:

```python
def QuaternionInvert(q: Quaternion) -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionMultiply"><code>QuaternionMultiply</code> function</h2>

> Calculate two quaternion multiplication

Defined in raylib.h:

```c
Quaternion QuaternionMultiply(Quaternion q1, Quaternion q2) 
```

Python wrapper:

```python
def QuaternionMultiply(q1: Quaternion, q2: Quaternion) -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionScale"><code>QuaternionScale</code> function</h2>

> Scale quaternion by float value

Defined in raylib.h:

```c
Quaternion QuaternionScale(Quaternion q1, float mul) 
```

Python wrapper:

```python
def QuaternionScale(q1: Quaternion, mul: float) -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionDivide"><code>QuaternionDivide</code> function</h2>

> Divide two quaternions

Defined in raylib.h:

```c
Quaternion QuaternionDivide(Quaternion q1, Quaternion q2) 
```

Python wrapper:

```python
def QuaternionDivide(q1: Quaternion, q2: Quaternion) -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionNlerp"><code>QuaternionNlerp</code> function</h2>

> Calculate slerp-optimized interpolation between two quaternions

Defined in raylib.h:

```c
Quaternion QuaternionNlerp(Quaternion q1, Quaternion q2, float amount) 
```

Python wrapper:

```python
def QuaternionNlerp(q1: Quaternion, q2: Quaternion, amount: float) -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionSlerp"><code>QuaternionSlerp</code> function</h2>

> Calculates spherical linear interpolation between two quaternions

Defined in raylib.h:

```c
Quaternion QuaternionSlerp(Quaternion q1, Quaternion q2, float amount) 
```

Python wrapper:

```python
def QuaternionSlerp(q1: Quaternion, q2: Quaternion, amount: float) -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionFromVector3ToVector3"><code>QuaternionFromVector3ToVector3</code> function</h2>

> Calculate quaternion based on the rotation from one vector to another

Defined in raylib.h:

```c
Quaternion QuaternionFromVector3ToVector3(Vector3 from_, Vector3 to) 
```

Python wrapper:

```python
def QuaternionFromVector3ToVector3(from_: Vector3, to: Vector3) -> Quaternion
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionToMatrix"><code>QuaternionToMatrix</code> function</h2>

> Get a quaternion for a given rotation matrix

Defined in raylib.h:

```c
Matrix QuaternionToMatrix(Quaternion q) 
```

Python wrapper:

```python
def QuaternionToMatrix(q: Quaternion) -> Matrix
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionFromMatrix"><code>QuaternionFromMatrix</code> function</h2>

> Get a quaternion for a given rotation matrix

Defined in raylib.h:

```c
Quaternion QuaternionFromMatrix(Matrix mat) 
```

Python wrapper:

```python
def QuaternionFromMatrix(mat: Matrix) -> Quaternion
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionFromAxisAngle"><code>QuaternionFromAxisAngle</code> function</h2>

> Get rotation quaternion for an angle and axis. Angle must be provided in radians

Defined in raylib.h:

```c
Quaternion QuaternionFromAxisAngle(Vector3 mat, float angle) 
```

Python wrapper:

```python
def QuaternionFromAxisAngle(mat: Vector3, angle: float) -> Quaternion
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionToAxisAngle"><code>QuaternionToAxisAngle</code> function</h2>

> Get the rotation angle and axis for a given quaternion

Defined in raylib.h:

```c
void QuaternionToAxisAngle(Quaternion q, Vector3 * outAxis, float outAngle) 
```

Python wrapper:

```python
def QuaternionToAxisAngle(q: Quaternion, outAxis: Vector3Ptr, outAngle: Union[Seq[float], FloatPtr]) -> None
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionFromEuler"><code>QuaternionFromEuler</code> function</h2>

> Get the quaternion equivalent to Euler angles. Rotation order is ZYX

Defined in raylib.h:

```c
Quaternion QuaternionFromEuler(float pitch, float yaw, float roll) 
```

Python wrapper:

```python
def QuaternionFromEuler(pitch: float, yaw: float, roll: float) -> Quaternion
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionToEuler"><code>QuaternionToEuler</code> function</h2>

> Get the quaternion equivalent to Euler angles. Rotation order is ZYX

Defined in raylib.h:

```c
Vector3 QuaternionToEuler(Quaternion q) 
```

Python wrapper:

```python
def QuaternionToEuler(q: Quaternion) -> Vector3
```

See also:
<a href="#Vector3">Vector3</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionTransform"><code>QuaternionTransform</code> function</h2>

> Transform a quaternion given a transformation matrix

Defined in raylib.h:

```c
Quaternion QuaternionTransform(Quaternion q, Matrix mat) 
```

Python wrapper:

```python
def QuaternionTransform(q: Quaternion, mat: Matrix) -> Quaternion
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="QuaternionEquals"><code>QuaternionEquals</code> function</h2>

> Check whether two given quaternions are almost equal

Defined in raylib.h:

```c
int QuaternionEquals(Quaternion p, Quaternion q) 
```

Python wrapper:

```python
def QuaternionEquals(p: Quaternion, q: Quaternion) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlMatrixMode"><code>rlMatrixMode</code> function</h2>

> Choose the current matrix to be transformed

Defined in raylib.h:

```c
void rlMatrixMode(int mode) 
```

Python wrapper:

```python
def rlMatrixMode(mode: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlPushMatrix"><code>rlPushMatrix</code> function</h2>

> Push the current matrix to stack

Defined in raylib.h:

```c
void rlPushMatrix() 
```

Python wrapper:

```python
def rlPushMatrix() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlPopMatrix"><code>rlPopMatrix</code> function</h2>

> Pop lattest inserted matrix from stack

Defined in raylib.h:

```c
void rlPopMatrix() 
```

Python wrapper:

```python
def rlPopMatrix() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadIdentity"><code>rlLoadIdentity</code> function</h2>

> Reset current matrix to identity matrix

Defined in raylib.h:

```c
void rlLoadIdentity() 
```

Python wrapper:

```python
def rlLoadIdentity() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlTranslatef"><code>rlTranslatef</code> function</h2>

> Multiply the current matrix by a translation matrix

Defined in raylib.h:

```c
void rlTranslatef(float x, float y, float z) 
```

Python wrapper:

```python
def rlTranslatef(x: float, y: float, z: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlRotatef"><code>rlRotatef</code> function</h2>

> Multiply the current matrix by a rotation matrix

Defined in raylib.h:

```c
void rlRotatef(float angle, float x, float y, float z) 
```

Python wrapper:

```python
def rlRotatef(angle: float, x: float, y: float, z: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlScalef"><code>rlScalef</code> function</h2>

> Multiply the current matrix by a scaling matrix

Defined in raylib.h:

```c
void rlScalef(float x, float y, float z) 
```

Python wrapper:

```python
def rlScalef(x: float, y: float, z: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlMultMatrixf"><code>rlMultMatrixf</code> function</h2>

> Multiply the current matrix by another matrix

Defined in raylib.h:

```c
void rlMultMatrixf(float matf) 
```

Python wrapper:

```python
def rlMultMatrixf(matf: Union[Seq[float], FloatPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlFrustum"><code>rlFrustum</code> function</h2>

> 

Defined in raylib.h:

```c
void rlFrustum(double left, double right, double bottom, double top, double znear, double zfar) 
```

Python wrapper:

```python
def rlFrustum(left: float, right: float, bottom: float, top: float, znear: float, zfar: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlOrtho"><code>rlOrtho</code> function</h2>

> 

Defined in raylib.h:

```c
void rlOrtho(double left, double right, double bottom, double top, double znear, double zfar) 
```

Python wrapper:

```python
def rlOrtho(left: float, right: float, bottom: float, top: float, znear: float, zfar: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlViewport"><code>rlViewport</code> function</h2>

> Set the viewport area

Defined in raylib.h:

```c
void rlViewport(int x, int y, int width, int height) 
```

Python wrapper:

```python
def rlViewport(x: int, y: int, width: int, height: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlBegin"><code>rlBegin</code> function</h2>

> Initialize drawing mode (how to organize vertex)

Defined in raylib.h:

```c
void rlBegin(int mode) 
```

Python wrapper:

```python
def rlBegin(mode: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnd"><code>rlEnd</code> function</h2>

> Finish vertex providing

Defined in raylib.h:

```c
void rlEnd() 
```

Python wrapper:

```python
def rlEnd() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlVertex2i"><code>rlVertex2i</code> function</h2>

> Define one vertex (position) - 2 int

Defined in raylib.h:

```c
void rlVertex2i(int x, int y) 
```

Python wrapper:

```python
def rlVertex2i(x: int, y: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlVertex2f"><code>rlVertex2f</code> function</h2>

> Define one vertex (position) - 2 float

Defined in raylib.h:

```c
void rlVertex2f(float x, float y) 
```

Python wrapper:

```python
def rlVertex2f(x: float, y: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlVertex3f"><code>rlVertex3f</code> function</h2>

> Define one vertex (position) - 3 float

Defined in raylib.h:

```c
void rlVertex3f(float x, float y, float z) 
```

Python wrapper:

```python
def rlVertex3f(x: float, y: float, z: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlTexCoord2f"><code>rlTexCoord2f</code> function</h2>

> Define one vertex (texture coordinate) - 2 float

Defined in raylib.h:

```c
void rlTexCoord2f(float x, float y) 
```

Python wrapper:

```python
def rlTexCoord2f(x: float, y: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlNormal3f"><code>rlNormal3f</code> function</h2>

> Define one vertex (normal) - 3 float

Defined in raylib.h:

```c
void rlNormal3f(float x, float y, float z) 
```

Python wrapper:

```python
def rlNormal3f(x: float, y: float, z: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlColor4ub"><code>rlColor4ub</code> function</h2>

> Define one vertex (color) - 4 byte

Defined in raylib.h:

```c
void rlColor4ub(unsigned char r, unsigned char g, unsigned char b, unsigned char a) 
```

Python wrapper:

```python
def rlColor4ub(r: int, g: int, b: int, a: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlColor3f"><code>rlColor3f</code> function</h2>

> Define one vertex (color) - 3 float

Defined in raylib.h:

```c
void rlColor3f(float x, float y, float z) 
```

Python wrapper:

```python
def rlColor3f(x: float, y: float, z: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlColor4f"><code>rlColor4f</code> function</h2>

> Define one vertex (color) - 4 float

Defined in raylib.h:

```c
void rlColor4f(float x, float y, float z, float w) 
```

Python wrapper:

```python
def rlColor4f(x: float, y: float, z: float, w: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableVertexArray"><code>rlEnableVertexArray</code> function</h2>

> Enable vertex array (VAO, if supported)

Defined in raylib.h:

```c
bool rlEnableVertexArray(unsigned int vaoId) 
```

Python wrapper:

```python
def rlEnableVertexArray(vaoId: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableVertexArray"><code>rlDisableVertexArray</code> function</h2>

> Disable vertex array (VAO, if supported)

Defined in raylib.h:

```c
void rlDisableVertexArray() 
```

Python wrapper:

```python
def rlDisableVertexArray() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableVertexBuffer"><code>rlEnableVertexBuffer</code> function</h2>

> Enable vertex buffer (VBO)

Defined in raylib.h:

```c
void rlEnableVertexBuffer(unsigned int id) 
```

Python wrapper:

```python
def rlEnableVertexBuffer(id: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableVertexBuffer"><code>rlDisableVertexBuffer</code> function</h2>

> Disable vertex buffer (VBO)

Defined in raylib.h:

```c
void rlDisableVertexBuffer() 
```

Python wrapper:

```python
def rlDisableVertexBuffer() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableVertexBufferElement"><code>rlEnableVertexBufferElement</code> function</h2>

> Enable vertex buffer element (VBO element)

Defined in raylib.h:

```c
void rlEnableVertexBufferElement(unsigned int id) 
```

Python wrapper:

```python
def rlEnableVertexBufferElement(id: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableVertexBufferElement"><code>rlDisableVertexBufferElement</code> function</h2>

> Disable vertex buffer element (VBO element)

Defined in raylib.h:

```c
void rlDisableVertexBufferElement() 
```

Python wrapper:

```python
def rlDisableVertexBufferElement() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableVertexAttribute"><code>rlEnableVertexAttribute</code> function</h2>

> Enable vertex attribute index

Defined in raylib.h:

```c
void rlEnableVertexAttribute(unsigned int index) 
```

Python wrapper:

```python
def rlEnableVertexAttribute(index: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableVertexAttribute"><code>rlDisableVertexAttribute</code> function</h2>

> Disable vertex attribute index

Defined in raylib.h:

```c
void rlDisableVertexAttribute(unsigned int index) 
```

Python wrapper:

```python
def rlDisableVertexAttribute(index: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlActiveTextureSlot"><code>rlActiveTextureSlot</code> function</h2>

> Select and active a texture slot

Defined in raylib.h:

```c
void rlActiveTextureSlot(int slot) 
```

Python wrapper:

```python
def rlActiveTextureSlot(slot: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableTexture"><code>rlEnableTexture</code> function</h2>

> Enable texture

Defined in raylib.h:

```c
void rlEnableTexture(unsigned int id) 
```

Python wrapper:

```python
def rlEnableTexture(id: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableTexture"><code>rlDisableTexture</code> function</h2>

> Disable texture

Defined in raylib.h:

```c
void rlDisableTexture() 
```

Python wrapper:

```python
def rlDisableTexture() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableTextureCubemap"><code>rlEnableTextureCubemap</code> function</h2>

> Enable texture cubemap

Defined in raylib.h:

```c
void rlEnableTextureCubemap(unsigned int id) 
```

Python wrapper:

```python
def rlEnableTextureCubemap(id: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableTextureCubemap"><code>rlDisableTextureCubemap</code> function</h2>

> Disable texture cubemap

Defined in raylib.h:

```c
void rlDisableTextureCubemap() 
```

Python wrapper:

```python
def rlDisableTextureCubemap() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlTextureParameters"><code>rlTextureParameters</code> function</h2>

> Set texture parameters (filter, wrap)

Defined in raylib.h:

```c
void rlTextureParameters(unsigned int id, int param, int value) 
```

Python wrapper:

```python
def rlTextureParameters(id: int, param: int, value: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableShader"><code>rlEnableShader</code> function</h2>

> Enable shader program

Defined in raylib.h:

```c
void rlEnableShader(unsigned int id) 
```

Python wrapper:

```python
def rlEnableShader(id: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableShader"><code>rlDisableShader</code> function</h2>

> Disable shader program

Defined in raylib.h:

```c
void rlDisableShader() 
```

Python wrapper:

```python
def rlDisableShader() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableFramebuffer"><code>rlEnableFramebuffer</code> function</h2>

> Enable render texture (fbo)

Defined in raylib.h:

```c
void rlEnableFramebuffer(unsigned int id) 
```

Python wrapper:

```python
def rlEnableFramebuffer(id: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableFramebuffer"><code>rlDisableFramebuffer</code> function</h2>

> Disable render texture (fbo), return to default framebuffer

Defined in raylib.h:

```c
void rlDisableFramebuffer() 
```

Python wrapper:

```python
def rlDisableFramebuffer() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlActiveDrawBuffers"><code>rlActiveDrawBuffers</code> function</h2>

> Activate multiple draw color buffers

Defined in raylib.h:

```c
void rlActiveDrawBuffers(int count) 
```

Python wrapper:

```python
def rlActiveDrawBuffers(count: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableColorBlend"><code>rlEnableColorBlend</code> function</h2>

> Enable color blending

Defined in raylib.h:

```c
void rlEnableColorBlend() 
```

Python wrapper:

```python
def rlEnableColorBlend() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableColorBlend"><code>rlDisableColorBlend</code> function</h2>

> Disable color blending

Defined in raylib.h:

```c
void rlDisableColorBlend() 
```

Python wrapper:

```python
def rlDisableColorBlend() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableDepthTest"><code>rlEnableDepthTest</code> function</h2>

> Enable depth test

Defined in raylib.h:

```c
void rlEnableDepthTest() 
```

Python wrapper:

```python
def rlEnableDepthTest() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableDepthTest"><code>rlDisableDepthTest</code> function</h2>

> Disable depth test

Defined in raylib.h:

```c
void rlDisableDepthTest() 
```

Python wrapper:

```python
def rlDisableDepthTest() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableDepthMask"><code>rlEnableDepthMask</code> function</h2>

> Enable depth write

Defined in raylib.h:

```c
void rlEnableDepthMask() 
```

Python wrapper:

```python
def rlEnableDepthMask() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableDepthMask"><code>rlDisableDepthMask</code> function</h2>

> Disable depth write

Defined in raylib.h:

```c
void rlDisableDepthMask() 
```

Python wrapper:

```python
def rlDisableDepthMask() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableBackfaceCulling"><code>rlEnableBackfaceCulling</code> function</h2>

> Enable backface culling

Defined in raylib.h:

```c
void rlEnableBackfaceCulling() 
```

Python wrapper:

```python
def rlEnableBackfaceCulling() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableBackfaceCulling"><code>rlDisableBackfaceCulling</code> function</h2>

> Disable backface culling

Defined in raylib.h:

```c
void rlDisableBackfaceCulling() 
```

Python wrapper:

```python
def rlDisableBackfaceCulling() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableScissorTest"><code>rlEnableScissorTest</code> function</h2>

> Enable scissor test

Defined in raylib.h:

```c
void rlEnableScissorTest() 
```

Python wrapper:

```python
def rlEnableScissorTest() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableScissorTest"><code>rlDisableScissorTest</code> function</h2>

> Disable scissor test

Defined in raylib.h:

```c
void rlDisableScissorTest() 
```

Python wrapper:

```python
def rlDisableScissorTest() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlScissor"><code>rlScissor</code> function</h2>

> Scissor test

Defined in raylib.h:

```c
void rlScissor(int x, int y, int width, int height) 
```

Python wrapper:

```python
def rlScissor(x: int, y: int, width: int, height: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableWireMode"><code>rlEnableWireMode</code> function</h2>

> Enable wire mode

Defined in raylib.h:

```c
void rlEnableWireMode() 
```

Python wrapper:

```python
def rlEnableWireMode() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableWireMode"><code>rlDisableWireMode</code> function</h2>

> Disable wire mode

Defined in raylib.h:

```c
void rlDisableWireMode() 
```

Python wrapper:

```python
def rlDisableWireMode() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetLineWidth"><code>rlSetLineWidth</code> function</h2>

> Set the line drawing width

Defined in raylib.h:

```c
void rlSetLineWidth(float width) 
```

Python wrapper:

```python
def rlSetLineWidth(width: float) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetLineWidth"><code>rlGetLineWidth</code> function</h2>

> Get the line drawing width

Defined in raylib.h:

```c
float rlGetLineWidth() 
```

Python wrapper:

```python
def rlGetLineWidth() -> float
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableSmoothLines"><code>rlEnableSmoothLines</code> function</h2>

> Enable line aliasing

Defined in raylib.h:

```c
void rlEnableSmoothLines() 
```

Python wrapper:

```python
def rlEnableSmoothLines() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableSmoothLines"><code>rlDisableSmoothLines</code> function</h2>

> Disable line aliasing

Defined in raylib.h:

```c
void rlDisableSmoothLines() 
```

Python wrapper:

```python
def rlDisableSmoothLines() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlEnableStereoRender"><code>rlEnableStereoRender</code> function</h2>

> Enable stereo rendering

Defined in raylib.h:

```c
void rlEnableStereoRender() 
```

Python wrapper:

```python
def rlEnableStereoRender() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDisableStereoRender"><code>rlDisableStereoRender</code> function</h2>

> Disable stereo rendering

Defined in raylib.h:

```c
void rlDisableStereoRender() 
```

Python wrapper:

```python
def rlDisableStereoRender() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlIsStereoRenderEnabled"><code>rlIsStereoRenderEnabled</code> function</h2>

> Check if stereo render is enabled

Defined in raylib.h:

```c
bool rlIsStereoRenderEnabled() 
```

Python wrapper:

```python
def rlIsStereoRenderEnabled() -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlClearColor"><code>rlClearColor</code> function</h2>

> Clear color buffer with color

Defined in raylib.h:

```c
void rlClearColor(unsigned char r, unsigned char g, unsigned char b, unsigned char a) 
```

Python wrapper:

```python
def rlClearColor(r: int, g: int, b: int, a: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlClearScreenBuffers"><code>rlClearScreenBuffers</code> function</h2>

> Clear used screen buffers (color and depth)

Defined in raylib.h:

```c
void rlClearScreenBuffers() 
```

Python wrapper:

```python
def rlClearScreenBuffers() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlCheckErrors"><code>rlCheckErrors</code> function</h2>

> Check and log OpenGL error codes

Defined in raylib.h:

```c
void rlCheckErrors() 
```

Python wrapper:

```python
def rlCheckErrors() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetBlendMode"><code>rlSetBlendMode</code> function</h2>

> Set blending mode

Defined in raylib.h:

```c
void rlSetBlendMode(int mode) 
```

Python wrapper:

```python
def rlSetBlendMode(mode: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetBlendFactors"><code>rlSetBlendFactors</code> function</h2>

> Set blending mode factor and equation (using OpenGL factors)

Defined in raylib.h:

```c
void rlSetBlendFactors(int glSrcFactor, int glDstFactor, int glEquation) 
```

Python wrapper:

```python
def rlSetBlendFactors(glSrcFactor: int, glDstFactor: int, glEquation: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlglInit"><code>rlglInit</code> function</h2>

> Initialize rlgl (buffers, shaders, textures, states)

Defined in raylib.h:

```c
void rlglInit(int width, int height) 
```

Python wrapper:

```python
def rlglInit(width: int, height: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlglClose"><code>rlglClose</code> function</h2>

> De-inititialize rlgl (buffers, shaders, textures)

Defined in raylib.h:

```c
void rlglClose() 
```

Python wrapper:

```python
def rlglClose() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadExtensions"><code>rlLoadExtensions</code> function</h2>

> Load OpenGL extensions (loader function required)

Defined in raylib.h:

```c
void rlLoadExtensions(void loader) 
```

Python wrapper:

```python
def rlLoadExtensions(loader: bytes) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetVersion"><code>rlGetVersion</code> function</h2>

> Get current OpenGL version

Defined in raylib.h:

```c
int rlGetVersion() 
```

Python wrapper:

```python
def rlGetVersion() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetFramebufferWidth"><code>rlSetFramebufferWidth</code> function</h2>

> Set current framebuffer width

Defined in raylib.h:

```c
void rlSetFramebufferWidth(int width) 
```

Python wrapper:

```python
def rlSetFramebufferWidth(width: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetFramebufferWidth"><code>rlGetFramebufferWidth</code> function</h2>

> Get default framebuffer width

Defined in raylib.h:

```c
int rlGetFramebufferWidth() 
```

Python wrapper:

```python
def rlGetFramebufferWidth() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetFramebufferHeight"><code>rlSetFramebufferHeight</code> function</h2>

> Set current framebuffer height

Defined in raylib.h:

```c
void rlSetFramebufferHeight(int height) 
```

Python wrapper:

```python
def rlSetFramebufferHeight(height: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetFramebufferHeight"><code>rlGetFramebufferHeight</code> function</h2>

> Get default framebuffer height

Defined in raylib.h:

```c
int rlGetFramebufferHeight() 
```

Python wrapper:

```python
def rlGetFramebufferHeight() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetTextureIdDefault"><code>rlGetTextureIdDefault</code> function</h2>

> Get default texture id

Defined in raylib.h:

```c
unsigned int rlGetTextureIdDefault() 
```

Python wrapper:

```python
def rlGetTextureIdDefault() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetShaderIdDefault"><code>rlGetShaderIdDefault</code> function</h2>

> Get default shader id

Defined in raylib.h:

```c
unsigned int rlGetShaderIdDefault() 
```

Python wrapper:

```python
def rlGetShaderIdDefault() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetShaderLocsDefault"><code>rlGetShaderLocsDefault</code> function</h2>

> Get default shader locations

Defined in raylib.h:

```c
int rlGetShaderLocsDefault() 
```

Python wrapper:

```python
def rlGetShaderLocsDefault() -> Union[Seq[int], IntPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadRenderBatch"><code>rlLoadRenderBatch</code> function</h2>

> Load a render batch system

Defined in raylib.h:

```c
rlRenderBatch rlLoadRenderBatch(int numBuffers, int bufferElements) 
```

Python wrapper:

```python
def rlLoadRenderBatch(numBuffers: int, bufferElements: int) -> rlRenderBatch
```

See also:
<a href="#rlRenderBatch">rlRenderBatch</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlUnloadRenderBatch"><code>rlUnloadRenderBatch</code> function</h2>

> Unload render batch system

Defined in raylib.h:

```c
void rlUnloadRenderBatch(rlRenderBatch batch) 
```

Python wrapper:

```python
def rlUnloadRenderBatch(batch: rlRenderBatch) -> None
```

See also:
<a href="#rlRenderBatch">rlRenderBatch</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDrawRenderBatch"><code>rlDrawRenderBatch</code> function</h2>

> Draw render batch data (Update->Draw->Reset)

Defined in raylib.h:

```c
void rlDrawRenderBatch(rlRenderBatch * batch) 
```

Python wrapper:

```python
def rlDrawRenderBatch(batch: rlRenderBatchPtr) -> None
```

See also:
<a href="#rlRenderBatch">rlRenderBatch</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetRenderBatchActive"><code>rlSetRenderBatchActive</code> function</h2>

> Set the active render batch for rlgl (NULL for default internal)

Defined in raylib.h:

```c
void rlSetRenderBatchActive(rlRenderBatch * batch) 
```

Python wrapper:

```python
def rlSetRenderBatchActive(batch: rlRenderBatchPtr) -> None
```

See also:
<a href="#rlRenderBatch">rlRenderBatch</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDrawRenderBatchActive"><code>rlDrawRenderBatchActive</code> function</h2>

> Update and draw internal render batch

Defined in raylib.h:

```c
void rlDrawRenderBatchActive() 
```

Python wrapper:

```python
def rlDrawRenderBatchActive() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlCheckRenderBatchLimit"><code>rlCheckRenderBatchLimit</code> function</h2>

> Check internal buffer overflow for a given number of vertex

Defined in raylib.h:

```c
bool rlCheckRenderBatchLimit(int vCount) 
```

Python wrapper:

```python
def rlCheckRenderBatchLimit(vCount: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetTexture"><code>rlSetTexture</code> function</h2>

> Set current texture for render batch and check buffers limits

Defined in raylib.h:

```c
void rlSetTexture(unsigned int id) 
```

Python wrapper:

```python
def rlSetTexture(id: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadVertexArray"><code>rlLoadVertexArray</code> function</h2>

> Load vertex array (vao) if supported

Defined in raylib.h:

```c
unsigned int rlLoadVertexArray() 
```

Python wrapper:

```python
def rlLoadVertexArray() -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadVertexBuffer"><code>rlLoadVertexBuffer</code> function</h2>

> Load a vertex buffer attribute

Defined in raylib.h:

```c
unsigned int rlLoadVertexBuffer(void buffer, int size, bool dynamic) 
```

Python wrapper:

```python
def rlLoadVertexBuffer(buffer: bytes, size: int, dynamic: bool) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadVertexBufferElement"><code>rlLoadVertexBufferElement</code> function</h2>

> Load a new attributes element buffer

Defined in raylib.h:

```c
unsigned int rlLoadVertexBufferElement(void buffer, int size, bool dynamic) 
```

Python wrapper:

```python
def rlLoadVertexBufferElement(buffer: bytes, size: int, dynamic: bool) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlUpdateVertexBuffer"><code>rlUpdateVertexBuffer</code> function</h2>

> Update GPU buffer with new data

Defined in raylib.h:

```c
void rlUpdateVertexBuffer(unsigned int bufferId, void data, int dataSize, int offset) 
```

Python wrapper:

```python
def rlUpdateVertexBuffer(bufferId: int, data: bytes, dataSize: int, offset: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlUpdateVertexBufferElements"><code>rlUpdateVertexBufferElements</code> function</h2>

> Update vertex buffer elements with new data

Defined in raylib.h:

```c
void rlUpdateVertexBufferElements(unsigned int id, void data, int dataSize, int offset) 
```

Python wrapper:

```python
def rlUpdateVertexBufferElements(id: int, data: bytes, dataSize: int, offset: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlUnloadVertexArray"><code>rlUnloadVertexArray</code> function</h2>

> 

Defined in raylib.h:

```c
void rlUnloadVertexArray(unsigned int vaoId) 
```

Python wrapper:

```python
def rlUnloadVertexArray(vaoId: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlUnloadVertexBuffer"><code>rlUnloadVertexBuffer</code> function</h2>

> 

Defined in raylib.h:

```c
void rlUnloadVertexBuffer(unsigned int vboId) 
```

Python wrapper:

```python
def rlUnloadVertexBuffer(vboId: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetVertexAttribute"><code>rlSetVertexAttribute</code> function</h2>

> 

Defined in raylib.h:

```c
void rlSetVertexAttribute(unsigned int index, int compSize, int type, bool normalized, int stride, void pointer) 
```

Python wrapper:

```python
def rlSetVertexAttribute(index: int, compSize: int, type: int, normalized: bool, stride: int, pointer: bytes) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetVertexAttributeDivisor"><code>rlSetVertexAttributeDivisor</code> function</h2>

> 

Defined in raylib.h:

```c
void rlSetVertexAttributeDivisor(unsigned int index, int divisor) 
```

Python wrapper:

```python
def rlSetVertexAttributeDivisor(index: int, divisor: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetVertexAttributeDefault"><code>rlSetVertexAttributeDefault</code> function</h2>

> Set vertex attribute default value

Defined in raylib.h:

```c
void rlSetVertexAttributeDefault(int locIndex, void value, int attribType, int count) 
```

Python wrapper:

```python
def rlSetVertexAttributeDefault(locIndex: int, value: bytes, attribType: int, count: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDrawVertexArray"><code>rlDrawVertexArray</code> function</h2>

> 

Defined in raylib.h:

```c
void rlDrawVertexArray(int offset, int count) 
```

Python wrapper:

```python
def rlDrawVertexArray(offset: int, count: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDrawVertexArrayElements"><code>rlDrawVertexArrayElements</code> function</h2>

> 

Defined in raylib.h:

```c
void rlDrawVertexArrayElements(int offset, int count, void buffer) 
```

Python wrapper:

```python
def rlDrawVertexArrayElements(offset: int, count: int, buffer: bytes) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDrawVertexArrayInstanced"><code>rlDrawVertexArrayInstanced</code> function</h2>

> 

Defined in raylib.h:

```c
void rlDrawVertexArrayInstanced(int offset, int count, int instances) 
```

Python wrapper:

```python
def rlDrawVertexArrayInstanced(offset: int, count: int, instances: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlDrawVertexArrayElementsInstanced"><code>rlDrawVertexArrayElementsInstanced</code> function</h2>

> 

Defined in raylib.h:

```c
void rlDrawVertexArrayElementsInstanced(int offset, int count, void buffer, int instances) 
```

Python wrapper:

```python
def rlDrawVertexArrayElementsInstanced(offset: int, count: int, buffer: bytes, instances: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadTexture"><code>rlLoadTexture</code> function</h2>

> Load texture in GPU

Defined in raylib.h:

```c
unsigned int rlLoadTexture(void data, int width, int height, int format, int mipmapCount) 
```

Python wrapper:

```python
def rlLoadTexture(data: bytes, width: int, height: int, format: int, mipmapCount: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadTextureDepth"><code>rlLoadTextureDepth</code> function</h2>

> Load depth texture/renderbuffer (to be attached to fbo)

Defined in raylib.h:

```c
unsigned int rlLoadTextureDepth(int width, int height, bool useRenderBuffer) 
```

Python wrapper:

```python
def rlLoadTextureDepth(width: int, height: int, useRenderBuffer: bool) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadTextureCubemap"><code>rlLoadTextureCubemap</code> function</h2>

> Load texture cubemap

Defined in raylib.h:

```c
unsigned int rlLoadTextureCubemap(void data, int size, int format) 
```

Python wrapper:

```python
def rlLoadTextureCubemap(data: bytes, size: int, format: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlUpdateTexture"><code>rlUpdateTexture</code> function</h2>

> Update GPU texture with new data

Defined in raylib.h:

```c
void rlUpdateTexture(unsigned int id, int offsetX, int offsetY, int width, int height, int format, void data) 
```

Python wrapper:

```python
def rlUpdateTexture(id: int, offsetX: int, offsetY: int, width: int, height: int, format: int, data: bytes) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetGlTextureFormats"><code>rlGetGlTextureFormats</code> function</h2>

> Get OpenGL internal formats

Defined in raylib.h:

```c
void rlGetGlTextureFormats(int format, unsigned int glInternalFormat, unsigned int glFormat, unsigned int glType) 
```

Python wrapper:

```python
def rlGetGlTextureFormats(format: int, glInternalFormat: Union[Seq[int], UIntPtr], glFormat: Union[Seq[int], UIntPtr], glType: Union[Seq[int], UIntPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetPixelFormatName"><code>rlGetPixelFormatName</code> function</h2>

> Get name string for pixel format

Defined in raylib.h:

```c
char * rlGetPixelFormatName(unsigned int format) 
```

Python wrapper:

```python
def rlGetPixelFormatName(format: int) -> Union[str, CharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlUnloadTexture"><code>rlUnloadTexture</code> function</h2>

> Unload texture from GPU memory

Defined in raylib.h:

```c
void rlUnloadTexture(unsigned int id) 
```

Python wrapper:

```python
def rlUnloadTexture(id: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGenTextureMipmaps"><code>rlGenTextureMipmaps</code> function</h2>

> Generate mipmap data for selected texture

Defined in raylib.h:

```c
void rlGenTextureMipmaps(unsigned int id, int width, int height, int format, int mipmaps) 
```

Python wrapper:

```python
def rlGenTextureMipmaps(id: int, width: int, height: int, format: int, mipmaps: Union[Seq[int], IntPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlReadTexturePixels"><code>rlReadTexturePixels</code> function</h2>

> Read texture pixel data

Defined in raylib.h:

```c
void rlReadTexturePixels(unsigned int id, int width, int height, int format) 
```

Python wrapper:

```python
def rlReadTexturePixels(id: int, width: int, height: int, format: int) -> bytes
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlReadScreenPixels"><code>rlReadScreenPixels</code> function</h2>

> Read screen pixel data (color buffer)

Defined in raylib.h:

```c
unsigned char * rlReadScreenPixels(int width, int height) 
```

Python wrapper:

```python
def rlReadScreenPixels(width: int, height: int) -> Union[Seq[int], UCharPtr]
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadFramebuffer"><code>rlLoadFramebuffer</code> function</h2>

> Load an empty framebuffer

Defined in raylib.h:

```c
unsigned int rlLoadFramebuffer(int width, int height) 
```

Python wrapper:

```python
def rlLoadFramebuffer(width: int, height: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlFramebufferAttach"><code>rlFramebufferAttach</code> function</h2>

> Attach texture/renderbuffer to a framebuffer

Defined in raylib.h:

```c
void rlFramebufferAttach(unsigned int fboId, unsigned int texId, int attachType, int texType, int mipLevel) 
```

Python wrapper:

```python
def rlFramebufferAttach(fboId: int, texId: int, attachType: int, texType: int, mipLevel: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlFramebufferComplete"><code>rlFramebufferComplete</code> function</h2>

> Verify framebuffer is complete

Defined in raylib.h:

```c
bool rlFramebufferComplete(unsigned int id) 
```

Python wrapper:

```python
def rlFramebufferComplete(id: int) -> bool
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlUnloadFramebuffer"><code>rlUnloadFramebuffer</code> function</h2>

> Delete framebuffer from GPU

Defined in raylib.h:

```c
void rlUnloadFramebuffer(unsigned int id) 
```

Python wrapper:

```python
def rlUnloadFramebuffer(id: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadShaderCode"><code>rlLoadShaderCode</code> function</h2>

> Load shader from code strings

Defined in raylib.h:

```c
unsigned int rlLoadShaderCode(char * vsCode, char * fsCode) 
```

Python wrapper:

```python
def rlLoadShaderCode(vsCode: Union[str, CharPtr], fsCode: Union[str, CharPtr]) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlCompileShader"><code>rlCompileShader</code> function</h2>

> Compile custom shader and return shader id (type: RL_VERTEX_SHADER, RL_FRAGMENT_SHADER, RL_COMPUTE_SHADER)

Defined in raylib.h:

```c
unsigned int rlCompileShader(char * shaderCode, int type) 
```

Python wrapper:

```python
def rlCompileShader(shaderCode: Union[str, CharPtr], type: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadShaderProgram"><code>rlLoadShaderProgram</code> function</h2>

> Load custom shader program

Defined in raylib.h:

```c
unsigned int rlLoadShaderProgram(unsigned int vShaderId, unsigned int fShaderId) 
```

Python wrapper:

```python
def rlLoadShaderProgram(vShaderId: int, fShaderId: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlUnloadShaderProgram"><code>rlUnloadShaderProgram</code> function</h2>

> Unload shader program

Defined in raylib.h:

```c
void rlUnloadShaderProgram(unsigned int id) 
```

Python wrapper:

```python
def rlUnloadShaderProgram(id: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetLocationUniform"><code>rlGetLocationUniform</code> function</h2>

> Get shader location uniform

Defined in raylib.h:

```c
int rlGetLocationUniform(unsigned int shaderId, char * uniformName) 
```

Python wrapper:

```python
def rlGetLocationUniform(shaderId: int, uniformName: Union[str, CharPtr]) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetLocationAttrib"><code>rlGetLocationAttrib</code> function</h2>

> Get shader location attribute

Defined in raylib.h:

```c
int rlGetLocationAttrib(unsigned int shaderId, char * attribName) 
```

Python wrapper:

```python
def rlGetLocationAttrib(shaderId: int, attribName: Union[str, CharPtr]) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetUniform"><code>rlSetUniform</code> function</h2>

> Set shader value uniform

Defined in raylib.h:

```c
void rlSetUniform(int locIndex, void value, int uniformType, int count) 
```

Python wrapper:

```python
def rlSetUniform(locIndex: int, value: bytes, uniformType: int, count: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetUniformMatrix"><code>rlSetUniformMatrix</code> function</h2>

> Set shader value matrix

Defined in raylib.h:

```c
void rlSetUniformMatrix(int locIndex, Matrix mat) 
```

Python wrapper:

```python
def rlSetUniformMatrix(locIndex: int, mat: Matrix) -> None
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetUniformSampler"><code>rlSetUniformSampler</code> function</h2>

> Set shader value sampler

Defined in raylib.h:

```c
void rlSetUniformSampler(int locIndex, unsigned int textureId) 
```

Python wrapper:

```python
def rlSetUniformSampler(locIndex: int, textureId: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetShader"><code>rlSetShader</code> function</h2>

> Set shader currently active (id and locations)

Defined in raylib.h:

```c
void rlSetShader(unsigned int id, int locs) 
```

Python wrapper:

```python
def rlSetShader(id: int, locs: Union[Seq[int], IntPtr]) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadComputeShaderProgram"><code>rlLoadComputeShaderProgram</code> function</h2>

> Load compute shader program

Defined in raylib.h:

```c
unsigned int rlLoadComputeShaderProgram(unsigned int shaderId) 
```

Python wrapper:

```python
def rlLoadComputeShaderProgram(shaderId: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlComputeShaderDispatch"><code>rlComputeShaderDispatch</code> function</h2>

> Dispatch compute shader (equivalent to *draw* for graphics pilepine)

Defined in raylib.h:

```c
void rlComputeShaderDispatch(unsigned int groupX, unsigned int groupY, unsigned int groupZ) 
```

Python wrapper:

```python
def rlComputeShaderDispatch(groupX: int, groupY: int, groupZ: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadShaderBuffer"><code>rlLoadShaderBuffer</code> function</h2>

> Load shader storage buffer object (SSBO)

Defined in raylib.h:

```c
unsigned int rlLoadShaderBuffer(unsigned long long * size, void data, int usageHint) 
```

Python wrapper:

```python
def rlLoadShaderBuffer(size: int, data: bytes, usageHint: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlUnloadShaderBuffer"><code>rlUnloadShaderBuffer</code> function</h2>

> Unload shader storage buffer object (SSBO)

Defined in raylib.h:

```c
void rlUnloadShaderBuffer(unsigned int ssboId) 
```

Python wrapper:

```python
def rlUnloadShaderBuffer(ssboId: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlUpdateShaderBufferElements"><code>rlUpdateShaderBufferElements</code> function</h2>

> Update SSBO buffer data

Defined in raylib.h:

```c
void rlUpdateShaderBufferElements(unsigned int id, void data, unsigned long long * dataSize, unsigned long long * offset) 
```

Python wrapper:

```python
def rlUpdateShaderBufferElements(id: int, data: bytes, dataSize: int, offset: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetShaderBufferSize"><code>rlGetShaderBufferSize</code> function</h2>

> Get SSBO buffer size

Defined in raylib.h:

```c
unsigned long long * rlGetShaderBufferSize(unsigned int id) 
```

Python wrapper:

```python
def rlGetShaderBufferSize(id: int) -> int
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlReadShaderBufferElements"><code>rlReadShaderBufferElements</code> function</h2>

> Bind SSBO buffer

Defined in raylib.h:

```c
void rlReadShaderBufferElements(unsigned int id, void dest, unsigned long long * count, unsigned long long * offset) 
```

Python wrapper:

```python
def rlReadShaderBufferElements(id: int, dest: bytes, count: int, offset: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlBindShaderBuffer"><code>rlBindShaderBuffer</code> function</h2>

> Copy SSBO buffer data

Defined in raylib.h:

```c
void rlBindShaderBuffer(unsigned int id, unsigned int index) 
```

Python wrapper:

```python
def rlBindShaderBuffer(id: int, index: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlCopyBuffersElements"><code>rlCopyBuffersElements</code> function</h2>

> Copy SSBO buffer data

Defined in raylib.h:

```c
void rlCopyBuffersElements(unsigned int destId, unsigned int srcId, unsigned long long * destOffset, unsigned long long * srcOffset, unsigned long long * count) 
```

Python wrapper:

```python
def rlCopyBuffersElements(destId: int, srcId: int, destOffset: int, srcOffset: int, count: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlBindImageTexture"><code>rlBindImageTexture</code> function</h2>

> Bind image texture

Defined in raylib.h:

```c
void rlBindImageTexture(unsigned int id, unsigned int index, unsigned int format, int readonly) 
```

Python wrapper:

```python
def rlBindImageTexture(id: int, index: int, format: int, readonly: int) -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetMatrixModelview"><code>rlGetMatrixModelview</code> function</h2>

> Get internal modelview matrix

Defined in raylib.h:

```c
Matrix rlGetMatrixModelview() 
```

Python wrapper:

```python
def rlGetMatrixModelview() -> Matrix
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetMatrixProjection"><code>rlGetMatrixProjection</code> function</h2>

> Get internal projection matrix

Defined in raylib.h:

```c
Matrix rlGetMatrixProjection() 
```

Python wrapper:

```python
def rlGetMatrixProjection() -> Matrix
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetMatrixTransform"><code>rlGetMatrixTransform</code> function</h2>

> Get internal accumulated transform matrix

Defined in raylib.h:

```c
Matrix rlGetMatrixTransform() 
```

Python wrapper:

```python
def rlGetMatrixTransform() -> Matrix
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetMatrixProjectionStereo"><code>rlGetMatrixProjectionStereo</code> function</h2>

> Get internal projection matrix for stereo render (selected eye)

Defined in raylib.h:

```c
Matrix rlGetMatrixProjectionStereo(int eye) 
```

Python wrapper:

```python
def rlGetMatrixProjectionStereo(eye: int) -> Matrix
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlGetMatrixViewOffsetStereo"><code>rlGetMatrixViewOffsetStereo</code> function</h2>

> Get internal view offset matrix for stereo render (selected eye)

Defined in raylib.h:

```c
Matrix rlGetMatrixViewOffsetStereo(int eye) 
```

Python wrapper:

```python
def rlGetMatrixViewOffsetStereo(eye: int) -> Matrix
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetMatrixProjection"><code>rlSetMatrixProjection</code> function</h2>

> Set a custom projection matrix (replaces internal projection matrix)

Defined in raylib.h:

```c
void rlSetMatrixProjection(Matrix proj) 
```

Python wrapper:

```python
def rlSetMatrixProjection(proj: Matrix) -> None
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetMatrixModelview"><code>rlSetMatrixModelview</code> function</h2>

> Set a custom modelview matrix (replaces internal modelview matrix)

Defined in raylib.h:

```c
void rlSetMatrixModelview(Matrix view) 
```

Python wrapper:

```python
def rlSetMatrixModelview(view: Matrix) -> None
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetMatrixProjectionStereo"><code>rlSetMatrixProjectionStereo</code> function</h2>

> Set eyes projection matrices for stereo rendering

Defined in raylib.h:

```c
void rlSetMatrixProjectionStereo(Matrix right, Matrix left) 
```

Python wrapper:

```python
def rlSetMatrixProjectionStereo(right: Matrix, left: Matrix) -> None
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlSetMatrixViewOffsetStereo"><code>rlSetMatrixViewOffsetStereo</code> function</h2>

> Set eyes view offsets matrices for stereo rendering

Defined in raylib.h:

```c
void rlSetMatrixViewOffsetStereo(Matrix right, Matrix left) 
```

Python wrapper:

```python
def rlSetMatrixViewOffsetStereo(right: Matrix, left: Matrix) -> None
```

See also:
<a href="#Matrix">Matrix</a>

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadDrawCube"><code>rlLoadDrawCube</code> function</h2>

> Load and draw a cube

Defined in raylib.h:

```c
void rlLoadDrawCube() 
```

Python wrapper:

```python
def rlLoadDrawCube() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="rlLoadDrawQuad"><code>rlLoadDrawQuad</code> function</h2>

> Load and draw a quad

Defined in raylib.h:

```c
void rlLoadDrawQuad() 
```

Python wrapper:

```python
def rlLoadDrawQuad() -> None
```

[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
<h2 id="contexts">Context Managers</h2>

To use context managers, you can do like below:

```python
# this example shows a rendering step

with drawing():

    with texture_mode(minimap_texture):
        # render the minimap
        draw_line(2, 2, 5, 5, RED)
    # no texture mode after this line

    with mode2d(main_camera):
        # 2d drawing logic...
        draw_texture(minimap_texture, 10, 10, WHITE)
    # no mode 2d after this line
# no drawing after this line

```

Item|Item|Item|Item|Item
--------|--------|--------|--------|--------
<a href="#Drawing">Drawing</a> | <a href="#Mode2D">Mode2D</a> | <a href="#Mode3D">Mode3D</a> | <a href="#ScissorMode">ScissorMode</a> | <a href="#ShaderMode">ShaderMode</a>
<a href="#TextureMode">TextureMode</a> | <a href="#VrStereoMode">VrStereoMode</a>

[ <a href="#toc">ToC</a> ]

<h2 id="Drawing"><code>Drawing</code> context manager</h2>

> On entering the context: *Setup canvas (framebuffer) to start drawing*
> On leaving the context: *End canvas drawing and swap buffers (double buffering)*

```python
@contextmanager
def Drawing() -> None
```

[ <a href="#contexts">Contexts</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ScissorMode"><code>ScissorMode</code> context manager</h2>

> On entering the context: *Begin scissor mode (define screen area for following drawing)*
> On leaving the context: *End scissor mode*

```python
@contextmanager
def ScissorMode(x: 'int', y: 'int', width: 'int', height: 'int') -> None
```

[ <a href="#contexts">Contexts</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Mode2D"><code>Mode2D</code> context manager</h2>

> On entering the context: *Begin 2D mode with custom camera (2D)*
> On leaving the context: *Ends 2D mode with custom camera*

```python
@contextmanager
def Mode2D(camera: 'Camera2D') -> None
```

[ <a href="#contexts">Contexts</a> | <a href="#toc">ToC</a> ]

---
<h2 id="Mode3D"><code>Mode3D</code> context manager</h2>

> On entering the context: *Begin 3D mode with custom camera (3D)*
> On leaving the context: *Ends 3D mode and returns to default 2D orthographic mode*

```python
@contextmanager
def Mode3D(camera: 'Camera3D') -> None
```

[ <a href="#contexts">Contexts</a> | <a href="#toc">ToC</a> ]

---
<h2 id="ShaderMode"><code>ShaderMode</code> context manager</h2>

> On entering the context: *Begin custom shader drawing*
> On leaving the context: *End custom shader drawing (use default shader)*

```python
@contextmanager
def ShaderMode(shader: 'Shader') -> None
```

[ <a href="#contexts">Contexts</a> | <a href="#toc">ToC</a> ]

---
<h2 id="TextureMode"><code>TextureMode</code> context manager</h2>

> On entering the context: *Begin drawing to render texture*
> On leaving the context: *Ends drawing to render texture*

```python
@contextmanager
def TextureMode(target: 'RenderTexture2D') -> None
```

[ <a href="#contexts">Contexts</a> | <a href="#toc">ToC</a> ]

---
<h2 id="VrStereoMode"><code>VrStereoMode</code> context manager</h2>

> On entering the context: *Begin stereo rendering (requires VR simulator)*
> On leaving the context: *End stereo rendering (requires VR simulator)*

```python
@contextmanager
def VrStereoMode(config: 'VrStereoConfig') -> None
```

[ <a href="#contexts">Contexts</a> | <a href="#toc">ToC</a> ]

---
