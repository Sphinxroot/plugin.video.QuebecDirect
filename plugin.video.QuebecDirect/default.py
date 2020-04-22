########################################

import os, sys, xbmc, xbmcgui, xbmcplugin, xbmcaddon
	
#Quebec Direct By Sphinxroot QC

# Various constants used throughout the script
HANDLE = int(sys.argv[1])
ADDON = xbmcaddon.Addon(id='plugin.video.QuebecDirect')
LANGUAGE  = ADDON.getLocalizedString
THUMBNAIL_PATH = os.path.join( ADDON.getAddonInfo( 'path' ), 'resources', 'media')

def start() :

	li = xbmcgui.ListItem(label=LANGUAGE(30000), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'QC.gif'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="plugin://plugin.video.youtube/play/?video_id=MJLB4Qv38vM", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30001), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'TVA.png'))		
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://tvalive.akamaized.net/hls/live/2012413/tva01/high_1080p/high_1080p.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30002), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'LCN.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://tvalcn.akamaized.net/hls/live/2013847/tvalcn01/high_1080p/high_1080p.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30003), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'RDI.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://rcavlive.akamaized.net/hls/live/704025/xcanrdi/master_2500.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30004), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'TQC.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://teleqmmd.mmdlive.lldns.net/teleqmmd/f386e3b206814e1f8c8c1c71c0f8e748/chunklist_b2592000.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30005), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'TeleV.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://bcsecurelivehls-i.akamaihd.net/hls/live/551061/618566855001/master.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30006), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'RC.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://rcavlive-dai.akamaized.net/hls/live/696614/cancbftprem/master_5000.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30007), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'RC.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://rcavlive.akamaized.net/hls/live/704024/cancjbr/master_2500.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30008), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'RC.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://rcavlive.akamaized.net/hls/live/704016/cancksh/master_2500.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30009), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'RC.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://rcavlive.akamaized.net/hls/live/704021/cancktm/master_2500.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30010), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'RC.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://rcavlive.akamaized.net/hls/live/664046/cancboft/master_2500.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30011), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'RC.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://rcavlive.akamaized.net/hls/live/664045/cancbvt/master_2500.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30012), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'RC.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://rcavlive.akamaized.net/hls/live/704023/cancktv/master_2500.m3u8", listitem=li, isFolder=False)	
   	li = xbmcgui.ListItem(label=LANGUAGE(30013), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'ici.jpg'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://ici-i.akamaihd.net/hls/live/873426/ICI-Live-Stream/59f8cf257de98a7e0db5ea592e9e081b/1.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30014), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'assnat.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="http://diffusionm3.assnat.qc.ca/canal10/250.sdp/chunklist_w592829221.m3u8", listitem=li, isFolder=False)
  	li = xbmcgui.ListItem(label=LANGUAGE(30015), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'CS.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://hls.savoir.media/live/stream.m3u8", listitem=li, isFolder=False)
 	li = xbmcgui.ListItem(label=LANGUAGE(30016), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'cpac.jpg'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://bcsecurelivehls-i.akamaihd.net/hls/live/680604/1242843915001_3//Assets_1586134027986/Layer2_master.m3u8", listitem=li, isFolder=False)
 	li = xbmcgui.ListItem(label=LANGUAGE(30017), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'emcitv.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://emci-fr-hls.akamaized.net/hls/live/2007265/emcifrhls/04.m3u8", listitem=li, isFolder=False)
  	li = xbmcgui.ListItem(label=LANGUAGE(30018), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'egarizim.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://5790d294af2dc.streamlock.net/8150/8150/chunklist_w893346968.m3u8", listitem=li, isFolder=False)
  	li = xbmcgui.ListItem(label=LANGUAGE(30019), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'mag.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="plugin://plugin.video.youtube/play/?video_id=Ctm-7JcJ5HM", listitem=li, isFolder=False)
   	li = xbmcgui.ListItem(label=LANGUAGE(30020), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'TVC9.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="plugin://plugin.video.youtube/play/?video_id=g-0o--6bbpM", listitem=li, isFolder=False)
   	li = xbmcgui.ListItem(label=LANGUAGE(30021), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'Yoopa.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://tvayoopa.akamaized.net/hls/live/2013885/tvayoopa01/high_1080p/high_1080p.m3u8", listitem=li, isFolder=False)
	setViewMode("500")		
	xbmcplugin.endOfDirectory( HANDLE )		
	
def setViewMode(id):
	if xbmc.getSkinDir() == "skin.confluence":
		xbmc.executebuiltin("Container.SetViewMode(" + id + ")")
			
start()