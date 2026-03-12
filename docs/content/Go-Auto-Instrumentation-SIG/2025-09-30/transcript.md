SIG: Go Auto-Instrumentation SIG
Date: 2025-09-30
Duration: 10 minutes
Zoom Recording URL: https://zoom.us/rec/share/H6widOpt6FS6GrdWv6CmE1Gams3IfaPjZaRn109LDiIeXQ9ze4reQopzxcFE9heV.QLKu6zDjfvxUTrQZ
============================================================

## Zoom Recording Transcript

**Mike Dame** 01:59 Hey, Tyler.
**Tyler Yahn** 02:01 Hey, Mike, how's it going?
**Mike Dame** 02:05 How's it going?
**Tyler Yahn** 02:06 Good, yeah. How are you?
**Mike Dame** 02:09 Good.
**Tyler Yahn** 02:11 Nice.
Yeah, just, chugging along, yep.
I know… This is probably gonna be a light meeting. I know Nicola and Rafael are both out. There's a Canadian holiday today.
**Mike Dame** 02:29 Oh, yeah.
**Tyler Yahn** 02:31 I don't know if…
**Mike Dame** 02:32 Bronze.
Let's see, I think… I think Ron should be able to join.
Though it is also the holiday season in Israel, but… I think tomorrow he's off, so it might be… Might be taken off early, because it's evening for them, so it's, you know, the Friday before.
Holiday, tech, you know, for them, the day before a holiday.
**Tyler Yahn** 03:01 Yeah, yeah, okay, that makes sense.
Well, I didn't really have anything… on the agenda, other than I wanted to ask the question of whether we wanted to reduce the frequency of these meetings. Seems like the topic list has gotten smaller and smaller the past few weeks, so I didn't know if we wanted to just reduce it to, like, every other week instead of having it every week.
**Mike Dame** 03:26 Yeah, you know, we could probably do that, I wouldn't mind that. It seems like the OB calls are kind of the main, factor for this.
And, you know, there's obviously a lot of overlap between the two SIGs, too.
So yeah, I think, like, I'd be down with it. You'd probably want to check with everyone else, too, but I don't think anyone else would mind.
**Tyler Yahn** 03:50 Yeah, maybe just post this in the Slack channel then?
**Mike Dame** 03:54 Yep, I'll let you go ahead and do that. Yeah, I just like keeping the separation of, like, concerns between what this achieves and what Obi achieves, but that's, you know, if there's not issues all the time for this, then we don't need to be meeting about, you know, this… this is… this project's kind of in more of a… I guess it's not to say what we could… we could work towards getting this to, like, a stable state, right? Wasn't there still… what happened with, like, the, the C?
you know, like, trying to standardize those C…
**Tyler Yahn** 04:30 Yeah, I mean, that's… that's kind of like the… That's it. Like, yeah, if we can standardize, like, our probe definitions across the different distributions, I think that then there's a line of sight on getting some sort of stability in both projects, to be honest. Yeah, and so, like, yeah, I mean, the other project doesn't even have a release yet, that's a whole other thing. That's true. But, yeah, so we're working on a lot of things at once, but, I mean, I definitely know that, you know, Nicola's a big part of that. He's obviously out today, and he's… working on presentations, he's working on other, you know, Grafana-specific stuff, so it's going slower than normal, so we probably have to have somebody else… I mean, I'm trying to pick up the slack as well, but I also am, like, overloaded on that, so…
**Mike Dame** 05:11 So, I mean, I think hammer out… I guess, hammer out the details and, you know, keep pushing on the OB side, and that kind of is a driver for… for this, we're going to be looking more at LMD using this, too, as, you know, I'm meeting with Sally again later today.
But yeah, let's drop this. I'd be all for it, I don't think anyone else would complain either, but I'll let you post.
**Tyler Yahn** 05:36 Yeah, I mean, there's nothing stopping us, like, if there's more velocity all of a sudden, to reestablish every week. That's not…
**Mike Dame** 05:43 That could be a problem. So.
**Tyler Yahn** 05:45 Yeah, I just figure, especially until at least the end of the year, I think maybe every other week sounds reasonable.
**Mike Dame** 05:51 Yeah, when everyone's busy there, you know, holiday season's coming up and everything, too.
**Tyler Yahn** 05:55 Yeah, exactly.
**Mike Dame** 05:58 Good work on that, outage the other day, too, by the way.
**Tyler Yahn** 06:02 Oh, yeah.
**Mike Dame** 06:05 fun, I… I wasn't much help, but I'm glad that, you know, we at least had this in, like, hotel control.
**Tyler Yahn** 06:15 Yeah, that would have been rough, had it happened, like, a year ago.
**Mike Dame** 06:19 Yeah.
**Tyler Yahn** 06:20 Yeah, but, I mean, there's all kinds of things that needs to happen.
I think it addressed there. I think the Netlify…
**Mike Dame** 06:28 approach is fine Yeah.
**Tyler Yahn** 06:30 I mean, because you're just serving static files, essentially. They just need to be configured as to, like, how to generate those static files is all the only thing, so…
**Mike Dame** 06:39 Yeah. I mean, that's the whole idea of, like, donating this project to at least give, like, the community the ability to migrate it, instead of trying to migrate… like, we would have never been able to do both of those steps at the same time and, like, reach a consent, like, had it happen.
**Tyler Yahn** 06:55 Yeah, I agree. Like, I think we did the right thing, it's just… I… I just would need… I need, like, 5 of me to be able to start working on these other things, so, yeah.
**Mike Dame** 07:08 Yeah, well, I mean, other people had ideas about that, too, like, I think it was, like, Damien and Austin, you know, like, that's the whole point, is now it doesn't have to be you that does it, it can be, you know, other people.
**Tyler Yahn** 07:21 I… oh, I'm… I'm 100% on board, I just, like, I… they need to do it, like… like, that's the thing, like, somebody just needs to do it, like…
**Mike Dame** 07:30 I'm surprised it went this long, but it's, you know, it's a squeaky wheel problem, right? You know, it's…
**Tyler Yahn** 07:35 Yeah.
**Mike Dame** 07:36 We donated it, and there was all this noise about, let's, you know, get it migrated over, and then it worked for a year until it broke again. Now the noise is back, and can we keep making noise?
**Tyler Yahn** 07:48 Yeah, I mean, that was why I was also just, like, I don't… I really didn't want to change the application itself, because, like, it has been working so successfully for so long. And it… this past incident would have continued to be successful if, like, the DNS records hadn't been messed with, you know? So it's like… there really isn't any problem with the application. Like, I am sure from a cost perspective, it's cheaper to store some static sites over probably a number of hosts, you know? So, like.
That is a good motivator, but then, like, it's just, like, yeah, there's also risk associated with that, so, yeah.
**Mike Dame** 08:24 Yep, I mean, I get it. It's… it's a lot of work, but… Yeah, it's… it's up now. Good job hopping in on that, and, you know.
it's a small little app that clearly serves a lot. I mean, I know when we were doing it, we were thinking that, like, oh, most people should have it cached, and it shouldn't be an issue, but, like, when it goes down, it goes down. OpenTelemetry goes down.
**Tyler Yahn** 08:45 Yeah. And our adoption is so high that everyone all of a sudden starts being a little frustrated by that, yeah, which scary, yeah.
Which is, like, I mean, like… Yeah, like, that's actually a good… I mean, like, I think… having, like, a CDN also in front of it would also be helpful, but, like, you know, you can't really get around DNS, like, when…
**Mike Dame** 09:10 Or certificates, right? Like, so…
**Tyler Yahn** 09:13 there's not, like, a duplicate, like, redundancy you can provide there, it's like… but it does kind of say, like, you know, like, yeah, the impact of this is severe. You know, one of the other things we may want to look at is, like, like, you know, maybe Netlify actually has some CDN caching across, like, the globe, so… because, like, that's another failure case is, like.
If the app actually did go down, then we'd be pretty, you know… Yeah. Yeah, in a lot of trouble there. Well… I don't know. It's also, like, rolling that back is not that hard, so I don't think that that's too big a deal. But yeah, I agree, like, I think there's just, like.
from a, SRE perspective, there's definitely a lot that I think could be analyzed and done here. It's just, like you said, like, it's just not a… Squeaky wheel, so, yeah.
**Mike Dame** 09:55 Yeah, and that's why it was so tough to get it moved over to a hotel in the first place, was because it was just sitting there, and it was working.
So…
**Tyler Yahn** 10:05 Yeah.
**Mike Dame** 10:06 Motivation of people.
**Tyler Yahn** 10:07 I guess you're right, it's just, it's more about, like, the… the hidden, risks that are, are sitting there, potentially, so I, I think that, yeah.
It's definitely something we'd love to… I'd love to look at other options for, but I'm also, like…
**Mike Dame** 10:25 Yeah, not super motivated when something's working like this, but yeah.
It's understandable, for sure.
**Tyler Yahn** 10:32 Yeah.
**Mike Dame** 10:33 Well, I mean, it sounds like we can, probably cut the meeting short, I don't need to keep you on here, but I just love chatting.
**Tyler Yahn** 10:40 Oh, yeah, absolutely, yeah.
Cool. Well, it's good seeing you, man.
**Mike Dame** 10:44 Yep, you too. Have a good one.
**Tyler Yahn** 10:46 Good, right?
