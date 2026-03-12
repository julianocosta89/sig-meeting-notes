SIG: Go SIG
Date: 2025-12-04
Duration: 23 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 00:13 Hey, Owen.
How's it going?
How's, how's the day going?
**Owen Williams (he/she)** 00:22 Pretty good. I've been doing a bunch of, like, making little tasks types of things.
**Tyler Yahn** 00:29 Yeah, those are… those are good days when you can parse it out like that. You don't have just insurmountable things that block you forever.
**Owen Williams (he/she)** 00:36 Well, this is even better, it's just, like, making tasks lists and projects and just sort of moving them around and feeling very productive by reordering everybody else's work.
**Tyler Yahn** 00:46 Yeah, that's… it's actually kind of fun. I'm doing a lot more of that with, like, AI development stuff, trying to, like.
Parse tasks just for that kind of thing, but… It's a… it's a new skill. I'm better at software development than I am at that, yeah.
Yeah, this is all for.
**Owen Williams (he/she)** 01:06 Delta temporality and Prometheus stuff.
**Tyler Yahn** 01:09 Oh, cool, yeah, yeah. That definitely sounds like a lot.
**Owen Williams (he/she)** 01:13 Yeah, exactly, exactly, and so… and it's something where it's like, you just kind of have to hope that other people want to work on it, and sometimes having a pretty project in GitHub is a way to get people excited to work on things.
**Tyler Yahn** 01:24 Yeah, I actually think that's a really great strategy, because it's like, you motivate them both sides, like, one, they see that it's really well-structured, but then you also get, like, their PM, like, just yelling at you, because they're like, why aren't we doing this?
**Owen Williams (he/she)** 01:37 Exactly.
**Tyler Yahn** 01:37 Yeah, so… Yeah.
**Owen Williams (he/she)** 01:42 This one's blocked, yeah.
**Tyler Yahn** 01:43 Yeah, yeah, exactly, yeah.
Hey Sam, how's it going?
**Sam** 01:52 Yes.
How about you?
**Tyler Yahn** 01:55 Doing well, yeah. Just, getting through the day, yeah.
Are you… you're back in the Bay Area still?
**Sam** 02:02 Yeah.
**Tyler Yahn** 02:03 You staying there for the holidays?
**Sam** 02:05 pretty much just staying at home.
**Tyler Yahn** 02:09 Yeah, yeah, yeah. That's… Same. I kind of don't like, traveling anyway, so I prefer staying at home, yeah.
Well, I only had one thing on the agenda for today. I guess, also, I should probably put my name down on the attendees list. If you haven't yet, also, go ahead and add yourself there. If you have things you wanted to talk about, please go ahead and add them as well.
I guess we can wait just a minute or two.
I can start sharing my screen here.
Cool. Yes, the only thing that I had… I wanted to talk about was the release. We're pretty overdue on that one, and, I think that we're moving along. I think there's still some things we want to try to get… Merged prior to… getting this done, but I'm hoping tomorrow it's something we could… we could do, given the current state of things.
But maybe just go through… go through what's open. So, we have… Observability, issues still open.
None of these are blocking, so I'm gonna take these and move them to the next, Can't do that anymore?
Okay. I don't know how to… Maybe go at it from a different angle.
Yeah, alright, I guess you can't move things to a new milestone from here. Alright.
Kiss reading it manually. Okay.
**Sam** 04:32 I think you can filter by the milestone on the pull request page.
**Tyler Yahn** 04:37 Yeah, they're not all pull requests, though, they're issues as well.
But yeah, actually, maybe that's a good… I don't think you can filter… Or here.
**Sam** 04:48 Based on the milestone.
**Tyler Yahn** 04:50 Yeah, and you don't have to have his issue.
Yeah, there we go, that might be it.
Okay, yeah, that looks… No, I can't.
Huh.
Don't know how to reassign now. There's no way to click it.
**Sam** 05:13 If you're only doing PR, that… that could work.
**Tyler Yahn** 05:16 Yeah, okay.
Does it have to be a PR?
Nope, we can't do that. Okay, yeah, it's just, Man, that's kind of annoying. Okay.
Well, there is one PR, but let's just, I think, maybe go through and move this stuff.
Okay.
Mmm… Don't know if that didn't sync.
Yeah, okay, cool. Alright, so then… Next up, we have the optimized histogram reservoir and the sync map stuff for, non-locking Algorithms, I see David's on the call.
**David Ashpole (dashpole)** 06:49 Yep, thank you for the review. I think it just needs one more reviewer. It is pretty substantial, so, if someone's interested, but has questions, I'm happy to Like, help as much as I can.
**Tyler Yahn** 07:03 Yeah.
I was hoping to get this in this next release. I guess, David, you missed the first part of this. We were hopefully trying to get a release out somewhat soon, I don't know timeline-wise, I don't know if anybody can commit to this.
I also know that we need somebody besides the people on the call, given, Sam also works at the same company.
**David Ashpole (dashpole)** 07:31 Probably Damien.
**Tyler Yahn** 07:33 Yeah, so we're really looking at Damien here, or FLC.
Yeah.
Why does it always come up with Mike Dick?
**Owen Williams (he/she)** 08:01 GitHub autocomplete for usernames is… very mysterious.
**Tyler Yahn** 08:06 I… I feel like the Mike Dame and Damien, like, mix-up is just, like, it is… every time, everyone always, like, it's the wrong one, yeah.
**David Ashpole (dashpole)** 08:23 Looks like I've got… I, rebased it, so it looks like I need to fix some things.
**Tyler Yahn** 08:29 No. The macOS one's been really flaky lately.
**David Ashpole (dashpole)** 08:33 the coverage? Maybe, whatever.
**Tyler Yahn** 08:36 Yeah, here, I'll show you. Probably should open an issue for this. I noticed this yesterday, Yeah, there's… Yeah, some retry tests. Yeah, this cancel context. I think there's a PR… No, this is a different one. There's another PR for this. This is probably, again, like, our, testing is using the wrong context. It's using probably the testing context, and it's getting canceled.
Or something, but yeah, this is… this has been flaky. This just needs to get rerun, or… a PR needs to get open… I'm sorry, to address that, yeah.
Can I move this to the next, milestone, David, or did we want to block on…
**David Ashpole (dashpole)** 09:26 Don't… don't block on it, but…
**Tyler Yahn** 09:28 Okay.
**David Ashpole (dashpole)** 09:30 Yeah.
You know, I would of course love if it got in, but yeah, don't block on it.
**Tyler Yahn** 09:34 Yeah, me too. This one is the same. We need another review here, right?
**David Ashpole (dashpole)** 09:40 Yes. Oh, I didn't see that you approved it.
**Tyler Yahn** 09:44 Oh yeah, I proved this one a while ago.
**David Ashpole (dashpole)** 09:46 That was before… if you wouldn't mind re…
**Tyler Yahn** 09:50 Oh, oh, right, this is actually… right.
Let me see if I can dismiss this, I don't know if you can do this anymore.
Mmm… no. Yeah. It's as good as you're gonna get. Okay.
**David Ashpole (dashpole)** 10:05 Okay.
**Tyler Yahn** 10:05 Yeah, I'll take a look at this one as well. Again, I thought I'd… reviewed it, but I… you're right.
**David Ashpole (dashpole)** 10:12 You reviewed it before I figured out that it wasn't working at all.
**Tyler Yahn** 10:18 Yeah, oh, okay, and then you switched it to a different locking structure instead of using Atomic CI.
**David Ashpole (dashpole)** 10:23 You reviewed the really complicated version.
**Tyler Yahn** 10:27 Yeah.
I think I've reviewed this as well, I just haven't clicked the button since then. I don't remember why, but I'll put it on my list, so… And then, similar, I'm gonna move this one to the next milestone as well.
**David Ashpole (dashpole)** 10:43 Yep.
**Tyler Yahn** 10:48 Yeah, I'm gonna sync map one for the, fixed… bucket histograms. I think we can wait for a response from Damien. Like, if he's able to review this in the next, like, day or so, I think we can definitely move this into the current milestone.
But otherwise, yeah, I think we'll just try to…
**David Ashpole (dashpole)** 11:04 Yeah, I would, I would love to… Yeah, this, this is the hardest one.
And then the next one will be the last value aggregation, which will be pretty trivial, that's built on that. And then the final one… will be… fund review. I… given how long it's been taking, I do feel like I should try and split that one up more. But the final one is exponential histograms, which is really, kind of good.
**Tyler Yahn** 11:33 Yeah, that one's gonna be a, that was gonna be fun.
**David Ashpole (dashpole)** 11:37 Yep.
**Tyler Yahn** 11:39 Okay.
And then all of the other ones are just on semantic convention cleanup, which is… they're all approved. The link tests are failing, and some of those other tests are failing, but This… that's how I know this, Mac one is, just… a flaky test, because that's most of these, which are also failing. Okay, so then these could probably get merged today, so if… we'll wait on a sync map.
response here, but otherwise, I think that we can… Go ahead and make another release tomorrow if we don't get a response from her.
**David Ashpole (dashpole)** 12:12 Release candidate for, declarative config.
Yeah. That's what… that was the main thing.
**Tyler Yahn** 12:19 That was the main thing, yeah, and that's why I wanted to take another look at this. But yes, let's jump in here, because there also is some more cleanup as well.
Around declared config that I know Alex is working on?
This is… this is something that Robert's still working on, stuff that I'm gonna get resolved in the next week.
**David Ashpole (dashpole)** 12:40 I don't know if that's that important for this, really.
**Tyler Yahn** 12:43 No, I don't think so. I thought this was also, like…
**David Ashpole (dashpole)** 12:47 for the PR.
But I thought there were some issues with it that you pointed out. Like, it didn't…
**Tyler Yahn** 12:53 Yeah, but we also… yeah, it was this, it was that we wanted to deprecate these other things. I think this is done.
Yeah, deprecate Default Client, yeah. Okay.
**David Ashpole (dashpole)** 13:05 Maybe it's just tracking, like, the actual removal of them after the release?
**Tyler Yahn** 13:09 So, yeah.
**David Ashpole (dashpole)** 13:12 Because we can deprecate them, and then release, and then remove them.
But…
**Tyler Yahn** 13:15 Right, right, yeah.
**David Ashpole (dashpole)** 13:17 It's not blocking the release anymore.
**Tyler Yahn** 13:20 Yeah, I agree, yep, sorry, thanks. Blanken. I don't… Oof.
Guess we don't have one.
Okay, and, yeah, maybe we'll just take a look at what Alex has, here.
Okay. So… Right, there's a whole thing with, like, trying to support experimental things, but that's just, I think, around… I think that's something we can iterate on. This is something we wanted to take a look at. Like, right now, all of our experimental functionality is just in the main package.
Which may be surprising, so this isn't a stable package yet, so I think removing those things and putting them in a different place was the idea, just to get it out. The collector really needs something, here, so that's why we wanted to move forward with this.
But yeah, how we actually want to do experimental packages is a big question.
**David Ashpole (dashpole)** 14:45 When you say they need something here, Do they… they don't necessarily care that we tag it 1.0, right? They just need the… 1.0 release candidate.
**Tyler Yahn** 14:58 Yeah.
**David Ashpole (dashpole)** 14:59 big format supported. So, like, we can release without this experimental…
**Tyler Yahn** 15:04 Yeah, yeah, so, in fact, like, the current packaging structure right now includes all the experimental stuff as well. It's just that it's, yeah, our packaging structure, we may want to change, but that is… is not… it's, like, it's not stable, and that's okay. So, yeah, yeah.
So, I think he's also got parsing Resource Detector, this is… It's the whole thing. The description field would be nice. That's coming from upstream as well, that's also just getting implemented, so, probably waiting on another release candidate for that.
This OTEL experimental configuration file environment variable is… looks good, it just needs another review at this point. This is kind of similar to what was done in, like, all of our auto packages, so if you wanted to use… an override with an environment variable to send it to something else, like, this will do that. Essentially, what it does is it appends on this, with OpenTelemetry configuration handler for wherever you point it to, and it'll add it as an option.
The option is the last option, so it should take precedence, so it's defined to take precedence here. So, pretty straightforward. I think… The tests are failing here. Just a heads up, there's some sort of, like, Maybe, maybe Alex fixed it, actually.
Let's take a look.
Yeah, it looks like you might have fixed it, actually. Yeah, so it looks like it's successful. This one could get included if, people were willing to take a look at this.
David or Sam, is this?
**David Ashpole (dashpole)** 16:33 Yeah.
**Tyler Yahn** 16:34 Yeah, okay. So let's add this to the milestone. I think this would be great to include as well. So, yeah.
Okay, cool. So really the only thing blocking… Is, yeah, I think just this one here. Did I move everything else out?
**David Ashpole (dashpole)** 16:54 Well, and all of your cleanups, I assume, right?
**Tyler Yahn** 16:57 Oh, sorry, yeah, I… those are… I don't see any blocks there so far. It's got two approvals, and it's just waiting on a, a time.
Right now. Steve, what's going on here?
How did I do this?
Why wasn't this working in the other repository?
Alright, got some A-B testing going on here. Okay, so… Yeah, I'm super confused about that. Anyways, this looks… looks ready to go, then. So yeah, hopefully get a release out, Tomorrow or the beginning of next week, I think is kind of the goal.
After we get everything merged, yeah.
Okay.
That's the end of the written agenda.
Pause here. Any other topics people had, or work they're working on they wanted to talk about?
**David Ashpole (dashpole)** 18:44 No, there was, someone at KubeCon, who was interested in… Adding some Go runtime metrics.
But, yeah, I haven't had a chance to look at that since then.
**Tyler Yahn** 18:59 Yeah, this is, if I remember correctly, had to do with, like, the memory stuff, yep. Yeah.
I can't remember this.
Yeah.
Did they ever end up opening up an issue for this?
**David Ashpole (dashpole)** 19:13 They did, they did. I can try and find it, but I'm, of course, happy if other people have opinions as well, but I… I will, at some point, go and decide. I think… It is really unfortunate that we don't have a good way of having, like.
Optin metrics via views or something?
**Tyler Yahn** 19:30 It all has to be in config.
**David Ashpole (dashpole)** 19:32 But I think that's just something we'll have to accept, and .
**Tyler Yahn** 19:37 Wasn't there supposed to be, like, some… god, what were they called? Like, suggestions or something from the API?
Yes. Oh, like, attribute suggestions or something? Like, and then, in theory, we could use the views for that, right?
**David Ashpole (dashpole)** 19:52 Yeah, yeah, I opened that, but I just don't… haven't had… there's, like, a bunch of spec stuff I'd like to drive.
And, I don't know, it's all a lot, you know?
**Tyler Yahn** 20:01 But that… but that was one of the things, right? Like, in theory, that's how we could do this as well, is, like, you could… you could do that suggestion, and then somebody could override it that way, yeah.
Okay.
Yeah, yeah, I don't… yeah.
not to put pressure, but I was just trying to remember myself, like, what the options there were.
That makes sense.
Well, cool, yeah, well, I'll pay attention, and… Hopefully, we can get some movement on that one as well.
Awesome. Well, if there's nothing else from anybody, we can end the muting early.
Thanks, everyone, for joining. Good to see you all. I will see you all in a week's time, or asynchronously.
Bye.
**David Ashpole (dashpole)** 20:44 Bye.
