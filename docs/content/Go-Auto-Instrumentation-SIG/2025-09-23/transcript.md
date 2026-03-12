SIG: Go Auto-Instrumentation SIG
Date: 2025-09-23
Duration: 10 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 00:54 Hey, Rafael.
**Rafael Roquetto** 00:56 Hey, Tyler, can you hear me?
**Tyler Yahn** 00:58 Yeah, yep.
**Rafael Roquetto** 01:00 Okay.
How's it going?
**Tyler Yahn** 01:02 Good, how are you?
**Rafael Roquetto** 01:04 I'm good, thanks. Hi, Mike. Hi, Nicole.
**Mike Dame** 01:07 me, it'.
**Tyler Yahn** 01:08 Hey.
Yeah, sorry, just getting things, together here. Probably start in just a second. If you haven't yet, go ahead and add your name to the attendees list. If you have agenda items you wanted to talk about, please go ahead and add them there. We're also pretty light today, so… If not, it's gonna be a short one.
Mike, do you know if Ron's, able to make it? Sorry, I'm looking at…
**Mike Dame** 01:48 Oh, no, yeah, I… I don't know. He sent a couple messages, but it's also Rosh Hashanah, so he might not join him.
**Tyler Yahn** 01:55 Okay.
No worries. Well, if that's the case, we can probably jump in here. Let me start sharing my screen.
Cool.
Awesome. Alright, so, only one thing on the agenda. This is something that Mike was interested in talking about, around the Auto SDK, and the fact that we don't have any, docs on it. This is the thing where we probe the SDK that is by default in the global.
Which I think is, it's a phenomenal feature, that we are not… popularizing enough, as Mike is pointing out, here and elsewhere, like, so I think that there's, like, some great, opportunities here for, let alone just adding docs, but probably a bunch of other things. So, yeah, hand it over to you, Mike, sorry.
**Mike Dame** 02:57 Yeah, pretty much what you're saying. We've had a bunch of, users, not totally understand how to use the manual span integration, and this is, you know, just something upstream that we support in our, you know, in Otagos, and so it's, just something that, like, I don't have anything that I can point people to, and people really want to know how to do this. I had, you know, someone the other day, I was asking Tyler about the We're initializing, like, a global trace provider, and almost didn't believe that, you know, you could run OTEL spans without a trace provider, and I was trying to say it's actually the opposite, like, this will conflict and not work if you set one, so… because every… when you look up OTel span, you know, examples everywhere, they all say trace provider, there's, like, nothing for this, so… I just kind of wanted to… throw, like, a, you know, kind of stub together. I don't think this needs to be a very intense dock, but like Tyler's saying, it's a very cool feature that we should be popularizing, and there's also some kind of gotchas with it, and things to know about how it works. One, just to, you know, use it correctly, but also to kind of answer some questions that people have, or that people, I think, almost don't believe how it would work, or don't understand.
that this is something that is already available, that you're importing. The version requirements, that's kind of something I tried to allude to in this, so… Yeah, I'm thinking that it would kind of fit under the, just that Go Zero code section. I kind of looked under the Obi docs, and it could go there, too, if we have a good idea of where in there it could go.
But I didn't want to, you know, I don't know where would be the best idea, so if we can find a good section for it, I'm happy to open up a PR, just to kind of get it started and get the discussion, you know, get some feedback in there. It's easier than doing it in a Google Doc, and kind of get this page fleshed out, cover how the Auto SDK works, and what to know about when you're using it, so… Yeah, that's pretty much it. I think our action item here is decide, you know, what would be… should it be its own subheading under here? Should it go under the OB docs? I think either one is fine. So what does everyone else think about that?
**Tyler Yahn** 05:07 Yeah, I didn't realize that the… Obi is different than Go. I mean, I guess that makes sense, right? It's more than just Go. But yeah, maybe… Yeah, I think Go's probably fine to have it here. I was thinking, because, like, Java has this as well, like, you know, they've got a bunch of different sections, like a Spring Boot starter seems kind of equivalent, I think… so I think that that's something that we could probably just put at this top level, that makes sense to me, having a dock right here.
But yeah, I'm open to other places.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 05:44 Sounds good to me as well.
**Mike Dame** 05:46 Cool. Yeah, I mean?
**Tyler Yahn** 05:47 There's nothing that we couldn't, like, also link, if we need to, from…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 05:51 I'm older.
**Mike Dame** 05:53 Yeah, I mean, it absolutely should be… that's why I think that it'd kind of be a mutual link, like, this says… this is what Obi's using when you go to that page, and then when you go to Obi, it says if you're using Go, doing manual spans, links to here, and that's, you know, that's where it's all gonna… it's gotta be its own, like, section somewhere, so it's just deciding where to put it.
But if undergo looks good, I'm happy to open the PR. I mean, I definitely need some feedback from, you know, Tyler, probably Ron too, Nicola, anyone that worked really on the Auto SDK, but I kind of get the general technical ideas, so I'll kind of scaffold it out, and Then you guys can correct me and throw some feedback on the structure of it.
**Tyler Yahn** 06:37 Yeah, I guess that's kind of my question, is did you want feedback in this doc, or just wait for the PR?
**Mike Dame** 06:43 No, I was just… we can just do the PR. I kind of threw the doc together just, like, while it was fresh in my head, just to show this is the sort of thing that I'm thinking of, and then I thought, well, I'll share that out, but I'll basically paste this into a PR. I think review is a lot easier to do on GitHub than in the Google Docs.
So I'll just… I'll do that, and we can do it there, and I'll link the link in the notes here, too, and share it out on Slack.
**Tyler Yahn** 07:08 Okay, yeah, that sounds good. Yeah, because, like, by and large, this looks great. There's, you know, small details that I probably want to, maybe think about a little bit, and maybe provide feedback, but otherwise, yeah, I'll just wait for the PR then.
**Mike Dame** 07:21 Cool. Thanks, Ash. I'll open that and send it out when it's ready.
**Tyler Yahn** 07:26 Yeah, thanks for putting that together, I really appreciate it. I think there's, like you said, like, a lot of value there.
Okay, that's it for the agenda items we have. I was looking at open PRs, there's nothing that we haven't already gone over, other than, linter PR, and milestone stuff, not a lot of movement there either, so I think there's nothing really to talk about from a progress standpoint there.
Any other topics people wanted to talk about that aren't on the agenda? Maybe I can stop sharing my screen. That are maybe top of mind?
I know it's also kind of a busy time of year, with, talks getting presented, and KubeCon, and other, other conferences, and… I could just go down my list of things I'm working on, but… I'm sure everyone's got their own.
Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:23 Yeah.
At least for me. Okay. It's really hard.
**Tyler Yahn** 08:31 Yeah, I know, it's also, like, pretty exciting. We're getting towards some… like, it seems like always at the end of the year, you always get some pretty cool things, so…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:39 You know?
**Tyler Yahn** 08:39 Yeah.
It's, it's officially fall these days, so…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:43 address.
**Tyler Yahn** 08:44 Yeah.
Well, cool. Alright, if that makes, sense, we can have a short meeting. I'll keep an eye out, Mike, for your PR. I think if you do make a PR to the OpenTelemetry.io.
Just tag us, like, the, the, the group for the approvers in the docs, or in the document, just because I don't think that one we automatically subscribe to, so, yeah.
Challenge.
**Mike Dame** 09:12 Tag the, the Go Instrumentation Maintainers group, one of them.
**Tyler Yahn** 09:17 Yeah, do the approvers, though, just, I think they might be the same, but there might be one person. I don't know, but just, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:25 I'm not a maintainer.
**Mike Dame** 09:26 I'll tag everyone, you know, because I think it's the eBPF side, but also, I think, the SDK side, which… there's definitely some overlap, but…
**Tyler Yahn** 09:34 Whoa.
**Mike Dame** 09:35 Looking to both of them, so…
**Tyler Yahn** 09:36 Yeah, yeah, yeah, good point, good point. Yeah, definitely want, eyes on it from them as well, so…
**Mike Dame** 09:41 In that case, maybe we also do want to link it from the manual SDK, GoDocs, and say if you're writing spans with using something like OB or eBPF, here's things to know about, you know, enriching these manual spans with eBPF, too. That could be… Another good spot to…
**Tyler Yahn** 10:02 Yeah, like, maybe we can look at the docs on, like, what the global, setup for the SDK is, or the API, and, like, if… If there's… yeah, if there's something that just says, like.
If you don't set it, nothing will ever happen. We could put a little caveat in there and be like, nothing will ever happen unless…
**Mike Dame** 10:19 Or even a caveat that says, if you're using eBPF, don't set it, or… Yeah, yeah.
**Tyler Yahn** 10:24 Yeah.
**Mike Dame** 10:25 you know, both.
**Tyler Yahn** 10:25 Yeah.
**Mike Dame** 10:25 So, yeah, okay, so that's a good note, too.
**Tyler Yahn** 10:29 Yep.
Okay, cool. Alright, well, we'll keep an eye out. Quick one, happy to get back to doing all the other work. So, yeah, good to see you all. I'll see you all probably tomorrow, or in a week's time. Until then.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:41 Right?
