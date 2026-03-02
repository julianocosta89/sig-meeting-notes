SIG: Go Auto-Instrumentation SIG
Date: 2025-08-12
Duration: 12 minutes
============================================================

## Zoom Recording Transcript

**Rafael Roquetto** 00:23 Hey, Tyler.
**Tyler Yahn** 00:24 Hey, Raphael, how's it going?
**Rafael Roquetto** 00:26 I'm good, how are you?
**Tyler Yahn** 00:28 Doing well, yeah.
How was the weekend?
**Rafael Roquetto** 00:33 It was actually pretty good. There was a lot of street festivals here in Calgary.
Oh, yeah. Nice food. Nice food. Bad for the diet.
How about yours?
**Tyler Yahn** 00:44 Yeah, it was also good. It was pretty hot, so, like, not so great for being outside, but, yeah, it was, it was fun. First half was okay, but yeah.
**Rafael Roquetto** 00:57 Fair enough. Yeah. How about yours, Mike?
**Mike Dame** 01:00 My weekend?
**Rafael Roquetto** 01:02 Yep.
**Mike Dame** 01:02 I assume you guys were just talking about your weekends. Yeah, it was pretty good.
Had a wedding that we went to. It was the first time that, me and my wife had both been away from our son overnight since he was born, so… a big milestone for us, having the parents watch him. Sounds like he did great, had a lot of fun with the grandparents, but, …
Yeah, it was a Sunday wedding, so coming back on Monday, it's just kind of like, this is my Monday now. Kind of trying to get into it, but …
Fun, nice weather, it was hot, but, good time.
**Tyler Yahn** 01:35 Was the wedding in Massachusetts?
**Mike Dame** 01:37 Yeah, yeah, it was, … Oh, nice. …out near… out near Western Mass, Springfield area.
**Tyler Yahn** 01:42 Oh.
Yeah, I went to a wedding there this year as well.
…
Well, cool. We can jump in here in just a second. I don't have too much on the agenda item. I wanted to go over the milestones again.
For this next release.
But if y'all had anything you wanted to add.
You can go ahead and add it there. If you haven't yet, go ahead and add your, name as well.
And we can jump in. I see people are joining. Welcome, everyone.
Okay, cool. So yeah, I just wanted to start us off.
I think similar to what we did last time, I'm looking to try to get another release out, …
Although, it might behoove us to wait on the contribib rep repository releasing, with our latest thing that we just merged, but maybe we can just go down this, really quick. So, gRPC client, TraceHeady mixed up, we talked about this last time, this is something that, like, if we're looking for somebody to pick this up.
It was, …
fixed upstream in the Baylor repo. I think this is something I'll probably take a look at today, was kind of my idea. And so, yeah, thanks for, Nicola, for finding the PR that addressed this, and I can try to get a PR, to follow up on this, but…
Yeah.
Unless there's any other takers, I'll probably pick this up.
The Fix Other Arch subs, this is something, Ron, you said you were gonna take a look at, I don't know if you still have time to take a look at this one?
**Ron Federman** 03:29 I didn't get to it, should be pretty short, like, …
But I also don't think it should, like, block the release or something, if we want to release.
**Tyler Yahn** 03:41 Yeah, I think, … I think we probably want to release after the contrib, releases.
Well, actually, it's not too big a deal. I guess we don't have to. It's just annoying. We're depending on, like, a commit hash for the contrib repository for the auto-detect package, and so it's nice to have a tagged release for it, but…
It's also not, like, critical. Other folks can also do the same thing, so we can just release the same way, but…
Yeah, I think we have a little bit of time, is what I'm saying, so it's not like we're trying to get this out today.
Okay, well then, yeah, if it's not too big, we'll take a look, hopefully, within this next week. I'm hoping to get the GO, group. It looks like we're making a lot of progress, we might be able to get something out as well upstream.
And then, Raphael, I wanted to ask you about this one as well last week. I know you've done a lot of work on the Clang Tidy stuff in, the Obi project. I don't know if there's anything that you have, like, that you could just, like, copy-paste over to here, or if we're still wanting to, you know, nail down some of these things.
**Rafael Roquetto** 04:49 … I mean, we can definitely use what we've been using for Obi, if you guys are fine with it. It's… it's really easy, I can… this is something I could do if I can…
… important on the Eagle Auto instrumentation project. It's…
Yeah, it's just a simple configuration, and then probably run it.
And then commit to the results, and then probably we would like to…
run this on CI, like we do for… for Obi?
… yeah, I could do that, if you guys are happy with replicating Obi. This comment from AC, from me, it's just like…
Yeah, basically what's written there. If you have any preference.
And we can adjust for those preferences as well. And my only ideal sense would be, like, not do anything
alien, just, you know, there are a few different, C standards, but they are just a handful, like, common ones. I would say stick to something that's common.
Yeah.
**Tyler Yahn** 05:56 Yeah, I'm very much in favor of having some standard. I don't have really strong preferences, here, so if someone does have strong preferences, I think that, like, there's a void, and we're looking for somebody to fill it, otherwise it's just gonna be the default of what Raphael, finds.
So, yeah, like, if you have…
if you have preferences, speak up. Otherwise, I mean, I honestly… something is better. Like, the thing that annoys me more is going from one file to another in the same project, and they're, like, all over the place. So, like, as long as we have some consistency is more what I care about at that point.
**Rafael Roquetto** 06:30 Yeah, and also because then we have a linter that does the job of, quotes, nagging people.
And ensuring this, this, and then, yeah, I agree. So…
I mean, if no one has any preference, I can just migrate what we have from Obi.
**Tyler Yahn** 06:49 I think you should just do that. I think that sounds good. … If you…
Have a preference, speak now, or forever hold your peace.
**Rafael Roquetto** 06:59 That's mine.
**Tyler Yahn** 06:59 knows.
… yeah, so I… or just comment in the issue, but yeah, let's just do that. That sounds good. I mean, and also, it's, like, not, like, set in stone. We can, you know, as… we can adjust as it goes forward. I think also setting up the tooling is important, too, so, yeah.
**Rafael Roquetto** 07:15 Yep.
Yeah, there's still two tools that we could migrate. There's ClinkFormat for Enforcing format and Clink Tidy.
I think it's really useful, it's basically the linker, in the sense that it will complain if you have no
If you have any use of variables, or things like that, you know?
I can do two PRs, one for the formatting, and the other for link tiling.
**Tyler Yahn** 07:38 Yeah, I appreciate it. That sounds great. I… I think it looks… yeah, great idea.
**Rafael Roquetto** 07:43 Okay.
**Tyler Yahn** 07:44 Awesome. Thanks, Raphael.
**Rafael Roquetto** 07:46 Norris.
**Tyler Yahn** 07:47 Okay.
Other than that, those are the last few things we have in this milestone, so we're getting pretty close. actually, I forgot, maybe I'll just assign myself to this. So…
Yeah, in fact, we actually have it all assigned. So, I think, other than that, obviously, like, there's a lot more that's been done. I need to update the milestone, to include that, but we're getting pretty close to being ready for this release.
…
I don't know if there's… yeah, I don't think there's anything else blocking it, but if you do see something in this, please go ahead and add it. I think by the time of next week, I'd like to have…
this release out. I definitely want to focus on this, like, unify the EDPF program stuff going forward. I know Nicola is leaving, in just a little bit, so…
I think, you know, that's, something we'll probably be working on for a while, probably until he gets back.
To be honest, because there's probably going to be a lot of questions, and I'm not as fast as him. But, yeah, I think that that's, … yeah.
Something I'd like to do.
Okay.
Cool. I didn't have any other things on the agenda. There's definitely the goals that we could still talk about, but I think this is my priority for, at least for this next week, so maybe we can hold off on our, yearly goals and maybe check in next week on those.
So I'll pause here, and I can stop sharing my screen. Is there any other topics people wanted to talk about?
I know at the, maintainer meeting this morning, they were talking about the Observability Day, like, schedule is coming out tomorrow, so I'm pretty excited to see that as well. I don't know if people have their talks accepted, but yeah, I'm sure it's interesting just to see the talks tomorrow, so…
Yeah, I'm pretty excited about that. If you haven't yet.
signed up for the Atlanta Conference for North America. I have signed up, tentative approval to go. I'm pretty sure, Nicola, you said you have as well, right?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:50 Yeah, Mario and I both, but I had to cancel my maintainer.
**Nithin** 09:56 Good.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:56 unfortunately, family thing for the weekend. Mario will be there, I think.
**Tyler Yahn** 10:00 Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:01 Yeah, sorry, unfortunately, yeah, I didn't realize it was on Sunday, and then had to travel on Saturday for that, and missed both days on the weekend, it was impossible.
**Tyler Yahn** 10:13 Yeah, I just found out, like, somebody mentioned it was on Sunday today, and it, like, clicked in my head as well, and I was like, oh, yeah, that's kind of weird, but, yeah, understandable.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:21 Yeah, I wish it was on Monday, maybe, but I know we have the co-located events on Mondays, so….
**Nithin** 10:26 Thanks, Charlotte.
**Mike Dame** 10:30 Yeah, that's what makes it hard for me, too, is, already getting in on Sunday just to, like, make the, you know, observability Day stuff on Monday is a little tough, as much as I'd love to.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:41 Yeah, but I could fly Sunday evening and still make it for the morning because of the same time zone, but Saturday evening would be hard.
**Mike Dame** 10:49 Jim.
**Tyler Yahn** 10:51 Yeah, that makes sense. … Well, Mario should be there, though, right?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:57 Yeah, Mario, I think he's set to go. He got approval to travel, because we also have, like.
Like, our arrangement for the company, and the way we book these things, that to go through.
the standard way for everybody, because there's multiple Grafana people going, and I think…
He needs to go a bit earlier, because he's gotta arrive,
**Tyler Yahn** 11:21 Yeah, he's doing it.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:21 Or, yeah.
**Tyler Yahn** 11:22 International flight, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:23 National flight, yeah.
**Tyler Yahn** 11:28 I gotcha. Ron, are you… are you gonna be able to make it?
**Ron Federman** 11:34 Not sure yet. I really want to, but not sure yet.
**Tyler Yahn** 11:38 Yeah, yeah, it'd be cool. If you are, you should try to do the same thing with the international flight, get in early and come to the Maintainer Summit as well, yeah.
But, obviously, tentative, right?
**Ron Federman** 11:50 Yeah.
**Tyler Yahn** 11:51 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:51 I'm hoping we're gonna see each other at the hotel booth.
Throughout the conference, yeah.
**Tyler Yahn** 11:57 Definitely, definitely there, so…
Well, cool. Alright, if there's, nothing else, any cool projects, maybe, people have been working on, other than just the standard stuff?
**Rafael Roquetto** 12:16 Olby.
**Tyler Yahn** 12:17 Yeah, I know, right, a lot of that.
So, okay.
Well, on that note, I guess there's always the meeting tomorrow as well, tomorrow morning for the OB stuff, so we can talk more specific OB stuff there as well, but yeah.
Well, cool. We can end it here. Thanks, everyone, for joining, appreciate the time. We'll try to get this release out, and talk to you all next week.
But.
**Rafael Roquetto** 12:39 See ya. Bye.
