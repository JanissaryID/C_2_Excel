
/******************************************************************************************************

          Project Name : PLD32TV1855
          MCU Type  : MSD3663LWA
          Setting Version  : 3.6 (PreVolume)
          Modify by : Haris
          Filename  : C:\Users\user\Downloads\newsound_setting_default.c
          09-02-2021,12:23
          Note  : 


******************************************************************************************************/

/******************************************************************************************************

SETTING PRESCALE

******************************************************************************************************/

#define DEFAULT_PRESCALE_0dB   0x6f

//============>MAINSPEAKER<=====================
#define DEFAULT_PRESCALE_MAINSPEAKER_DTV   0x30
#define DEFAULT_PRESCALE_MAINSPEAKER_ATV   0x5F
#define DEFAULT_PRESCALE_MAINSPEAKER_AV   0x42
#define DEFAULT_PRESCALE_MAINSPEAKER_AV2   0x42
#define DEFAULT_PRESCALE_MAINSPEAKER_YPBPR   0x42
#define DEFAULT_PRESCALE_MAINSPEAKER_VGA   0x0E
#define DEFAULT_PRESCALE_MAINSPEAKER_HDMI   0x30
#define DEFAULT_PRESCALE_MAINSPEAKER_HDMI2   0x30
#define DEFAULT_PRESCALE_MAINSPEAKER_HDMI3   0x30
#define DEFAULT_PRESCALE_MAINSPEAKER_HDMI4   0x30
#define DEFAULT_PRESCALE_MAINSPEAKER_USB   0x4E
#define DEFAULT_PRESCALE_MAINSPEAKER_SV   0x30
#define DEFAULT_PRESCALE_MAINSPEAKER_SCART   0x42
#define DEFAULT_PRESCALE_MAINSPEAKER_STV   0x30

//============>LINEOUT_LO<=====================
#define DEFAULT_PRESCALE_LINEOUT_LO_DTV   0x09
#define DEFAULT_PRESCALE_LINEOUT_LO_ATV   0x09
#define DEFAULT_PRESCALE_LINEOUT_LO_AV   0x09
#define DEFAULT_PRESCALE_LINEOUT_LO_AV2   0x09
#define DEFAULT_PRESCALE_LINEOUT_LO_YPBPR   0x09
#define DEFAULT_PRESCALE_LINEOUT_LO_VGA   0x09
#define DEFAULT_PRESCALE_LINEOUT_LO_HDMI   0x09
#define DEFAULT_PRESCALE_LINEOUT_LO_HDMI2   0x09
#define DEFAULT_PRESCALE_LINEOUT_LO_HDMI3   0x09
#define DEFAULT_PRESCALE_LINEOUT_LO_HDMI4   0x09
#define DEFAULT_PRESCALE_LINEOUT_LO_USB   0x09
#define DEFAULT_PRESCALE_LINEOUT_LO_SV   0x09
#define DEFAULT_PRESCALE_LINEOUT_LO_SCART   0x09
#define DEFAULT_PRESCALE_LINEOUT_LO_STV   0x09

//============>LINEOUT_HI<=====================
#define DEFAULT_PRESCALE_LINEOUT_HI_DTV   0xD2E
#define DEFAULT_PRESCALE_LINEOUT_HI_ATV   0xA05
#define DEFAULT_PRESCALE_LINEOUT_HI_AV   0xC7A
#define DEFAULT_PRESCALE_LINEOUT_HI_AV2   0xC7A
#define DEFAULT_PRESCALE_LINEOUT_HI_YPBPR   0xC7A
#define DEFAULT_PRESCALE_LINEOUT_HI_VGA   0xC7A
#define DEFAULT_PRESCALE_LINEOUT_HI_HDMI   0xD2E
#define DEFAULT_PRESCALE_LINEOUT_HI_HDMI2   0xD2E
#define DEFAULT_PRESCALE_LINEOUT_HI_HDMI3   0xD2E
#define DEFAULT_PRESCALE_LINEOUT_HI_HDMI4   0xD2E
#define DEFAULT_PRESCALE_LINEOUT_HI_USB   0xD40
#define DEFAULT_PRESCALE_LINEOUT_HI_SV   0xD40
#define DEFAULT_PRESCALE_LINEOUT_HI_SCART   0xC7A
#define DEFAULT_PRESCALE_LINEOUT_HI_STV   0xD2E

