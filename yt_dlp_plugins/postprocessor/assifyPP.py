from yt_dlp.postprocessor.common import PostProcessor
from yt_dlp.utils import Popen, os
# ℹ️ See the docstring of yt_dlp.postprocessor.common.PostProcessor
# pylint: disable=W0311
class assifyPP(PostProcessor): # pylint: disable=C0103,C0115
  def __init__(self, downloader=None, **kwargs):
    super().__init__(downloader)
    self._kwargs = kwargs

  def _okay_to_run(self, information):
    if not information.get('filepath'):
      self.to_screen("❌ This post-processer should be run after downloading.")
      return False
    if information['ext'] != 'mkv':
      self.to_screen(f"❌ Extension should be 'mkv' but it is {information['ext']}.")
      return False
    if not information.get('requested_subtitles'):
      self.to_screen('ℹ️ got no subtitle; skipping')
      return False
    return True

  def _convert(self, info, lang, subtitle):
    """Convert srv3/ytt subtitle to ass format and update information."""
    Popen(['YTSubConverter', subtitle['filepath']]).communicate()  # 제대로 의도한대로 될 진 모름
    subtitle['filepath'] = subtitle['filepath'][:-len(subtitle['ext'])] + 'ass'
    info['requested_subtitles'][lang]['filepath'] = subtitle['filepath']
    return info

  def run(self, information):
    if not self._okay_to_run(information):  # TODO: Unforce if args?
      return [], information

    subs = information.get('requested_subtitles', {})
    list_of_files_to_delete = [
      s['filepath'] for s in subs.values() if s.get('ext') in {'srv3', 'ytt'}
    ]

    for lang, sub in subs.items():
      if lang == 'live_chat': continue
      if sub['ext'] in ["srv3", "ytt"]:
        try:
          info = self._convert(subtitle=sub, info=information, lang=lang)
          for s in info['requested_subtitles'].values():
            if os.path.exists(s.get('filepath')): information = info
        except Exception as e:
          self.to_screen(f"❌ YTSubConverter {sub['filepath']}\n{e}")
      else:
        self.to_screen(f"❌ {sub['filepath']} is not srv3 or ytt")

    return list_of_files_to_delete, information
