SIG: Ruby SIG
Date: 2025-09-23
Duration: 59 minutes
============================================================

## Zoom Recording Transcript

**Arjun Rajappa** 00:31 Cool.
**ericmustin** 02:09 Hello, hello?
**Ariel @arielvalentin (ATX, USA)** 02:12 Hey there, Eric, how you doing?
**ericmustin** 02:15 Tooin'.
Good.
Doing okay.
Good to see you. How are you?
**Ariel @arielvalentin (ATX, USA)** 02:22 Doing well. Thanks for asking.
Cool.
I saw that in Slack that Kayla said she's not gonna make it today.
Has she been the moderator for the meeting most of the time?
**ericmustin** 02:40 Yeah, I think, Wendy may have also been here. I was not here the past few weeks, So, I'm not sure, but yeah, I'm happy to drive, or if you want to pick the, the wheel back up and, you know, get back on the horse, happy to…
**Ariel @arielvalentin (ATX, USA)** 02:57 I feel weird.
**ericmustin** 02:59 Hell.
I'll share my screen. All good.
But, yeah, I'll be honest, as my… this point, it's kind of a stock thing, which is, like, I'm not particularly… I have not done any real review or preparation for this meeting.
I think we can all see my screen.
Today is September 23rd, we're all here.
I work at Elastic now, for context, if you're wondering.
Okay, yeah, I think, I don't, I don't know… oh, hey, Hannah, I, usually this is about the… The gang.
Schwab might come as well, but… Happy to get… Jump right in.
Did anyone happen to attend the Spec SIG?
Same. I, too, did not… But… We've been doing a pretty good job of time boxing, like a little 5-minute or so recap, so I can… We can quickly review and see if anything pops up.
If no one else, mines? Let's see… some updates came back from the entity SIG, which… I don't… Think anyone here has any specific… Questions on at the time, but… And I haven't been following too closely, so I'll…
**Wendy Smoak** 04:43 That looks like maybe what I was asking of?
The problem where when you add instruments, you can never get it back?
**ericmustin** 04:51 Oh, wait, no, this is a meter, not an instrument.
We are looking at.
**Wendy Smoak** 04:57 I was looking at the meter provider get meter name, but that's still not… that's the… that's the meter, not the…
**ericmustin** 05:05 I think they're providing, I guess, examples of how you'd access the entity.
Which, having just seen Mission Impossible Dead Reckoning and Final Reckoning back-to-back on a plane, is what the bad guy is called.
Mission Possible, so this is weird to me.
It's a terrible movie. Don't see it.
Okay, okay, anyway, it's like they're adding some, I guess, like, a higher level, abstraction that… and contains details about the session, maybe this is related to ROM not having the concept of, like, a session.
I'm not entirely sure. I'll keep going, though. So anyway, there's some discussion on that. There's discussion on some of the logging, configuration options that are available.
Which… is, I also, you know, Wendy, you may have more context here? I know you've been using logging, but, I think they want to allow, like, you to specify what the severity is, and then… trace-based is maybe saying emit things as traces, or… attach trace ID, perhaps?
I'm not sure.
It has been merged, so if people… Are interested in this subject, And have been working with the logger.
I would encourage them to check it out, because it looks like there's some additional specifications That have been added to the SDK configuration.
**Wendy Smoak** 06:42 So it got merged to the back, and now we need to implement it.
**ericmustin** 06:46 Here?
**Wendy Smoak** 06:47 Is that what happens? Okay.
**ericmustin** 06:49 We would, yeah, it would trickle down, I think. We'd now, it would be up to us to implement.
**Ariel @arielvalentin (ATX, USA)** 06:54 I don't think we have.
**Wendy Smoak** 06:54 The minimum severity thing is interesting, because right now you have to filter in the collector.
**ericmustin** 06:59 Yeah. This is also, I think to Arrow's point, using file-based config?
But I, I'm sure you can use a process. It seems… maybe there's a way to… Add it.
Via code as well. Yeah, and I think there's some improvements here for having to… run… do your own processing, okay.
Yeah, as you can tell, I've reached the scope of my knowledge.
So we'll keep going.
Okay, something, I don't know. Are they extending some of the, like, there's, like, more attribute op values that are possible?
I had seen that. I think that came up last week, as well, or a few weeks ago.
That probably will be a long-running thing.
They want to add, some more complex options, so… Yeah, still open, I'm sure, if people have opinions on this.
**Ariel @arielvalentin (ATX, USA)** 08:00 Alright, is that for the attributes generally? So, even on spans?
**ericmustin** 08:06 I believe so. So it would extend… it would, I guess give more options, which we may need to… Let's see… There's an OTEP? Okay, boy, there's a few things. There's an OTEP related to this.
Or… extending attributes to support more complex values.
**Ariel @arielvalentin (ATX, USA)** 08:32 Right, so, so if… The scope is on any attributes for metrics, resources, instrumentation, scope. That's great.
**ericmustin** 08:39 Yeah. Long overdue.
Yeah, I think, it's still… I guess the OTEP has been accepted. Well… My… shocks, are we?
**Ariel @arielvalentin (ATX, USA)** 08:50 And they've got the Golang prototype in place also.
**ericmustin** 08:52 Yeah. So… Yeah, this may be something we have to keep in mind. Let's get smart, just… sounds like we'll have to update. We… I know we have a lot of internal Kind of like… Coercion, and we end up with some… There must be some… I'm sure people will start complaining soon enough if we are putting things as nil, and they are valid, so… Okay. Kubecon's coming up.
They also mentioned… that's cool, And, oh, JMACD has something to say. Please pay attention.
When he's talking, he… is talking about… okay, so, and then there is, I guess, ongoing work around the updates to sampling, across OTEL.
I know they are pretty actively working on that, But they are going to deprecate, I think, what we now use, which is the trace ID ratio-based thingy.
and have a more, I guess, feature-rich probability sampler?
I think one of the long-standing issues is that, like, the… probabilities and sort of, like, what things… what rate things were sampled at isn't, like, propagated or exposed, so you can't do fun things like upsampling of, you know, like… getting metrics on post-sampled traces. You can't, like, up-count… what am I… I don't know the language to use. You can't, like, you know… If it's been sampled at a 50% rate, you don't know that it's been sampled at 50%, so you can't, like, multiply by 2 to get the appropriate metric representation.
So they are actively working on that, but I know it requires SDK changes, as well as New processors in the, collector, and then I think, like, modifications of existing processors, so it will, I'm sure, be a mess.
But all for the best. If you want to go far, go Together.
That's all I got for the Spec SIG, 10 minutes.
If anyone has anything else they wanted to add, we can… we can hop into it. Otherwise, I see there is something over in, core.
So we can hop into that. I wasn't sure who put that on the chat.
**Ariel @arielvalentin (ATX, USA)** 11:10 Oh, sorry, I should have, annotated that with my name, but… I just wanted to point out that.
You know, some things that we don't… actively look for, but I'm always looking for, are end of life.
So, Ruby End of Life 43.1 already happened.
3-2 happens in, 6 months?
So, it might… mean, wanting to freeze these versions of the SDK in contrib?
So that we don't have to worry about maintaining…
**ericmustin** 11:44 Yes.
**Ariel @arielvalentin (ATX, USA)** 11:46 insecure versions of Ruby, right? That's been the policy from the beginning.
**ericmustin** 11:50 And .
**Ariel @arielvalentin (ATX, USA)** 11:53 I feel like that's the area where I might be the most help, is kind of just being like, You know, the… End of life manager? I don't know.
We have to find… Like, use specifically? Yeah, because that's the part where it's like, I feel like I can still contribute.
**ericmustin** 12:11 Right.
Sure.
Oh, I'm sorry, let me… Yeah, I think… why can't I find the gem spec? Right down.
**Ariel @arielvalentin (ATX, USA)** 12:23 Why can't you find a gem spec? Because there's one gem spec per director.
**ericmustin** 12:27 Yeah, yeah, yeah, yeah.
Gosh, golly. I'll look at the SDK, for example. But basically, you want to, hmm.
You're saying we should bump, we should bump this?
**Ariel @arielvalentin (ATX, USA)** 12:38 Probably? Yeah.
And get rid of any tests that are associated with 3-1.
**ericmustin** 12:44 Yeah.
Hmm… that… I wonder if… and there's… I mean, I'm not, I wonder if there's any, sort of, like, glue, Cody-type behavior we could ever drop, now that we're… I don't know, I'm trying to think out loud, but .
**Ariel @arielvalentin (ATX, USA)** 13:03 Oh yeah, is it making… having RoboCop, Bumping RuboCop also to minimum version of the language helps with some of that.
**ericmustin** 13:12 Hmm.
Right. That makes sense.
**Ariel @arielvalentin (ATX, USA)** 13:15 And, because what'll happen is, if new rules are implemented.
Say there's, like, a preference for one thing versus another?
Rural Cop will help us see that.
**ericmustin** 13:29 I see. Yeah, that sounds… like, reasonable, code, cleanliness and quality things to do.
we… I think at minimum, let's all, I can, after this call, I can make an issue mentioning.
Yoel, and that, We'll need to bump… we'll need to go around to all the various gym specs, bump them… Ideally, try to update. It might be a good time while we're in there to update Rubicop, too.
Whatever major version or minor version is, you know, in line with what we have for our own Ruby, compatibility?
And, yeah, at least document it so that If folks do want to pick up that work, it's available, and can be assigned.
Well, that sounds good to me. I… Let me leave a note here.
Right.
**Hannah Ramadan** 14:30 Is that the kind of thing where we would need to, like, announce, like, an end of support?
Kind of thing, and give, like, a 3-month lead way, or we could just, like.
Rip it out, or, like, stop testing and stuff.
**Ariel @arielvalentin (ATX, USA)** 14:45 I think, In the past, what we've done is, we used to put a post-install message in there.
And then we got some feedback that I was like, that's super noisy.
So we can continue to use the post-install message, we can do sort of, like, a patch release that has… or… A version released that says, hey, look, we're, Freeze to this version… well, freeze to the previous version, we will no longer be supporting this after this date.
And then we release another, you know.
Another version after that.
We… that's the only way, really, that we've communicated it, is through the post-install messages.
**ericmustin** 15:29 Yeah.
**Ariel @arielvalentin (ATX, USA)** 15:29 Is there a better place that we could announce that?
**ericmustin** 15:33 I mean, also that, you know, when running bundle install or whatever, like, things will fail loudly if the min version is… Unsupported, as long as we bump the gem specs.
I, it's also worth noting that, like, that's… it's not, you know, if people have… their own end-of-life policies at, like, the organizations they work for. Those might be out of lockstep with… they may have their own particulars about How many years back they support things and stuff like that?
So, yeah, to… yeah, Hannah, to maybe not answer your question, I have no idea, what the thing is. It sounds like… Yeah, I don't, I don't want to… I'm always hesitant to put more debug logs, or more worn logs, or whatever. People always complain.
But, it might be nice to give people a way to at least know, like, see it once or something.
Okay.
Just, so yeah, TLDR, I don't know.
If that helps.
**Hannah Ramadan** 16:44 It'd be, like, some, like, a notice in, like, the changelog or something. Yeah.
Thanks.
**ericmustin** 16:51 That's a not… I mean… I think just having some… like, it's always nice, especially when people hop into the Slack, like, hey, I have a question, like, just being able to point to, like, a link with, like.
the little markdown, you know, query param, being like, yep, read more here, is always nice, rather than having to re-explain things over and over.
So… Okay, let's, I'll add a note.
Alright.
Well, if anyone else has any questions about CORE?
We can… let me get rid of this junk.
**Ariel @arielvalentin (ATX, USA)** 17:33 So… I have a, like, a… Curious design question, so… As we add more core components, or like, you know, metric readers… The log export and all.
Each batch processor that's associated with those is spinning up a new P thread.
Between all of… each one of them?
Is there a… Was there any discussion around, sort of, like, figuring out how to use… We're kind of, like, changing the way that that's… Done so that, we can control how many… Of those can run in parallel.
Will we attempt to run in parallel?
**ericmustin** 18:23 So you're saying we have 3 background threads, basically, for, like, you know, the log exporter, metric exporter?
Trace, you know, span exporter.
**Ariel @arielvalentin (ATX, USA)** 18:32 And even for the metrics, I think that there's, like, multiple things happening there, because there's the interval…
**ericmustin** 18:38 Hmm.
**Ariel @arielvalentin (ATX, USA)** 18:40 I don't know enough about the SDK, you know, the specification itself.
**ericmustin** 18:44 Right. So no.
**Ariel @arielvalentin (ATX, USA)** 18:48 And so… I was wondering if it made sense for us to be, like, you know, to try to… Examine that a little more?
**ericmustin** 18:58 Right, like, there's a single background thread or something, and it just checks all the stuff in the, you know, it goes and checks the spam buffer to see about if it can export, checks the metrics buffer. I, something along those lines, or give someone some… I can understand… someone, especially from, like, the performance engineering side, be like, hey, by the way, like, all these apps, this just got rolled out, and all of a sudden, like.
There's extra… you know, it's just, like, a bunch of… especially when we're deploying stuff, and, like, people probably, like.
aren't using, like, many metrics things right now, for example.
Yeah, I could see that being problematic.
And it would be nice to have a way that's not… That's just, like, config where we can limit that, rather than having to go and basically, like.
manually say, like, okay, we're not… we're only adding the tracing SDK, or things like that. I, I don't know if it's been discussed. I don't recall when I was here, but the thing is, I haven't been here too frequently.
Joan would have the most contacts, obviously.
Or maybe, like, Robert or something, who has done, you know, previously attempted some of the metrics implementation.
Yeah, okay, I mean… like, off the top of my head, like, I'm curious what Python's doing, or, you know, like.
I guess JavaScript's not the best example, but, like, I'm curious what some similar languages are doing, Or whether it's just a tax that people… everyone's incurring? .
**Ariel @arielvalentin (ATX, USA)** 20:34 Yeah, yeah. Or it's like, is it a bad idea, at all, right?
**ericmustin** 20:37 Yeah, what's the… why are you?
**Ariel @arielvalentin (ATX, USA)** 20:39 One thread that is just very busy doing all of it.
Yeah.
Yeah.
**ericmustin** 20:44 Listener.
**Ariel @arielvalentin (ATX, USA)** 20:45 I know some libraries are kind of, like.
You can run these in single-threaded mode, so they're… Effectively part of the parent process.
**ericmustin** 20:54 Right. Or running in threaded mode.
**Ariel @arielvalentin (ATX, USA)** 20:58 And it depends on, like, if you're using a… Fork model versus doing a multi-threaded model for your… for your runtime.
It's just, there's gotta be some way for us to… Understand the implications of turning each one of these things on.
**ericmustin** 21:14 Yeah.
That's fair. I wonder what the… yeah, it's like, I wonder what the trade-offs are. I guess… Yeah, so I guess there's then some contention on that thread between, like, the span buffer can't be as large or something, if it has to be… if they're all being, you know, all the buffers are being used.
or some… there would need to be some specification on, like, what's the dropping behavior that you do as things, you know, how do you measure those… how do you make those trade-offs? I think it's all valid questions that… I have no idea on, but, we… I mean, I think, you know, like, Arielle, as a user, if you're seeing user feedback, which is saying, like, hey, this is problematic, I would like to understand how this is addressed, like, I think that would be the… if anything, that might be a more effective avenue to get it looked at than being like, hey, I'm a maintainer with a hypothetical question.
**Ariel @arielvalentin (ATX, USA)** 22:10 Like.
**ericmustin** 22:10 Would be my… seeing how things work in… in OTEL. Generally, the end users tend to have, you know, people are just excited to see feedback come from them.
So, yeah, I'm not, again, I'm not running this, really, in production right now, so… I don't have the context.
Might be nice to, you know, next time Francis Robert are in the SIG, hear what they have to say on the matter, as well. Okay, why don't we, Let me make a note on the thing, so… Oh, gosh.
Probably out dent.
There we go.
Team.
Okay.
**Ariel @arielvalentin (ATX, USA)** 24:02 Thanks for, you know, Humoring me there.
**ericmustin** 24:05 No, no, it's… I appreciate it.
Cool. I mean, I am curious to hear about, I saw the Rails events announcement, or, you know, like, release.
So I'm curious, too, in the back of my mind, I was like, oh, sounds like we have work to do, like, it sounds like we'll have to, like, update our implementation.
to use these. But yeah, I'm curious… I have done no other work than that, so, like, if no one else has any core questions or feedback or whatever, burning thoughts, we can move to contribib.
Are there any new issues or new PRs that need to be reviewed?
**Ariel @arielvalentin (ATX, USA)** 24:40 Game 4?
**ericmustin** 24:42 It's like you've done this before, Oh, okay, well, it's like, one second, maybe let's start with the issues. Anything super funky? No, nothing new.
These are some feedback, some user feedback, which… I think they're kind of spec limited, but valid.
I don't know if anything new has been discussed over the past few weeks. I know is remote.
is… we're open to that. They're working on a PR for it. It was blocked for a long time.
by, are SEMCOM?
Like, our protos were old, that we were using?
**Ariel @arielvalentin (ATX, USA)** 25:18 Yeah, no.
**ericmustin** 25:19 Francis, this guy, another Francis until he updated it, which he did.
**Ariel @arielvalentin (ATX, USA)** 25:23 Yeah, so I'm wondering, like, is there some process that we can automate here, where when a new protobuf is released, that there's, like, a PR that gets opened on our side that auto-generates the protos?
And forces us to take a look at it to see.
**ericmustin** 25:39 Right.
**Ariel @arielvalentin (ATX, USA)** 25:42 if we're behind, up to date, whatever, and I mean…
**ericmustin** 25:45 there's something we want in the proto.
**Ariel @arielvalentin (ATX, USA)** 25:49 Even if we don't want it… I know that Protos are backward compatible, but Google Protobuff generation is, like, if we let it go stale, and new versions of Protobuffs comes out, we have these incompatibilities with…
**ericmustin** 26:00 Yeah… Yeah, it seems like… Theoretically, it just ought to be something that we should be able to, you know.
Automate and merge without really having to… be too, you know, we… there shouldn't be any concerns about minor upgrades.
I don't know if we… yeah, we don't do that. I don't know if there's anything possible. I am always curious, like, well, how are other SIGs managing to, like, keep up to date on this? Although they may just be… clued in more? Like, it might just be plugged in more.
Yeah, I don't have any answers, but it's updated through… sheer and, you know, the… just annoying and lots of pinging, so I would… yeah, definitely, like, there's still some open comments, I think, on this.
This remote, it feels vaguely AI-coded, but that's okay.
Yeah, slightly AI-coded.
He's been having… yeah, I think it's been difficult for him to keep having to ask the maintainers to rerun their workflows, but… That's…
**Ariel @arielvalentin (ATX, USA)** 27:07 I do what I can to keep an eye on that, so I can just keep pressing the button.
**ericmustin** 27:11 Yeah, no, I'm just… I mean… It's better than, security apparently is important all of a sudden in Ruby, so I'm not going to, you know, say not to, you know, we should open it up, or there's a better way.
Okay, but what's new is… so these aren't new, but these are new. Kayla has a PR that's in draft… We're improving the release workflows.
**Ariel @arielvalentin (ATX, USA)** 27:35 Yeah, let's give the draft ones, because she may not be ready for feedback on those, if that's okay with you all.
**ericmustin** 27:40 Good, good point, Ariel. The other one that's open is… The README for… SEMCOM?
**Ariel @arielvalentin (ATX, USA)** 27:49 I said, sure, why not?
**ericmustin** 27:51 Yeah, this feels fine.
Let me just look good to me. The last time I.
**Ariel @arielvalentin (ATX, USA)** 27:56 Give this a group.
**ericmustin** 27:58 It's just text, right? Yeah, it's just text formatting.
Okay, geez. I'm in the same boat, okay.
I know, there's some updates. There's some updates, but it all looks well and good here.
Yeah, okay, this all is fine with me, I'm glad she did this work. Cool.
Sorry to interrupt.
**Ariel @arielvalentin (ATX, USA)** 28:23 So when, can we filter by reviews required, maybe?
**ericmustin** 28:30 Damn, that's interesting, I didn't know.
**Ariel @arielvalentin (ATX, USA)** 28:34 And I don't know why drafts showing up in review is required, but that's okay. I'll give product feedback about that.
**ericmustin** 28:40 Yeah.
**Ariel @arielvalentin (ATX, USA)** 28:43 So we've got quite a few that need some attention. I don't know if folks are… Metrics experts, because a lot of these look like they're metrics-related.
**ericmustin** 28:52 Yeah, it's all med… I mean, that's where all… most of… almost all the active work is.
There's been plenty of feedback.
I, I could add it to a list of things I would claim I'll do and review, but I'll be honest and say I'm pretty just behind on all the metric stuff, so there might be some… ramp up just to get to a place where I can review it.
I mean, Wendy, like, from your perspective as someone who's been trying out, metrics, is there anything you see… you know, I noticed, like, exponential histograms, that seems… high value.
**Wendy Smoak** 29:35 My biggest metrics concern is the… and I know Sean had started on it, is the fact that there are no limits. There's something in the spec that says you can set a size, and then it just dumps everything into, into overflow or something? So right now, you can explode the… if you… happen to put an attribute that has too high a cardinality, like, there's nothing to stop you from having.
**ericmustin** 30:01 Yeah, yeah.
**Wendy Smoak** 30:03 I don't know what happened. Yeah, that. That's, like, the thing I'm looking for, just because right now I'm in control of all of it, but at some point, someone else is going to do something, and… Yep.
**ericmustin** 30:16 Yeah, yeah, you'll get cardinality bombed.
It's… we've all been there.
**Wendy Smoak** 30:21 So, yeah, I mean, the logs are fine, because there's a limit on the buffer size, and it will, as I've been complaining about, drop them. But the metrics just don't seem to… But yeah, it's… I mean, I rea… I understand it's in development right now, it's under construction, so…
**ericmustin** 30:40 Vendors want them to make more money, so they just.
**Wendy Smoak** 30:42 Yeah.
**ericmustin** 30:43 Don't put limits on the foot guns that help them.
**Wendy Smoak** 30:47 But yeah, other than that, I think that we're… And the thing I brought up earlier, like, I still… it's not really an issue here, it's that… There's… once you create a… an instrument, and you stick it in the instrument registry, there's no way to get it back out. Like, you can't. Right. And we had talked about going to talk to the… SpecSIG, but they, like, referred me back to Ruby. I was like, well, that's where I came from. Who do you talk to about this?
**ericmustin** 31:14 Huh, okay, yeah. Like, how do you…
**Wendy Smoak** 31:16 get something changed in the spec? Is this…
**ericmustin** 31:20 That's.
**Wendy Smoak** 31:20 So that kind of stuff.
**ericmustin** 31:23 That's, yeah. That's… I know the feeling.
**Wendy Smoak** 31:27 She's gonna go to… maybe… maybe Kayla is going to a meeting and she hasn't… Reported back yet, but…
**ericmustin** 31:34 Okay.
Kayla, okay, that's good.
**Wendy Smoak** 31:38 But yeah, other than… I mean, it's… logs are working, metrics are working, it's new, we're…
**ericmustin** 31:43 Boom.
**Wendy Smoak** 31:44 I don't feel like I have a good handle on it, because right now everything's just kind of all in one.
**ericmustin** 31:49 mirror, and…
**Wendy Smoak** 31:52 So, every single process… has all of the instruments, and I feel like they don't really all need it… need all of them, so I kind of want to do a find or create, and, like, I don't.
No, I… I'll do that in my wrapper right now, but…
**Ariel @arielvalentin (ATX, USA)** 32:08 Did you say every single process?
**Wendy Smoak** 32:11 Well, yeah, every passenger process that spins up the rails app.
runs my… in my metrics initiator, and it creates all the instruments, because the naive implementation I have right now is just keep adding an instrument and sending metrics to it.
So, yeah, at some point.
Like, I know I kind of… and I had to wrap it, because I have to be able to get the metrics back out.
So yeah, we're just kind of… it's new, and there's no… not really no examples around, so we're just trying to figure out how to…
**ericmustin** 32:42 Make the thing do it.
**Wendy Smoak** 32:45 But yeah, I haven't run into anything with it. Everything that I've almost run into, it's been, oh, that just got fixed 2 weeks ago, so…
**ericmustin** 32:52 Yeah.
Mom.
Okay. I'm good. I mean, that's good to… I mean, that's good to hear that you're not, you know, you haven't thrown it out the window yet. There's always.
**Wendy Smoak** 33:02 Yeah. Good.
That's what happens with logs the first time around. So the first time we came around to look at logs, it was not done. Kayla's stuff hadn't been merged yet.
**ericmustin** 33:11 Yep, okay.
**Wendy Smoak** 33:12 And then we came back around again, and that was done, and we were able to pick that up and use it. And then… we were trying to send StatsD through the collector, and that just didn't work, and I was on the side playing with the SDK, and I was like, huh, I've got metrics showing up in Prometheus. Why not? So…
**ericmustin** 33:33 Roll tide. Except apparently, You don't have exponential histograms when temporality is cumulative?
**Wendy Smoak** 33:39 Not needed that.
**ericmustin** 33:40 Yeah, yeah, yeah.
**Wendy Smoak** 33:41 yet. No worries. I'm trying to think what that is.
**ericmustin** 33:44 It's like the good, the good Mr. Brian.
**Wendy Smoak** 33:47 I switched to Delta, because cumulative was… I was worried about keeping everything cumulative everywhere, so…
**ericmustin** 33:54 All good.
**Wendy Smoak** 33:56 switched. Yeah, but yeah, that's working.
**ericmustin** 33:57 Sure, yeah, translating it somewhere, it's fine.
**Wendy Smoak** 34:00 Yeah, go ahead.
**ericmustin** 34:01 If you have to use Prom. But, okay, I, okay, that is great. Again, that's super awesome. Ariel, to your original point, yes, we probably got… need to do a little bit of tech debt, or, you know, debt pay down… paying down debt of reviews here for… Metrics, at the very least, because, like.
the bus factor, which, having just come back from Barcelona, I didn't realize Gaudi got hit by a bus. That's how he passed away, unfortunately. So the bus factor is, like… the true definition, like, Sagrada Familia truly has a bus factor. Sorry for a non sequitur. But yeah, the bus factor right now in histograms is, like.
Jess Schwan. So, yeah, it'd be good to, if anyone feels like diving in, that'd be awesome. I can try to… Grab one, maybe? Given my amount of time.
Sorry for the non-sequitur there. Okay.
Anything else pop out here, or do you guys wanna… spend a bit of time on the Rails, 8 stuff, and then… Okay, I'll take that as… A.
Let's move on.
So, Ariel, you had a, you had a note here in Contrib about Rails 8 events?
**Ariel @arielvalentin (ATX, USA)** 35:21 Oh, no, just, I wanted to, Note if there was any interest in folks starting to look at it. This is still, I believe, in beta.
I know Shopify, Andriano's the big… the… the contributor of this.
But the other one that's interesting is… is continuations, but we can come back to this one.
For structured event reporting, I don't know if the intention here is to eventually sunset notifications.
Favor of this.
And, you know, one of the things that I tried to push forward was.
for all of Rails to be instrumented using notifications, but that never…
**ericmustin** 36:06 Right.
**Ariel @arielvalentin (ATX, USA)** 36:06 Materialized, right? When we got as far as… Are users needed?
And, so similarly, when we're looking at what it looks like for the structure.
event. We see that this one example is a log subscriber. That would end up Meaning that, the active support lock subscriber looks like, might be going away.
**ericmustin** 36:30 Right.
**Ariel @arielvalentin (ATX, USA)** 36:31 So if that's the case, and eventually we're trying to, you know, they're gonna go sunset at it, seems to me like we're gonna need… a Rails 8 version of these gems that… They're gonna be forked. Well, not forked, but rather, A replacement for the notifications group, if that's true, if that's the way that it's going.
**ericmustin** 36:52 Yeah. But would they sunset active notifications in a minor version, with an 8? Or would they?
**Ariel @arielvalentin (ATX, USA)** 37:00 Oh, I don't know. That's… I'm just posing that as a, hey, here's what…
**ericmustin** 37:05 Yeah, this could be.
**Ariel @arielvalentin (ATX, USA)** 37:06 Here's what we don't want to happen. What we don't want to happen is for us to fall behind, and then somebody tries to upgrade their Rails 8.1, Right. And all of a sudden, their active record, you know, they wrote an active record.
**ericmustin** 37:18 Yeah, yeah.
**Ariel @arielvalentin (ATX, USA)** 37:18 and that's gone, you know what I mean? Yeah. So, like, Or, in my case, all of ActiveJobs implementation, is… is using… Notifications.
**ericmustin** 37:30 Yep. I mean, a lot of our stuff is using… yeah, we have a fair amount of it. Some of the… Active, yeah, active record, active job.
Few hours.
**Ariel @arielvalentin (ATX, USA)** 37:39 And events has, like, additional context… things, which I don't exactly know what.
**ericmustin** 37:45 scope of work.
**Ariel @arielvalentin (ATX, USA)** 37:46 context are… And if they should overlap with… The fiber local context objects, Okay.
**ericmustin** 37:56 what about, are you… do you know if it… I mean, from a performance perspective, is it, like… is there some performance wins there? Is it, like, I remember old school, like, Rails notifications had that ordering issue, where we were, like, constantly fighting the ordering, and… If things raise too early, the other things in the chain don't get called, so, like, maybe there's some quality of life improvements within… I would hope events has some better solutions there.
I don't know any… you know, I saw it came out in the back of my mind, I went, oh crap. And I did see it was from Shopify, and I was like, well, maybe Robert will just, like, pop up with, like, a fix.
So, yeah, I don't have any context on it, except, yeah, we should probably put it on our radar to…
**Ariel @arielvalentin (ATX, USA)** 38:41 Hmm?
**ericmustin** 38:41 I mean, at the very least, like, it might be worth, like, a POC.
Of what would it look like to move to, you know, let's pick… someone could pick one.
Example, and, you know, just try to swap in an implementation using… Events, and see if we get the same metadata that we need, or if there's any gaps, or any… Huge, you know, things that pop out as being like, wow, this is so much better, let's prioritize.
Doing this everywhere. And yeah, if anyone has, like, I mean… Very obviously, like, you have some… you may be able to get some inside baseball, or, like, the Shopify folks, but, like, if folks are… close in the Rails community, I wonder if they've… I would venture that someone, surely, upon… while reviewing all this work, mentioned the similarity to notifications, and, you know, asked the question of, like, well, what's the… what's the plan here?
So maybe we could dig in, maybe that's documented somewhere.
For any enterprising… folks out there, alright, but yeah, I don't have any answers. I don't know, if anyone else here is… Opinion?
**Ariel @arielvalentin (ATX, USA)** 39:51 Just wondering if anybody else was interested.
**ericmustin** 39:53 That's cool. I'm, I'm… I think it seems, It seems like it… I'm glad that Rails cares, at least, about, like, first-party support.
For, you know, These sort of, Behaviors that we tend to rely on, so that Yeah, we're not doing monkey patching forever.
**Wendy Smoak** 40:18 As far as interest, yes. In general, we've got it on the… Bored to keep an eye on.
We won't go to World 8, and, like, immediately, of course.
But the notification stuff just… I think it… either it said in here or in one of the blog posts that, like, everyone's doing this already, and it'll be nice to just have one way to do it.
**Ariel @arielvalentin (ATX, USA)** 40:41 Yeah.
**Wendy Smoak** 40:41 this event stuff, like, we're all doing this, like, ourselves, internally, somehow. And it would be nice for a new… I mean, I don't know whether we'll change some existing stuff, but anything new that starts up probably will.
Go along.
**ericmustin** 40:58 Yeah.
Yeah, I mean, certainly as a minimum, we could say, like, any new PRs coming in, like, we could… as long as we're comfortable with events, like the, you know, the interface, and we find it's possible to use for… We could just… reference.
**Ariel @arielvalentin (ATX, USA)** 41:15 What's certainly gonna be, you know, helpful for us is gonna be the fact that the any type is gonna be allowed for attribute values.
**ericmustin** 41:24 Hmm.
**Ariel @arielvalentin (ATX, USA)** 41:25 Which might make you a little more… Advertising?
**ericmustin** 41:32 Yeah. To say, oh, here's the payload, and the event payload that came in.
**Ariel @arielvalentin (ATX, USA)** 41:36 We can add it to… we have to figure out a way to kind of, like, map it right, I guess? But it would be.
**ericmustin** 41:45 Yeah, there's a little more, like, we're… We would have some more flexibility.
**Ariel @arielvalentin (ATX, USA)** 41:51 As opposed to trying to, like, take values that are in the nested values and then try to flatten them.
**ericmustin** 41:56 Yeah, yeah, yeah.
**Ariel @arielvalentin (ATX, USA)** 41:57 I don't know if there's a hierarchy that could be supported in there.
**ericmustin** 42:03 Ugh, okay. Yeah, I think, yeah, alright, so we're… sorry.
**Wendy Smoak** 42:09 I've been interested in this, but also, Kayla has the Rails Logger Bridge somewhere.
**ericmustin** 42:13 Right.
**Wendy Smoak** 42:14 Quite.
I'm working on a few, like, little things that… something that just anything that would take an app that is already doing Rails logging, however one does Rails logging, and… could stuff it into hotel logging without having to touch every single place that you're, you know, like, writing a log.
**ericmustin** 42:34 Oh, that's… yeah, she's work… I mean, I.
**Wendy Smoak** 42:36 Yeah, so whether it's this or… or… like, this… this feels like it will just work, but we're two… probably two years down the road from random person showing up and saying, hey, this just works, because all I have to do is subscribe to a thing.
voice… there's still tons of, like, regular, plain old rails lugger, worn… Out there. That's gonna be there forever.
**ericmustin** 43:00 Yeah, I mean… you know, back in the old days, we had some monkey patching libraries, which did, I guess, logger bridge type stuff, where we're… we were just, like.
hatching Logridge itself.
Or we would patch…
**Ariel @arielvalentin (ATX, USA)** 43:14 Yeah, it was mostly patching loggers. Symantec logger…
**ericmustin** 43:17 Yeah.
**Ariel @arielvalentin (ATX, USA)** 43:17 Something like that.
**Wendy Smoak** 43:18 It's like, as a… someone showing up to adopt it.
**ericmustin** 43:22 Yeah.
**Wendy Smoak** 43:22 Super easy when you've got an existing.
**ericmustin** 43:25 Right, in brownfield world, it's… the reality is different than the theory, or practice, and it's… yeah, there's a significantly higher bar, because you have to… you have to bring up the rest of… you can't just, like, start from scratch. I… I get it.
And yeah, there's not a… there's not just, like, a one… You know, a single… A one-click or, you know, a one-liner where you auto-magically, you know.
can capture all the individual lines.
**Ariel @arielvalentin (ATX, USA)** 43:53 Yeah, at the risk of sounding very, controversial.
Or, like, dragging this conversation on more. Okay. I think one of the challenges I mentioned to Kayla early on about the log bridge is that Ruby's Lager doesn't ba- doesn't have the same… Architecture, or design, or whatever you want to call it.
as other language loggers, so if you compare it to Java, for example, you'll have a logger factory, that logger factory, then you have formatters and… Oh, gosh, the I.O. layer, what is that called? I forget what the name… it's not Exporter, I don't want to call it Exporter. I'm confusing myself.
**ericmustin** 44:36 Some writer thing.
**Ariel @arielvalentin (ATX, USA)** 44:38 Yeah, so, yeah, streamwriters, yeah. So, like, what'll happen is, for Ruby, it's like the logger takes the logging device.
Which… is an I.O. object, so it's like, there's no… you know, and then the logger gets a formatter itself attached to it, so there's no separation there of concerns, right? So for us, it's kind of like, well, what is the thing that the log bridge what does a log bridge want to be the substitute for? It wants to be the substitute of the I.O.
But it doesn't conform to that interface, right? Because there's no way for you… an appender is what it's called, sorry. There's no… there's no concept of an appender. So we can't register, say, like, our log bridge as an appender, and say, oh, this is an alternative path to I.O. for your logs. And I think that that's the part that makes it hard. It's kind of like, for the Ruby standard logger.
we need to have, like, an I.O. that is an adapter or facade, or something that wraps the emitter. And then at that point, it's like, your logger had a format.
That whole format, whatever you use in that formatter, that gets thrown in the body, and the body is a string.
And it's still gonna be uns… like… Canonical logs for whatever language you had, so the.
**ericmustin** 45:57 Yeah.
**Ariel @arielvalentin (ATX, USA)** 45:58 But it'll have the additional metadata from the protobufs around it.
You know, like, your resource attributes and stuff. Right. But your log message will remain unchanged.
But then, you know, that's… I think that that's, like, for the minimum use case.
**ericmustin** 46:14 Yeah.
**Ariel @arielvalentin (ATX, USA)** 46:15 Probably would have been the design to say, hey, let's go with that.
Because Active Record… I'm sorry, Rails has, like, the broadcast logger.
**ericmustin** 46:23 Yeah.
**Ariel @arielvalentin (ATX, USA)** 46:24 Which is trying to emulate, sort of, like, the multiple appender group, because you want to have multiple outputs.
The tagged logger, which is trying to add attributes on top of that. So it's like, trying to kind of retrofit the log emitter to fit that whole thing.
It's like, you have to intercept the formatter and…
**ericmustin** 46:45 Yeah, I remember you had to monkey number of classes when I was doing some of the other stuff. It wasn't just as simple… there was, yeah, similar to how whatever. It's like in Faraday, there's middleware, I shouldn't pass middleware, but it's like most of these HTTP libraries, like, you're doing some unholy things just to… Fit.
I, okay. I appreciate the extra depth there, Ariel. I think it's, it would be… yeah, maybe I'm… maybe Kayla has some opinions here as well. She wrote some of the art, you know, is the one closest to the… work here? So…
**Ariel @arielvalentin (ATX, USA)** 47:26 Deep breaths, I know.
**ericmustin** 47:27 Questions? No, sorry, no, I just… Okay, alright. Well… it was a nice conversation, and we did approve a PR, so… We… we're doing good stuff.
Does anyone have any burning questions? Happy reports? Calls for reviews, things like that?
**Ariel @arielvalentin (ATX, USA)** 47:54 Are there… if we click through the PRs and issues on the control, we do the same thing?
**ericmustin** 48:00 Really bad.
Meeting church… Okay.
Trib.
Nothing new. I know, Hannah, you have some… fun long-term projects around some of the opt-in, opt-out stuff. And if it makes you, feel better, someone actually unprompted at work, like, heard that I worked, you know, like, hotel, and was like, what's up with all this opt-in stuff? It's really confusing.
And I was like, yeah, man, like… I bet it is, like, you should see what it looks like to implement, like, but yeah, so… I think the world… I think everyone will be a lot happier in, like, whatever, 6 months or something, when we can just be like, this is the new standard.
But yeah, you're not alone in feeling like this was… somewhat convoluted. Okay, so nothing new on issues and pull requests.
So there's some Dependabot stuff, this was on my radar, as it looks like… I mean, it looks like a straight-up bug, sort of, that Schwan found when grape is used in ways that are, like.
not… As we expected, although some tests are failing, but I guess maybe… you… Can… oh gosh, there's mo… when you're using multiple grape versions?
Okay, I don't know.
Sounds like there is a problem. He's suggesting a config option to solve it, which I thought was slightly interesting, rather than… Just having it magically work, I haven't… this is something that would be definitely a good place to review for folks if anyone has grape experience, but… Seems… I just… I mean, anytime I see someone adding a callable as an option.
**Ariel @arielvalentin (ATX, USA)** 49:52 It's like a red flag. Yeah, it's always a problem, yeah.
**ericmustin** 49:55 I have some.
**Ariel @arielvalentin (ATX, USA)** 49:56 else?
I can't remember who the original maintainer was. We never added the maintainer labels to stuff, right?
**ericmustin** 50:04 Probably me. This is like a… I know grape comes from, like.
I mean, in 2017, there were a lot more users, or whatever, when, like, some of the stuff got written.
I don't know how many people in the world are still using Grape, I guess some people are.
**Ariel @arielvalentin (ATX, USA)** 50:17 It was, it was Muriel Picon.
**ericmustin** 50:20 Huh? Okay.
**Ariel @arielvalentin (ATX, USA)** 50:21 Yeah, I thought Muriel was the person that contributed that package.
**ericmustin** 50:27 And we can… I guess it's on a go, be all the way back into the… before it was a separate… Repo?
This is, like, done a predate contribute itself.
Oh, no. Yeah.
Muriel? You are… you are correct. Is Muriel a co-worker?
**Ariel @arielvalentin (ATX, USA)** 50:44 I have a terrible memory… I have a terrible memory. Never met Muriel at all. I just know that anytime something happens with grapes, since… we don't use grape, and I'm not a grape user, I'm like.
please, look at these PRs, like… We never… one of the things we never implemented was the similar structure of the…
**ericmustin** 51:03 Collector.
**Ariel @arielvalentin (ATX, USA)** 51:03 Collector, right?
And, I gave feedback to the code owners teams, And it's not high on the priority list, so…
**ericmustin** 51:15 Yeah, yeah, it's what it is. E is what it is. Okay, yeah, it's based on the Dadog instrumentation.
Which sounds about right, in the sense that this was my bullshit from half a day from a decade ago.
**Ariel @arielvalentin (ATX, USA)** 51:30 Oh, you wrote the Datadog implementation?
**ericmustin** 51:32 I mean, I had to… at one point, I had to, like, go and change a bunch of stuff in it, but no, I don't think it… I think… I don't know. There is, like, you know, you get these stuff where, like, a customer wants to buy, but they've got to have these 7 random instrumentations, and you'll be like, alright, I guess I'll just do those.
But you wouldn't know what you're doing.
So, okay, sorry to ramble here.
Yeah, I mean, we can tag… Why don't I?
Why don't I just tag her on this PR and say check opinions?
**Ariel @arielvalentin (ATX, USA)** 52:08 Thank you.
**ericmustin** 52:11 it work?
**Ariel @arielvalentin (ATX, USA)** 52:13 Nope.
Oh, that's because, you know, the autocomplete, usually, for a repository?
Unless a person is a collaborator, or… Or something in the repo.
I don't know that the autocomplete's gonna work for you.
**ericmustin** 52:35 Oh, good.
Yum.
**Ariel @arielvalentin (ATX, USA)** 53:20 Hey, two cents given.
**ericmustin** 53:22 Cool.
Other things that popped up, Hannah, you have some… I think you have won the work in general that you're doing on the SQL processor, SEMCOM support?
And then… As a sort of spin-off of that, we have to sort of rename the gems themselves.
Do you want to chat at all, or see… is there anywhere specifically you'd like… I know you had put up some PRs?
I mean, where, if, you know, if someone here is, like, 30 minutes or 45 minutes, would you want them to start with the… summary thing? Do you want them to start with the… I don't know.
**Hannah Ramadan** 54:07 Yeah, I think probably the one… I mean, the thing that's ready for review are the series of three PRs introducing the new, yeah, SQL processor gem, which I think needs to go out first, so then we can deprecate the obfuscation one and point to SQL processor, and then that Third one in draft mode is Fairling, because it's replacing all the references, but hopefully once we do this here, we can rerun the chests and… Okay.
**Ariel @arielvalentin (ATX, USA)** 54:38 Cool.
**ericmustin** 54:39 We'll try my best to at least review some of these boilerplate ones, I thank you for the work here.
Of course.
There was one other one that popped out, which is, I know, They had mentioned… .
**Hannah Ramadan** 54:54 Clear.
**ericmustin** 54:55 this…
**Hannah Ramadan** 54:56 Yeah.
**ericmustin** 54:56 is putting up a PR, which was nice, actually.
**Hannah Ramadan** 54:59 Yeah, I reviewed this. I'd appreciate maybe another review, but I think this was a very fair change, and .
**ericmustin** 55:05 Yeah.
**Hannah Ramadan** 55:05 Yeah.
**Ariel @arielvalentin (ATX, USA)** 55:07 Proven run. What bug did I introduce?
**ericmustin** 55:09 Hmm.
the.
**Hannah Ramadan** 55:12 This is me, yeah.
**ericmustin** 55:13 Well, you know, I don't…
**Hannah Ramadan** 55:14 Not really.
**ericmustin** 55:15 Yeah.
**Hannah Ramadan** 55:16 Not really a bug, but it… Yeah, we basically introduced some new methods, middleware, args, and then, depending on what semantic convention you were using.
**Ariel @arielvalentin (ATX, USA)** 55:28 Oh, oh, oh.
**Hannah Ramadan** 55:28 Added, yeah, so this just made it so that people didn't have to change.
Before, we were like, hey, if you want to do, like.
get both semantic conventions, use mineral arts, dupe. This just makes it so that it actually respects the…
**ericmustin** 55:45 The environment variable, no one has to make any changes to their code.
**Ariel @arielvalentin (ATX, USA)** 55:48 Cool, cool, cool, cool, cool.
**ericmustin** 55:49 Yeah, it's basically we… this… we didn't… I don't think we… in hindsight, I don't think we realized this was being used, like, although it was public.
You know?
part of the public API, like, I don't think we realized we had been documenting to tell people to use it, which a small minority of people were, so now there's just this nice wrapper, which is, like, okay.
kind of, like, do the implicit resolution of the MVAR?
So yeah, I think it's all well and good. I'll try to… yeah, I can, let me assign this to myself.
I don't know, never mind. I'll just review it when I have a second, but yeah, that would be good to merge, if we can.
And yeah, I'm glad. It was nice to see someone come in and actually, like.
contribute, rather than just complain, so thank you to you, Sergio, if you're watching this, off hours.
**Ariel @arielvalentin (ATX, USA)** 56:37 You know he is.
**ericmustin** 56:37 Yeah, of course.
Everyone's watching. There's dozens of us.
**Ariel @arielvalentin (ATX, USA)** 56:43 The isolation level one looks like it was approved.
**ericmustin** 56:46 Hmm…
**Ariel @arielvalentin (ATX, USA)** 56:47 Can that one be merged?
**ericmustin** 56:49 Oh, boy.
Let's see, Kirs, okay, he's pretty smart.
Right, that's Kirstatrov.
Let's see… Okay.
**Ariel @arielvalentin (ATX, USA)** 57:00 Oh, is it very… is this very busy? Do an approved workflow run there. Let's see if the test passed.
**ericmustin** 57:05 Yeah.
**Ariel @arielvalentin (ATX, USA)** 57:06 Let's come back to it.
**ericmustin** 57:07 I had to do a small… all good. I had a small PR to update some of the, images due to VMware killing Bitnami soon, so there were some… Workflows have failed.
**Ariel @arielvalentin (ATX, USA)** 57:21 Can we merge that, though?
**ericmustin** 57:22 We merged it, but, it is not… Released or anything. But the… there are some… during that brownout period, I think some of the work… there are some failed workflows.
Someone did, yeah, it's in there.
**Ariel @arielvalentin (ATX, USA)** 57:41 Redis is in the… Are you looking for yours?
**ericmustin** 57:46 It doesn't contrib… sorry.
Yeah, it was like… Yeah, it's merch. Someone merch it.
**Ariel @arielvalentin (ATX, USA)** 57:54 I did, probably.
**ericmustin** 57:56 Okay.
**Ariel @arielvalentin (ATX, USA)** 57:56 I was desperate to get things passing.
**ericmustin** 57:58 Yeah, that sounds about right. But maybe we have to re-kick some of the workflows?
I don't know, I guess they wouldn't… it's unlikely they would have failed during that time. Anyway, we'll keep an eye on that.
**Ariel @arielvalentin (ATX, USA)** 58:11 Can we talk about that Docker Brown out?
**ericmustin** 58:13 Yeah, yeah, yeah.
Which we had… thank you, Kayla and Hannah, for surfacing last week.
Some eternal incidents on that as well.
Okay. I, we're, we're at time, I realized. I, I, I don't have anything else, If other folks, yeah, otherwise I'll give you all a minute back.
**Ariel @arielvalentin (ATX, USA)** 58:42 Eric, thank you for running the meeting.
Hannah, great to see you.
**Wendy Smoak** 58:47 Thanks!
**Ariel @arielvalentin (ATX, USA)** 58:48 Wendy? Arun, I'm sorry, did you get a chance… did we get a chance to address any of your concerns or questions? I apologize if, We didn't get to that point.
**Arjun Rajappa** 58:59 There are no concerns, Kat.
**ericmustin** 59:03 Okay, well, thank you, everybody, for letting me dominate the meeting with my two comments. That's… hey, somebody had to fill the space. I appreciate you having things to talk about here. Otherwise, just be me kind of doing the usual flailing and wacky way…
**Ariel @arielvalentin (ATX, USA)** 59:19 Right.
**Wendy Smoak** 59:21 So, whatever.
**Ariel @arielvalentin (ATX, USA)** 59:21 I'm gonna opt out. See you later.
**Hannah Ramadan** 59:23 By everyone's.
**ericmustin** 59:24 Sorry, Eva.
