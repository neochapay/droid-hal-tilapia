# These and other macros are documented in dhd/droid-hal-device.inc
%define device tilapia
%define vendor asus
%define vendor_pretty ASUS
%define device_pretty Nexus 7 GSM (2012)
%define installable_zip 1

%define straggler_files \
/selinux_version \
/service_contexts \
%{nil}

%include rpm/dhd/droid-hal-device.inc
