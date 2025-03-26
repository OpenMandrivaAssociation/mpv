%ifarch %{ix86} %{arm}
%define _disable_ld_no_undefined 1
%endif

%global optflags %{optflags} -O3

%define major 2
%define oldlibname %mklibname %{name} 2
%define libname %mklibname %{name}
%define devname %mklibname %{name} -d

%define date 20200126

# Is this actually useful, given most people who use samba mount
# the shares anyway?
# Let's enable this (and the slew of dependencies it pulls) only
# if and when we find a real use case...
%bcond_with samba

Name:		mpv
Version:	0.40.0
Release:	1
Summary:	Movie player playing most video formats and DVDs
Group:		Video
License:	GPLv2+
URL:		https://mpv.io/
Source0:	https://github.com/mpv-player/mpv/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	mpv.conf
#Patch0:		mpv-0.23.0-dont-overreact-to-ffmpeg-mismatch.patch
# From Rockchip repos -- improves support for HW decoding support
# on Rockchip SoCs
Patch0:		https://github.com/rockchip-linux/mpv/commit/c696ef634f25daa0c499f1424f13e76631839f38.patch
# FIXME needs porting to 0.37.0
#Patch1:		https://github.com/rockchip-linux/mpv/commit/22c019f4f4a95c727b38dd1b05e70d3f49d429e1.patch

BuildRequires:	hicolor-icon-theme
BuildRequires:	ladspa-devel
BuildRequires:	pkgconfig(libavutil) >= 56.6.100
BuildRequires:	pkgconfig(libavcodec) >= 58.7.100
BuildRequires:	pkgconfig(libavformat) >= 58.0.102
BuildRequires:	pkgconfig(libswscale) >= 5.0.101
BuildRequires:	pkgconfig(libavfilter) >= 7.0.101
BuildRequires:	pkgconfig(libswresample) >= 3.0.100
BuildRequires:	pkgconfig(ffnvcodec)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libmng)
BuildRequires:	pkgconfig(libmpg123)
BuildRequires:	pkgconfig(libquvi)
BuildRequires:	pkgconfig(libv4lconvert)
BuildRequires:	pkgconfig(liblircclient0)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	perl
# Mujs is broken in i686: libmujs.a: error adding symbols: file format not recognized
%ifnarch %{ix86}
BuildRequires:	pkgconfig(mujs)
%endif
BuildRequires:	pkgconfig(gbm)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(caca)
BuildRequires:	pkgconfig(dri)
BuildRequires:	pkgconfig(dvdnav)
BuildRequires:	pkgconfig(dvdread)
BuildRequires:	pkgconfig(enca)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libass)
BuildRequires:	pkgconfig(libbluray)
BuildRequires:	pkgconfig(libbs2b)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(libcdio_cdda)
BuildRequires:	pkgconfig(libcdio_paranoia)
BuildRequires:	pkgconfig(libdisplay-info)
BuildRequires:	pkgconfig(libiso9660)
BuildRequires:	pkgconfig(libpipewire-0.3)
BuildRequires:	pkgconfig(libplacebo) >= 6.338.0
BuildRequires:	pkgconfig(libudf)
BuildRequires:	pkgconfig(libva)
BuildRequires:	pkgconfig(libva-x11)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(sndio)
BuildRequires:	pkgconfig(shaderc)
%if %{with samba}
BuildRequires:	pkgconfig(smbclient)
Requires:	samba-libs
%endif
BuildRequires:	pkgconfig(rubberband)
BuildRequires:	pkgconfig(uchardet)
BuildRequires:	pkgconfig(vapoursynth)
BuildRequires:	pkgconfig(vdpau)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xpresent)
BuildRequires:	pkgconfig(xv)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(luajit)
BuildRequires:	texlive-cmap
BuildRequires:	texlive-preprint
BuildRequires:	texlive-caption
BuildRequires:	texlive-latex
BuildRequires:	pkgconfig(dvdread)
BuildRequires:	pkgconfig(dvdnav)
BuildRequires:	pkgconfig(libguess)
BuildRequires:	pkgconfig(libva-wayland)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-cursor)
BuildRequires:	pkgconfig(wayland-scanner)
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(vulkan)
BuildRequires:	pkgconfig(zimg)
BuildRequires:	krb5-devel
BuildRequires:	desktop-file-utils
BuildRequires:	imagemagick
BuildRequires:	python-docutils
BuildRequires:	meson
BuildRequires:	ninja
#BuildRequires:	kernel-release-headers
Requires:	hicolor-icon-theme
Suggests:	youtube-dl >= 2015.01.16

