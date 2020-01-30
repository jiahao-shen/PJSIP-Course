# build/os-auto.mak.  Generated from os-auto.mak.in by configure.

export OS_CFLAGS   := $(CC_DEF)PJ_AUTOCONF=1  -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -fPIC

export OS_CXXFLAGS := $(CC_DEF)PJ_AUTOCONF=1 -g -O2

export OS_LDFLAGS  :=   -lopus -lopenh264 -lstdc++ -lm -lpthread  -framework CoreAudio -framework CoreServices -framework AudioUnit -framework AudioToolbox -framework Foundation -framework AppKit -framework AVFoundation -framework CoreGraphics -framework QuartzCore -framework CoreVideo -framework CoreMedia -framework VideoToolbox -L/usr/local/lib -lSDL2  -L/usr/local/Cellar/ffmpeg/4.2.1_2/lib -lavdevice -lavformat -lavcodec -lswscale -lavutil -framework Security -lopencore-amrnb -lopencore-amrwb

export OS_SOURCES  := 


