%ifarch %{ix86} %{arm}
%define _disable_ld_no_undefined 1
%endif

%global optflags %{optflags} -O3

%define debug_package %{nil}
%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

%define date 20200126

# Is this actually useful, given most people who use samba mount
# the shares anyway?
# Let's enable this (and the slew of dependencies it pulls) only
# if and when we find a real use case...
%bcond_with samba

Name:		mpv
Version:	0.33.1
Release:	1
Summary:	Movie player playing most video formats and DVDs
Group:		Video
License:	GPLv2+
URL:		http://mpv.io/
Source0:	https://github.com/mpv-player/mpv/archive/v%{version}/%{name}-%{version}.tar.gz
# latest stable waf
Source1:	https://waf.io/pub/release/waf-2.0.22
Source2:	mpv.conf
#Patch0:		mpv-0.23.0-dont-overreact-to-ffmpeg-mismatch.patch
# From Rockchip repos -- improves support for HW decoding support
# on Rockchip SoCs
Patch0:		https://github.com/rockchip-linux/mpv/commit/c696ef634f25daa0c499f1424f13e76631839f38.patch
Patch1:		https://github.com/rockchip-linux/mpv/commit/22c019f4f4a95c727b38dd1b05e70d3f49d429e1.patch

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
BuildRequires:	pkgconfig(xrandr)
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
BuildRequires:	pkgconfig(libiso9660)
BuildRequires:	pkgconfig(libudf)
BuildRequires:	pkgconfig(libva)
BuildRequires:	pkgconfig(libva-x11)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(sdl2)
%if %{with samba}
BuildRequires:	pkgconfig(smbclient)
Requires:	samba-libs
%endif
BuildRequires:	pkgconfig(vdpau)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(xv)
BuildRequires:	pkgconfig(xxf86vm)
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
BuildRequires:	krb5-devel
BuildRequires:	desktop-file-utils
BuildRequires:	imagemagick
BuildRequires:	python-docutils
BuildRequires:	kernel-release-headers
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
%{_mandir}/man1/%{name}.*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/encoding-profiles.conf
%config(noreplace) %{_sysconfdir}/%{name}/mpv.conf

#------------------------------------
%package -n %{libname}
Summary:	Library for %{name}
Group:		System/Libraries

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
%{_includedir}/%{name}/opengl_cb.h
%{_includedir}/%{name}/stream_cb.h
#{_includedir}/%{name}/qthelper.hpp
%{_includedir}/%{name}/render.h
%{_includedir}/%{name}/render_gl.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

#----------------------------------------------------------------------------

%prep
%autosetup -p1

cp %{SOURCE1} waf
chmod +x waf
if [ ! -x "$(pwd)/waf" ]; then
    echo "Missing waf. Exiting."
    exit 1
fi

%build
%ifarch %{ix86}
export CC=gcc
export CXX=g++
%endif
%set_build_flags
CCFLAGS="%{optflags}" \
python ./waf configure \
	--prefix="%{_prefix}" \
	--bindir="%{_bindir}" \
	--mandir="%{_mandir}" \
	--libdir="%{_libdir}" \
	--docdir="%{_docdir}/%{name}" \
	--confdir="%{_sysconfdir}/%{name}" \
	--enable-sdl2 \
	--disable-build-date \
	--disable-debug \
	--enable-openal \
	--enable-pulse \
	--enable-cdda \
	--enable-dvdnav \
	--enable-dvbin \
	--enable-wayland \
	--enable-gl-wayland \
	--enable-egl \
	--enable-egl-x11 \
	--enable-egl-drm \
	--enable-vaapi \
	--enable-libmpv-shared

python ./waf build --verbose

%install
python ./waf --destdir=%{buildroot} install

mkdir -p %{buildroot}%{_sysconfdir}/%{name}/
cp etc/encoding-profiles.conf %{buildroot}%{_sysconfdir}/%{name}/
cp %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}/mpv.conf

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
echo 'NoDisplay=true' >>%{buildroot}%{_datadir}/applications/%{name}.desktop
