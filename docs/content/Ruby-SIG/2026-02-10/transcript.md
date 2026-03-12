SIG: Ruby SIG
Date: 2026-02-10
Duration: 70 minutes
============================================================

## Zoom Recording Transcript

Ariel @arielvalentin (ATX, USA) 00:04:26 Hello! How are you, Daniel?
Everything good?
Daniel Azuma 00:04:35 Good. Yeah, how about you?
Ariel @arielvalentin (ATX, USA) 00:04:37 Okay Just into her… just back from PTO, so… I'm taking it one day at a time.
Daniel Azuma 00:04:46 Do anything fun, interesting?
Ariel @arielvalentin (ATX, USA) 00:04:49 We're just family.
Spending some time with the family, you know?
Daniel Azuma 00:04:54 Good.
Ariel @arielvalentin (ATX, USA) 00:04:57 What did I miss while I was gone?
I didn't miss anything interesting while I was out.
Daniel Azuma 00:05:35 -Oh.
E… I missed last week, So I was just looking at the burning question from last week, the, The update before merge setting, Sounds like people are asking about that.
I also had a… question I want to… I brought up two weeks ago, regarding some… regarding the way that we might want to test, actions workflows with, with, and, and with Renovates, and… I had had a back and forth with James Thompson about, strategies for doing that, and wanted to get some additional opinions about it, but, so there was a little bit of discussion, but nothing really resolved. I was hoping to bring that up again.
Ariel @arielvalentin (ATX, USA) 00:06:46 Yeah, fortunately, I don't think that this time zone… this time slot is.
Daniel Azuma 00:06:52 Yeah, that's not gonna work for James. I think they're in Australia or something like that.
Ariel @arielvalentin (ATX, USA) 00:07:05 I mean, we could discuss that, because I don't have anything really on my list other than the fact that… we have a backlog of a bunch of PRs, and… updates that have to go out, I, I opened up an issue because… I have this one sort of, like, And I assigned it to you, if you can give me a hand with it.
I… I have… Have the release, please, running on a scheduled job?
So then she can create a release PR on, right before this meeting.
And I could try to get releases out, and it's failing currently due to an undefined method.
Error, and hoping that you might be able to… Giving me a hand with looking into that.
Daniel Azuma 00:07:49 Yeah, yeah, I totally… just… probably just forgot to update something.
Take a look. You have, I'll just look at the… is it in the, in the main repo, or in the, contrib repo?
Ariel @arielvalentin (ATX, USA) 00:08:03 It's in the control repo. I don't think that I have… that there's an equivalent job in the main repo. I don't do a lot of work in the main repo.
So, we're getting more regular updates on the instrumentations.
But one thing, if there is something to discuss, I'll put it on the list here, actually, but But I'll go… Do it later.
this…
Daniel Azuma 00:09:00 What did I screw up here?
Interesting… Okay, yeah, I'll take a quick look at it, that I'm sure that's easy to deal with.
Ariel @arielvalentin (ATX, USA) 00:09:41 Go ahead and adding some stuff to the agenda.
As we're talking here now… Happy to discuss the burning questions first.
Okay, so as we… As we're waiting for, Things will spin up.
We see some stuff that's on the board here, or sorry, some stuff on the agenda now.
I didn't attend this… I don't attend the spec sig, so I don't have anything to add, but if anybody noticed anything in the spec sig that was interesting… You know, please, Bring it forward.
Daniel Azuma 00:12:18 I didn't attend, and I don't… I didn't… haven't looked at it, so…
Ariel @arielvalentin (ATX, USA) 00:12:25 Okay, well, I'm gonna go ahead and share my screen here.
With you, my friends, so that… We can get an idea of what… You know, we can kind of peruse it and see if there's anything together.
That might be of interest to us.
So, I'm gonna go ahead and click through, and see if there's anything of interest, And don't mind my view of GitHub, I have all these other little widgets that you don't see, or you might see a new… Feature Flag version of something.
And you're like, oh, that looks different. Those are features that are available to me.
To the general public.
But, sharing resource attributes… with external readers.
Okay.
So this is a mechan… this is looking like it's a mechanism to share, or like, to define an OTEP for sharing these… resource attributes with the eBPF profiler so that they can… Do correlation.
So I imagine if, eBPF profile is running, and you have a resource.
At, you know, detector that is… enabled in your SDK.
As the profiler is trying to… extract data, it wants to be able to say, okay, what are the resource attributes associated With the process that's running right now.
The one that I'm profiling.
You know, what's the process ID? What's the… the Oto, service name.
What's the service version? That way you can do all of that correlation.
I think right now, we might be interested in looking at this, because it might impact how we share… this safely.
from the Ruby context.
So I think that's something that… Might be interesting for folks who are on the SDK side.
To take a look at this, and to try to better understand it. Now, Ivo… Or Ivan here.
he's a Rubyist, and has been in Ruby Engineering at Datadog, so he's got a lot of context on how, you know, how to do this stuff for Ruby, so… I imagine that he's gonna be a good voice.
for how to potentially do this with a Ruby SDK, but… He's not a maintainer on our side, so… I think, you know, getting our input in there would be, would be, necessary.
and important.
Another thing we've got here is the Hotel Unplugged meeting that's happening.
Looks like for the next event?
That might take place in Vancouver, Canada.
Might be looking for folks to participate in that.
And then there's the system package manager and controller.
Proposal, let's see here… What is this?
Okay, there's a wall of text here that I'm not ready to read.
At least not in person, not while all of us sit here and wait.
So… I'm gonna skip that one.
This might be interesting, especially, Schwan, since you've been trying to get that auto-instrumentation in place.
Because now, you know, there's competing implementations of the auto instrumentation, the zero instrumentation, right?
you know, whatever that is, like, code versus eBPF style, and which one of those should win?
I'm gonna… I suspect that there's gonna be something that's interesting to us there.
Especially if we want to continue to try to do that.
Let's see here, then we've got… Defining a clock interface?
Okay, the reason for this instrumentation author needs to take the timestamp that's included in the telemetry.
And it should be in sync with the SDK's clock for the sense that stuff, and, okay.
Okay, so they want to do something more standard?
Okay.
If we're dealing with… Clock skew, I guess.
And wanna try to include that in the SDK? That might be interesting, sure.
But it wants to be defined in the API.
As opposed to… every SDK having its own implementation of it to try to force the SDK day.
Included? Okay.
We've got the… And I'm sorry if I'm, like, brushing past these, if anybody has any questions, you can, of course, unmute yourself.
And, and try to take that discussion away.
Or, you know, move the discussion on, but… I see. So, this is interesting. So, there's a proposal, it looks like, here on the table for schema URLs to include manifest and metadata information.
So that's interesting. So, Interesting. So is this supposed to be… I wonder if this is supposed to be… key… would it be… is it support for arbitrary registries that could depend on Ulta?
So it looks like there's, like, the ability to have Your own schemas, maybe?
that extended the OpenTelemetry schema?
So you can perform transformations on things?
Just give me your roles, now return a manifest with a metadata plus link.
to the resolve schema, the single file has everything baked in, support for arbitrary registries that could depend on hotel conventions? I don't know, I have to think, you know, maybe we need to dig into this a little bit deeper. This will affect us.
Because, you know, as somebody who's trying to, we don't support schemas today as part of our instrumentations, and as part of the Ulta SDK, there is a… Instrumentation scope PR, that's, in draft mode.
where it would add support for schema URLs as part of the… As part of the SDK?
And that's important, because as… We tried… we right now are in this mode where we're in this mixed mode.
Using pre-conventions and post-conventions, and we want to be able to have downstream telemetry consumers.
to… Be able to process the data and transform it as part of a transformation pipeline to, say, upgrade a schema, if you're, like, using instrumentation with an old version of the schema.
But I'm very interested in knowing, like, what this is specifically. I'm just gonna click through and see what some of the proposed changes are.
Let's see… Let's do a preview here.
That supports multiple conversion convention registries and provides full access to metadata.
Semantic Conventions describes this, conventions are common concepts… Hotel collector and language-specific instrumentations should be published to their own conventions, okay?
Instrumentations that are not hosted by OTEL should be able to document and publish their own conventions. Okay, yeah, so it's sort of like the superset, like, for example, if there is no… there is no, sort of, like, Rails conventions, or things for Active Record, or… you know, and so on and so forth. So it's like, where do we… where would we publish those semantic conventions? Or if you, an end user, have an internal library that you want to instrument.
And you want to supply a schema for your internal instrumentation.
When you attach a schema to that.
You want to be able to publish it.
And for an auto collector who does transformations, or for the backend vendor, Would transform the data.
That metadata would be included as part of the… as an extension of the existing, you know, supported upstream semantic conventions. So… Okay, that's interesting. That's exactly what I thought it was.
Based on the… Based on a guess.
And, that may not be necessarily, directly relevant to us, but if we wanted to publish internal instrumentation things for Rails, for example, or Active Record, or Sinatra… Then we can publish those attributes independently.
Of the hotel specification.
And that's where it might get interesting.
Otap stable by the fall.
Okay.
Okay, yeah, so this is more details about, sort of, like.
Making sure things are stable, so instrumentation, stability, it's separate from the… distribution, stability, which makes sense, right? I mean, that's how we kind of operate today.
where the OTA SDK is separate from… Any of the contrib packages, which includes instrumentation, and… And, and such.
So that works out okay. So there's not much more in the SIG to go over, I don't think.
So, what did I have? So, my, my, other notes here, so… Gonna broadcast those suckers over here, y'all.
I don't know if y'all can see that again.
So, now that we've gotten through that.
Let's see here. Here are the issues that we'd like to discuss today, and… Let's get through some of those. Who do you say?
Xuan Cao 00:23:15 Hey, I just have one, comments about the spec sync, about the eBPF.
Ariel @arielvalentin (ATX, USA) 00:23:22 Yes.
Xuan Cao 00:23:23 So, from my understanding.
the eBPF, is suitable for the, the compiled language, like Go and then… Java… But for those in interpreted language, it may be very hard to… Introduce the PPPM.
So, that's just what I are thinking, that's, for the EPPF, alternate implementation. It will… it will take a long time for, Python, JavaScript, and Ruby to have those, ePPF, alternating implementation.
Ariel @arielvalentin (ATX, USA) 00:24:03 I think that's something that we can probably ask Iwo about, because I believe that, you know, from the… Ruby side, there is some… there is some… Profiling already working, at least for, you know, MRI Ruby, or whatever version it is now called.
But, for… I think what's missing is correlation information.
Whereas, like, for example, for Java.
They, they provide, like, Thread local variables to add, say, like, the trace parent.
And then the profile's able to correlate What traces were being executed at the time?
You know, or what span's active at the time that this profile was… active.
Or were sampled.
I think that's already in place, so if you've ran, because, you know, when I attended, when I attended, KubeCon, the hotel profiler was already… generating profiles for Ruby, but what it couldn't do was get… contextual information out of the Ruby application, so it knew where the stack trace was, or whatever.
But it couldn't tell you, like, what span was active right now.
And so you couldn't make meaningful… connections between traces that were exemplars at that moment. Does that make sense?
Xuan Cao 00:25:41 Yeah, yeah.
Ariel @arielvalentin (ATX, USA) 00:25:42 So I think it's already supported, it's just not, It's not, not, not, not doing very… a good job of, of doing correlation.
And I think that the issue that Ivo specifically is talking about is not only grabbing the trace parent, because trace parent typically seems like… The model is share it as a thread local variable.
But things like the resource attributes.
How do we enrich the profile with resource attributes?
Which it can't do right now, because resource attributes aren't thread-local variables that can be easily passed around.
It's like, there has to be some sort of, like, A way to access them.
I think that's what that OTEP is trying to… Recommend.
So I think that's something to look into, if that's of interest of you, Schwan.
Yeah, yeah, yeah. We definitely need to need more people involved in that.
Any other thoughts or concerns?
Xuan Cao 00:26:55 I don't.
Ariel @arielvalentin (ATX, USA) 00:26:59 So, daniel, my man.
There's a lot of text in here, I haven't had a… myself haven't had a chance to review.
What's on your mind?
Daniel Azuma 00:27:10 Yeah, so this actually is, just the upgrading of the main repo to, the… the new resource… the new release system. We've already done this on the contrib side. We did it several, like, almost a month ago now. We, but we never, we never merged the PR on the main repo side.
So, it's just, yeah, getting it, getting it in line with what we're, what we're doing on the contribib side. The… I mean, the current release system that is, the old release system, I'm just not maintaining it, that codebase anymore. In fact, it's been deleted from the head of the toys repo.
Ariel @arielvalentin (ATX, USA) 00:27:59 Okay.
Daniel Azuma 00:28:00 So… So yeah, I just wanted to get this…
Ariel @arielvalentin (ATX, USA) 00:28:04 Reviewed as soon as possible.
Daniel Azuma 00:28:06 Up to date, so that I can actually move both repos forward at the same time.
Ariel @arielvalentin (ATX, USA) 00:28:11 That's fair. I'll try to make some time for this, you know, to do a review myself a little bit later.
I, you know what? Something that… I didn't get a chance to take a look at.
But at some point, I was getting errors about… Closing… About some of the action… from some of the actions… I'm gonna make sure… Let me see… process release… Nope.
I don't know if you had Address some of those issues… I probably could do a better job of saying, hey, show me all the ones Failed.
It's a failure… Okay, no, these are not them… You know, it might have been… Might have been addressed already.
I felt like I was running into an issue where it was trying to do… The, sort of, like, post… Post-merge jobs?
Where it was trying to open, you know, update any… Open releases? Maybe that's the one.
Yeah, so updating open releases… I was just seeing failures, let me see if this is fixed again. Yeah, okay, so it looks like it was fixed after some change.
So, never mind what I had to say.
Daniel Azuma 00:29:48 Yeah, I did make… I did make some fix. I think it was… I thought it was longer ago than… Oh, I guess that was over a week ago already.
Ariel @arielvalentin (ATX, USA) 00:30:00 Yeah, time flies, time flies.
I've been off for a week, so the last time I saw it and I wanted to ask you about it, but I assume that all that has been incorporated into these changes that are here.
Daniel Azuma 00:30:10 Yes, yeah.
Ariel @arielvalentin (ATX, USA) 00:30:11 Okay, sounds good. So I'll come back and take a look at this later. Aleshuan beats me to the punch.
Okay, and so for this change here, what is it that we're waiting on for this change?
Schwan, it looks like we just need a maintainer to merge, right? To do a review and a merge on this one?
Xuan Cao 00:30:29 Not yet.
Ariel @arielvalentin (ATX, USA) 00:30:31 I'm not authorized to push to this branch, which looks like… I don't even know what that means, this error right now.
Does that mean that you're out of sync and I can't update?
Doesn't make sense to me, but but yeah. Daniel, if you have a minute.
Daniel Azuma 00:30:50 Yeah, I can try B.
Ariel @arielvalentin (ATX, USA) 00:30:52 Basically, the problem is that You know, there's two problems that we're addressing here. Number one is… you know, Ruby 4 doesn't… no longer has CGI, by default.
Daniel Azuma 00:31:05 Yeah. Number two, we're…
Ariel @arielvalentin (ATX, USA) 00:31:08 we were pinned at, like, a super old version of Rake, and really don't want to be pinned on an old version of Rake anymore. And then the third thing is addressing some, The usage of these, of the context values here, because, you know, I think that this was trying to, like, re… like, in the test case, tries to redefine this constant, but it's already in the scope.
of the… of the test, so there's no need to sort of, like, open and redefine the class, so I think that there's just, like, a little bit of cleanup that's there that's happening at the same time, in all of these test cases, essentially.
But outside of that, You know what I mean? I don't have anything else, I don't have anything else, specifically about this. I looked at it, and it seemed, like, totally fine.
All the tests are passing, and we're good.
Daniel Azuma 00:32:05 Okay. Yep.
Ariel @arielvalentin (ATX, USA) 00:32:06 And the last one here, which is this URL, so I think I owe you a review on this one, right, Truan? Where we're looking at… Replacing the usage of CGI altogether, which came up in a different conversation.
But, essentially, per the specification, we were using CGI escaping when we should be using URI encoding.
Which is, obviously gonna be different to support UTF-8 characters versus… non-UTFA characters, and how CGI encodes spaces, say, with using plus signs versus using Unicode encodings of, you know, percent 20.
So this is a more proper way of… Per… per on-spec of… Serializing headers.
one, but there's, like, interoperability.
for URI encodings, where it's, like, plus signs, right, Schwan?
are supported by URL encoders.
So… It'll interpret it the same way.
So there'll be some inter… but we want to let folks know that this is sort of like a breaking fix.
Because they might find some weird behavior where they're starting… they're… they're encoding things using… expecting things to be encoded in Plus, using CGI versus using URI encoding.
So.
Daniel Azuma 00:33:31 As a breaking fix, are we actually, intending to do a Simver Major release with it, or is it that breaking?
Ariel @arielvalentin (ATX, USA) 00:33:40 I suspect that it's a minor bump, because I don't think that this is… I don't… so that's a good question.
I don't know how we communicate, and I think this might be on the hotel spec.
But I don't know that we do major… I think major bumps are gonna be more tied to the hotel specification than they are gonna be towards… hour changes, so it'd be, like, a minor bump, I would think, on a braking change.
But well-documented, I suppose?
versus a major bump, if that makes sense.
Because it's these things where it's like.
do we do major bumps for Ruby language changes? Like, if we stop supporting Ruby 3 and it's only Ruby 4?
Do we constitute that as a major bump?
Or do we… you know, I don't know that we have a, like, well-defined set of… Expectations around what stability means.
And maybe that's in the specification, and that's what… you know, Austin is trying to figure out, as part of that.
That OTAP that he was putting together?
About what constitutes a major, you know, stability changes, or, like, some semantic versioning, or whatever?
So I might be trying to reinvent the wheel.
But it was my suggestion, to treat it as a breaking change, at least, to notify our users that this functionality is changing.
Daniel Azuma 00:35:17 Okay.
Just from a mechanic standpoint around releases, currently, if you do… if you… If you use the bang in the conventional commit tag, and do nothing else, it will, bump the major, version number when it does a release, because it assumes, okay, that's a breaking change, it's a December major, we should, you know, we should go from 1.X to 2.0.
Ariel @arielvalentin (ATX, USA) 00:35:43 Oh, or whatever it is. there, there are…
Daniel Azuma 00:35:48 There are… note, notations that we can put in, extra notations that it's actually… it's supported in the newer, release system, where you can override that. So if he wants to, have that fixed bang, but still have a… do a feverminer, I… I can, I can put a note in the, that PR of how to construct the, the commit mess… the final commit message, the merge commit message, accordingly. But, otherwise, just as a note to… that… that does happen, so…
Ariel @arielvalentin (ATX, USA) 00:36:27 Okay, so, as a… To make it simpler for the person who does merge right now.
and avoid a mistake, should we… at least… so then, should we revert what I was suggesting and say, let's just use feet?
Daniel Azuma 00:36:43 Yeah, we can just use feet, that'll… that'll do minor.
Nevermind.
Ariel @arielvalentin (ATX, USA) 00:36:47 Schwan, how do you feel about that? That alright?
Xuan Cao 00:36:51 Yeah, yeah, I… I have no problem with it.
Ariel @arielvalentin (ATX, USA) 00:36:54 Okay, so I'm gonna go ahead and, switch this over to feet.
I'm gonna give this woman pass.
One final pass. I suspect that I'm not gonna have any issues, and I'll just say.
Green Light, and Daniel F.
Xuan Cao 00:37:08 Yeah, just, just one thing about, yeah, you were talking about, using the, encode, B3.
Provocators, yeah, I, I just put my, salt on the view to look at.
Ariel @arielvalentin (ATX, USA) 00:37:22 Okay.
Okay, so we'll create a separate issue for that, specifically to discuss how to… If we really… if it really matters.
Is that right?
Xuan Cao 00:37:44 Yeah, I think so. Because I think, I think for the… ID, they probably come with, S-code, or we have to, encode them into S-code, so…
Ariel @arielvalentin (ATX, USA) 00:38:00 Yeah, yeah, sorry, I was… it was more the baggage header, though. Like, you know, in this example of the baggage headers, and I hope that I'm making myself clear here.
The baggage headers is, like, user-defined keys, right?
Xuan Cao 00:38:12 Yeah, yep.
Ariel @arielvalentin (ATX, USA) 00:38:13 So, in this case, we're switching from CGI to… this. And so my question was, are the original… was this just wrong altogether? And the original Uber Libraries… I don't know… Were they the Zipkin libraries, right? Those are the Zipkin ones?
Is Uber Zington, or is Uber Jaeger? I can't remember.
Xuan Cao 00:38:38 This is a year.
Ariel @arielvalentin (ATX, USA) 00:38:39 Yeah, okay. So, the original Jaeger ones, were they CGI encoded, and we just did it wrong?
And, and, the baggage headers are now gonna be URI encoded, and it's gonna be right. That was really my only question.
But, you're saying that the other languages don't… Don't… don't have anything specific around…
Xuan Cao 00:39:09 Decoding or encoding those baggage headers?
Yeah, that's what I saw on the Python JSONECO.
Ariel @arielvalentin (ATX, USA) 00:39:18 Okay, so from that, you know, from that standpoint, I think that there's, you know, nothing here to… Nothing here that is unexpected, so I think I'm gonna go ahead and say… approve on this one, and so Daniel can get a shot at taking a look at this, and… You know, let me know if he sees anything that stands out to him that is of concern.
Look at that, we are on… 1235. I see that, also Arun joined the call as well.
And I'm hoping that, you know, we're… if he has any concerns, or they have any concerns, if they're represented here.
Or if there's anything that they want to go over, let me know.
But… we've got two PRs that are interesting that came up.
Recently, as we start to see the emergence of more and more desire, right, for… Ruby Community.
to… have… Hotel support as a first?
first-party instrumentation, and DALI 4.2… Quite interestingly, added first-party instrumentation, so we no longer have to maintain… our… fork here in the… or our implementation, our gem.
as part of… As part of the all package, right? As part of the contribute package.
Because they've implemented their own first-party instrumentation, right? And so if we look at what that looks like… What's interesting, right, is that they've implemented their own library, and they're… and they are looking to define a tracer.
And they'll assign a tracer based on a tracer provider, which is great, because what that'll do is give them a proxy tracer, which can be upgraded later, once the library has been installed.
But it'll bypass it if the gem is not present, the OpenTelemetry API gem.
And, you know, they've got, like, these little helpers that kind of help them through.
And then they have a very simple interface for them doing, instrumentation for their libraries, right? They're using our API and span helpers, which is really nice, because they don't depend on anything in the SDK as… As they should, right?
So, that's pretty awesome.
This means that their library, will get automatically instrumented because they've written they've made it possible in their code to do that. If we look at their… they have the instrumentation getting autoloaded in their gem, and it'll only generate traces.
If… the SDK has been in… is the… the SDK has been installed.
And that's a very interesting and great thing to have.
On the other hand, we have, folks who are, who have their own framework called the RAGE Framework.
And they've implemented OpenTelemetry instrumentation as a separate gem.
And they want to include it as part of the all package, and include it in the all package.
However, the all package, this would mean that the all package now… Has a dependency on a third-party library.
That's being hosted and maintained by another… Set of engineers.
And they… what they did was, And perhaps, you know, A little bit of, not great guidance on my part, was to say that they've, they've, They're relying on the bass instrumentation package to get a lot of the features that were available.
You know, for example, compatibility, and so on and so forth.
And, in order for them to load the gem, they are not loading it as part of… their library, their rage instrumentation library, as the hook To hook everything into.
But rather, they are installing the instrumentation as if it was a third-party library install.
If that makes sense.
So, and they're relying on things because they're building on top of existing OpenTelemetry instrumentations, so that's another sort of, like, interesting, hook in here, is that they're saying… Go ahead and, and, and, Build on top of the rack instrumentation, because this is a server framework.
And mix it into their… Sort of stack when they're configuring their application.
So I don't have an easy answer in those cases, but this is a very interesting case to look into.
Can we figure out a way to register the instrumentations and load them without them being included as part of the All Gem in some way?
Because this creates a dependency on an external library that we can't really validate.
As part of all.
That's something, you know, some food for thought.
Could use some input there, any ideas that folks might have?
But I'm like, I'm liking the simplicity of the dolly instrumentation.
But then we have, again, these very, like, complex… Instrumentations that depend on our libraries, like the rack instrumentation.
And what we can do to kind of smooth that over.
I had suggested that I did not want… so, how we got into this situation was… The maintainers of the Rage Gem wanted to include it in the contrib package.
But I think that we're… trying to lean away from accepting more things. If you're a maintainer of a gem.
you definitely should be able to make changes to support OpenTelemetry directly.
As opposed to treating it like a third-party instrumentation framework.
that the wood needs to get mixed in somehow into your library. You have the ultimate control.
Of how you instrument things, you should do it as a… You should use your discretion to run things and install it.
But again, in this example, it's much harder.
Because Dolly doesn't have a dependency on other things like rack.
for this thing.
So…
Daniel Azuma 00:46:12 Yeah, it's… I think it makes sense for, things if… if… if that's, that the Rage, maintainers, If, you know, if that, if their instrumentation is, you know, closely tied to their, you know, their specific, framework, and they, you know, they expect to be maintaining it.
their instrumentation, it's… I don't think it makes sense for it to go into our contribib rep repo. That's… it's just… Having too many people who need to do too much in the same repo makes it very difficult to manage.
I think things in the contrib repo really should be things that are actually maintained and should be maintained by this team here.
Brilliant.
Ariel @arielvalentin (ATX, USA) 00:47:11 Eventually, it would be awesome if, for example, we moved all of the instrumentation out of there.
put them into their own gems, or if Ruby Core could support open telemetry directly.
Daniel Azuma 00:47:21 Yeah.
Ariel @arielvalentin (ATX, USA) 00:47:24 But we're not, you know, we're not gonna be at that point.
Daniel Azuma 00:47:27 One question I had, so this, this, question about, adding it to the all, the instrumentation all gem, how do we make those, determinations? What goes into all? And what, what is, like, even what is the purpose of all? Because I'm, I'm, it, it seems to me, odd to have an all-gem, that depends basically on, you know, a large number and growing number of other gems, Probably only a very small number of which are going to be used by any given application.
I, you know, I wonder what the use case for this, or why someone would want to install the all-gem as opposed to just installing the specific instrumentation gems that they need for their application.
Ariel @arielvalentin (ATX, USA) 00:48:31 I think that the primary use case would be for… out-of-the-box instrumentation without a lot of hassle. So… In the case of, like, a zero instrumentation style thing, You run your application.
And you actually don't include any gems at all.
Yourself?
an operator somewhere goes into, say, like, a Kubernetes operator.
And says, turn on the Ruby instrumentation.
And the most popular libraries are gonna be lit up automatically.
And there's nothing special for the Ruby application engineer to do.
I think that that's, like, the baseline kind of dream.
And to have some sort of, like.
User experience that's similar to what third-party vendors provide.
like, one, you know, if you looked at, say, DD Trace.
It had a set of baseline gems that were already installed, and… and instrumented, and you only had to install one gem and not have to worry about all of the dependencies. Because DDTrace was an all- is an all-in-one bundle.
That includes all of the gen… all of the instrumentations together.
Right? Because it's more of, like, that out-of-the-box experience.
Versus… Folks like us, who are very picky and choosy about what we want to turn on.
And turn off.
Because it may be very noisy.
is all still worth it, is the question that you're asking, Daniel.
Or should we be steering people more towards Don't do the all-in-one package.
Select the instrumentations that you really want.
And if you're using the Kubernetes operator, we will enumerate all those gems Our, you know, in the, in the operator ourselves.
Daniel Azuma 00:50:20 I… I think… I mean, yes, that's… that is my question. It's also… Related to this question of, do we include, things like rage instrumentation, instrumentation gems that, you know, may be third-party that we don't… we don't necessarily, maintain ourselves, we don't know what their status might be.
of… But, you know, do they belong? You know, so, you know, given the purpose, what we think of the all-instrumentation is, you know, how do we make those decisions?
Ariel @arielvalentin (ATX, USA) 00:50:57 That's a great question. I don't know… I don't think that we want to include things that we don't maintain.
Or release things that we don't maintain.
Because it also, you know.
If the rage interpretation is not stable, and it makes the all unstable, it's a transitive dependency that we're like, -oh, what can we do about that?
But at the same time, what we want to do is have a smooth user experience for instrumentation authors.
So, if somebody's on OpenTelemetry I.O. right now, And they're looking at… You know… Which section am I in here? So, dogs? Sorry, I, like… For whatever reason, I was looking at recording exceptions.
But if we were looking at languages and SDKs… so our tutorial here tells them… Hey, go ahead and… Install this… And, where's the all?
The All Gem, somewhere. It's somewhere, I swear to you.
Whoop.
Oh, it's not in here.
Getting started, man, what the heck?
Yeah, okay.
So, it's like here, it's saying, install the All Gem, so that you can get your instrumentation… instrumentation going. So is it wrong for us to even call this all, and maybe this should be, like, instrumentation contribib, or something like that, to disambiguate?
That it is only packages that are from here.
Or is there a change that we can make to the… to the SDK registry that allows people to… for it to, like, auto-discover these instrumentations and turn them on automatically, and therefore that all gem doesn't even need to exist.
You know, we steer people towards install the instrumentation genders manually.
Daniel Azuma 00:53:16 Yeah, I don't know, this, this might be a, you know, this might be a longer question, a longer discussion. You know, my, my initial thoughts, might be, that, you know, you have… you have kind of a getting started experience, where, you know, you, you know, you're just getting started with OpenTelemetry, I don't want to think about… figuring out which instrumentation gems I need, I just want to kind of… getting a starter pack, of, of, of… of instrumentation that kind of covers, you know, some of the common cases, HTTP, Sinatra, whatever, whatever the common… we think the common cases are, curated by us. Small number, so not all, not dozens, but maybe five.
And then, and, you know, just to get people started, and then, and then once they've worked with it, then they understand, okay, I know what an instrumentation is, I can go find the gem for the particular frameworks that I'm actually using.
Ariel @arielvalentin (ATX, USA) 00:54:23 That's interesting. So, it changes the role of what the, like, the all-in-one experience is.
Where, like, if we looked at it, and we said, does all really need to include grape?
Does all need to include GRPC?
what should all include? And it's like, maybe… maybe we're looking… or maybe I'm thinking about this the wrong way.
Maybe there's, like, the instrumentation… like, instrumentation, the Rails instrumentation, right, is like, if you have a Rails app, you should use the Rails gem.
Like, there might be, like, the… maybe there's, like, the Ruby Core instrumentations, where it's, like.
here's the package that includes all of the core libraries, like NetHTTP, or, you know, LDAP, or whatever that's, like, not included in the… That, you know, that we had to write instrumentations for.
Then you have the… and if you want to, extend that, you use the Rails one. The Rails one is gonna have, like.
All of the active record, active support.
But we're not gonna have a gem that says, take all of Rails and all of the Rubicorn and mix those two together. If you want to light them up.
light them up by doing, like, the core and the Rails one. So we can have, like, sort of meta subset.
You know, subset packs, instead of having to try to light them up for everything.
similarly, it's like, you know, I don't know what those categories would be. Like, we could have, say, like, the… like, looking at Anthropic here, as more AI ones come in.
It's like the AI suite.
Like, you know, instrumentation is for all AIs.
Because I hear you, it's like, if you're… Unless you're like GitHub, where we both… we… it both uses Ethon XCON NetHTTP and HTTP client because of legacy.
Most of the time, folks are gonna be, like, standardized, like, I really only care about Faraday, I don't really want to instrument everything with Faraday.
You know?
So that might be interesting.
To look at.
I like that idea. I like that idea. Maybe we should have, like, an RFC or a discussion more about, like, what's the future of all?
And how, you know, how do we want all to… What do we want out of all going forward?
Do we want an all-in-one experience, or do we want curated experiences?
If that makes, if that seems sensible.
Daniel Azuma 00:57:01 I can, I can start a… open an issue, or start a discussion, or what… or whatever it is on the… on the repo.
You wanna…
Ariel @arielvalentin (ATX, USA) 00:57:11 That sounds awesome. Thank you very much.
I'm not very good at note-taking here, I should have taken notes.
Okay, and here's another, is there anything else that anyone wants to add to that? I'm sorry, I keep, like… Not creating space on the floor for folks.
To discuss things.
Okay, with silence, I'm gonna say I'm moving on.
You got a few more, which are interesting in themselves.
Is that, in this PR, rather than having gem specs point at, say, you know, the source code URIs, rather than having them point at main.
that they point to the specific Shah when that gem was released.
And I think that that's, heck, you know, that is a great idea.
I'd say number one.
The next question I had was, should it be the shot, or should it be the… The version number that was released.
Daniel Azuma 00:58:26 Yeah, the release tag.
This should be the tag, I totally think.
Ariel @arielvalentin (ATX, USA) 00:58:30 So, I think that, that's the feedback that I'm gonna provide for this one. It should be the release tag.
That way they can go to a specific snapshot of it. But why I think that's important, and why I think it's interesting, is because somebody's proposing archiving gems to remove them from the all repo. So, for example, in this case, I… Ruby Kafka is no longer supported as a gem, like, there's no updates going on there, and folks are saying, move over to RD Kafka instead.
And so it's like, okay, well, I don't want to support instrumentations for old libraries anymore.
But this person has submitted a PR, or, you know, this contributor is attempting to remove the Ruby Kafka gem altogether.
But it's like, oh, if someone wants to see the source code of that particular version of the gem, now there's no source history for it, it's gone forever, because it was pointing to main and now it's removed.
So, I think that that's where these two things are gonna come in handy.
And so I think that, I wanted to just mention this, that that's very cool.
That, you know, these cool ideas that people have. I like the idea of thinning out the repository, because right now, I… I think that, Swan and I went through something very similar with the Jaeger.
with Jaeger, which is no longer supported.
I do apologize, I got distracted. Jaeger no longer supported it, and we did not do this.
And I've also removed gems in the past and just… I've left them lingering.
So, I don't know if there's something I can do to kind of, like, restore it… Release the next version and say, oh.
We are, you know, this is no longer getting any updates.
I can't, I can't remember… if I did that already with a gem.
That was in this repository, but… You know… Something super interesting to look at.
So I think that's the feedback we'll provide to James on that, and to the other contributor, around 5.
And, that's that. Moving on to the burning questions.
Do we want to go back to our old merge settings?
Which was, your branch must be up-to-date before merging? I think so. Yes, that's why I said yes.
Is there any objections to that, or concerns about it?
Daniel Azuma 01:01:01 I mean, the obvious concern is, do we have enough activity in our monorepos, where, it just becomes too annoying or even unwieldy, to have to, you know, update and, Pull requests, you know, to, you know, or update your pull requests every single time, because someone else has merged in the meantime.
Ariel @arielvalentin (ATX, USA) 01:01:27 I think it's mostly happening with the robots.
Daniel Azuma 01:01:31 Hmm.
Ariel @arielvalentin (ATX, USA) 01:01:34 Like, when the robots are, like, affecting each other, like, because there's, like, so many actions that are getting updated, and they're not batched together.
that's where I see most of the… Annoying conflicts happening.
Myself.
Daniel Azuma 01:01:48 When I was at Google, we maintained, some very large monorepos, like the… a monorepo that included all of the Ruby API clients for all the Google APIs, for example, and we have code generation that runs all the time to generate, to regenerate those things.
So… our organization wanted to turn this on, and I said, no, there is no way that we could, we could do that, because we would be, we would be spending a ton of time updating the, these, you know, hundreds of pull requests every single time.
Ariel @arielvalentin (ATX, USA) 01:02:27 Okay.
Daniel Azuma 01:02:28 I don't… you know, we're not… we're not at that point, but are we moving in that direction where that might become annoying? I guess is the question.
Ariel @arielvalentin (ATX, USA) 01:02:36 I mean, that, you know, that's fair.
That's fair.
I don't… We don't have a lot of churn right now, other than the robots.
So, like, the robots is the exact, you know, opposite example.
Right? Where it's like, you have… you're describing, we have robots, you know, we have robots updating these things by regenerating code all the time. There really weren't any conflicts.
No reason to, like, constantly be in this update, wait for the builds to complete, and merge cycle.
Because, you know, if there's a conflict, we can't merge the PR anyway, so you have to do the regeneration, or the merge, or whatever it is.
So what, what use is it?
To have those two things up to date. I hear… I hear that position, totally fine. I mean, if you feel like… I don't feel strongly, Either way, but.
Daniel Azuma 01:03:32 I don't feel strongly. I guess I don't. I haven't worked in the repo for long enough recently to have a sense for how this is going to go. Can we turn it on, turn it back on, and then see how it goes, and if it looks like it's going to be a problem, ask for it to be reverted?
Ariel @arielvalentin (ATX, USA) 01:03:51 Yeah, that's totally fine with me. So I have my approval, they're waiting on a maintainer of the upstream repo approval, of the SDK repo approval, so… That's all that's… that Trask is waiting on to merge.
Thank you, Trask, I've been behind seeing this, I'll bring this up in the next SIG.
I mean, Kayla didn't have much, you know, much to say about it, but…
Daniel Azuma 01:04:15 Well, I can…
Ariel @arielvalentin (ATX, USA) 01:04:16 If there's any objections, that's all good.
Daniel Azuma 01:04:19 I can approve it, that's fine.
Ariel @arielvalentin (ATX, USA) 01:04:28 Was this not released?
Daniel Azuma 01:04:38 I think it hasn't been released yet.
the…
Ariel @arielvalentin (ATX, USA) 01:04:43 So, then…
Daniel Azuma 01:04:45 It might be that the…
Ariel @arielvalentin (ATX, USA) 01:04:48 The nightly bug thing that I had mentioned, scheduled release bug thing.
Daniel Azuma 01:04:52 So, yeah, I'll get on that right away. I'm sure it's simple.
Ariel @arielvalentin (ATX, USA) 01:04:57 So, I haven't looked at this myself, but I think… I suspect that we're gonna have a lot of these kinds of problems where Because of… we still have re-entrants We still have the mutex problem in the SDK repo.
So let me, let me whine about that a little bit.
Daniel Azuma 01:05:19 We're at 11 o'clock.
Ariel @arielvalentin (ATX, USA) 01:05:21 Oh, are we? I just love talking.
I love talking.
We can pause here for today.
Because we are at time.
But I'd love to keep the conversation going async in Slack for folks.
The one thing that I want to point out, and Daniel, I don't know if you had a chance to look at this… But… Here is my… Rant about concurrency and parallel… parallel… parallelism.
You know what I mean? Please look at this. But right now, there is a bug in the SDK. Because we use mutexes and try and tried to meet the specification.
Right.
where, we're unable… to mutate spans.
Because of the use of mutexes and mutexes being non-reentrant in… for, in, in, in the current threat.
So.
Daniel Azuma 01:06:32 Have we considered just swapping them out for monitors, which are reentrant?
Ariel @arielvalentin (ATX, USA) 01:06:38 There you go. So that's some work that would have to be done in the OTA SDK.
To address this, so that it could, So that we could do… we'd be able to mutate spans.
That's part of, As part of this, and that would also mean that, you know, the loggers, for example, we wouldn't have to be dealing You know, because if it were to use monitors, it wouldn't have to… Have those hacks where it's kind of like, are you… already emitting a log or something like that. Like, I just saw that there was a… PR… that PR to try to address the problems with the… The logger running into a deadlock issue.
Because it's trying to log something?
Sorry, let me go back to what that issue was, but… I'll go back into that issue, and I'll read that PR one more time, but it looks like they were trying to address a problem with concurrency.
In… Related to the lager.
Which was causing a recursive deadlock.
And I don't know if it's… and it's… and we're using thread local variables… sorry, fiber… fiber local variables.
Let me go back here.
Let me reshare my screen.
I'm sorry for making everybody late, or, like, go over a few minutes.
But I didn't get a chance to review this PR. But it looks like the solution here is to use fiber local variables order to… Avoid re-logging something.
And it was preventing a deadlock.
No, I didn't know… let me see what the deadlocks were. It was referring to… Causes a deadlock when trying to do this.
So, it's trying to format a message, which tries to call on a minute, which tries to put a queue in, which tries to put a warning… oh, okay. So this is more of, like, a… a circular reference, but then it's trying to use the same mutex which causes a deadlock, right? Okay.
So it's non-reentrant in that case, but I think also there's, like, a circular dependency here.
Where a logger is trying to log something, but it's using the… OpenTelemetry Logger.
To log a problem that the OpenTelemetry logger has.
I don't know!
It's kind of like, okay, enough.
Right?
Enough. So there's gotta be, like, There's an inception problem going on in that case.
Daniel Azuma 01:09:33 Mr.
Ariel @arielvalentin (ATX, USA) 01:09:34 But again, but again, I'm trying to acquire the same mutex, making them… and utilizing mutexes, which are non-reentrant, is at the core of some of these problems here.
But anyway… That's enough of that. Thank you very much for allowing me to go over 5 minutes. I hope I, did not bore you to death, and I was, better… I'll do better next time, you know?
Daniel Azuma 01:10:00 Good to see you again, welcome back.
Ariel @arielvalentin (ATX, USA) 01:10:02 Thank you, my friend. You take care now.
Daniel Azuma 01:10:04 Tube.