/******************************************************************************************************

SETTING EQUALIZER

******************************************************************************************************/

//============>MUSIC<=====================
#define MUSIC_120HZ   100
#define MUSIC_500HZ   95
#define MUSIC_1_5KHZ   90
#define MUSIC_5KHZ   95
#define MUSIC_10KHZ   100
#define MUSIC_TREBLE   90
#define MUSIC_BASS   95

//============>NEWS<=====================
#define NEWS_120HZ   55
#define NEWS_500HZ   75
#define NEWS_1_5KHZ   90
#define NEWS_5KHZ   90
#define NEWS_10KHZ   95
#define NEWS_TREBLE   90
#define NEWS_BASS   95

//============>SPORTS<=====================
#define SPORTS_120HZ   75
#define SPORTS_500HZ   75
#define SPORTS_1_5KHZ   70
#define SPORTS_5KHZ   85
#define SPORTS_10KHZ   100
#define SPORTS_TREBLE   90
#define SPORTS_BASS   95

//============>STANDARD<=====================
#define STANDARD_120HZ   60
#define STANDARD_500HZ   60
#define STANDARD_1_5KHZ   60
#define STANDARD_5KHZ   60
#define STANDARD_10KHZ   60
#define STANDARD_TREBLE   90
#define STANDARD_BASS   95

//============>USER<=====================
#define USER_120HZ   100
#define USER_500HZ   95
#define USER_1_5KHZ   70
#define USER_5KHZ   95
#define USER_10KHZ   100
#define USER_TREBLE   90
#define USER_BASS   95

/******************************************************************************************************

SETTING VOLUME NONLINEAR

******************************************************************************************************/

#define VOL_NONLINEAR_DTV      { 0,40,70,75,100, }
#define VOL_NONLINEAR_ATV      { 0,40,70,75,100, }
#define VOL_NONLINEAR_AV      { 0,40,70,75,100, }
#define VOL_NONLINEAR_AV2      { 0,40,70,75,100, }
#define VOL_NONLINEAR_HDMI      { 0,40,70,75,100, }
#define VOL_NONLINEAR_HDMI2      { 0,40,70,75,100, }
#define VOL_NONLINEAR_HDMI3      { 0,40,70,75,100, }
#define VOL_NONLINEAR_HDMI4      { 0,40,70,75,100, }
#define VOL_NONLINEAR_USB      { 0,62,63,75,85, }

/******************************************************************************************************

SETTING EQUALIZER NONLINEAR

******************************************************************************************************/

//============>DTV<=====================
#define EQ_NONLINEAR_DTV_120HZ      { 0,25,50,75,100 }
#define EQ_NONLINEAR_DTV_500HZ      { 0,35,60,85,100 }
#define EQ_NONLINEAR_DTV_1_5KHZ      { 0,35,60,85,100 }
#define EQ_NONLINEAR_DTV_5KHZ      { 0,40,65,90,100 }
#define EQ_NONLINEAR_DTV_10KHZ      { 0,25,50,75,100 }

//============>ATV<=====================
#define EQ_NONLINEAR_ATV_120HZ      { 0,25,50,75,100 }
#define EQ_NONLINEAR_ATV_500HZ      { 0,40,65,90,100 }
#define EQ_NONLINEAR_ATV_1_5KHZ      { 0,40,65,90,100 }
#define EQ_NONLINEAR_ATV_5KHZ      { 0,40,65,90,100 }
#define EQ_NONLINEAR_ATV_10KHZ      { 0,25,50,75,100 }

