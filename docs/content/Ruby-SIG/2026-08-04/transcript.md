SIG: Ruby SIG
Date: 2026-08-04
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Matt Wear** 01:18 Club.
**Kayla Reopelle** 01:19 Hi, Matt.
Pichuan.
I think this is all of us today, unless we have any… Special guests, because Hannah's not able to make it.
Meetings… share my screen… Okay, I had a couple of things… From the spec SIG… Hi, Daniel.
So, yeah, in the spec SIG today, there was a discussion about schema URL behavior with entities. I don't think this is quite ready for us yet, because we haven't started looking at entities and don't have any schema URL support.
We… Also… I think there wasn't really a ton of… Stuff today that felt relevant to our group.
Matt, were you there today? Was there anything… You wanted to go over?
**Matt Wear** 03:00 I… yeah, I… I was there, I don't think there was anything at all relevant either, so…
**Kayla Reopelle** 03:06 Cool.
And we'll move on.
Let's see, I had a few things in core. Also, at some point, I want to talk about, some issues we're having with our release workflows. Daniel, thank you for coming today. I wonder if we should just chat about that first, and then kind of go through some of the other things.
Yes, so if everyone's okay with that, we can… go there.
I think that the Zizmor PRs that we merged into Core and Contrib last week, caused some permission issues with our workflows. I'm still looking into them to try to figure out what exactly is going wrong, but both of those repos should have had a new pull request open today, and the… workflows failed for different reasons. One of them, the OTilbot token, doesn't seem to have the right permissions to do what it needs to do anymore. And then the other one felt like it was maybe a little bit more of a vague failure.
Related to the GitHub API.
But, that's kind of putting releases in those two areas on hold. A different problem that we're having… is with Ruby Instrumentation. We're still working to get our first release pull request out, and there is… a warning now, or an error that says, MFA is required for your account now with Ruby Gems, and we don't have MFA currently enabled.
I think we've left it that way to make it easier for admin, but if that is, in fact, a requirement, then we're gonna have to figure out… what MFA level we want to set, how we want to set it, or look into trusted publishing on Ruby Gems.
Daniel, at this point, I think I'll roll it over to you. I'm kind of curious, if you've done any research, what you've found. If not, not a problem at all. I'm just assuming you were here for the release question, and you might have some thoughts to share.
**Daniel Azuma** 05:14 Yeah, I… I haven't done any, actual look at it. The, We… excuse me, when we… Did… when I was working at Google, we did have to… you know, this was… this was before trusted publishing was a thing, and I did… we did have to enable MFA on our accounts. I think you have to do that once your download rate goes above a certain threshold, or…
**Kayla Reopelle** 05:44 Or whatever.
**Daniel Azuma** 05:45 Okay.
So we did have to enable MFA, and apparently, there are several different, levels of MFA. There's, UI and… there's UI and API, which is the highest level, where everything requires MFA, and then there's UI and… sign-in, I think, which is a lower level where you can still make API calls without MFA, and that level… that lower level is specifically intended for workflows like this, where.
**Kayla Reopelle** 06:16 Nice.
**Daniel Azuma** 06:17 where you have automated scripts that are publishing Ruby gems and so forth, where actually implementing MFA into that workflow is challenging because, you know, you don't necessarily have a human or a wave to inject a human into that workflow.
So, that's what we did, when… when I was at Google, is we just implemented the lower level MFA, and it just… it was just fine.
**Kayla Reopelle** 06:47 Okay.
**Daniel Azuma** 06:48 So I… that's what I would recommend, that we just, Just do that. It should just work.
It's possible, at most, we'll have to regenerate the, the API token keys.
But, It should just work.
**Kayla Reopelle** 07:10 Okay, great. Then I can give that a try today.
**Daniel Azuma** 07:14 the, the others, the other stuff, is more and stuff. I'll go ahead and look at the, the logs for those, those jobs, and, I'll go ahead and debug that stuff, later today.
**Kayla Reopelle** 07:27 Great, thank you so much.
Awesome. Okay, any other release thoughts before we continue?
Cool.
Okay, on this pull request, this one's just been open for a while. I'm not really sure… where we're at. Matt, you had some suggestions for them, and I didn't know… if we want to see those implemented before we merge this PR. It's currently marked as stale. I think we could just let it close itself. I think I've… I've pinged them once.
But we could ping them again.
Xuan, I think you also took a look at this. So, yeah, I'm kind of curious about your thoughts on… on this particular feature, and… Where we should go next.
**Matt Wear** 08:41 I know the limits are incorrect, So I'm not sure if we should, like, merge this as is, then follow up and fix those. I haven't looked at this in a while, so I'm not sure, if there was… More to be worried about.
**Kayla Reopelle** 09:09 Well, yeah, I think I would rather see… The limits implemented correctly.
in the same PR, especially since it seems limits-related.
So… Yeah, what do you think about just pinging them one more time?
And letting it go through the stale bot after that.
**Matt Wear** 09:34 That sounds good.
**Kayla Reopelle** 09:51 Okay.
The next pull request… This one… I think, yeah, we have some changes requested here. It's just kind of died off a little bit.
Matt or Xuan, since you've both checked in with him, would you mind, like, kind of seeing where this is at, or is this a pull request we would kind of prefer to let Fade. Fade into the background.
**Matt Wear** 10:27 I'm fine letting it fade, unless, unless you think we really need to reach out.
**Kayla Reopelle** 10:37 No, I think it's okay, I think that the change is requested are… There, And it's not a first… first time, so… Cool. Alright, well then we'll leave that one be.
Those were the two main ones I wanted to look at in core. I know we have some other pull requests, well, we have a lot of other pull requests that are open.
Is there anything else in here we want to talk about today? I see there's been a little more discussion on declarative config.
I don't know if we want to continue that.
**Matt Wear** 11:26 Yeah, I was hoping to spend a little more time looking at the declarative config PR before this meeting so we could have a better discussion about it, but I didn't have enough time, but, But I feel like a good… I don't know, in my mind, like, a good spot.
For this would be that we, that we kind of have the API that we want for it, at least, like, at… at a higher level, because I kind of feel like the… suggestions James had were kind of like… Not so much with the top-level API.
And he had some suggestions about how, like, about how to kind of refactor, you know, some of the things underneath that to make passing config down through, you know, these different objects a little cleaner, and I feel like that could be handled separately, and then I know he wants, He wants to be able to kind of register custom components.
And… I think that's a good aspirational goal, but, but I think it's, like.
Yeah, I think there's gonna be a lot of challenges with that, just in terms of, like, At application startup.
knowing about things, I think, you know, with auto instrumentation, We load the, We load all of our stuff first.
So, anything that's, like, custom provided would show up after the fact, which I think just leads… Not that it's impossible, it just leads to, like, a lot of… complications, I think, around startup and discovery, because you kind of really need discovery Or… I guess you would need to, like… Set up your, Yeah, it's like you would need to set up the SDK kind of last in order for that to work properly, but then… You had this issue of what if things were already kind of recorded in the beginning?
all of that. I'm not… I'm not saying any of this is impossible, it's like, we deal with this sort of stuff, but it's all… Harder than it seems on the surface.
I feel like that stuff definitely should be left out of, like, kinda… V1.
**Kayla Reopelle** 13:56 Yeah, yeah, those sound like better improvements later on, or, you know, other features off of it.
Cool. Okay. Yeah, I also wanted to look at this last week and didn't get a chance to.
So, hopefully, we can get to that this week to keep moving it forward.
**Matt Wear** 14:18 Yeah, I'll definitely make it a goal to have more things to say about it next week.
**Kayla Reopelle** 14:22 Okay, cool.
Great. Okay, anything else in… Core before we move to contrib… oh, I guess one update, because I think we've talked about this one in the meetings before. I put changes requested on it, because I think the… The kind of scope of the fix right now is a little too large.
I wasn't able to view the recording when we discussed this in the meeting to figure out what we initially talked about, but I'm a little concerned about this, like, normalized attribute encodings. I don't think it's strictly spec compliant, but feel like it requires a little more reading into the spec to know if it is or not.
But the fix at the exporter level feels really sound to me, so I would like to see that and this, like, utilities fix, So that's… that's kind of where this is at, and waiting until Bart can take another look at it.
If anyone thinks that's wrong, that's also totally fine. Just, you know, kind of put your comments in the PR so that we can keep moving on it.
Okay, contrib.
Alright, this one… is new, we've got Renovate.
Oh yeah, I opened this one recently. This is a fix for a Sinatra bug.
That came in, that's kind of a more general… rack bug.
But basically, our rack instrumentation assumes that there's only ever one app running, and so currently it only manages a single context. But this Sinatra pattern that allows you to have multiple Sinatra middlewares running at once.
That then causes problems with the context, because it's just attaching a single context, it doesn't have a list of all the contexts that are available.
Or, you know, that are really at play, and so it's getting popped for, like, a con… a middleware that's further down the train, the… Further down the list, and then when it gets back to that original top-level middleware that the context was initially related to.
The context is gone, and so this, calls to detach error is raised.
So I think… One strategy to fix this, just kind of from running tests with the example app, too, is to use, like, an array now to manage context, instead of just… Having a single one, and use, like, a last in, first out.
Process to pop.
Context off of the stack.
This is a change to rack instrumentation, so it is… potentially impacting a lot of different things, so I would love, like, critical feedback on it to make sure that this is the best way to handle this.
Yeah, yeah, so if you can take a look… The person who reported the bug hasn't been back in touch, so I don't think it's really, urgent.
But just so you're aware.
Is there anything in here?
We want to take a look at together.
Eventually, not in this meeting, but maybe… In a future one.
We have a lot of pull requests that are labeled as keep that are quite old, and I would like to… Kind of go through them, think through them, and see what we actually do still intend on reviewing and working on, or what we can close and get rid of.
Yeah. Yeah, so just something to put on other people's radars if, there's any time to kind of look at those. I know these, like, Hannah pull requests, she's picked them up and is starting to work on them again. They were drafts for some comp stability, but since we have Trilogy, I believe, figured out, she's applying those changes to these PRs, so they should be officially opened soon.
**Xuan** 19:25 I don't know.
One PR I wanted to chat about.
I think it's a resource detector for the OS.
**Kayla Reopelle** 19:38 Okay, is that in…
**Xuan** 19:40 Yeah.
**Kayla Reopelle** 19:40 Here?
**Xuan** 19:41 I think it's a country, yeah. Yeah, that's fine, so… Yeah, I'll… But it's because this person is trying to ask to merge this, but since one of the concerns is, this is that, somehow, maybe, It's not stable yet.
**Kayla Reopelle** 20:03 So I'm…
**Xuan** 20:04 One function is to really merge something that is not stable.
That's my only concern, yeah.
**Kayla Reopelle** 20:12 Hmm, yeah, that's a good question.
I guess with… the logs instrumentation… the logger instrumentation we did kind of merge something that wasn't stable, but I guess the imp… like… just our implementations of logs wasn't stable. It's not like the idea of the logger instrumentation and what it should do wasn't stable.
Does this seem like… have you looked at the stability status? Does it seem like this is something that they're actively working on making stable?
**Xuan** 20:46 to be honest, I haven't looked at them.
**Kayla Reopelle** 20:50 Okay.
**Xuan** 20:50 pretty long time.
**Kayla Reopelle** 20:54 Yeah, that's a good… that's a good question. Because also, would we eventually, if it does become stable, want this to be maintained in the contrib repo?
Most likely, I think if they're also willing to… Maintain it, that helps as well.
Which we'd need to add them to the contributor files.
Yeah, I would be curious to see, like, where the spec is at with this, and… because we, like, generally… proposals do need prototypes to… to move forward. Oh, thanks, I just saw your link.
So, status is in development.
Yeah, I mean, I think I'd be kind of surprised if… OS conventions weren't eventually stabilized?
I've been doing a lot of talking. What do other people think?
**Matt Wear** 22:10 I think… that… JS has an OS… detector in their… Those are being shipped with, kind of like the default SDK resource detectors.
So I feel like I'm not… All that.
worried about it, because I feel like… I mean, isn't the majority of contrib at this point in time unstable still? Like, we haven't really crossed that bridge?
**Kayla Reopelle** 22:49 I don't think we've stabilized anything.
**Matt Wear** 22:51 So… As long as this is spec compliant with what, you know, is spec'd today.
I think I will… I think I'm fine with it.
**Kayla Reopelle** 23:10 Okay, nice. That works for me, too.
Does that sound good to you, Xuan, or do you have other concerns?
**Xuan** 23:18 Hey, Chris, how's it going?
**Kayla Reopelle** 23:20 Cool.
Alright, any other pull requests on here?
Okay.
I'll try to add the other PRs that we looked at.
Let's see, auto-instrumentation… Matt, I'm sorry, I went another week without looking at it. I really hope that I can look at it this week.
**Matt Wear** 24:03 That's fine, yeah, I guess… I can mention, like, when I originally implemented this, I kind of… Added this functionality, that when all the instrumentation that Could be installed, had been attempted.
That it disables the trace point sweep.
It turns out that doesn't actually work in the real world, at least not without jumping through a bunch of hoops, because, like.
Things load in stages, I guess.
**Kayla Reopelle** 24:37 Hmm.
**Matt Wear** 24:38 So, like, you know, the active support constant may become available before, like, the version constant is, or something. So, like, that… that… Does not really play well with, like, the compatible check.
And you just kind of end up giving up early on instrumentation.
So, I just made it so that the trace point is always enabled, and, And it handles all of these cases, and… In reality, I don't think it is really, I don't think there's any effective changes, because for, like, your average contributor, for example, they're not using all of the instrumentation, so that TracePoint would never actually get disabled. It would only… the only situation that that would actually work is if you had you know, an exact match of, like, my app uses exactly this instrumentation, and that's what I'm bundling.
And, it turns out that the, The sweep is actually faster if you don't have to do all the bookkeeping, To be able to disable it?
**Kayla Reopelle** 25:52 So…
**Matt Wear** 25:53 Oh.
Yeah, I think Clocking at, like, 9 microseconds per sweep, which is kind of basically noise.
**Kayla Reopelle** 26:03 Yeah.
**Matt Wear** 26:04 But yeah, that was just one update to that after I started using it in some more complicated scenarios. But the good news is I have been using it in some more complicated scenarios, and it seems to be working well.
**Kayla Reopelle** 26:17 Awesome.
Yeah, I did look at it a little bit, and one of the questions I had was, like, how it does with something like, like, Zeit work?
has just a little bit of a different loading, especially in a large app? Like, do we start to… Lose performance, or are we just not expecting an app that large to probably use auto-instrumentation?
**Matt Wear** 26:42 of… It's a good question. I haven't tested it with ZItWork, and I… would… Yeah, obviously that's… an escape hatch, I guess, if you… Yeah, if it does create problems with SIG workers, don't use auto instrumentation, but I think, I think at the end of the day, we need to kind of weigh what… what we're targeting these towards, I guess, because I guess we have multiple strategies for how we can, How we can handle auto-instrumentation, and they all seem to have, some kind of gaps.
So, yeah, I guess we will just need to… Decide which ones we're most comfortable with.
**Kayla Reopelle** 27:40 Yeah.
And hope that if the use case isn't working for people, that they'll let us know.
**Matt Wear** 27:47 Yeah.
**Kayla Reopelle** 27:52 Yeah. Okay.
Cool, that's a helpful update. Thank you.
All right, anything else today?
Okay, cool. Well, thanks everyone for coming, and yeah, we'll keep chatting online.
See you guys next week.
**Xuan** 28:30 Dear.
**Matt Wear** 28:31 See you.
**Kayla Reopelle** 28:33 P.
