#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-plexus-i18n
Version  : 1.0.beta.10
Release  : 3
URL      : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-i18n/1.0-beta-10/plexus-i18n-1.0-beta-10.jar
Source0  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-i18n/1.0-beta-10/plexus-i18n-1.0-beta-10.jar
Source1  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-i18n/1.0-beta-10/plexus-i18n-1.0-beta-10.pom
Source2  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-i18n/1.0-beta-6/plexus-i18n-1.0-beta-6.jar
Source3  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-i18n/1.0-beta-6/plexus-i18n-1.0-beta-6.pom
Source4  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-i18n/1.0-beta-7/plexus-i18n-1.0-beta-7.jar
Source5  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-i18n/1.0-beta-7/plexus-i18n-1.0-beta-7.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-plexus-i18n-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-plexus-i18n package.
Group: Data

%description data
data components for the mvn-plexus-i18n package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-i18n/1.0-beta-10
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-i18n/1.0-beta-10

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-i18n/1.0-beta-10
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-i18n/1.0-beta-10

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-i18n/1.0-beta-6
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-i18n/1.0-beta-6

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-i18n/1.0-beta-6
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-i18n/1.0-beta-6

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-i18n/1.0-beta-7
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-i18n/1.0-beta-7

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-i18n/1.0-beta-7
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-i18n/1.0-beta-7


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-i18n/1.0-beta-10/plexus-i18n-1.0-beta-10.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-i18n/1.0-beta-10/plexus-i18n-1.0-beta-10.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-i18n/1.0-beta-6/plexus-i18n-1.0-beta-6.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-i18n/1.0-beta-6/plexus-i18n-1.0-beta-6.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-i18n/1.0-beta-7/plexus-i18n-1.0-beta-7.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-i18n/1.0-beta-7/plexus-i18n-1.0-beta-7.pom
