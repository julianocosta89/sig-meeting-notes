SIG: Collector SIG (EU/ET)
Date: 2026-09-02
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Andrzej Stencel** 01:30 Yeah, folks.
**Israel Blancas** 01:35 Hey.
**Andrzej Stencel** 02:42 Doesn't look like we have anything specific on the agenda. Jade, do you want to touch on the first one? Do you have anything for the first one?
**Jade Guiton** 02:51 No, not in particular.
**Andrzej Stencel** 02:54 Same. Israel.
How about you?
**Israel Blancas** 02:59 No, nothing.
**Andrzej Stencel** 03:04 We have some more people joining.
**Jade Guiton** 03:07 Yeah, let's wait a few minutes, and then… I guess, if no one… As a topic to bring it in, we'll just close it out.
**Andrzej Stencel** 03:34 Folks, if you have a topic for the agenda, please add it in the doc. I posted in the chat.
Hey folks, once again, for those who joined again.
Add your topics to the agenda if you have any thoughts.
And if not, this will be a very short meeting.
**Evan Bradley** 06:53 I think it's six minutes after, so we can probably get started. Does anybody have anything they want to discuss on the Stability Board?
**Andrzej Stencel** 07:06 Nope.
**Evan Bradley** 07:18 Alright, and then… I suppose not.
just since we have nothing on the agenda, this is mostly an FYI for Israel, but, in case anybody else wants to take a look, I have a PR open that adds.
A new grouping strategy to the group by trace processor.
So it groups traces… or it groups the batches into subtraces, where a subtrace is defined as all the spans emitted from a particular service.
This is helpful for if you have huge spans, so, like, you know, 10,000 spans, and you don't want to.
You don't want to have to buffer all of those, but you still want to do things like red metrics or service discovery or things like that, that lets you, emit all of those spans that you can perform those operations without needing to, buffer the entire trace into memory. So that's the goal with this. But I'm looking for feedback if anybody else has.
additional ideas for how to achieve this sort of thing. This just seemed like the most straightforward option.
**Israel Blancas** 08:30 Yeah, I will try to take a look to the VR today. I cannot promise anything.
**Evan Bradley** 08:34 No, no, of course, of course.
**Israel Blancas** 08:36 you But yeah, I took a look, for instance, to the new field name and everything, and sounds… sounds good to me, right? It's more like implementation details, what I have to… to take a look. I think it totally makes sense to what this.
Yeah.
**Evan Bradley** 08:56 Cool, thank you.
Alright, that's all that's on the agenda. Unless anybody has anything else, I think we can call it early today.
**Andrzej Stencel** 09:20 Thanks.
**Evan Bradley** 09:21 All right. Thanks everyone. Thank you.
**Ravishankar** 09:23 Thank you.
