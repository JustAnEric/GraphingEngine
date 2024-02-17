#version 330 core

layout (location = 0) in vec2 in_tex_coord_0;
layout (location = 1) in vec3 in_position;

uniform mat4 m_proj;
uniform mat4 m_view;
uniform mat4 m_model;
uniform uint mode_id;

const vec3 marker_colors[2] = vec3[2](
    /*vec3(0.48, 0.48, 0.48),*/ vec3(1.00, 0.00, 0.00),
    vec3(0, 0.28, 0.28)
);

out vec3 marker_color;
out vec2 uv;


void main() {
    uv = in_tex_coord_0;
    marker_color = marker_colors[mode_id];
    gl_Position = m_proj * m_view * m_model * vec4((in_position - 0.5) * 1.01 + 0.5, 1.0);
}