//============>AV<=====================
#define EQ_NONLINEAR_AV_120HZ      { 0,25,50,75,100 }
#define EQ_NONLINEAR_AV_500HZ      { 0,40,65,90,100 }
#define EQ_NONLINEAR_AV_1_5KHZ      { 0,35,60,85,100 }
#define EQ_NONLINEAR_AV_5KHZ      { 0,40,65,90,100 }
#define EQ_NONLINEAR_AV_10KHZ      { 0,25,50,75,100 }

//============>AV2<=====================
#define EQ_NONLINEAR_AV2_120HZ      { 0,25,50,75,100 }
#define EQ_NONLINEAR_AV2_500HZ      { 0,40,65,90,100 }
#define EQ_NONLINEAR_AV2_1_5KHZ      { 0,35,60,85,100 }
#define EQ_NONLINEAR_AV2_5KHZ      { 0,40,65,90,100 }
#define EQ_NONLINEAR_AV2_10KHZ      { 0,25,50,75,100 }

//============>YPBPR<=====================
#define EQ_NONLINEAR_YPBPR_120HZ      { 0,25,50,75,100 }
#define EQ_NONLINEAR_YPBPR_500HZ      { 0,40,65,90,100 }
#define EQ_NONLINEAR_YPBPR_1_5KHZ      { 0,35,60,85,100 }
#define EQ_NONLINEAR_YPBPR_5KHZ      { 0,40,65,90,100 }
#define EQ_NONLINEAR_YPBPR_10KHZ      { 0,25,50,75,100 }

//============>VGA<=====================
#define EQ_NONLINEAR_VGA_120HZ      { 0,25,50,75,100 }
#define EQ_NONLINEAR_VGA_500HZ      { 0,40,65,90,100 }
#define EQ_NONLINEAR_VGA_1_5KHZ      { 0,35,60,85,100 }
#define EQ_NONLINEAR_VGA_5KHZ      { 0,40,65,90,100 }
#define EQ_NONLINEAR_VGA_10KHZ      { 0,25,50,75,100 }

//============>HDMI<=====================
#define EQ_NONLINEAR_HDMI_120HZ      { 0,25,50,75,100 }
#define EQ_NONLINEAR_HDMI_500HZ      { 0,35,60,85,100 }
#define EQ_NONLINEAR_HDMI_1_5KHZ      { 0,35,60,85,100 }
#define EQ_NONLINEAR_HDMI_5KHZ      { 0,40,65,90,100 }
#define EQ_NONLINEAR_HDMI_10KHZ      { 0,25,50,75,100 }

//============>HDMI2<=====================
#define EQ_NONLINEAR_HDMI2_120HZ      { 0,25,50,75,100 }
#define EQ_NONLINEAR_HDMI2_500HZ      { 0,35,60,85,100 }
#define EQ_NONLINEAR_HDMI2_1_5KHZ      { 0,35,60,85,100 }
#define EQ_NONLINEAR_HDMI2_5KHZ      { 0,40,65,90,100 }
#define EQ_NONLINEAR_HDMI2_10KHZ      { 0,25,50,75,100 }

//============>HDMI3<=====================
#define EQ_NONLINEAR_HDMI3_120HZ      { 0,25,50,75,100 }
#define EQ_NONLINEAR_HDMI3_500HZ      { 0,35,60,85,100 }
#define EQ_NONLINEAR_HDMI3_1_5KHZ      { 0,35,60,85,100 }
#define EQ_NONLINEAR_HDMI3_5KHZ      { 0,40,65,90,100 }
#define EQ_NONLINEAR_HDMI3_10KHZ      { 0,25,50,75,100 }

//============>HDMI4<=====================
#define EQ_NONLINEAR_HDMI4_120HZ      { 0,25,50,75,100 }
#define EQ_NONLINEAR_HDMI4_500HZ      { 0,35,60,85,100 }
#define EQ_NONLINEAR_HDMI4_1_5KHZ      { 0,35,60,85,100 }
#define EQ_NONLINEAR_HDMI4_5KHZ      { 0,40,65,90,100 }
#define EQ_NONLINEAR_HDMI4_10KHZ      { 0,25,50,75,100 }

