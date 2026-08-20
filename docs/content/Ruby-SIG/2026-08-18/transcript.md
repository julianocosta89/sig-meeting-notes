SIG: Ruby SIG
Date: 2026-08-18
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Kayla Reopelle (New Relic, Inc.)** 00:50 Hello!
Okay, I guess let's go ahead and get started.
I know we don't have Hannah today, she's… Recovering from a sickness. I'll share my screen.
Hey, Matt.
**Matthew Wear** 01:50 Hello.
**Kayla Reopelle (New Relic, Inc.)** 01:53 Alright, so… Let's see Spec SIG today, what were some of the things I thought were interesting? I thought that this, Concurrent export calls could be going somewhere, something to… keep an eye on. It felt like there was enough discussion during it, though, where, the exact implementation might still be up for discussion.
The service, there was this discussion about trying to… Detect, like, service name to avoid unknown service.
And what I found interesting about this is I don't know if we do that automatically for Rails applications, it's something I'd be curious about looking into, and if we don't, then I wonder if… Adding some sort of… resource detector for Rails to pull out the app name, and then including it in our Rails instrumentation package, if that could be helpful for users. But also, I imagine, you know, this is pretty important for seeing your telemetry, so people have likely already said it.
Essentially the proposal was to try to discover it so that we avoid, Having, like, unknown service as the default if someone hasn't set the service name, or a detector hasn't found it.
**Matthew Wear** 03:29 And I think… Maybe the goal there is even kind of… beyond that, to some degree, like, I think… I'm not positive, but I think… from what I can tell from doing that issue, it's like… there's, like, an issue that… or, yeah, if you scroll down a little bit in the issue, I think it… shows, like, what's going on in Java, that… There are, like, resource detectors that will probably Detect your service name in certain environments.
It's like, you gotta know about it, you gotta, like, wire it up.
And, that seems to be something that, you know, is… that users don't find, I guess, in general, so there's a lot of friction in trying to get that working, so I think maybe… maybe I'm reading into this, but I think maybe the goal is to have, like, a… like, a service name detector for Ruby that was smart enough to, like, you know.
check Rails, you know, check Rails conventions and see if you can find a Rails name, and if not, maybe check Sinatra conventions and see if that matches, and then, you know.
Check.
check Hanami, and then just kind of go down the list.
And then, if you find nothing, then you ultimately just have unknown service, but you kind of have this… Service name detector that is smart enough to kind of, like, detect, like, the main… the main environments that you would expect to be running in.
**Kayla Reopelle (New Relic, Inc.)** 04:59 Got it Yeah, yeah, I feel like that… would probably be helpful. I know I've been… bit a few times, thinking that I had set the service name somewhere, and then needed to dig through unknown service to try to read something.
**Matthew Wear** 05:18 Yeah, and I think, like, the whole motivation behind this is for, like, injection, for, like, automatically instrumenting apps with, like, zero code changes.
I think, yeah, the more things that just kind of happen out of the box, the easier that whole process becomes. It's like, when you have to set off… set one-off configs, I think that, That makes injection quite a bit more difficult.
**Kayla Reopelle (New Relic, Inc.)** 05:50 Okay, got it.
Thank you.
Is there anything… You think that we should do on this issue now, or just kind of wait out the conversation?
**Matthew Wear** 06:03 We can wait out the conversation, Ultimately.
I did write something similar that we could, consider Consider if we like it enough, work in Trib.
Let me see… Let me say, dig up a link.
Yeah, it's… it would be a variation of this.
So I think the… that numbered list is actually a pretty good thing to look at.
So, it'll first try to see if there's a config application RB, or a config app RB, and then kind of pull, like, the… the application name, And that will work for Rails and Hanami.
Most web apps will have a config.ru, so you just kind of, like.
Turned the app class into, like, a… The name, and that could be a pretty decent name.
And then… Boom.
And then you can just fall back to the script name, but the script name, like… that works for a lot of languages, it doesn't really work for Ruby very well, because it's usually, like, bundle.
**Kayla Reopelle (New Relic, Inc.)** 08:06 Unbelievable.
**Matthew Wear** 08:07 suck.
So, like, script name usually ends up just being bundle for a lot of things.
**Kayla Reopelle (New Relic, Inc.)** 08:19 Yeah, I think that could be… this could be really helpful and contrib… especially as… I mean, I guess we could wait for the discussion to… settle down and see whether it belongs in Core or Contrib, wherever they… decide for it to go. Are users using this right now?
**Matthew Wear** 08:38 Yeah, I I think so.
we… yeah, like, Dash Zero has their own operator, and And, yeah, like, it has automatic injection for supported languages, so Ruby is now one of those languages, and that's kind of what this distro, like, feeds. It just kind of, like, packages up OpenTelemetry in a way that Boom.
Kind of just makes it… Hands-off for the user, for the dash zero operator.
So… So, yeah, it's getting… it's getting some use, and I think, I think as this gets more use, I'll probably get some feedback if it's… Not working well for anybody, The other thing that this is also exercising is the TracePoint installer, like.
**Kayla Reopelle (New Relic, Inc.)** 09:31 Kind of. Oh, okay.
**Matthew Wear** 09:33 adapted the TracePoint installer for this, also.
So it's using the same.
**Kayla Reopelle (New Relic, Inc.)** 09:40 Is that in here?
You see it.
**Matthew Wear** 09:44 basic scheme.
**Kayla Reopelle (New Relic, Inc.)** 09:46 Cool.
Have you had feedback on that from users yet?
**Matthew Wear** 09:52 None either way, so I feel like… Usually, if it's broken, you will hear.
**Kayla Reopelle (New Relic, Inc.)** 09:59 feedback. Yeah.
**Matthew Wear** 10:02 Just not yet.
**Kayla Reopelle (New Relic, Inc.)** 10:03 Huh.
no one has broken or praised it yet. I mean, that's… That's a sign, as well.
**Matthew Wear** 10:10 Nobody has broken it or praised it, like, it… I've done some end-to-end tests, like, that it actually, like, works on a real app, you know?
**Kayla Reopelle (New Relic, Inc.)** 10:19 Yeah.
**Matthew Wear** 10:19 "-0 installer, and… And that's working. That's kind of where I… I did find that, you know, optimistically trying to, like, disable the trace point when all instrumentation was installed, that that really doesn't work, just because of the way that you know, Code loads in pieces, in files, you know, so when certain constants become available, it looks to, like, our Our instrumentation that, oh, we can install this, that it's present, but it, you know, it might not be compatible because you haven't loaded the version constant yet, or, Things like that. It's just that… Just when a constant becomes available doesn't mean that that whole namespace has loaded, and that's usually what you need for instrumentation installation to be successful.
So, just kind of letting… letting the trace point, the trace point remain active during… during the process is… Is the right way to handle that, and… You know, the list becomes smaller over time, and Not having to do all the accounting that you had to do on the TracePoint makes it actually run faster, so it seems like it wasn't not.
Not a big deal, overall.
**Kayla Reopelle (New Relic, Inc.)** 11:40 Nice.
Nice. Yeah, I, was reviewing that this morning, and I realized that I had an older version pulled down, and so, I have a couple of comments, but I want to recheck them now that I realize I have the more accurate code.
**Matthew Wear** 12:00 Alright, cool, yeah, thanks for reviewing.
**Kayla Reopelle (New Relic, Inc.)** 12:03 Yeah.
Let me add… Let's see, okay, was there anything else in the Spec SIG that you think we should call out today, Matt?
**Matthew Wear** 12:23 So… It was talked about a little bit more last week, but followed up on this week, this, conformance.
**Kayla Reopelle (New Relic, Inc.)** 12:32 Oh, yeah.
**Matthew Wear** 12:33 test repo?
**Kayla Reopelle (New Relic, Inc.)** 12:33 Interesting,
**Matthew Wear** 12:36 So, apparently they have no Ruby apps yet, but, if you scroll down, maybe, to last week's, Let's see… Click on that trask.github.io link.
**Kayla Reopelle (New Relic, Inc.)** 12:51 Trust could give… oh, this one?
**Matthew Wear** 12:53 Yeah, let's see if that still has something. So, look at the HTTP spans.
Just look at the client's fans.
**Kayla Reopelle (New Relic, Inc.)** 13:01 And scroll.
**Matthew Wear** 13:02 allowed to, like, Ruby… Looks like, at least in his, initial experiments, he, The TLDR is, I think, in that repo, they're having these small, you know, scripts that actually, Exercise the instrumentation?
**Kayla Reopelle (New Relic, Inc.)** 13:22 with…
**Matthew Wear** 13:22 Yeah, that actually exercise the instrumentation, and then track What came out of it.
So, the goal… He was saying last time was to publish this data somewhere, and at least to He was saying, pressure people to make their, Their instrumentation conformant, more or less.
**Kayla Reopelle (New Relic, Inc.)** 13:47 Hmm, okay.
**Matthew Wear** 13:48 So…
**Kayla Reopelle (New Relic, Inc.)** 13:49 Cool.
**Matthew Wear** 13:50 Today, the question was, like, should you have, like, Weaver live checks, for example, in your… Instrumentation repos, or does this kind of, like, you know… Does this kind of replaced that? And I think the answer was, like, having both is, like, the… the right thing to do, but ultimately, I think, the, as he starts adding Ruby in there, we should review that, but we should also see… About… Trying to, you know, track which of ours are not conformant, and what we need to do to make them conformant.
And… I don't know where we actually stand, because… There was kind of, like, this… there was the early days of OTEL, where we… I don't know. There was some level of semantic conventions, and we followed those to the best that we could.
But I think some things maybe even predated those.
When instrumentation was being developed, so there's… There's definitely some, you know, inaccuracies for semantic convention.
And then they kind of had, like, the phase where, like, at least HTTP, you know, became stable.
So there's the scheme where you could, like, Where you could emit the old conventions, you could emit the new conventions, or you could Emit both.
**Kayla Reopelle (New Relic, Inc.)** 15:23 Yeah.
I can…
**Matthew Wear** 15:26 I'm just wondering where we are on… in that.
in that world, because I know, like, JavaScript, I think they actually removed the emit the old stuff already.
**Kayla Reopelle (New Relic, Inc.)** 15:37 Yeah.
**Matthew Wear** 15:37 For where we are on that journey.
**Kayla Reopelle (New Relic, Inc.)** 15:40 So where we're at right now is that we have that, environment variable in all of our HTTP libraries, and we have… I believe set the stable… as the default convention that's being emitted. I don't remember that specifically. We haven't removed the environment variable entirely, because the thing that we're waiting on is adding in the schema URLs. That was a request from Ariel before we… before he, Left the… the maintaining group.
And Hannah, I know, has that on her list. I think she was planning to start working on that now, because she just finished up a different project.
But once, I think we get those schema URLs in there so that the people who are on the old conventions, like, know… You know, what version of the conventions that mostly adheres to.
then we will start emitting only the stable conventions and pull out… right now we're doing it through, Module prepending, like, which group of conventions are installed.
So there's a lot of duplication in the code, And so we'll pull that out and just have the stable conventions after that. And then in databases, that's just getting started, so Trilogy has the environment variable ready. I think Hannah has a bunch of PRs for the other libraries, but is just opening them one at a time.
So LMDB is open, I think DynamoDB may have just been merged.
And, she's out sick today, but I imagine when she's back, she'll open some more, since some have been merged.
So we're getting there, slowly but surely. And I think seeing, too, on that, list, you know, things that we're… we're not using, because it was mostly translating the existing attributes, and I think adding a few new attributes, so there might be… more attributes that we could add. I think we recently… I had, like, a question in, the core repo looking for client address, I forget which semantic convention that maps to, but I could see users wanting more of the, you know, recommended attributes, so we could consider adding those soon.
**Matthew Wear** 18:08 Cool, yeah, I think just as this comes together, we should try to, like, figure out how we can track these things and make issues for things that are, like.
not quite conformant, and then just, yeah, scope them properly, I guess. You know, supporting old plus new is a little bit of a…
**Kayla Reopelle (New Relic, Inc.)** 18:30 Yeah.
**Matthew Wear** 18:31 We just need to, need to document how we do that, but I think… Boom.
**Kayla Reopelle (New Relic, Inc.)** 18:38 Yeah, I think we have some documentation in the READMEs, but, if we need more… I'm hoping that we can pull this out, like, in September, but if we need more in the meantime, Yeah, I guess take a look and let us know if that's not enough.
If you can't.
**Matthew Wear** 19:00 Yeah, sounds good.
**Kayla Reopelle (New Relic, Inc.)** 19:03 Alright, I'll add a link to this… Okay, I was just trying really hard to catch up on old PRs. I'm still not all the way there, but that's where most of these little discussion points come from.
I know, though, that, there's been a lot of discussion on declarative config. I haven't reviewed it yet. I saw that you approved it, Matt. Before we dive into these other things, I just wanted to see if you and Xuan had anything you wanted to talk about on it before… We kind of switched topics.
**Matthew Wear** 19:57 I have too much to say, other than, yeah, I've gone through it a few times, and just wanted to thank Xuan for bearing with all of my reviews and addressing those things, but I feel like it's coming together pretty well, so I'd be interested to see what you think after looking at it.
**Kayla Reopelle (New Relic, Inc.)** 20:15 Okay.
**Matthew Wear** 20:16 Because, yeah, ultimately, declarative config is… Something that's needed in order to add Ruby to the packaging project.
So… So yeah, I… like, Xuan seems to be, actively working on this stuff, as long as we're, you know, as long as we're willing to come and review it and have opinions, so… I think once we kind of figure out what we want to do for the tracer provider kind of arm of it, that adding it for metrics and logs should be doable.
Mostly mechanical at that point.
Boom.
**Kayla Reopelle (New Relic, Inc.)** 21:08 Okay, sounds good.
**Matthew Wear** 21:10 And… Yeah, I don't know if Xuan had anything to say.
**Xuan** 21:18 No.
Yeah, self-reviewed.
**Kayla Reopelle (New Relic, Inc.)** 21:26 Okay, great.
**Matthew Wear** 21:27 Oh, yeah. Maybe half related to this, and half related to this, I could SIG. Like, the other thing I noticed was, like.
CJ was talking about self-telemetry.
**Kayla Reopelle (New Relic, Inc.)** 21:37 Yes, yeah.
**Matthew Wear** 21:40 And, Yeah, since I still feel like I'm catching up on, like, what has happened in Ontel in the time when I was gone, like, I know we have a metrics SDK, I know it is not yet stable, but I'm just wondering what… Do we have a roadmap for that? And kind of where are we with that?
**Kayla Reopelle (New Relic, Inc.)** 22:05 Yeah, I, have a skill I've been playing around with. I can probably share the results of it tomorrow, just looking at where we're at with metrics, because I wanted to… Start opening up PRs for spec, or, like, stabilization conversations.
And just double checking to see where we're at. So I think we're really close.
I'm not aware of any major features that we still need to implement for metrics before they go stable, but Xuan was writing most of that code. Xuan, do you have any… to-dos in your mind. One of the issues, you know, on our agenda today is a conversation about a bug in one of the features, but Xuan, do you know of any major work off the top of your head that you want to accomplish with metrics that we haven't done yet?
**Xuan** 23:02 Not in my mind. I can take a look about spec to see if they add anything new.
I can't get back to you this day to, Safe, to confirm if he's ready to, Just stable or not, yeah.
**Kayla Reopelle (New Relic, Inc.)** 23:20 Okay, yeah, yeah, and, you know.
That would be helpful. I'll share what I have with my notes tomorrow when they look a little more… I'll just post them in the group channel, and then, It would be good as the writer, though, for you to also verify it and make sure it makes sense.
**Xuan** 23:45 Okay, yeah.
**Kayla Reopelle (New Relic, Inc.)** 23:48 But yeah, yeah, so I think we had some conversations about this A while back… wait, is this the right one?
**Matthew Wear** 23:57 Yeah, that's the issue that was there, but I think I followed… That, yeah, that one's actually C.
**Kayla Reopelle (New Relic, Inc.)** 24:03 This one? Okay, this one. Yeah.
Yeah, we had talked about removing the… Old metrics reporters, and… moving more towards this. I forget who was interested in it. It might have been a community member.
But I think we have all the right pieces to probably start to add these metrics, or think about adding them.
**Matthew Wear** 24:32 Cool, yeah, and I think, like.
you know, the next… the next thing is actually… I know you had worked on… Trying to add metrics to instrumentation itself.
**Kayla Reopelle (New Relic, Inc.)** 24:43 Yeah.
**Matthew Wear** 24:44 having kind of, like, a non-stable SDK just makes that… more work, I guess.
That would unlock that work.
**Kayla Reopelle (New Relic, Inc.)** 24:54 Yeah.
**Matthew Wear** 25:02 So yeah, any kind of, like, roadmap or plan to stability on this would be awesome, and it sounds like this is something you've thought about a little bit?
**Kayla Reopelle (New Relic, Inc.)** 25:13 Yeah, yeah, it's been, like, my backburner thing lately.
So, yes, I agree. I think it would be great to do that. It'd be awesome to get metrics and instrumentation.
So… so yeah, yeah, let's do a little more planning in our next meeting to see what we need to accomplish when we have a clearer view of where we're at right now.
**Matthew Wear** 25:36 Sounds good.
**Kayla Reopelle (New Relic, Inc.)** 25:38 Sweet.
**Xuan** 25:39 Just one question, so does that mean that the metrics and then possibly the logs SDK will merge to the main SDK in the near future?
**Kayla Reopelle (New Relic, Inc.)** 25:52 So… Yeah.
When I was looking at, like, the road to stability, it often seemed like it was on maybe, like, a 6-month timeline. So, even if we have all the pieces together, it could take a while.
But I don't know for sure… what the… yeah, what the best thing is to do there. I think… in Rubyland, it's nice to have, you know, one gem to install multiple things, but also to have the option to install dependencies as well, so… we could leave them as separate gems in libraries, but I know when we originally embarked on this, I think we… planned on merging them into the SDK gem. So, yeah, I feel like I don't have a good answer on what we should do.
Do either of you have a preference, or, like, an idea of what you think would be the best course?
**Matthew Wear** 26:49 I might have to think about it a little more, but yeah, I'm open to whatever.
I know with the JS SIG, everything is, like, an independent package, but I think this might… B… an artifact of generally how people built things in the Node world as well, you know, so not necessarily something that we need to follow, but… But ultimately, I do think there should be, like, one gem to install everything.
So whether the SDK is, like.
Kind of like a gem that… Oh.
you know, Bundles the necessary other gems for everything to be there.
Whether or not it is physically in the SDK doesn't really matter to me, I guess.
But… Yeah, I'd just be interested if anybody has opinions about how… how… if there's any, like, benefits to maintainability, keeping these separate.
And if so, if, like, you know, trace should really just be, you know, extracted out of the SDK, and then the SDK includes trace and metrics, and then, you know.
We add on to it as things become… mature, that's…
**Kayla Reopelle (New Relic, Inc.)** 28:12 Yeah.
**Matthew Wear** 28:12 Absolutely.
**Kayla Reopelle (New Relic, Inc.)** 28:13 Yeah, that's interesting.
Okay, yeah, well, let's, we'll think on that, too, and can add that to our agenda for next week.
Cool. Okay, so… Are we good to move on to some of these other topics?
**Matthew Wear** 28:35 Yep.
**Kayla Reopelle (New Relic, Inc.)** 28:36 Sweet.
Alright, so this one, new contributor found a bug with the way total recorded attributes is loaded. Since I last looked at the log record spec, it's changed so that attributes are allowed to be… like, updated and edited during the lifetime of the log. The log doesn't just need to be kind of emitted immediately, and because of Ruby's Infinite flexibility, This user is, like, creating log record instances, and then emitting them later on, and augmenting the attributes, and so that doesn't work with the way attributes are counted right now.
They have a fix, it's great. The sticking point right now is on what exactly this, Dropped attributes count… like… attribute in the proto file for the logs export, what exactly it's supposed to mean.
So Thompson, Tomo, or James and I are having a discussion. It seems like… The logs proto doesn't have a lot of details on this. It doesn't have any description at all, but since it's very similar to the Traces proto.
Traces Proto says that this should represent the number of attributes that were discarded, and that they're discarded because their keys are too long, or there were too many attributes. So, kind of, when there's some sort of limits at play.
Then we increment the dropped attributes count.
That… makes sense to me. There's a different inter… or I guess that's my interpretation of this.
On James's side, he's interpreting dropped attributes as being something that should increment every time Like, the attributes hash is changed, so if a key is edited to a new value, then we should increment the dropped attributes count.
I don't think that that's quite how it works in… the… In the tracing SDK right now for Ruby, but it also is a little bit different because you're just… I think adding attributes, there's not so much of the… removing attributes. So, yeah, so I'd love to unblock this user. This is a fix that they want in their environment.
So my question is kind of, what do you all think dropped attributes count should represent? Should it be aligned with limits being reached, and so attributes being discarded, or should it be related to You know, attributes that might get removed from changing the hash, and… The hash of attributes overall, and or the key being changed to a new value.
Here's the board bus, too, if you… You don'.
**Matthew Wear** 31:52 My… my instinct is that it's… Like, attributes over the limit, you end up dropping.
But… But I feel like we don't… probably need to make this up, like, if any other SIG supports this.
Cross-reference and see… See what they're doing,
**Kayla Reopelle (New Relic, Inc.)** 32:18 Sounds good.
**Matthew Wear** 32:18 Spec is unclear.
then I feel like the spec… Needs to be, Amended, at least to, like, you know, make sure that, That this can only be interpreted one way, you know?
**Kayla Reopelle (New Relic, Inc.)** 32:42 Yeah, that is a good point. Okay, so I'll, I don't remember if I've looked at other implementations, but I'll do that again, if I haven't yet.
And then…
**Matthew Wear** 33:00 And then if we are the first, I do kind of feel like this falls into spec interpretation realm, which means probably a spec SIG.
A spec question, and maybe, Asking it at the spec SIG.
**Kayla Reopelle (New Relic, Inc.)** 33:14 Okay.
Sounds good. Alright, I'll look in that.
And… yeah, if we need to wait until the spec SIG next week, we can.
Yeah, I'd just like to get it out for him soon.
**Matthew Wear** 33:31 I guess James said he asked.
Some questions in the spec channel as the area feels underdefined.
**Kayla Reopelle (New Relic, Inc.)** 33:37 Yeah, he did, and no one responded. Yeah.
So, yeah, I think bringing it to a meeting is probably good. The other place I found that I considered posting is that there is, like, a logs… specific… a Slack channel, like a log spec Slack channel.
So I could bring it there as well, the logs… Spec meeting is at the same time as this one, so can't really bring it there.
But maybe, maybe I'll post in that logs.
spec channel this week and see if we can get anything else before the spec SIG on Tuesday.
**Matthew Wear** 34:21 Sounds good, yeah.
**Kayla Reopelle (New Relic, Inc.)** 34:35 Alright, cool. Okay, so the next one is this… Xuan, I know you've been talking with Steven about this in Slack.
But this bug report, It's long, there's a lot going on. I think that this… Demonstrates the issue well, that we just have Some things behaving, calculating unexpectedly in, asynchronous instruments.
And he had a few… Questions or kind of decisions that he was hoping could be made?
To help him move forward with a fix.
**Xuan** 35:22 Right, right, so, oh, yeah, sorry, I forgot he posted his stuff. Oh, I'll tickle today, yeah.
**Kayla Reopelle (New Relic, Inc.)** 35:29 Okay, sounds good.
Nice. Yeah, if you… if you can take a look and comment on it, that would be great. And then, if you want to discuss anything further, we can chat about it next week.
**Xuan** 35:44 Sense.
**Kayla Reopelle (New Relic, Inc.)** 35:46 Yeah, no problem. Thank you.
Okay… Okay, the last step of the GitHub pages deprecation is deleting the GitHub pages branch. It seems like the fix that… James… Maid is working, and all of the redirects are happening.
So, I'm just trying to find it, but I guess I don't need to demonstrate it. It's working, so does anyone have any concerns about deleting the GitHub pages branch? I think it's fine, I just… it felt like a… Big-ish branch to delete independently.
**Matthew Wear** 36:38 Seems fine to me.
**Kayla Reopelle (New Relic, Inc.)** 36:41 Okay.
Awesome.
Alright, so this next one is, we've had some bugs with RAC.
context management in a few different cases. This one was reported back in March with, a fiber-related framework, specifically Rage RB, which this person is a maintainer of.
And… because we just have a single context that we store on rack instrumentation, Fibers, you know, can be… Passing things around, things might… and the wrong thing might get finished, and so down the line, The detach calls wouldn't match, and the wrong context could be popped, and we'd be getting an error.
A little bit later, we had a bug report.
about Sinatra, and using… kind of, like, multiple apps, or using Sinatra apps as middleware inside of the same rack environment would cause a different context error. I guess the same error would be raised, kind of the same thinking, just not dealing with multiple fibers, where, You know, one middleware would have its context popped, it could be the wrong one, and so when the, you know, one that was further up the chain eventually wanted to finish their span, the context would be gone, and we'd be getting these detach errors.
So, I had had a fix for that one that was kind of putting context in an array, so that that way we had maybe, like, a last-in, first-out approach. That was before I reviewed this fiber-safe PR.
And I don't think… I think there's a better solution that we can figure out together. I worked with, this fellow to kind of Merge the two, and so now the proposal is to store… the context in rack in a hash, and to use the request itself as the key in that hash.
And in addition to just storing the context token in the span, we also store the current fiber, so it works for those fiber frameworks, like Falcon and Async and Rage.
And this seems to be working well in example apps. I think… It solves both of the issues, but because I helped contribute the solution, I don't want to be the only one to… kind of approve it and review it at this point. So, it's mostly a request that, like, if you have some bandwidth this week to take a look, I would appreciate your feedback.
Any questions?
Sorry, what'd you say, Matt?
**Matthew Wear** 39:43 I said, I'll take a look.
No questions, but from what you said, the… This solution sounds like it.
Like, it has some potential, so…
**Kayla Reopelle (New Relic, Inc.)** 39:57 Great.
Thank you.
Yeah, and since it's rack, it just… it feels like it's underneath so many things that… The more eyes, the better.
Alright, what is this one?
Oh, yes, Xuan, thank you for commenting on this. Oh, I see you approved it now.
That's changed since I last looked at it.
I was curious about what we thought the best solution would be here, but since you've looked at it, I wonder if you want to share what your thinking is on it?
**Xuan** 40:35 I think he made a valid point about adding this, because I saw it's in front of spec, and also, Go, they also use a function.
Oh, sorry, the Kabul to do this stuff, so… I… yeah, I've approved, but I also just wanted to get a… be back to see if the carbo is the right call. I don't mind to use the carbo since we really have a lot of carbo.
For the, for the, for the options, so… Oh, yeah.
Yeah, to sum up, I think he made a, valid, yeah.
That, yeah, for these kind of links, or link spans, yeah.
**Kayla Reopelle (New Relic, Inc.)** 41:25 Okay.
Sounds good.
Alright, yeah, I'll take another look. I feel like it's… it's kind of in a funny area where… I wasn't sure if it's something that… You know, like a spam processor, or… A collector, something or other should be taking care of it, but, Yeah, maybe, maybe this is just the right solution. I'll look at it again today.
Okay, and then this one, it… sounds like… a lot of the other OpenTelemetry repos are running CodeQL directly in the pull request and getting comments, in the PRs.
I think right now we have CodeQL set up.
But, things are getting missed.
I haven't noticed this personally, just in the security and quality area, but because CodeQL and, like, Zizmor can create a decent amount of comments and things in PRs, I wanted to get some feedback before enabling this on the admin side.
Do you guys have preferences or thoughts on integrating CodeQL into Ruby repos, I think whatever we do in Contrib, we'd probably also want to move to Core.
**Matthew Wear** 43:06 Overall, I'm for it.
Let's see… how would this work, though, exactly, and do we have any other repos where it's actually turned on, where I can kind of see what we're… Signing up for?
**Kayla Reopelle (New Relic, Inc.)** 43:36 Let's just try the collector.
I haven't found… a specific pull request with that example, and so that's something that I can… pulled together.
I think what I've seen before… is similar to, like, what we've been getting for Zismor, if that's how you say it. There's just some comments in pull requests about security concerns that are found by CodeQL.
I don't know if we need both tools, since Sizmor is around now.
That might be a follow-up question for Trask. I think he knows more about the tooling.
But we can try… Another one, and see…
**Matthew Wear** 44:28 This would just be, like, a comment on a PR, if there was a security issue.
**Kayla Reopelle (New Relic, Inc.)** 44:33 Yeah, I think so, like, in the code itself.
**Matthew Wear** 44:37 Consumer.
**Kayla Reopelle (New Relic, Inc.)** 44:42 The… that shows here.
Mmm… No examples there.
Yeah, and I… I could be wrong, I mean, maybe it's showing up CodeQL… Someplace else, like in the Security tab.
But I'm pretty sure it's making comments.
So, yeah, if we don't have any… specific objections or concerns, I can… work with Trask. If you want to see more examples ahead of time, I can put those together, too.
I suppose we can also always pull it out if we don't like it.
So… Maybe that's an easier approach.
**Matthew Wear** 45:37 I have… I have no objections, if… If this is still valuable, even with Zizmo, then… been added.
This is more… Supersedes it, then maybe we don't need it.
**Kayla Reopelle (New Relic, Inc.)** 45:52 Sounds good.
Cool, Okay, I guess my last… we kind of talked about TracePoint and your PR over there already. Matt, was there more that you wanted to go over? I mean, I added this to the agenda, so I just wanted to follow up on it, mostly, since I wasn't here last week.
**Matthew Wear** 46:13 No, thanks, thanks for the reviews and calling it out. That's all I'm just waiting for, is some feedback.
**Kayla Reopelle (New Relic, Inc.)** 46:20 Sounds good.
Oh.
**Xuan** 46:26 I post a, I post a PR, you can see, I got some review from the, this more, I think, I think Zoomer already includes those, Pokio, so… We'll have this, Maurice, is enough.
**Kayla Reopelle (New Relic, Inc.)** 46:44 Oh, thank you.
**Xuan** 46:46 I think this more is, like, a standard, cost scanning tool for all the wholesale… well, not all the tools, but for the… a new OTL repo, I guess.
**Kayla Reopelle (New Relic, Inc.)** 47:00 Yeah, I remember seeing… Yeah, like this one.
I haven't posted my review yet, but, because I wanted to go through it a little more. But yeah, I think this… Feels like enough.
Okay, so… I guess, maybe I'll just check in with Trask to see if he has any… like, known differences between the two, reasons why we should include both, but otherwise… Sounds like we could just lean on Zizmor.
And… try to, kind of keep CodeQL where it's at.
Does that sound right, Xuan? Does that sound good to you?
**Xuan** 47:50 Yeah.
Yeah, sounds good. Thanks.
**Kayla Reopelle (New Relic, Inc.)** 47:54 Thanks for the example.
We'll add that.
Someone's here, yeah.
Okay, yeah, kind of last question, we've been getting a lot of contributions for the OTLP common library in the core repo, but we don't… that library isn't released, it's not a dependency right now of any of our other exporters.
it does seem like we're wanting to move more towards shared code. Do we want to think about… trying to get it ready to release, or integrating it further. I think there's just a few… pull requests right now related to it that I'm not quite sure what to do with since, it's not kind of a first-party gem right now.
**Matthew Wear** 49:02 I'm fine, either way, one thing, One thing I noticed, though, is that, OTLP Common… GemSpec?
I think it is, It's… It depends on Protobuff?
**Kayla Reopelle (New Relic, Inc.)** 49:27 Mmm,
**Matthew Wear** 49:28 it.
**Kayla Reopelle (New Relic, Inc.)** 49:29 No, it looks like just the… This is old.
**Matthew Wear** 49:31 OpenTelemetry common, this is not OTLP common.
**Kayla Reopelle (New Relic, Inc.)** 49:34 Oh, okay, thank you. Exporter… comment… Jumps back. Thank you.
Yeah, so it does have protobuf dependencies right now.
**Matthew Wear** 49:48 So I think that, That is likely to cause issues with, anybody that has a protobuff dependency, whereas if you look at our exporter.
we just are greater than or equal to 3-something, so it's a much wider spread, I guess.
We're not fixing it, yeah. So we should match that, whatever we do.
**Kayla Reopelle (New Relic, Inc.)** 50:14 I'm… Okay, yeah, that's a great catch.
Like, I think we've… I think the main concern… common the last time we talked about it was testing, but there's been a lot of testing added to it, and I think there's pull requests for more So, that's not as much of an issue now.
Xuan, I remember you had some… You opened an issue about, like, protobufs and sharing them amongst exporters a while back. Would… Opening this, do you think, help resolve those issues, if this was, like, a shared gem that they could all install?
**Xuan** 51:25 Oh yeah, definitely. I think this is the right call.
Oh, but we probably also need to… Some kind of a, dependent port, like, or, or, renovate that to, OpenPR to update the… Portal version?
**Kayla Reopelle (New Relic, Inc.)** 51:45 Oh, yeah, yeah.
That's a great point. I didn't realize it wasn't doing that already.
**Xuan** 51:54 And I think once it's out, and then… Now we can move on to update those, ask orders to users.
**Kayla Reopelle (New Relic, Inc.)** 52:03 We can… sorry, say that again?
**Xuan** 52:05 Oh, we can, we can have a PR to… for other exporters, like Nature Cyprus, Expert audiences come in.
**Kayla Reopelle (New Relic, Inc.)** 52:14 Yeah.
Good point.
Alright, great. Then… Let's see, I don't remember which pull request exactly… are related… I think this one… And this one, perhaps? But, but yeah, yeah, they'll… We can take a look at those pull requests later, but it's good to know that… we're on the same page. I guess, does anyone want to take this on, of trying to see… what we need to do to get OTLP Common ready to release.
**Xuan** 53:05 I can… I can keep eye on this.
Okay. Dude.
**Kayla Reopelle (New Relic, Inc.)** 53:11 Great, thank you so much.
Wow, we went the whole hour! I feel like we never do that. But thanks, everyone, for the discussion. Before we go, we've got, like, 5 minutes left. Is there anything else that we want to talk about today?
**Xuan** 53:32 I'm good.
**Matthew Wear** 53:33 I'm good, too.
**Kayla Reopelle (New Relic, Inc.)** 53:34 Alright, sweet. Well, thank you both. I will see you next week.
**Matthew Wear** 53:39 Alright, thanks.
**Xuan** 53:41 Okay, thank you.
Thanks.
