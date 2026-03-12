SIG: System Sem Conv Stability WG
Date: 2026-01-29
Duration: 30 minutes
Zoom Recording URL: https://zoom.us/rec/share/144D9D6_1z06gjB7dYEFqjx69OnbSTDyhHj0ma_c1qnBQ8kDlcZlKo76iDXZ5e5-.cQKSYxJbYZeRKeru
============================================================

## Zoom Recording Transcript

**Donal O'Sullivan** 01:41 Blue.
**Pablo Baeyens** 01:44 Ape.
**Christos Markou** 01:48 Hello?
**Donal O'Sullivan** 01:53 Hey, guys.
**Braydon Kains (Google)** 01:54 Neil.
**Donal O'Sullivan** 02:00 earnings.
**Braydon Kains (Google)** 02:05 Not too bad.
Quite cold where I'm at.
**Donal O'Sullivan** 02:11 Oh yeah? What temperature is it?
**Braydon Kains (Google)** 02:14 I don't know what it is exactly, I think it's… Negative 25C today, something in that realm.
**Donal O'Sullivan** 02:20 Holy cow, yeah, that's cold.
**Pablo Baeyens** 02:24 I don't think I've ever been somewhere.
That cold.
**Donal O'Sullivan** 02:32 Is this known? I assume so.
**Braydon Kains (Google)** 02:34 It is not actively snowing, but it was… it has been snowing. My… my car is covered, and I need to go somewhere after this meeting, so… Embracing myself for that.
**Donal O'Sullivan** 02:50 Nice.
I only had, I had one small topic to bring up, if we wanted to start, or are we waiting?
**Braydon Kains (Google)** 03:22 Sure, we can… we can get started, I… Imagine.
The rest of the folks trickling.
**Donal O'Sullivan** 03:28 Yeah, I was talking to… Roger and… Christos about this, what we were thinking… well, the idea was to promote process to release candidate in semantic conventions.
**Braydon Kains (Google)** 03:42 Yeah, that's what we're… we're aiming for. I think we're kind of… kind of blocked on me at this point, unfortunately, which…
**Donal O'Sullivan** 03:49 Hmm, I'm gonna need to…
**Braydon Kains (Google)** 03:51 find some time to finish up the things I need to…
**Donal O'Sullivan** 03:53 Finish up in that namespace before we start.
**Braydon Kains (Google)** 03:58 I think one of the things that I need to do doesn't necessarily need to block release candidate, it's something I'd like to get in, but it's not.
The end of the world, which is the, process state metric.
Hmm. Which, I… I got to a certain point on it, And then got kind of blocked when I had to figure out… when I had to, like, figure out how to handle this with, Windows, because it is a pretty… for Linux, it's a very basic and logical metric. On Windows, the model does not match at all.
And I'm… I'm… I'm reticent to… call it process.linux.status.
I don't… I don't love that.
Name.
Because… you wouldn't think something like process status is exclusive to Linux, but as it turns out, that model on Windows just doesn't work the same at all. You can't map it in a time series for just, like, an overall process.
So, it might end up being that way. I think that's probably what I will end up doing to finish that PR.
And the other one is a PR that I have opened that I… I know what to do, I just haven't finished it yet, which is marking different things as required… attributes as required, or recommended. And… in the discussion on the PR, we realized that the the description on one of the attributes, specifically for, CPU.mode on processCPU time.
the… description made it seem optional, and logically, I just kind of assumed it wasn't, and… in talking back and forth, we realized that, like, we don't think it should be optional, because it is a useless metric without the mode label attached. So, I have to submit a PR to either submit a PR to fix that and then rebase it, or just do it in the same PR. I could just do it in the same PR. It's, like, it's not a huge PR.
I think those two things are the main things that are missing for us to… Throw a release candidate together.
**Donal O'Sullivan** 06:08 Alright, so… wait half or no, I guess, is the… is that the consensus?
**Braydon Kains (Google)** 06:14 Yeah, and unfortunately, it's on me to actually, like, Put some time into it.
to fix this up, and I will… I should be… I should be able to do that soon. Yeah.
**Donal O'Sullivan** 06:29 No, that makes sense. I don't want to put you under pressure either, Braden. Should… would I open a draft PR just to get the discussion going, or would you… will I just hold off for now?
**Braydon Kains (Google)** 06:40 Do we have an issue right now for our intention to make it… to release?
**Donal O'Sullivan** 06:47 Don't… not that I'm aware of.
**Braydon Kains (Google)** 06:48 I'm a market release candidate. If we don't, Then… Perhaps an issue there to say.
This is our intention, this is what's blocking.
**Christos Markou** 06:58 We have one for, oh, got it.
But this has stabilized, not release candidates, so… .
**Braydon Kains (Google)** 07:09 it could be part of this as the parent. We could… we could make a comment on here saying that, Following the remaining items we intend to… to… Grab a release candidate, put a release candidate together.
**Donal O'Sullivan** 07:24 Yeah, makes sense, right? I can… I'll comment on that, on that issue, so about that.
**Christos Markou** 07:33 From my side, I support the idea. I haven't looked into the whole set of metrics and attributes, though.
Yeah, so I'm not sure if I missed something, or if we missed something. If we had a draft PR at some point, like, the following weeks, I guess this would help us, like, go actually through the list and see, like, okay.
How we feel about this change, and if we're confident enough to do these promotions.
But yeah, I'm open. That would be just my approach. We do something similar for Kubernetes attributes, and in that case, we went from development to alpha.
Now we are using the alpha semant conventions already in the collector, and there is another PR in semant conventions to make them better. Trask asked, why not going directly from development to release candidate, and I just, shared my thoughts there that maybe it's smoother if you go from alpha to beta, and then to release candidate. But for this group specifically, we have spent, lots of time, so maybe we can go to release candidate directly.
And do any reviews on the PR directly.
And check how confident we are about this change.
**neilyashinsky** 09:03 Normally, I'd be shy about something like this. Hi, everyone, this is Neil, but I recently ran across, and I'm… but please correct me if I'm wrong, the… I believe it was the OTEL LLM semantic group.
Was in a similar conversation, and they pointed me to, like, their standards for what qualifies as what release. But I'm so new, I forgot where it was, and I was literally looking for it yesterday.
But given that we're in the semantic business, so to speak, is there a… I wonder if there's a semantic definition of the release quality that would, rather than deciding, we just… we just follow it? Does that make sense?
**Braydon Kains (Google)** 09:40 There is a standard for, like.
once we declare something as stable, we are declaring that we will not change it in certain particular ways. There's some… there's also a definition for, like, what constitutes a breaking change, necessarily.
**neilyashinsky** 09:53 Huh, huh.
**Braydon Kains (Google)** 09:53 There's a certain class of changes that we are blocking ourselves from once we say we're stable, so we have to feel good about it, basically.
**neilyashinsky** 09:59 Right, and thank you so much, Braden, for that, and then I was just wondering if, like, because I think we were talking, if I heard correctly, we were in, like, whatever, preliminary, you know, the opposite end of the spectrum from stable, or what have you?
**Braydon Kains (Google)** 10:14 We're in development, yes.
**neilyashinsky** 10:15 development, and I thought there were some guidelines, or for lack of a better word, semantics conventions around the release Like, it was, like, a hotel maturity model, or stability maturity… let me see if I can find it, actually.
**Christos Markou** 10:29 the link here from Samanth Convent specifically, which actually, describes the stability levels, and it's actually, a copy of the OpenTelemetry generic, maturity levels, let's say, guidelines.
**neilyashinsky** 10:47 Thank you so much, Crystal. So do you think… is this applicable, or am I wildly off the mark?
**Braydon Kains (Google)** 10:52 I think that this is what… this is what we're following, and I think the… the question is, like, is there… is there much reason for our group to feel that we need to go to Alpha, and then to Beta, and then to release candidate, or should we just get to a point where we feel good and…
**neilyashinsky** 11:05 rated.
**Braydon Kains (Google)** 11:06 Great to release it.
**neilyashinsky** 11:07 Thank you so much for reading me in on that, I appreciate it.
**Braydon Kains (Google)** 11:09 Yep.
I personally feel like… We've lived with these metrics for long enough to try for Release Candidate.
In my eyes, like, we've… we've litigated a lot of stuff back and forth on this, and it still deserves one more critical comb through from everyone, I think, but I would feel pretty good about going for Release Candidate.
**Pablo Baeyens** 11:39 Yeah, I tend to agree. I think what we need, if anything, is, like, user feedback, and we're going to get that once we… have something on host metrics receiver.
**Braydon Kains (Google)** 11:52 Yeah, that's… that'll be… that'll be a big… a big thing, is that, we should… Get to a point where we can have a reference implementation of the release candidate.
And there… there are some… some technical things blocking us from Maybe not… maybe not necessarily blocking us from having an implementation, but some… some things about that host… host metrics receiver transitioning to host metric… transitioning to semantic conventions that we're not feeling technically good about yet.
Just in, like, collector libraries, basically. Like, nothing to do with our semantic convention schema.
**neilyashinsky** 12:30 More like the nature of the reference architecture itself to be… Referenceable-ish?
**Braydon Kains (Google)** 12:36 It's… it's, making sure… it's about double writing. So, like, we… we know that this change is going to be disruptive to people.
**neilyashinsky** 12:44 Oh, right.
**Braydon Kains (Google)** 12:47 Yeah, yeah. Like, we did… actually, yeah, we did talk about this last week, too. It's the same thing. Yeah.
**neilyashinsky** 12:53 Yeah.
**Braydon Kains (Google)** 12:53 We want to make sure we don't just hard swap people, like, that's not going to go over well. This receiver's too popular. So we need to be able to double-write them, and we need to try and… reduce breaking changes, but to… to this point, I have not been able to think of a panacea solution that doesn't somehow break configs. There's multiple ways we can do it to specify it nicely.
that does… Bias into some breaking change in config.
it's not the end of the world, but I'm not stoked about it either.
The thing I imagine is that there are probably, like, tons and tons of deployments of the host metrics receiver out there in the wild.
And people are probably upgrading without thinking about it, because host metrics receiver hasn't broken config.
In my entire time owning it, it's been, like, two and a half years, three years, we've never… Broken config on people.
And if we do… the solutions so far that do that risk the potential of people's metrics configs suddenly breaking under the hood, and if they've just been, like, without thinking about it, updating their collectors and running a host metrics receiver config for ages, and suddenly it's busted.
Right. Like, not everybody is as in tune of the braking changes as we are. Of, like, the refactors and the braking changes and the updates to the receiver and stuff as we are.
So I'm… I'm… trying to be very careful about how we introduce the new schema, and I can't think of a nice way yet.
**neilyashinsky** 14:32 Oh, I think I… okay, so hear me out, Braden, because again, I'm still very new, so, like, I will admit that I… I put this together on my Fisher-Price, you know, my first IDE or whatever, but what I did is, instead of… if I heard you right, you're talking about having, like, two independent feature… feature gates, if you will, is that right?
**Braydon Kains (Google)** 14:51 So that's… that's what it's gonna be. There's gonna be two feature gates, but then to go with that, there needs to be two metric… there needs to be two fields in the config that allow you to enable and disable metrics within either schema.
**neilyashinsky** 15:01 Rather than relying on two feature gates, could you use a single configuration with three explicit modes, one for the legacy, one for the dual?
and one for, like, the SEMCON, you know, the conventions themselves, the, you know, the target state, if you will, post-migration. Because that's kind of what I examine doing, so that way.
You, the error, if both are disabled to edge case, is eliminated, because you don't need two feature gates. You can use one That has 3 explicit modes, and that way, the ambiguity goes away, and it's replaced with, like, forward compatibility of metrics legacy versus a metric config keys.
**Braydon Kains (Google)** 15:47 So…
**neilyashinsky** 15:48 Does that make sense?
**Braydon Kains (Google)** 15:49 I understand why it eliminates the both disabled edge case. I don't understand how it fixes the metrics and metrics legacy problem necessarily, because eventually we're gonna get to a point where the old schema needs to go away, and so metrics, like.
Either the metrics key breaks for people because the names have all changed to be, like, new names in the metric builder config.
Or we break… Or we break them later by having our metrics, semconf and old metrics, and then swapping it at some point.
**neilyashinsky** 16:24 If I'm understanding correctly, rather than doing that, I think you define the mapping a single time. You know, the three mappings to match the three modes.
That way, then, you can either be, like, you know, unchanged, from system CPU time to then be from process CPU.utilization, then from system.file, system.usage, like the rename from custom one.
So at recording time, you can do any of the three, and then the mapping happens once.
Depending on your… whichever value you're using, the same mapping scheme will still apply for All the use cases can be, you know, handled with that.
Is what I suspect. Again, I, you know, I'm really, really new, and I haven't thought this all the way through, but I believe that that's how I dealt with this myself.
And so, I don't have a legacy framework to test it with, but I'm happy to show you everything that I wrote, and you can see for yourself, you know, exactly into the details if it's helpful.
**Braydon Kains (Google)** 17:33 Yeah. I'll take a look to see if… I'll take a look at if you… if you're okay to send it over.
**neilyashinsky** 17:39 I'm still not quite seeing how it…
**Braydon Kains (Google)** 17:44 On how it doesn't event… we don't eventually buy into a breaking change, even with that?
**neilyashinsky** 17:51 So in the alpha phase, I think you basically… it defaults to a new legacy, where you opt in.
And then, for.
**Braydon Kains (Google)** 17:58 Yeah, that part is easier.
**neilyashinsky** 18:01 Right, right, and then there's the dual, basically, support, dual. You have, like, both of them are supported for some period of time.
And then, once you get the stable.
then the default is moved over from, like, you know, from dual to the new SEMCOM, and the legacy, then, is the opt-in. And then, so legacy… eventually, you can remove the legacy entirely, but you could still support it in stable.
With the default to the SEMCOM convention.
**Braydon Kains (Google)** 18:32 So I think that… that point.
The… the part where the new version becomes the default.
That is, I think, functionally the same breaking change as what we have to deal with here, where users are not paying attention necessarily to what's the default now, and then when the default changes, the config, the YAML that they have written.
no longer works, like, their collector won't start anymore.
**neilyashinsky** 18:58 It will, though, because you've done the mapping a single time, not two times. So with the two feature gates, you have two, two mappings. But this way, you have a single mapping, and so that mapping still works, it's still valid.
It's just… it's just no longer the default.
**Braydon Kains (Google)** 19:13 But if… if the… that mapping Wouldn't work if the default is now the new schema?
I don't see how it would work.
**neilyashinsky** 19:23 Oh, cause you were… well, you were writing for… you have to… you have to spend some amount of time in… in dual mode, basically.
To prepare yourself for the cutover, yes, that's kind of the essence of this, that's the second feature gate. And so… If you… to support the older mode, you know, when you're moving… once it becomes available, and then you'd be able to emit across both the standards.
then… When you make that final cutover is less important, because they're both supported still, and stable.
They haven't… we haven't removed anything. The dual mapping, or I should say, the tri mapping, you know, it's not really dual mapping, or… well, it's dual mapping as the one supported approach, but the dual approaches still are supported in stable, because you are using… configuration mode that has 3 settings.
And so that's why, even in the legacy setting, you can still do the mapping, it's still valid.
Until you decide to cut it off.
**Braydon Kains (Google)** 20:28 But if they were relying on the default to be a certain way, and so they've… they've specified the old schema in their leg.
**neilyashinsky** 20:35 Yeah. Like, the legacy one.
**Braydon Kains (Google)** 20:37 They were relying on that being the default, so they didn't explicitly say, I am mapping for Legacy, or I'm, like, I'm configuring for Legacy, or I'm configuring for SEMCOM.
And then that default changes.
**neilyashinsky** 20:50 Oh, I…
**Braydon Kains (Google)** 20:50 The YAML that they've written to enable the old thing no longer works.
**Donal O'Sullivan** 20:54 Yeah. And so, they could…
**Braydon Kains (Google)** 20:56 It's either via feature gate or via a config flag, they could.
Like, unbreak this for some amount of time.
it's that breaking change that I was hoping to find a way to avoid.
it seems like I… there may not be a way around it, that, like, we may be stuck with that no matter what.
**neilyashinsky** 21:16 Yeah, I'll take it offline, but I am wondering if you are not using two featured gates, but one, and if the… that means the legacy can be maintained as long as it's still mapped.
And until you flip over from the legacy, the mapping should still work, because it exists, it's valid. It's only when you get to, like… after it's been deprecated or whatever, after… beyond stable, that you're comfortable making a braking change, that that mode is removed entirely. It's still… it's still supported in a backwards compatible sense, because you've updated the options rather than eliminated it.
**Braydon Kains (Google)** 21:56 So I think the… the reason for two feature gates is… is the… what Pablo linked. There's a… we… we did… we had an RFC in the collector about why we're specifically doing two-feature gates, and what the plan is for… all receivers will be following this two-feature gate mode, and I think that probably answers the question better than I could here.
I think… The main reason is… That there needs to be a way to control SEMCOM on a broader level, like, there may be users who want to be, like, anything that is announcing a SEMCOM transaction, just opt me into all of it, so I'm up to date. Right. Bleeding edge. Yeah, and so there… there kind of needs to be… multiple controls for that, either control for everything, or control for individual. If you're ready to adopt Kate's semantic conventions, but not the system one yet, then you need to be able to unbreak yourself. That's the reason we're doing the two-feature gate thing.
**neilyashinsky** 22:59 I see, I see. Yeah, I knew… thank you so much for reading me, because I figured I wasn't… You guys weren't missing something I was, so to speak. Okay, thank you. I'll read more on this and let you know if I have feedback on it. I'll throw my email in the chat, if you will, if you want to chat more about this offline, too.
**Braydon Kains (Google)** 23:14 Yep, email or CNCF Slack is fine.
**Pablo Baeyens** 23:17 Or even if you… if you want to maybe, like, take a look at the… the link I shared, Braden said, on… if there's something that you would change.
We can discuss it on GitHub, even.
**neilyashinsky** 23:29 Perfect. Thank you so much, Pablo, for the link, and thank you as well, Braden, for humoring me.
**Braydon Kains (Google)** 23:35 Yep, thank you for the ideas. I hope we can find something here, but we might… we might be doomed to some manner of config breakage at some point.
**neilyashinsky** 23:44 What wouldn't be the first time humanity was doomed to something?
**Braydon Kains (Google)** 23:47 Yes, it's true.
**Donal O'Sullivan** 23:50 So is the ideal situation that the config just stays the same? Obviously, that's looking like it won't happen.
**Braydon Kains (Google)** 23:56 Well, I would love that.
You know, I think that this is something the collectors stuck with a long time. We had a lot of receivers that we've said, oh, they're beta, like, don't, like, be ready for breaking changes, and then we just don't change them for a long time, and people just kind of rely on them.
And so I'm a little scared for what happens when we get to that point of needing to break the NB… and, like, actually exercising our beta… Privileges, basically.
**Donal O'Sullivan** 24:21 Yeah, yeah.
We end up breaking more stuff, because you're… you're waiting. The longer you wait, the more people end up using the collector, and the more people end up with a breaking change.
**Braydon Kains (Google)** 24:31 Yes.
Yes.
**neilyashinsky** 24:34 It's very much for profitability.
**Braydon Kains (Google)** 24:36 Well,
**neilyashinsky** 24:37 Oh, right, we don't have profits. Darn!
**Braydon Kains (Google)** 24:39 Yeah.
The companies we work for have profits.
**neilyashinsky** 24:44 Oh, true, yeah, we'll have to engineer that somehow.
**Donal O'Sullivan** 24:46 Allegedly.
**Braydon Kains (Google)** 24:48 Allegedly.
**Christos Markou** 24:51 For internal telemetry, metrics.
I found out, like, a month ago, when I initially raised the question to Braden, that seems to be easier to do this transition. But while trying to do this, I… before even using the dual metadata YAML file approach.
I was wondering if the MTAT Agent tool should be more, like, intelligent in a way to be able to, you know.
take decisions about the dual scheme, or the… using the legacy, or the, the stable schema. So maybe we could potentially try to think of this from this angle, and see if we can change M.Gen, and I think this would allow us to have a seamless transition in the configuration.
Maybe with some additional annotations, similar things to what semantic conventions do.
And then mdataGen, under the hood, does the whole magic, like, deciding if it should emit a metric using the dual scheme, or using the legacy, or the stable one. So users would not even notice. All the changes should happen on the, metadata.yaml files.
configuration remains the same, unless users add additional metrics, and then based on the feature gates, the generated code takes the decision which one to use. So, we add extra logic to the generated code to make this decision for us.
And I think this would be easier in the future for the receivers that will need to follow the same pattern. Instead of changing the receiver itself and handling the feature gates and the decisions there, having the generated code to take these decisions of the dual scheme, or… Yeah, I don't have anything specific.
Right now, it was just… chatting about this before, with Donald, and, yeah, maybe that's worth… Taking place.
**Donal O'Sullivan** 27:01 I… no, I agree, Crystal, so I think it might be a good shout-out. I had a quick look at this, and… like, you could change the mdata gen tool to allow Like, almost like a… Composite key, so you could have, like, a versioned I suppose, field in your schema, so, like, if you have one metric, you could have different versions for that metric, maybe? Then you don't need two different schemas, you know?
I'm not… I've been able… I've looked at it briefly, but it might be… as you say, we might be able to do something there and not break the user's config, but I'd have to look at it more. But I think it should… it might be possible.
**Braydon Kains (Google)** 27:44 I'm definitely open to revisiting, like, fixing this more broadly in mDataGen, because at the time that I made the choice, and it's now been a while since I made the design to use two metadata packages, and… the reason I did that at the time was partially because, like, it was just me working by myself, and I wasn't confident I could, like, fully design a solution for this by myself. And also.
Partially because… Well, actually, really, that was mostly what it was. Like, it seemed like there was going to be a lot of complexity in solving this in generated code, and I didn't feel confident pushing it by myself if it was going to be, like, a major refactor to mdataGen, but if there are multiple of us, including maintainers and approvers, who all want to find a way to push a better solution for this into mDataGen itself.
then… I'm open to revisiting that, rather than, like, I'm not married to that two… two metadata package.
method. That just seemed like the most realistic path at the time.
I'm… I'm… Especially now that we have an RFC for, How the feature gates are going to be structured, if we could… leverage that to solve this in the generated code, I think that would be good.
**Christos Markou** 29:09 Yeah, sounds good. I think the highlight here is that the main blocker for us is the config.
that we need to tackle. For internal telemetry, it works seamlessly, because those metrics are not exposed in the config.
Yeah. So, approaching it this way from the config perspective.
Might give us the solution.
Yeah, cool.
**Braydon Kains (Google)** 29:39 Alright.
I think we're out of time, but… If anybody has anything else… We can… Talking the system metrics channel.
**Christos Markou** 29:55 Sounds good.
**neilyashinsky** 29:55 Thanks for letting me in the sign box.
**Christos Markou** 29:58 Yeah, no problem. Thank you all. Thanks for being here. Bye.
**neilyashinsky** 30:01 Thank you, guys. Have a good one.
**Braydon Kains (Google)** 30:02 go.