//============>USB<=====================
#define EQ_NONLINEAR_USB_120HZ      { 0,25,50,75,93 }
#define EQ_NONLINEAR_USB_500HZ      { 0,40,65,90,100 }
#define EQ_NONLINEAR_USB_1_5KHZ      { 0,40,65,90,100 }
#define EQ_NONLINEAR_USB_5KHZ      { 0,40,65,90,100 }
#define EQ_NONLINEAR_USB_10KHZ      { 0,25,50,75,100 }

//============>SV<=====================
#define EQ_NONLINEAR_SV_120HZ      { 0,35,55,70,80 }
#define EQ_NONLINEAR_SV_500HZ      { 0,35,50,60,70 }
#define EQ_NONLINEAR_SV_1_5KHZ      { 0,45,70,80,90 }
#define EQ_NONLINEAR_SV_5KHZ      { 0,40,60,85,100 }
#define EQ_NONLINEAR_SV_10KHZ      { 0,25,50,75,100 }

//============>SCART<=====================
#define EQ_NONLINEAR_SCART_120HZ      { 0,40,70,85,90 }
#define EQ_NONLINEAR_SCART_500HZ      { 0,40,50,65,75 }
#define EQ_NONLINEAR_SCART_1_5KHZ      { 0,40,60,80,100 }
#define EQ_NONLINEAR_SCART_5KHZ      { 0,50,75,90,100 }
#define EQ_NONLINEAR_SCART_10KHZ      { 0,25,50,75,100 }

//============>STV<=====================
#define EQ_NONLINEAR_STV_120HZ      { 0,25,50,75,100 }
#define EQ_NONLINEAR_STV_500HZ      { 0,35,60,85,100 }
#define EQ_NONLINEAR_STV_1_5KHZ      { 0,35,60,85,100 }
#define EQ_NONLINEAR_STV_5KHZ      { 0,40,65,90,100 }
#define EQ_NONLINEAR_STV_10KHZ      { 0,25,50,75,100 }


/******************************************************************************************************

SETTING DRC

******************************************************************************************************/

#define DEFAULT_DRC_ENABLE      0
#define DEFAULT_DRC_THRESHOLD      0x05
/******************************************************************************************************

SETTING AVC THRESHOLD

******************************************************************************************************/

#define DEFAULT_AVC_THRESHOLD_DTV      0x37
#define DEFAULT_AVC_THRESHOLD_ATV      0x35
#define DEFAULT_AVC_THRESHOLD_AV      0x36
#define DEFAULT_AVC_THRESHOLD_AV2      0x36
#define DEFAULT_AVC_THRESHOLD_YPBPR      0x36
#define DEFAULT_AVC_THRESHOLD_VGA      0x10
#define DEFAULT_AVC_THRESHOLD_HDMI      0x37
#define DEFAULT_AVC_THRESHOLD_HDMI2      0x37
#define DEFAULT_AVC_THRESHOLD_HDMI3      0x37
#define DEFAULT_AVC_THRESHOLD_HDMI4      0x37
#define DEFAULT_AVC_THRESHOLD_USB      0x36
#define DEFAULT_AVC_THRESHOLD_SV      0x37
#define DEFAULT_AVC_THRESHOLD_SCART      0x36
#define DEFAULT_AVC_THRESHOLD_STV      0x37

/******************************************************************************************************

SETTING AVL

******************************************************************************************************/

#define DEFAULT_AVL_DTV      0x41
#define DEFAULT_AVL_ATV      0x3B
#define DEFAULT_AVL_AV1      0x41
#define DEFAULT_AVL_AV2      0x41
#define DEFAULT_AVL_AV3      0x41
#define DEFAULT_AVL_YPBPR1      0x15
#define DEFAULT_AVL_YPBPR2      0x41
#define DEFAULT_AVL_VGA      0x41
#define DEFAULT_AVL_HDMI1      0x41
#define DEFAULT_AVL_HDMI2      0x41
#define DEFAULT_AVL_HDMI3      0x41
#define DEFAULT_AVL_HDMI4      0x41
#define DEFAULT_AVL_USB      0x3B
#define DEFAULT_AVL_STV      0x41

