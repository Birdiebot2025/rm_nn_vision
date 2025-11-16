// Copyright (C) 2024 Zheng Yu
// Licensed under the MIT License.

#include "buff_calculate.h"

#include <stdint.h>
#include <stdio.h>
#include <chrono>
#include "math.h"
#define PI 3.1415926

void calcuateBuffPostition(float xc, float yc, float zc, float theta,
                           int blade_id, float a, float b, float w,
                           uint64_t cap_timestamp, uint16_t t_offset,
                           float* target_x, float* target_y, float* target_z) 
{

    auto now = std::chrono::system_clock::now();
    auto duration = now.time_since_epoch();
    int64_t self_timestamp = std::chrono::duration_cast<std::chrono::milliseconds>(duration).count(); // ms

    float delay = 0.3; // s

    float r = 0.7;

    float t0 = (float)(cap_timestamp + t_offset) / 1000;
    float t1 = (float)(self_timestamp+ t_offset) / 1000 + delay;
    if (w == 0) 
    {
        theta += b * (t1 - t0);
    } else 
    {
        theta += a / w * (cos(w * t0) - cos(w * t1)) + b * (t1 - t0);
    }
        *target_x = xc + r * (sin(theta) * yc / sqrt(pow(xc, 2) + pow(yc, 2)));
        *target_y = yc + r * (-sin(theta) * xc / sqrt(pow(xc, 2) + pow(yc, 2)));
        *target_z = zc + r * cos(theta);
}

