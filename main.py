import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from functions import *

""" for plotting figures,
PgWidth in points, either collumn width page with of Latex"""
fraction = 1.5
dpi = 300
PgWidthPt = 245
defBack = mpl.get_backend()

##
file = '/home/lennartgolks/PycharmProjects/TwoForOnePlusNonLin/'
#file = '/home/lennartgolks/PycharmProjects/showTests/SNR10/'


# for t in range(0,57):
#     VMR_O3 = np.loadtxt(file +'VMR_O3.txt', delimiter= '\t')
#     O3Res = np.loadtxt(file +'O3Res'+str(t).zfill(3)+'.txt', delimiter= '\t')
#     Results = O3Res
#     print(str(t).zfill(3))
#     print(np.linalg.norm(VMR_O3-np.mean(Results[0:],0)))

for t in range(0,1):

    height_values = np.loadtxt(file + 'height_values.txt', delimiter= '\t')
    pressure_values = np.loadtxt(file +'pressure_values.txt', delimiter= '\t')
    tang_heights_lin = np.loadtxt(file +'tang_heights_lin.txt', delimiter= '\t')
    y = np.loadtxt(file + 'dataYtest' + str(t).zfill(3) + '.txt', delimiter= '\t')
    deltRes = np.loadtxt(file +'deltRes'+str(t).zfill(3)+'.txt', delimiter= '\t')
    gamRes = np.loadtxt(file +'gamRes'+str(t).zfill(3)+'.txt', delimiter= '\t')
    VMR_O3 = np.loadtxt(file +'VMR_O3.txt', delimiter= '\t')
    O3Res = np.loadtxt(file +'O3Res'+str(t).zfill(3)+'.txt', delimiter= '\t')
    PressResults = np.loadtxt(file + 'PressRes'+str(t).zfill(3)+'.txt', delimiter= '\t')
    TempResults = np.loadtxt(file + 'TempRes'+str(t).zfill(3)+'.txt', delimiter= '\t')
    # print(str(t).zfill(3)+' low '+ str(1 / np.var(y[0:15])))
    # print(str(t).zfill(3)+' up '+ str(1 / np.var(y[20:])))
    Results = O3Res
    SampleRounds = len(gamRes)


    ##
    plt.close('all')
    DatCol =  'gray'
    ResCol = "#1E88E5"
    TrueCol = [50/255,220/255, 0/255]

    mpl.use(defBack)

    mpl.rcParams.update(mpl.rcParamsDefault)
    plt.rcParams.update({'font.size': 10})
    plt.rcParams["font.serif"] = "cmr"
    # BigFig = plt.figure(figsize=(10,8))
    # ax0 = BigFig.add_subplot(2,3,1)
    #  = axs[0, 0]
    # ax1 = axs[0, 1]
    # ax2 = axs[0, 2]
    # ax4 = axs[1, 0]
    fig0, ax0 = plt.subplots(figsize=set_size(245, fraction=fraction))
    line3 = ax0.scatter(y, tang_heights_lin, label = r'data', zorder = 0, marker = '*', color =DatCol )#,linewidth = 5

    ax01 = ax0.twiny()

    ax01.plot(VMR_O3,height_values,marker = 'o',markerfacecolor = TrueCol, color = TrueCol , label = 'true profile', zorder=1 ,linewidth = 1.5, markersize =7)

    for r in range(1,SampleRounds-1):
        Sol = Results[r, :]

        ax01.plot(Sol,height_values,marker= '+',color = ResCol, zorder = 0, linewidth = 0.5, markersize = 5, alpha = 0.6)
        # with open('Samp' + str(n) +'.txt', 'w') as f:
        #     for k in range(0, len(Sol)):
        #         f.write('(' + str(Sol[k]) + ' , ' + str(height_values[k]) + ')')
        #         f.write('\n')
    O3_Prof = np.mean(Results[0:],0)

    ax01.plot(O3_Prof, height_values, marker='>', color="k", label='sample mean', zorder=2, linewidth=0.5,
                 markersize=5)

    ax01.set_xlabel(r'Ozone volume mixing ratio ')

    ax0.set_ylabel('(Tangent) Height in km')
    handles, labels = ax01.get_legend_handles_labels()
    handles2, labels2 = ax0.get_legend_handles_labels()
    ax01.set_ylim(height_values[0], height_values[-1])

    #ax2.set_xlabel(r'Spectral radiance in $\frac{\text{W } \text{cm}}{\text{m}^2 \text{ sr}} $',labelpad=10)# color =dataCol,
    ax0.tick_params(colors = DatCol, axis = 'x')
    ax0.xaxis.set_ticks_position('top')
    ax0.xaxis.set_label_position('top')
    ax01.xaxis.set_ticks_position('bottom')
    ax01.xaxis.set_label_position('bottom')
    ax01.spines[:].set_visible(False)
    #ax2.spines['top'].set_color(pyTCol)
    ax01.legend()
    plt.savefig('O3Results'+str(t).zfill(3)+'.png')
    #plt.show()
    ##
    fig1, ax1 = plt.subplots(tight_layout=True, figsize=set_size(245, fraction=fraction))
    #ax1 = BigFig.add_subplot(2, 3, 2)
    #ax1.plot(press, heights, label='true press.')
    ax1.plot(pressure_values, height_values, label='true pressure', color = TrueCol, marker ='o', zorder =1, markersize=10)
    #ax1.plot(recov_press, height_values, linewidth=2.5, label='samp. press. fit')  #
    for r in range(0, SampleRounds):
        Sol = PressResults[r, :]

        ax1.plot(Sol, height_values, marker='+', color=ResCol, zorder=0, linewidth=0.5,
                 markersize=5)
    PressProf = np.mean(PressResults[0:],0)
    ax1.plot(PressProf, height_values, marker='>', color="k", label='sample mean', zorder=2, linewidth=0.5,
             markersize=5)

    #ax1.plot(2500 * np.exp(-np.mean(grad) * height_values[:,0]),height_values[:,0])
    ax1.set_xlabel(r'Pressure in hPa ')
    ax1.set_ylabel('Height in km')
    ax1.legend()
    plt.savefig('samplesPress'+str(t).zfill(3)+'.png')
    #plt.show()

    #plt.show()