/******************************************************************************************************

VOLUME TABLE

******************************************************************************************************/

U16 DTVVolumeTable[]= { 
0x7F00,  
0x4700,  0x4400,  0x4100,  0x3E00,  0x3C00,  0x3A00,  0x3800,  0x3600,  0x3400,  0x3200,  
0x3000,  0x2E00,  0x2D00,  0x2C00,  0x2B00,  0x2A00,  0x2900,  0x2800,  0x2700,  0x2600,  
0x2500,  0x2400,  0x2300,  0x2200,  0x2100,  0x2000,  0x1F00,  0x1E04,  0x1E00,  0x1D04,  
0x1D00,  0x1C04,  0x1C00,  0x1B04,  0x1B00,  0x1A04,  0x1A00,  0x1904,  0x1900,  0x1804,  
0x1800,  0x1704,  0x1700,  0x1604,  0x1600,  0x1504,  0x1502,  0x1500,  0x1406,  0x1404,  
0x1402,  0x1400,  0x1306,  0x1304,  0x1302,  0x1300,  0x1206,  0x1204,  0x1202,  0x1200,  
0x1106,  0x1104,  0x1102,  0x1100,  0x1006,  0x1004,  0x1002,  0x1000,  0x0F07,  0x0F06,  
0x0F05,  0x0F04,  0x0F03,  0x0F02,  0x0F01,  0x0F00,  0x0E07,  0x0E06,  0x0E05,  0x0E04,  
0x0E03,  0x0E02,  0x0E01,  0x0E00,  0x0D07,  0x0D06,  0x0D05,  0x0D04,  0x0D03,  0x0D02,  
0x0D01,  0x0D00,  0x0C07,  0x0C06,  0x0C05,  0x0C04,  0x0C03,  0x0C02,  0x0C01,  0x0C00,  
};

U16 ATVVolumeTable[]= { 
0x7F00,  
0x4700,  0x4400,  0x4100,  0x3E00,  0x3C00,  0x3A00,  0x3800,  0x3600,  0x3400,  0x3200,  
0x3000,  0x2E00,  0x2D00,  0x2C00,  0x2B00,  0x2A00,  0x2900,  0x2800,  0x2700,  0x2600,  
0x2500,  0x2400,  0x2300,  0x2200,  0x2100,  0x2000,  0x1F00,  0x1E04,  0x1E00,  0x1D04,  
0x1D00,  0x1C04,  0x1C00,  0x1B04,  0x1B00,  0x1A04,  0x1A00,  0x1904,  0x1900,  0x1804,  
0x1800,  0x1704,  0x1700,  0x1604,  0x1600,  0x1504,  0x1502,  0x1500,  0x1406,  0x1404,  
0x1402,  0x1400,  0x1306,  0x1304,  0x1302,  0x1300,  0x1206,  0x1204,  0x1202,  0x1200,  
0x1106,  0x1104,  0x1102,  0x1100,  0x1006,  0x1004,  0x1002,  0x1000,  0x0F07,  0x0F06,  
0x0F05,  0x0F04,  0x0F03,  0x0F02,  0x0F01,  0x0F00,  0x0E07,  0x0E06,  0x0E05,  0x0E04,  
0x0E03,  0x0E02,  0x0E01,  0x0E00,  0x0D07,  0x0D06,  0x0D05,  0x0D04,  0x0D03,  0x0D02,  
0x0D01,  0x0D00,  0x0C07,  0x0C06,  0x0C05,  0x0C04,  0x0C03,  0x0C02,  0x0C01,  0x0C00,  
};

