SIG: Go Auto-Instrumentation SIG
Date: 2026-02-03
Duration: 8 minutes
Zoom Recording URL: https://zoom.us/rec/share/96hXLb2U4BTku4AZsmHkhhunypOMwLFE9XzdOocHQJ7O4LHrj5yPgERtM9jpm81M.9HZIIkY6G6RiweSF
============================================================

## Zoom Recording Transcript

**Tyler** 00:12 Hey.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 00:12 Hey, Tyler, how's it going?
**Tyler** 00:14 Good, good, how are you?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 00:16 I'm good.
You didn't go to Hotel Unplug, right?
**Tyler** 00:20 I didn't know… I'm still here in the States. How about you?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 00:23 No, me neither. Oh, okay. Last minute, sort of… I was able to go. I had an appointment, I wasn't able to go, but then I was able to go, but I couldn't find a decent flight.
**Tyler** 00:34 Oh, yeah, fair enough. Yeah, that would have been quite a trip, all the way to Brussels. Yeah, that one, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 00:42 Oh, yeah.
It seems it was great. I got some feedback from Mario today, and he loved it.
**Tyler** 00:49 Oh, really?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 00:50 Lots of good discussions, yeah. I was more than 100… People participated, community people, and… Lots of hotel maintainers.
**Tyler** 01:01 Yeah, I've seen some reactions from people as well, and they were saying it was pretty great. And so, yeah, I don't know the specifics. I heard there was, like, actually a lot of good, like, presentations.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 01:11 More than… more than people could go to all of them, so, yeah, yeah.
**Tyler** 01:16 Yeah, it sounded pretty cool. I, I don't know if they're gonna do more, like, over here.
Like, they had that one in Seattle a while ago that was pretty great.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 01:26 I see.
**Tyler** 01:27 Yeah, I, like, that was, It wasn't last year, so it must have been, like, 2024.
And my favorite part about that was I could drive to it, so… Yeah. Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 01:39 Oh, yeah.
**Tyler** 01:41 Yeah.
But yeah, it's like, it's always tough to, like, get somebody to travel for just, like, a day.
event, you know, yeah. But, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 01:50 I know, I know. I think they were thinking maybe it was, like, Fosden could kind of lure people in.
**Tyler** 01:56 And I think it did. I think that people were kind of already planning to go there, or had thought about it, or that put it over the edge, but yeah, I think that, like, yeah, especially, like, the one that they did in Seattle, it was, like.
I don't think there was anything else going on, I think it was just that, and it still had a pretty good turnout. I'd say, I don't know, about 100, but pretty close to 100 people, maybe, like, 80, something like that, showed up, and so, yeah, it was a good community, so, yeah.
Yeah.
Are you going to KubeCon in Europe?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 02:24 I am, yeah, I agree.
**Tyler** 02:25 Oh, nice.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 02:26 accepted.
**Rafael Roquetto** 02:27 What is it? Oh, sweet.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 02:29 Yeah, I didn't propose it. It was, like, I was just added, by a co-author. Andre, you remember the guy that came that wanted DNS?
brackets, Tracking Inovi?
From Causeley, Andrea showed up, and oh yeah, I heard…
**Mike Dame** 02:47 You giving a talk with Andre? Andrea?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 02:49 Yeah, so…
**Mike Dame** 02:50 leash your head.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 02:50 Yeah, Andre, yeah, Andre, like, so he submitted a talk on DNS and put me as co-author, and I was like, sure, whatever, I don't even know what this talk is about, and then, he got in. He's really cool, he helped us with some… I was doing some, like, OpenShift-specific stuff, and he knows that.
**Mike Dame** 03:07 Thought about that, too, so… really nice guy.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 03:10 Yeah, great, great, great guy, yeah.
**Tyler** 03:14 Is that Observability Day, or is that, main, main conference? Main, main, main track, yeah. Oh, nice, yeah. Awesome.
That must be great.
Yeah, I think there's a chance I should be there as well. Oh, nice. Not 100% yet, so… but, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 03:31 That's great. Yeah, we have the hotel booth and all.
**Tyler** 03:34 Yeah. I'm arriving late for Preservability Day, I think I'm arriving…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 03:38 2PM or something?
On the Monday.
**Tyler** 03:43 Yeah, and then there's, like, again, the Maintainers, summit.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 03:48 On a Sunday? Oh, really?
**Tyler** 03:50 Yeah, it's like a day negative one, so, yeah, it's, it's definitely… The KubeCon North America one was tough. Like, there was definitely some, some, some people there, but it was definitely not as well attended, I think, as it has.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 04:04 Oh.
**Tyler** 04:04 Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 04:06 Yeah, I completely forgot about that.
Well…
**Tyler** 04:10 I don't think you're alone.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 04:12 And now, flights are booked, everything, so…
**Tyler** 04:16 Yeah, if you're coming in on a Monday… that's the other thing, is, like, it's kind of like what happened with the North America one, where, like, what you're doing is you're asking everybody to travel in on a Saturday, and, like, that cuts into a lot of personal time, you know, it's like…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 04:28 That's right, yeah.
**Tyler** 04:29 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 04:30 Same for Monday, right? I mean, observability Day for me would… I would have to leave on Saturday night.
Yeah. My whole week is shot, so…
**Tyler** 04:39 Yeah.
Yeah, I… I… if I go, I'm gonna try to… spend some extra time there, but yeah, I… again, like, super tentative on what that actually means right now. It may turn into me not actually going, so who knows? Oh, okay.
But… Mike, are you… are you planning on joining? And EU?
**Mike Dame** 05:01 Probably not, no, not EU, but we're looking at, like, the Observability Summit, and just been trying to do some KubeCon North America stuff this year.
Actually, when does it use, what, next month?
**Tyler** 05:13 March, yeah, end of March.
**Mike Dame** 05:15 Orange, yeah. Yeah, I just moved, so I'm, like, trying to… down a little bit. Yeah, I went from Massachusetts to New York, so, oh, okay.
**Tyler** 05:26 Boo. Come on, dude.
**Mike Dame** 05:30 I got family out here, but, yeah, it's… it sounds like, it'll be a good time, so I'll have to catch… I'll definitely catch the recording of your talk, Nicole, and if, I didn't… was anyone else… did you guys say you were giving talks, too, or…
**Tyler** 05:42 I'm not giving a talk, no.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 05:44 No. Just one oldie, right?
**Rafael Roquetto** 05:46 No, I'm not even going. Like.
**Mike Dame** 05:50 My brother's getting married the same weekend, so…
**Tyler** 05:55 What's the, observability conf, Mike, you're talking about?
**Mike Dame** 05:59 The… the… what's that, the open source summit?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:02 one in Minneapolis, or…
**Rafael Roquetto** 06:05 Yeah.
**Mike Dame** 06:06 Yeah, SRECon's another one that I know we were… we've been talking about trying to get to.
**Tyler** 06:11 Oh, nice, yeah.
**Mike Dame** 06:13 I've never been to that one. I've pretty much only been to KubeCon and DevConf, the one that you and I did, Tyler, so… I need to get to some more conferences.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:21 Yeah, this one's great if you can get in, yes. I submitted talks last year, two of them, and they got rejected, so…
**Mike Dame** 06:30 Wow. Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:31 Alright.
I think I prefer a local crowd.
But… or maybe it was another one. There's another one, Open Source North or something? Oh, yeah, they're… they're two… I'm mixing them up now. I think I submitted to Open Source North last year.
That's also in Minneapolis, yeah.
**Tyler** 06:50 Oh, nice, yeah.
Yeah, the SRE conferences are also really fun. I've been to, I think, one of those as well?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:59 Casser is great, yeah.
**Tyler** 07:00 But that was probably, like, 7 years ago, so, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:05 password's gone.
**Tyler** 07:06 So, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:10 It's much smaller than KubeCon, though.
**Tyler** 07:12 It's super small, yeah, and I kind of like that, because, like, there's a lot more, I think, hallway conversation that gets sparked because of that, and, like, yeah, it's way more, yeah, I definitely like that.
Well, cool. I'm looking at the meeting notes, I don't see anything on the agenda. I didn't have anything in specific to talk about. I could pause here, if anybody else had things to talk about, I think everyone's… yeah, it looks like everyone's already added their name to the agenda.
But yeah, there's tons of work going on in the background for me, so… Yeah, I don't have too much to say here.
But yeah, we could probably end the meeting early here, and we can plan on… Continuing the discussion tomorrow as well. Seems to be a lot of meetings.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:06 Yep.
**Rafael Roquetto** 08:07 Sounds good.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:08 Yeah, nice catching up.
**Tyler** 08:09 Yep. Alright, bro.
**Rafael Roquetto** 08:11 Jason?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:12 Bye. Bye.
**Rafael Roquetto** 08:13 Bye.