##

    #ax4 = BigFig.add_subplot(2, 3, 4)
    fig4, ax4 = plt.subplots(4,1,tight_layout = True,figsize=set_size(245, fraction=fraction))
    #ax4 = BigFig.add_subplot(4, 3, 4)
    ax4[0].hist(gamRes, bins = 50)
    ax4[0].axvline(x=gamRes[0], color = 'r')
    #ax5 = BigFig.add_subplot(4, 3, 7)
    ax4[1].hist(deltRes[:,0], bins = 50)
    #ax6 = BigFig.add_subplot(4, 3,10)
    ax4[2].hist(deltRes[:,1], bins = 50)
    #ax7 = BigFig.add_subplot(4, 3,13)
    ax4[3].hist(deltRes[:,2], bins = 50)
    #ax4[3].axvline(x=deltRes[0,2]/0.4, color='r')
    plt.savefig('HistSamp'+str(t).zfill(3)+'.png')
##
    fig3, ax3 = plt.subplots(figsize=set_size(245, fraction=fraction))

    for r in range(1, SampleRounds):
        Sol = TempResults[r, :]

        ax3.plot(Sol, height_values, marker='+', color=ResCol, zorder=0, linewidth=0.5,
                 markersize=5)
    TempProf = np.nanmean(TempResults,0)
    ax3.plot(TempProf, height_values, marker='>', color="k",label = 'sample mean', zorder=2, linewidth=0.5,
             markersize=5)
    ax3.plot(TempResults[0, :], height_values, linewidth=5, label='true T', color=TrueCol, zorder=1)
    ax3.legend()
    plt.savefig('TempSamp'+str(t).zfill(3)+'.png')

    ##

    fig4, ax5 = plt.subplots(figsize=set_size(245, fraction=fraction))

    for r in range(0, SampleRounds):
        Sol = Parabel(height_values, *deltRes[r, :])

        ax5.plot(Sol, height_values, marker='+', color=ResCol, zorder=0, linewidth=0.05)
    ax5.axvline(x= deltRes[0, 2]/0.4, color='r')
    ax5.set_xlabel(r'$\delta$ ')
    ax5.set_ylabel('Height in km')
    plt.savefig('DeltaSamp'+str(t).zfill(3)+'.png')


    # ##
    # BigFig = plt.figure(figsize=(15,8))
    #
    # ax0 = BigFig.add_subplot(1, 3, 1)
    # line3 = ax0.scatter(y, tang_heights_lin, label = r'data', zorder = 0, marker = '*', color =DatCol )#,linewidth = 5
    # ax01 = ax0.twiny()
    # ax01.plot(VMR_O3,height_values,marker = 'o',markerfacecolor = TrueCol, color = TrueCol , label = 'true profile', zorder=1 ,linewidth = 1.5, markersize =7)
    # for r in range(1,SampleRounds-1):
    #     Sol = Results[r, :]
    #     ax01.plot(Sol,height_values,marker= '+',color = ResCol, zorder = 0, linewidth = 0.5, markersize = 5, alpha = 0.6)
    # O3_Prof = np.mean(Results[0:],0)
    # ax01.plot(O3_Prof, height_values, marker='>', color="k", label='sample mean', zorder=2, linewidth=0.5,
    #              markersize=5)
    # ax01.set_xlabel(r'Ozone volume mixing ratio ')
    # ax0.set_ylabel('(Tangent) Height in km')
    # handles, labels = ax01.get_legend_handles_labels()
    # handles2, labels2 = ax0.get_legend_handles_labels()
    # ax01.set_ylim(height_values[0], height_values[-1])
    # #ax2.set_xlabel(r'Spectral radiance in $\frac{\text{W } \text{cm}}{\text{m}^2 \text{ sr}} $',labelpad=10)# color =dataCol,
    # ax0.tick_params(colors = DatCol, axis = 'x')
    # ax0.xaxis.set_ticks_position('top')
    # ax0.xaxis.set_label_position('top')
    # ax01.xaxis.set_ticks_position('bottom')
    # ax01.xaxis.set_label_position('bottom')
    # ax01.spines[:].set_visible(False)
    # #ax2.spines['top'].set_color(pyTCol)
    # ax01.legend()
    #
    #
    # ax3 = BigFig.add_subplot(1, 3, 3)
    # for r in range(1, SampleRounds):
    #     Sol = TempResults[r, :]
    #     ax3.plot(Sol, height_values, marker='+', color=ResCol, zorder=0, linewidth=0.5,
    #              markersize=5)
    # TempProf = np.nanmean(TempResults,0)
    # ax3.plot(TempProf, height_values, marker='>', color="k",label = 'sample mean', zorder=2, linewidth=0.5,
    #          markersize=5)
    # ax3.plot(TempResults[0, :], height_values, linewidth=5, label='true T', color=TrueCol, zorder=1)
    # ax3.legend()
    #
    # ax1 = BigFig.add_subplot(1, 3, 2)
    # ax1.plot(pressure_values, height_values, label='true pressure', color = TrueCol, marker ='o', zorder =1, markersize=10)
    # for r in range(0, SampleRounds):
    #     Sol = PressResults[r, :]
    #     ax1.plot(Sol, height_values, marker='+', color=ResCol, zorder=0, linewidth=0.5,
    #              markersize=5)
    # PressProf = np.mean(PressResults[0:],0)
    # ax1.plot(PressProf, height_values, marker='>', color="k", label='sample mean', zorder=2, linewidth=0.5,
    #          markersize=5)
    # ax1.set_xlabel(r'Pressure in hPa ')
    # ax1.set_ylabel('Height in km')
    # ax1.legend()
    # plt.savefig('Res' + str(t).zfill(3) + '.png')

##



#plt.show()

#print('bla')