U16 AVVolumeTable[]= { 
0x7F00,  
0x4700,  0x4400,  0x4100,  0x3E00,  0x3C00,  0x3A00,  0x3800,  0x3600,  0x3400,  0x3200,  
0x3000,  0x2E00,  0x2D00,  0x2C00,  0x2B00,  0x2A00,  0x2900,  0x2800,  0x2700,  0x2600,  
0x2500,  0x2400,  0x2300,  0x2200,  0x2100,  0x2000,  0x1F00,  0x1E04,  0x1E00,  0x1D04,  
0x1D00,  0x1C04,  0x1C00,  0x1B04,  0x1B00,  0x1A04,  0x1A00,  0x1904,  0x1900,  0x1804,  
0x1800,  0x1704,  0x1700,  0x1604,  0x1600,  0x1504,  0x1502,  0x1500,  0x1406,  0x1404,  
0x1402,  0x1400,  0x1306,  0x1304,  0x1302,  0x1300,  0x1206,  0x1204,  0x1202,  0x1200,  
0x1106,  0x1104,  0x1102,  0x1100,  0x1006,  0x1004,  0x1002,  0x1000,  0x0F07,  0x0F06,  
0x0F05,  0x0F04,  0x0F03,  0x0F02,  0x0F01,  0x0F00,  0x0E07,  0x0E06,  0x0E05,  0x0E04,  
0x0E03,  0x0E02,  0x0E01,  0x0E00,  0x0D07,  0x0D06,  0x0D05,  0x0D04,  0x0D03,  0x0D02,  
0x0D01,  0x0D00,  0x0C07,  0x0C06,  0x0C05,  0x0C04,  0x0C03,  0x0C02,  0x0C01,  0x0C00,  
};

U16 HDMIVolumeTable[]= { 
0x7F00,  
0x4700,  0x4400,  0x4100,  0x3E00,  0x3C00,  0x3A00,  0x3800,  0x3600,  0x3400,  0x3200,  
0x3000,  0x2E00,  0x2D00,  0x2C00,  0x2B00,  0x2A00,  0x2900,  0x2800,  0x2700,  0x2600,  
0x2500,  0x2400,  0x2300,  0x2200,  0x2100,  0x2000,  0x1F00,  0x1E04,  0x1E00,  0x1D04,  
0x1D00,  0x1C04,  0x1C00,  0x1B04,  0x1B00,  0x1A04,  0x1A00,  0x1904,  0x1900,  0x1804,  
0x1800,  0x1704,  0x1700,  0x1604,  0x1600,  0x1504,  0x1502,  0x1500,  0x1406,  0x1404,  
0x1402,  0x1400,  0x1306,  0x1304,  0x1302,  0x1300,  0x1206,  0x1204,  0x1202,  0x1200,  
0x1106,  0x1104,  0x1102,  0x1100,  0x1006,  0x1004,  0x1002,  0x1000,  0x0F07,  0x0F06,  
0x0F05,  0x0F04,  0x0F03,  0x0F02,  0x0F01,  0x0F00,  0x0E07,  0x0E06,  0x0E05,  0x0E04,  
0x0E03,  0x0E02,  0x0E01,  0x0E00,  0x0D07,  0x0D06,  0x0D05,  0x0D04,  0x0D03,  0x0D02,  
0x0D01,  0x0D00,  0x0C07,  0x0C06,  0x0C05,  0x0C04,  0x0C03,  0x0C02,  0x0C01,  0x0C00,  
};

