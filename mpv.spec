# debuginfo-without-sources 
# badness 50 WTF ???
%define debug_package	%{nil}

Name:           mpv
Version:        0.7.2
Release:        1
Summary:        Movie player playing most video formats and DVDs
Group:		Video
License:        GPLv2+
URL:            http://%{name}.io/
Source0:        https://github.com/%{name}-player/%{name}/archive/v%{version}.tar.gz
# latest stable waf
Source1:        http://ftp.waf.io/pub/release/waf-1.8.4
Patch0:         %{name}-config.patch


BuildRequires:  hicolor-icon-theme
BuildRequires:  ladspa-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  jpeg-devel
BuildRequires:  pkgconfig(libmng)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libquvi)
BuildRequires:  pkgconfig(libv4lconvert)
BuildRequires:  pkgconfig(liblircclient0)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(caca)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(dvdnav)
BuildRequires:  pkgconfig(dvdread)
BuildRequires:  pkgconfig(enca)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libbluray)
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcdio_cdda)
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(libiso9660)
BuildRequires:  pkgconfig(libudf)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  texlive-cmap
BuildRequires:  texlive-preprint
BuildRequires:  texlive-caption
BuildRequires:  texlive-latex
BuildRequires:  pkgconfig(libguess)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  krb5-devel
BuildRequires:  desktop-file-utils
BuildRequires:  imagemagick 
BuildRequires:	python-docutils

Requires:       hicolor-icon-theme

%description
Mpv is a movie player based on MPlayer and mplayer2. It supports a wide variety
of video file formats, audio and video codecs, and subtitle types. Special
input URL types are available to read input from a variety of sources other
than disk files. Depending on platform, a variety of different video and audio
output methods are supported.

%prep
%setup -q
%apply_patches

cp %{SOURCE1} waf
chmod 0755 waf

%build
CCFLAGS="%{optflags}" \
./waf configure \
    --prefix="%{_prefix}" \
    --bindir="%{_bindir}" \
    --mandir="%{_mandir}" \
    --docdir="%{_docdir}/%{name}" \
    --confdir="%{_sysconfdir}/%{name}" \
    --enable-joystick \
    --enable-lirc \
    --disable-sdl1 --disable-sdl2 \
    --disable-build-date \
    --disable-debug
    
./waf build --verbose 

%install
./waf --destdir=%{buildroot} install 

# Default config files
install -Dpm 644 etc/example.conf %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -Dpm 644 etc/input.conf %{buildroot}%{_sysconfdir}/%{name}/input.conf
desktop-file-install etc/mpv.desktop

for RES in 16 32 64; do
  install -Dpm 644 etc/mpv-icon-8bit-${RES}x${RES}.png %{buildroot}%{_datadir}/icons/hicolor/${RES}x${RES}/apps/%{name}.png
done

%files
%doc LICENSE README.md Copyright
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}.*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}/encoding-profiles.conf
%config(noreplace) %{_sysconfdir}/%{name}/input.conf