%description
Mpv is a movie player based on MPlayer and mplayer2. It supports a wide variety
of video file formats, audio and video codecs, and subtitle types. Special
input URL types are available to read input from a variety of sources other
than disk files. Depending on platform, a variety of different video and audio
output methods are supported.

%files
%doc README.md Copyright etc/input.conf
%{_docdir}/%{name}/mplayer-input.conf
%{_docdir}/%{name}/mpv.conf
%{_docdir}/%{name}/restore-old-bindings.conf
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/icons/hicolor/symbolic/apps/mpv-symbolic.svg
%{_datadir}/zsh/site-functions/_mpv
%{_datadir}/bash-completion/completions/mpv
%{_datadir}/fish/vendor_completions.d/mpv.fish
%{_datadir}/metainfo/mpv.metainfo.xml
%{_datadir}/doc/mpv/restore-osc-bindings.conf
%{_mandir}/man1/%{name}.*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/encoding-profiles.conf
%config(noreplace) %{_sysconfdir}/%{name}/mpv.conf

#------------------------------------
%package -n %{libname}
Summary:	Library for %{name}
Group:		System/Libraries
%rename %{oldlibname}

%description -n %{libname}
Mpv is a movie player based on MPlayer and mplayer2. It supports a wide variety
of video file formats, audio and video codecs, and subtitle types. Special
input URL types are available to read input from a variety of sources other
than disk files. Depending on platform, a variety of different video and audio
output methods are supported.

%files -n %{libname}
%doc README.md Copyright
%{_libdir}/*.so.%{major}*

#------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Mpv is a movie player based on MPlayer and mplayer2. It supports a wide variety
of video file formats, audio and video codecs, and subtitle types. Special
input URL types are available to read input from a variety of sources other
than disk files. Depending on platform, a variety of different video and audio
output methods are supported.

%files -n %{devname}
%doc README.md Copyright
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/client.h
%{_includedir}/%{name}/stream_cb.h
%{_includedir}/%{name}/render.h
%{_includedir}/%{name}/render_gl.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

#----------------------------------------------------------------------------

%prep
%autosetup -p1

# Workaround for using a #define that isn't being set anywhere
sed -i -e 's,#if HAVE_JPEGXL,#if 1,g' video/image_writer.c

%meson \
	-Dlibmpv=true \
	-Dcdda=enabled \
	-Ddvbin=enabled \
	-Ddvdnav=enabled \
	-Drubberband=enabled \
	-Dsdl2=enabled \
 	-Dsdl2-gamepad=enabled \
  	-Dsdl2-audio=enabled \
	-Dopenal=enabled \
	-Dgl-x11=enabled \
	-Dwin32-threads=disabled \
	-Dcocoa=disabled \
	-Dgl-cocoa=disabled \
	-Dmacos-cocoa-cb=disabled \
	-Dmacos-media-player=disabled \
	-Dmacos-touchbar=disabled \
	-Daudiounit=disabled \
	-Dcoreaudio=disabled \
	-Dopensles=disabled \
	-Doss-audio=disabled \
	-Dwasapi=disabled \
	-Dgl-win32=disabled \
	-Ddirect3d=disabled \
	-Dd3d-hwaccel=disabled \
	-Dd3d9-hwaccel=disabled \
	-Dd3d11=disabled \
	-Dgl-dxinterop-d3d9=disabled \
	-Dgl-dxinterop=disabled \
	-Dsixel=disabled \
	-Dspirv-cross=disabled \
 	-Dshaderc=disabled \
	-Degl-angle=disabled \
	-Degl-angle-lib=disabled \
	-Degl-angle-win32=disabled \
	-Degl-android=disabled \
	-Dandroid-media-ndk=disabled \
	-Dios-gl=disabled \
	-Dvideotoolbox-pl=disabled \
	-Dvideotoolbox-gl=disabled \
	-Davfoundation=disabled \
	-Dvaapi-win32=disabled \
	-Dswift-build=disabled \
 	-Dmacos-10-15-4-features=disabled \
  	-Dmacos-11-features=disabled \
   	-Dmacos-11-3-features=disabled \
    	-Dmacos-12-features=disabled \
     	-Dmacos-cocoa-cb=disabled \
      	-Dmacos-media-player=disabled \
       	-Dmacos-touchbar=disabled

%build
%meson_build

%install
%meson_install

mkdir -p %{buildroot}%{_sysconfdir}/%{name}/
cp etc/encoding-profiles.conf %{buildroot}%{_sysconfdir}/%{name}/
cp %{S:1} %{buildroot}%{_sysconfdir}/%{name}/mpv.conf

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
