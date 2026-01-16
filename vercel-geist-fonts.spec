Version:        1.6.0
Release:        1%{?dist}
URL:            https://vercel.com/font

%global foundry vercel
%global fontlicense OFL-1.1
%global fontlicenses geist-font-%{version}/OFL.txt
%global fontdocsex %{fontlicenses}

%global fontfamily0 Geist
%global fontsummary0 The Geist font family
%global fonts0 geist-font-%{version}/fonts/Geist/otf/*.otf
%global fontconfs0 %{SOURCE10}
%global fontdescription0 %{expand:Geist is a sans-serif typeface designed for
legibility and simplicity. It is a modern, geometric typeface that is based on
the principles of classic Swiss typography. It is designed to be used in
headlines, logos, posters, and other large display sizes.}

%global fontfamily1 Geist Mono
%global fontsummary1 The Geist Mono font family
%global fonts1 geist-font-%{version}/fonts/GeistMono/otf/*.otf
%global fontconfs1 %{SOURCE11}
%global fontdescription1 %{expand:Geist Mono is a monospaced typeface that has
been crafted to be the perfect partner to Geist Sans. It is designed to be used
in code editors, diagrams, terminals, and other textbased interfaces where code
is represented.}

Source0:        https://github.com/vercel/geist-font/releases/download/%{version}/geist-font-%{version}.zip
Source10:       63-vercel-geist.conf
Source11:       63-vercel-geist-mono.conf

%fontpkg -a

%prep
%autosetup -c

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a
%fontfiles -a

%changelog
* Thu Jan 16 2025 Basil Crow <me@basilcrow.com> - 1.6.0-1
- Initial packaging
