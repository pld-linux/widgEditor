Summary:	widgEditor - WYSIWYG editor for simple content
Summary(pl.UTF-8):   widgEditor - edytor WYSIWYG dla prostej treści
Name:		widgEditor
# no version. use last changed date from sources.
%define	_snap 20050309
Version:	0.%{_snap}
Release:	1.0
Epoch:		0
License:	GPL
Group:		Applications/WWW
Source0:	http://www.themaninblue.com/experiment/widgEditor/widgEditor.zip
# Source0-md5:	3a9ef2cccaeea1302f0867d90f1a1be6
URL:		http://www.themaninblue.com/experiment/widgEditor/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
widgEditor is an easily installed, easily customisable WYSIWYG editor
for simple content. It replaces existing textareas with an improved
editing pane using JavaScript, therefore if you don't have JavaScript
(or your browser doesn't support HTML editing) it degrades gracefully.

%description -l pl.UTF-8
widgEditor to łatwy w instalacji i konfiguracji edytor WYSIWYG dla
prostej treści. Zastępuje istniejące pola textarea ulepszonym polem
edycyjnym używającym JavaScriptu - więc bez obsługi JavaScriptu (albo
jeśli przeglądarka nie obsługuje edycji HTML) wdzięcznie się
degraduje.

%prep
%setup -q -c
# undos the source
mv example.htm example.html
find . '(' -name '*.html' -o -name '*.css' -o -name '*.js' ')' -print0 | xargs -0 sed -i -e 's,
$,,'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -a css scripts images $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a example.html $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%{_datadir}/%{name}
