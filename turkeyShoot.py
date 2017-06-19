#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: TurkeyShoot
# Author: Mark Busby <mark@BusbyCreations.com>
# Description: Single SDRs, multiple demodulators, multiple output paths
# Generated: Mon Jun 19 01:12:28 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
from rxAM_3 import rxAM_3  # grc-generated hier_block
from rxNBFM import rxNBFM  # grc-generated hier_block
import sip
import time
from gnuradio import qtgui


class turkeyShoot(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "TurkeyShoot")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("TurkeyShoot")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "turkeyShoot")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.center_freq_ = center_freq_ = 270.1
        self.samp_rate = samp_rate = 24e6
        self.outGain_ = outGain_ = 2
        self.channel_freq_rxFM_5_ = channel_freq_rxFM_5_ = center_freq_
        self.channel_freq_rxFM_4_ = channel_freq_rxFM_4_ = center_freq_
        self.channel_freq_rxFM_3_ = channel_freq_rxFM_3_ = center_freq_
        self.channel_freq_rxFM_2_ = channel_freq_rxFM_2_ = center_freq_
        self.channel_freq_rxFM_1_ = channel_freq_rxFM_1_ = center_freq_
        self.channel_freq_rxAM_ = channel_freq_rxAM_ = center_freq_
        self.outGain = outGain = outGain_
        self.mute_rxFM_5_ = mute_rxFM_5_ = True
        self.mute_rxFM_4_ = mute_rxFM_4_ = True
        self.mute_rxFM_3_ = mute_rxFM_3_ = True
        self.mute_rxFM_2_ = mute_rxFM_2_ = True
        self.mute_rxFM_1_ = mute_rxFM_1_ = True
        self.mute_rxAM_ = mute_rxAM_ = False
        self.channel_freq_rxFM_5 = channel_freq_rxFM_5 = 1e6*channel_freq_rxFM_5_
        self.channel_freq_rxFM_4 = channel_freq_rxFM_4 = 1e6*channel_freq_rxFM_4_
        self.channel_freq_rxFM_3 = channel_freq_rxFM_3 = 1e6*channel_freq_rxFM_3_
        self.channel_freq_rxFM_2 = channel_freq_rxFM_2 = 1e6*channel_freq_rxFM_2_
        self.channel_freq_rxFM_1 = channel_freq_rxFM_1 = 1e6*channel_freq_rxFM_1_
        self.channel_freq_rxAM = channel_freq_rxAM = 1e6*channel_freq_rxAM_
        self.center_freq = center_freq = 1e6*center_freq_
        self.bandwidth = bandwidth = samp_rate
        self.audioRate = audioRate = 48000

        ##################################################
        # Blocks
        ##################################################
        self.tabWidget0 = Qt.QTabWidget()
        self.tabWidget0_widget_0 = Qt.QWidget()
        self.tabWidget0_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabWidget0_widget_0)
        self.tabWidget0_grid_layout_0 = Qt.QGridLayout()
        self.tabWidget0_layout_0.addLayout(self.tabWidget0_grid_layout_0)
        self.tabWidget0.addTab(self.tabWidget0_widget_0, 'Input')
        self.tabWidget0_widget_1 = Qt.QWidget()
        self.tabWidget0_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabWidget0_widget_1)
        self.tabWidget0_grid_layout_1 = Qt.QGridLayout()
        self.tabWidget0_layout_1.addLayout(self.tabWidget0_grid_layout_1)
        self.tabWidget0.addTab(self.tabWidget0_widget_1, 'Output')
        self.top_grid_layout.addWidget(self.tabWidget0, 0,0,2,1)
        _mute_rxFM_5__check_box = Qt.QCheckBox('Mute')
        self._mute_rxFM_5__choices = {True: True, False: False}
        self._mute_rxFM_5__choices_inv = dict((v,k) for k,v in self._mute_rxFM_5__choices.iteritems())
        self._mute_rxFM_5__callback = lambda i: Qt.QMetaObject.invokeMethod(_mute_rxFM_5__check_box, "setChecked", Qt.Q_ARG("bool", self._mute_rxFM_5__choices_inv[i]))
        self._mute_rxFM_5__callback(self.mute_rxFM_5_)
        _mute_rxFM_5__check_box.stateChanged.connect(lambda i: self.set_mute_rxFM_5_(self._mute_rxFM_5__choices[bool(i)]))
        self.tabWidget0_grid_layout_0.addWidget(_mute_rxFM_5__check_box, 7,1)
        _mute_rxFM_4__check_box = Qt.QCheckBox('Mute')
        self._mute_rxFM_4__choices = {True: True, False: False}
        self._mute_rxFM_4__choices_inv = dict((v,k) for k,v in self._mute_rxFM_4__choices.iteritems())
        self._mute_rxFM_4__callback = lambda i: Qt.QMetaObject.invokeMethod(_mute_rxFM_4__check_box, "setChecked", Qt.Q_ARG("bool", self._mute_rxFM_4__choices_inv[i]))
        self._mute_rxFM_4__callback(self.mute_rxFM_4_)
        _mute_rxFM_4__check_box.stateChanged.connect(lambda i: self.set_mute_rxFM_4_(self._mute_rxFM_4__choices[bool(i)]))
        self.tabWidget0_grid_layout_0.addWidget(_mute_rxFM_4__check_box, 6,1)
        _mute_rxFM_3__check_box = Qt.QCheckBox('Mute')
        self._mute_rxFM_3__choices = {True: True, False: False}
        self._mute_rxFM_3__choices_inv = dict((v,k) for k,v in self._mute_rxFM_3__choices.iteritems())
        self._mute_rxFM_3__callback = lambda i: Qt.QMetaObject.invokeMethod(_mute_rxFM_3__check_box, "setChecked", Qt.Q_ARG("bool", self._mute_rxFM_3__choices_inv[i]))
        self._mute_rxFM_3__callback(self.mute_rxFM_3_)
        _mute_rxFM_3__check_box.stateChanged.connect(lambda i: self.set_mute_rxFM_3_(self._mute_rxFM_3__choices[bool(i)]))
        self.tabWidget0_grid_layout_0.addWidget(_mute_rxFM_3__check_box, 5,1)
        _mute_rxFM_2__check_box = Qt.QCheckBox('Mute')
        self._mute_rxFM_2__choices = {True: True, False: False}
        self._mute_rxFM_2__choices_inv = dict((v,k) for k,v in self._mute_rxFM_2__choices.iteritems())
        self._mute_rxFM_2__callback = lambda i: Qt.QMetaObject.invokeMethod(_mute_rxFM_2__check_box, "setChecked", Qt.Q_ARG("bool", self._mute_rxFM_2__choices_inv[i]))
        self._mute_rxFM_2__callback(self.mute_rxFM_2_)
        _mute_rxFM_2__check_box.stateChanged.connect(lambda i: self.set_mute_rxFM_2_(self._mute_rxFM_2__choices[bool(i)]))
        self.tabWidget0_grid_layout_0.addWidget(_mute_rxFM_2__check_box, 4,1)
        _mute_rxFM_1__check_box = Qt.QCheckBox('Mute')
        self._mute_rxFM_1__choices = {True: True, False: False}
        self._mute_rxFM_1__choices_inv = dict((v,k) for k,v in self._mute_rxFM_1__choices.iteritems())
        self._mute_rxFM_1__callback = lambda i: Qt.QMetaObject.invokeMethod(_mute_rxFM_1__check_box, "setChecked", Qt.Q_ARG("bool", self._mute_rxFM_1__choices_inv[i]))
        self._mute_rxFM_1__callback(self.mute_rxFM_1_)
        _mute_rxFM_1__check_box.stateChanged.connect(lambda i: self.set_mute_rxFM_1_(self._mute_rxFM_1__choices[bool(i)]))
        self.tabWidget0_grid_layout_0.addWidget(_mute_rxFM_1__check_box, 3,1)
        _mute_rxAM__check_box = Qt.QCheckBox('Mute')
        self._mute_rxAM__choices = {True: True, False: False}
        self._mute_rxAM__choices_inv = dict((v,k) for k,v in self._mute_rxAM__choices.iteritems())
        self._mute_rxAM__callback = lambda i: Qt.QMetaObject.invokeMethod(_mute_rxAM__check_box, "setChecked", Qt.Q_ARG("bool", self._mute_rxAM__choices_inv[i]))
        self._mute_rxAM__callback(self.mute_rxAM_)
        _mute_rxAM__check_box.stateChanged.connect(lambda i: self.set_mute_rxAM_(self._mute_rxAM__choices[bool(i)]))
        self.tabWidget0_grid_layout_0.addWidget(_mute_rxAM__check_box, 2,1)
        self._center_freq__tool_bar = Qt.QToolBar(self)

        if None:
          self._center_freq__formatter = None
        else:
          self._center_freq__formatter = lambda x: x

        self._center_freq__tool_bar.addWidget(Qt.QLabel('Center Frequency [MHz]'+": "))
        self._center_freq__label = Qt.QLabel(str(self._center_freq__formatter(self.center_freq_)))
        self._center_freq__tool_bar.addWidget(self._center_freq__label)
        self.tabWidget0_grid_layout_0.addWidget(self._center_freq__tool_bar, 1,0,1,2)

        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("type=b200", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_source_0.set_gain(0, 0)
        self.uhd_usrp_source_0.set_antenna('TX/RX', 0)
        self.rxNBFM_0_0_0_0_0 = rxNBFM(
            rxNBFM_audioRate=audioRate,
            rxNBFM_channelFreq=channel_freq_rxFM_5,
            rxNBFM_freq=center_freq,
            rxNBFM_gain=1,
            rxNBFM_sampleRate=samp_rate,
        )
        self.rxNBFM_0_0_0_0 = rxNBFM(
            rxNBFM_audioRate=audioRate,
            rxNBFM_channelFreq=channel_freq_rxFM_4,
            rxNBFM_freq=center_freq,
            rxNBFM_gain=1,
            rxNBFM_sampleRate=samp_rate,
        )
        self.rxNBFM_0_0_0 = rxNBFM(
            rxNBFM_audioRate=audioRate,
            rxNBFM_channelFreq=channel_freq_rxFM_3,
            rxNBFM_freq=center_freq,
            rxNBFM_gain=1,
            rxNBFM_sampleRate=samp_rate,
        )
        self.rxNBFM_0_0 = rxNBFM(
            rxNBFM_audioRate=audioRate,
            rxNBFM_channelFreq=channel_freq_rxFM_2,
            rxNBFM_freq=center_freq,
            rxNBFM_gain=1,
            rxNBFM_sampleRate=samp_rate,
        )
        self.rxNBFM_0 = rxNBFM(
            rxNBFM_audioRate=audioRate,
            rxNBFM_channelFreq=channel_freq_rxFM_1,
            rxNBFM_freq=center_freq,
            rxNBFM_gain=1,
            rxNBFM_sampleRate=samp_rate,
        )
        self.rxAM_3_0 = rxAM_3(
            rxAM_audioRate=48e3,
            rxAM_channelFreq=channel_freq_rxAM,
            rxAM_freq=center_freq,
            rxAM_gain=outGain,
            rxAM_sampleRate=samp_rate,
        )
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	center_freq, #fc
        	bandwidth, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 0,1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	center_freq, #fc
        	bandwidth, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not False:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 1,1)
        self._outGain__range = Range(0, 15, 1, 2, 10)
        self._outGain__win = RangeWidget(self._outGain__range, self.set_outGain_, 'Output Gain [dB]', "counter_slider", float)
        self.tabWidget0_grid_layout_1.addWidget(self._outGain__win, 0,0)
        self._channel_freq_rxFM_5__range = Range(center_freq_ - (samp_rate / 2e6), center_freq_ + (samp_rate / 2e6), 0.025, center_freq_, 200)
        self._channel_freq_rxFM_5__win = RangeWidget(self._channel_freq_rxFM_5__range, self.set_channel_freq_rxFM_5_, 'FM5 Channel Frequency [MHz]', "counter_slider", float)
        self.tabWidget0_grid_layout_0.addWidget(self._channel_freq_rxFM_5__win, 7,0)
        self._channel_freq_rxFM_4__range = Range(center_freq_ - (samp_rate / 2e6), center_freq_ + (samp_rate / 2e6), 0.025, center_freq_, 200)
        self._channel_freq_rxFM_4__win = RangeWidget(self._channel_freq_rxFM_4__range, self.set_channel_freq_rxFM_4_, 'FM4 Channel Frequency [MHz]', "counter_slider", float)
        self.tabWidget0_grid_layout_0.addWidget(self._channel_freq_rxFM_4__win, 6,0)
        self._channel_freq_rxFM_3__range = Range(center_freq_ - (samp_rate / 2e6), center_freq_ + (samp_rate / 2e6), 0.025, center_freq_, 200)
        self._channel_freq_rxFM_3__win = RangeWidget(self._channel_freq_rxFM_3__range, self.set_channel_freq_rxFM_3_, 'FM3 Channel Frequency [MHz]', "counter_slider", float)
        self.tabWidget0_grid_layout_0.addWidget(self._channel_freq_rxFM_3__win, 5,0)
        self._channel_freq_rxFM_2__range = Range(center_freq_ - (samp_rate / 2e6), center_freq_ + (samp_rate / 2e6), 0.025, center_freq_, 200)
        self._channel_freq_rxFM_2__win = RangeWidget(self._channel_freq_rxFM_2__range, self.set_channel_freq_rxFM_2_, 'FM2 Channel Frequency [MHz]', "counter_slider", float)
        self.tabWidget0_grid_layout_0.addWidget(self._channel_freq_rxFM_2__win, 4,0)
        self._channel_freq_rxFM_1__range = Range(center_freq_ - (samp_rate / 2e6), center_freq_ + (samp_rate / 2e6), 0.025, center_freq_, 200)
        self._channel_freq_rxFM_1__win = RangeWidget(self._channel_freq_rxFM_1__range, self.set_channel_freq_rxFM_1_, 'FM1 Channel Frequency [MHz]', "counter_slider", float)
        self.tabWidget0_grid_layout_0.addWidget(self._channel_freq_rxFM_1__win, 3,0)
        self._channel_freq_rxAM__range = Range(center_freq_ - (samp_rate / 2e6), center_freq_ + (samp_rate / 2e6), 0.025, center_freq_, 200)
        self._channel_freq_rxAM__win = RangeWidget(self._channel_freq_rxAM__range, self.set_channel_freq_rxAM_, 'AM1 Channel Freq [MHz]', "counter_slider", float)
        self.tabWidget0_grid_layout_0.addWidget(self._channel_freq_rxAM__win, 2,0)
        self.blocks_wavfile_sink_0_0_0_0_0_0 = blocks.wavfile_sink('C:\\TurkeyShootRecorder\\rxNBFM_5.wav', 1, audioRate, 16)
        self.blocks_wavfile_sink_0_0_0_0_0 = blocks.wavfile_sink('C:\\TurkeyShootRecorder\\rxNBFM_4.wav', 1, audioRate, 16)
        self.blocks_wavfile_sink_0_0_0_0 = blocks.wavfile_sink('c:\\TurkeyShootRecorder\\rxNBFM_3.wav', 1, audioRate, 16)
        self.blocks_wavfile_sink_0_0_0 = blocks.wavfile_sink('c:\\TurkeyShootRecorder\\rxNBFM_2.wav', 1, audioRate, 16)
        self.blocks_wavfile_sink_0_0 = blocks.wavfile_sink('c:\\TurkeyShootRecorder\\rxNBFM_1.wav', 1, audioRate, 16)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink('C:\\TurkeyShootRecorder\\rxAM.wav', 1, audioRate, 16)
        self.blocks_mute_xx_0_1_0_0_0 = blocks.mute_ff(bool(mute_rxFM_5_))
        self.blocks_mute_xx_0_1_0_0 = blocks.mute_ff(bool(mute_rxFM_4_))
        self.blocks_mute_xx_0_1_0 = blocks.mute_ff(bool(mute_rxFM_3_))
        self.blocks_mute_xx_0_1 = blocks.mute_ff(bool(mute_rxFM_2_))
        self.blocks_mute_xx_0_0 = blocks.mute_ff(bool(mute_rxFM_1_))
        self.blocks_mute_xx_0 = blocks.mute_ff(bool(mute_rxAM_))
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.audio_sink_0 = audio.sink(audioRate, '', False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_xx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_mute_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_mute_xx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_mute_xx_0_1, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_mute_xx_0_1_0, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_mute_xx_0_1_0_0, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.blocks_mute_xx_0_1_0_0_0, 0), (self.blocks_add_xx_0, 5))
        self.connect((self.rxAM_3_0, 0), (self.blocks_mute_xx_0, 0))
        self.connect((self.rxAM_3_0, 0), (self.blocks_wavfile_sink_0, 0))
        self.connect((self.rxNBFM_0, 0), (self.blocks_mute_xx_0_0, 0))
        self.connect((self.rxNBFM_0, 0), (self.blocks_wavfile_sink_0_0, 0))
        self.connect((self.rxNBFM_0_0, 0), (self.blocks_mute_xx_0_1, 0))
        self.connect((self.rxNBFM_0_0, 0), (self.blocks_wavfile_sink_0_0_0, 0))
        self.connect((self.rxNBFM_0_0_0, 0), (self.blocks_mute_xx_0_1_0, 0))
        self.connect((self.rxNBFM_0_0_0, 0), (self.blocks_wavfile_sink_0_0_0_0, 0))
        self.connect((self.rxNBFM_0_0_0_0, 0), (self.blocks_mute_xx_0_1_0_0, 0))
        self.connect((self.rxNBFM_0_0_0_0, 0), (self.blocks_wavfile_sink_0_0_0_0_0, 0))
        self.connect((self.rxNBFM_0_0_0_0_0, 0), (self.blocks_mute_xx_0_1_0_0_0, 0))
        self.connect((self.rxNBFM_0_0_0_0_0, 0), (self.blocks_wavfile_sink_0_0_0_0_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.rxAM_3_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.rxNBFM_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.rxNBFM_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.rxNBFM_0_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.rxNBFM_0_0_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.rxNBFM_0_0_0_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "turkeyShoot")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_center_freq_(self):
        return self.center_freq_

    def set_center_freq_(self, center_freq_):
        self.center_freq_ = center_freq_
        Qt.QMetaObject.invokeMethod(self._center_freq__label, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.center_freq_)))
        self.set_center_freq(1e6*self.center_freq_)
        self.set_channel_freq_rxFM_5_(self.center_freq_)
        self.set_channel_freq_rxFM_4_(self.center_freq_)
        self.set_channel_freq_rxFM_3_(self.center_freq_)
        self.set_channel_freq_rxFM_2_(self.center_freq_)
        self.set_channel_freq_rxFM_1_(self.center_freq_)
        self.set_channel_freq_rxAM_(self.center_freq_)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_bandwidth(self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.rxNBFM_0_0_0_0_0.set_rxNBFM_sampleRate(self.samp_rate)
        self.rxNBFM_0_0_0_0.set_rxNBFM_sampleRate(self.samp_rate)
        self.rxNBFM_0_0_0.set_rxNBFM_sampleRate(self.samp_rate)
        self.rxNBFM_0_0.set_rxNBFM_sampleRate(self.samp_rate)
        self.rxNBFM_0.set_rxNBFM_sampleRate(self.samp_rate)
        self.rxAM_3_0.set_rxAM_sampleRate(self.samp_rate)

    def get_outGain_(self):
        return self.outGain_

    def set_outGain_(self, outGain_):
        self.outGain_ = outGain_
        self.set_outGain(self.outGain_)

    def get_channel_freq_rxFM_5_(self):
        return self.channel_freq_rxFM_5_

    def set_channel_freq_rxFM_5_(self, channel_freq_rxFM_5_):
        self.channel_freq_rxFM_5_ = channel_freq_rxFM_5_
        self.set_channel_freq_rxFM_5(1e6*self.channel_freq_rxFM_5_)

    def get_channel_freq_rxFM_4_(self):
        return self.channel_freq_rxFM_4_

    def set_channel_freq_rxFM_4_(self, channel_freq_rxFM_4_):
        self.channel_freq_rxFM_4_ = channel_freq_rxFM_4_
        self.set_channel_freq_rxFM_4(1e6*self.channel_freq_rxFM_4_)

    def get_channel_freq_rxFM_3_(self):
        return self.channel_freq_rxFM_3_

    def set_channel_freq_rxFM_3_(self, channel_freq_rxFM_3_):
        self.channel_freq_rxFM_3_ = channel_freq_rxFM_3_
        self.set_channel_freq_rxFM_3(1e6*self.channel_freq_rxFM_3_)

    def get_channel_freq_rxFM_2_(self):
        return self.channel_freq_rxFM_2_

    def set_channel_freq_rxFM_2_(self, channel_freq_rxFM_2_):
        self.channel_freq_rxFM_2_ = channel_freq_rxFM_2_
        self.set_channel_freq_rxFM_2(1e6*self.channel_freq_rxFM_2_)

    def get_channel_freq_rxFM_1_(self):
        return self.channel_freq_rxFM_1_

    def set_channel_freq_rxFM_1_(self, channel_freq_rxFM_1_):
        self.channel_freq_rxFM_1_ = channel_freq_rxFM_1_
        self.set_channel_freq_rxFM_1(1e6*self.channel_freq_rxFM_1_)

    def get_channel_freq_rxAM_(self):
        return self.channel_freq_rxAM_

    def set_channel_freq_rxAM_(self, channel_freq_rxAM_):
        self.channel_freq_rxAM_ = channel_freq_rxAM_
        self.set_channel_freq_rxAM(1e6*self.channel_freq_rxAM_)

    def get_outGain(self):
        return self.outGain

    def set_outGain(self, outGain):
        self.outGain = outGain
        self.rxAM_3_0.set_rxAM_gain(self.outGain)

    def get_mute_rxFM_5_(self):
        return self.mute_rxFM_5_

    def set_mute_rxFM_5_(self, mute_rxFM_5_):
        self.mute_rxFM_5_ = mute_rxFM_5_
        self._mute_rxFM_5__callback(self.mute_rxFM_5_)
        self.blocks_mute_xx_0_1_0_0_0.set_mute(bool(self.mute_rxFM_5_))

    def get_mute_rxFM_4_(self):
        return self.mute_rxFM_4_

    def set_mute_rxFM_4_(self, mute_rxFM_4_):
        self.mute_rxFM_4_ = mute_rxFM_4_
        self._mute_rxFM_4__callback(self.mute_rxFM_4_)
        self.blocks_mute_xx_0_1_0_0.set_mute(bool(self.mute_rxFM_4_))

    def get_mute_rxFM_3_(self):
        return self.mute_rxFM_3_

    def set_mute_rxFM_3_(self, mute_rxFM_3_):
        self.mute_rxFM_3_ = mute_rxFM_3_
        self._mute_rxFM_3__callback(self.mute_rxFM_3_)
        self.blocks_mute_xx_0_1_0.set_mute(bool(self.mute_rxFM_3_))

    def get_mute_rxFM_2_(self):
        return self.mute_rxFM_2_

    def set_mute_rxFM_2_(self, mute_rxFM_2_):
        self.mute_rxFM_2_ = mute_rxFM_2_
        self._mute_rxFM_2__callback(self.mute_rxFM_2_)
        self.blocks_mute_xx_0_1.set_mute(bool(self.mute_rxFM_2_))

    def get_mute_rxFM_1_(self):
        return self.mute_rxFM_1_

    def set_mute_rxFM_1_(self, mute_rxFM_1_):
        self.mute_rxFM_1_ = mute_rxFM_1_
        self._mute_rxFM_1__callback(self.mute_rxFM_1_)
        self.blocks_mute_xx_0_0.set_mute(bool(self.mute_rxFM_1_))

    def get_mute_rxAM_(self):
        return self.mute_rxAM_

    def set_mute_rxAM_(self, mute_rxAM_):
        self.mute_rxAM_ = mute_rxAM_
        self._mute_rxAM__callback(self.mute_rxAM_)
        self.blocks_mute_xx_0.set_mute(bool(self.mute_rxAM_))

    def get_channel_freq_rxFM_5(self):
        return self.channel_freq_rxFM_5

    def set_channel_freq_rxFM_5(self, channel_freq_rxFM_5):
        self.channel_freq_rxFM_5 = channel_freq_rxFM_5
        self.rxNBFM_0_0_0_0_0.set_rxNBFM_channelFreq(self.channel_freq_rxFM_5)

    def get_channel_freq_rxFM_4(self):
        return self.channel_freq_rxFM_4

    def set_channel_freq_rxFM_4(self, channel_freq_rxFM_4):
        self.channel_freq_rxFM_4 = channel_freq_rxFM_4
        self.rxNBFM_0_0_0_0.set_rxNBFM_channelFreq(self.channel_freq_rxFM_4)

    def get_channel_freq_rxFM_3(self):
        return self.channel_freq_rxFM_3

    def set_channel_freq_rxFM_3(self, channel_freq_rxFM_3):
        self.channel_freq_rxFM_3 = channel_freq_rxFM_3
        self.rxNBFM_0_0_0.set_rxNBFM_channelFreq(self.channel_freq_rxFM_3)

    def get_channel_freq_rxFM_2(self):
        return self.channel_freq_rxFM_2

    def set_channel_freq_rxFM_2(self, channel_freq_rxFM_2):
        self.channel_freq_rxFM_2 = channel_freq_rxFM_2
        self.rxNBFM_0_0.set_rxNBFM_channelFreq(self.channel_freq_rxFM_2)

    def get_channel_freq_rxFM_1(self):
        return self.channel_freq_rxFM_1

    def set_channel_freq_rxFM_1(self, channel_freq_rxFM_1):
        self.channel_freq_rxFM_1 = channel_freq_rxFM_1
        self.rxNBFM_0.set_rxNBFM_channelFreq(self.channel_freq_rxFM_1)

    def get_channel_freq_rxAM(self):
        return self.channel_freq_rxAM

    def set_channel_freq_rxAM(self, channel_freq_rxAM):
        self.channel_freq_rxAM = channel_freq_rxAM
        self.rxAM_3_0.set_rxAM_channelFreq(self.channel_freq_rxAM)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.uhd_usrp_source_0.set_center_freq(self.center_freq, 0)
        self.rxNBFM_0_0_0_0_0.set_rxNBFM_freq(self.center_freq)
        self.rxNBFM_0_0_0_0.set_rxNBFM_freq(self.center_freq)
        self.rxNBFM_0_0_0.set_rxNBFM_freq(self.center_freq)
        self.rxNBFM_0_0.set_rxNBFM_freq(self.center_freq)
        self.rxNBFM_0.set_rxNBFM_freq(self.center_freq)
        self.rxAM_3_0.set_rxAM_freq(self.center_freq)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.center_freq, self.bandwidth)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.center_freq, self.bandwidth)

    def get_bandwidth(self):
        return self.bandwidth

    def set_bandwidth(self, bandwidth):
        self.bandwidth = bandwidth
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.center_freq, self.bandwidth)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.center_freq, self.bandwidth)

    def get_audioRate(self):
        return self.audioRate

    def set_audioRate(self, audioRate):
        self.audioRate = audioRate
        self.rxNBFM_0_0_0_0_0.set_rxNBFM_audioRate(self.audioRate)
        self.rxNBFM_0_0_0_0.set_rxNBFM_audioRate(self.audioRate)
        self.rxNBFM_0_0_0.set_rxNBFM_audioRate(self.audioRate)
        self.rxNBFM_0_0.set_rxNBFM_audioRate(self.audioRate)
        self.rxNBFM_0.set_rxNBFM_audioRate(self.audioRate)


def main(top_block_cls=turkeyShoot, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
