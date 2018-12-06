# Run tests in check section
%bcond_without check

# https://github.com/gopherjs/gopherjs
%global goipath         github.com/gopherjs/gopherjs
%global commit          1babbf986f6fcb1156d0646cdba5c4f81bc32849

%global common_description %{expand:
GopherJS compiles Go code (golang.org) to pure JavaScript code. Its main 
purpose is to give you the opportunity to write front-end code in Go 
which will still run in all browsers.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Compiler from Go to JavaScript for running Go code in a browser 
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/fsnotify/fsnotify)
BuildRequires: golang(github.com/neelance/astrewrite)
BuildRequires: golang(github.com/neelance/sourcemap)
BuildRequires: golang(github.com/shurcooL/httpfs/filter)
BuildRequires: golang(github.com/shurcooL/httpfs/vfsutil)
BuildRequires: golang(golang.org/x/sys/unix)
BuildRequires: golang(golang.org/x/tools/go/buildutil)
BuildRequires: golang(golang.org/x/tools/go/gcexportdata)
BuildRequires: golang(golang.org/x/tools/go/types/typeutil)

%if %{with check}
BuildRequires: golang(github.com/kisielk/gotool)
BuildRequires: golang(github.com/shurcooL/go/importgraphutil)
%endif

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks -d build -d tests
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Oct 05 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20181005git1babbf9
- Bump to commit 1babbf986f6fcb1156d0646cdba5c4f81bc32849

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git8dffc02
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180628git8dffc02
- Bump to commit 8dffc02ea1cb8398bb73f30424697c60fcf8d4c5

* Mon Apr 23 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20180418gite14987c
- Unbootstrap

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180418gite14987c
- First package for Fedora