U16 USBVolumeTable[]= { 
0x7F00,  
0x4700,  0x4400,  0x4100,  0x3E00,  0x3C00,  0x3A00,  0x3800,  0x3600,  0x3400,  0x3200,  
0x3000,  0x2E00,  0x2D00,  0x2C00,  0x2B00,  0x2A00,  0x2900,  0x2800,  0x2700,  0x2600,  
0x2500,  0x2400,  0x2300,  0x2200,  0x2100,  0x2000,  0x1F00,  0x1E04,  0x1E00,  0x1D04,  
0x1D00,  0x1C04,  0x1C00,  0x1B04,  0x1B00,  0x1A04,  0x1A00,  0x1904,  0x1900,  0x1804,  
0x1800,  0x1704,  0x1700,  0x1604,  0x1600,  0x1504,  0x1502,  0x1500,  0x1406,  0x1404,  
0x1402,  0x1400,  0x1306,  0x1304,  0x1302,  0x1300,  0x1206,  0x1204,  0x1202,  0x1200,  
0x1106,  0x1104,  0x1102,  0x1100,  0x1006,  0x1004,  0x1002,  0x1000,  0x0F07,  0x0F06,  
0x0F05,  0x0F04,  0x0F03,  0x0F02,  0x0F01,  0x0F00,  0x0E07,  0x0E06,  0x0E05,  0x0E04,  
0x0E03,  0x0E02,  0x0E01,  0x0E00,  0x0D07,  0x0D06,  0x0D05,  0x0D04,  0x0D03,  0x0D02,  
0x0D01,  0x0D00,  0x0C07,  0x0C06,  0x0C05,  0x0C04,  0x0C03,  0x0C02,  0x0C01,  0x0C00,  
};


/******************************************************************************************************

SETTING SUBWOOFER

******************************************************************************************************/

#define SETTING_SUBWOOFER_LOW     { 255, 209, 204, 200, 199, 195, 193, 190, 187, 184, 182 } 
#define SETTING_SUBWOOFER_HIGH     { 255, 204, 199, 193, 187, 181, 174, 167, 157, 147, 133 } 

#define CUSTOM_PWM1_PERIOD  500
#define CUSTOM_INIT_PWM1_DUTY  70
#define CUSTOM_PWM1_DIV  0

/******************************************************************************************************

LOUDNESS OFFSET TABLE

******************************************************************************************************/

U8 LowSubwLoudnessOffset[]= { 0,  0,  0,  0,  14,  31,  40,  46,  46,  46,  46,  46,  30,  28,  14,  6,  0  };
U8 LowTrebleLoudnessOffset[]= { 0,  0,  0,  0,  0,  1,  2,  2,  2,  2,  2,  2,  1,  1,  0,  0,  0  };
U8 HighSubwLoudnessOffset[]= { 0,  0,  0,  0,  47,  133,  133,  133,  133,  133,  133,  133,  65,  57,  30,  6,  0  };
U8 HighTrebleLoudnessOffset[]= { 0,  0,  0,  0,  1,  3,  4,  5,  5,  5,  5,  4,  3,  2,  1,  0,  0  };

/******************************************************************************************************

SETTING PEQ

******************************************************************************************************/

#define CUSTOM_GAIN_BAND1      163
#define CUSTOM_FO_BAND1      60
#define CUSTOM_Q_BAND1      5
#define CUSTOM_GAIN_BAND2      130
#define CUSTOM_FO_BAND2      135
#define CUSTOM_Q_BAND2      5
#define CUSTOM_GAIN_BAND3      120
#define CUSTOM_FO_BAND3      1150
#define CUSTOM_Q_BAND3      10
#define CUSTOM_GAIN_BAND4      155
#define CUSTOM_FO_BAND4      3000
#define CUSTOM_Q_BAND4      15
#define CUSTOM_GAIN_BAND5      140
#define CUSTOM_FO_BAND5      11500
#define CUSTOM_Q_BAND5      10

/******************************************************************************************************

Setting HPF

******************************************************************************************************/

#define CUSTOM_HPF_ENABLE      0
#define CUSTOM_FO_VALUE      30
#define CUSTOM_Q_VALUE      90

/******************************************************************************************************

Setting PRE VOLUME

******************************************************************************************************/

#define CUSTOM_REG_0x112D58_VALUE      0x18
#define CUSTOM_REG_0x112D5A_VALUE      0x18
#define CUSTOM_REG_0x112D5C_VALUE      0x18
#define CUSTOM_REG_0x112D5E_VALUE      0x18


