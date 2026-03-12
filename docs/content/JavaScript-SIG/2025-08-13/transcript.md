SIG: JavaScript SIG
Date: 2025-08-13
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

Marc Pichler (Dynatrace) 00:00:27 Blue?
MG Marylia Gutierrez 00:00:29 Hello.
Marc Pichler (Dynatrace) 00:01:53 Looks like we are ready to get started.
the first topic on here is actually my own. So… yeah, guess we can get started right away with this one. This is mostly a question to folks that are involved in the browser-seq as well.
… I think we have discussed it in the past, but I'm not exactly sure anymore what the outcome was back then.
basically what our OTLP exporters are doing right now is, they… use XHR to, export, OTRP, and… There is a push right now to add a fetch transport as well.
… And I'm just generally asking if there's any chance that we could possibly ditch XHR for fetch in these exporters.
Mainly because, it's… basically doing the same thing, more or less, XHR has is more compatible with more browsers, whereas Fetch seems to be less compatible, checking can I use and whatnot, so I'm just wondering if there's any strong opinions on These things.
Removing XHR would help us keep bundle size roughly the same, while still accommodating that feature request.
So, yeah, just running that by all of you to see what your opinions are.
Daniel Dyla (Dynatrace) 00:03:42 I just pasted the Can I Use link, just for reference. Seems like, as usual, IE is the… Is the only significant … Problem.
Marc Pichler (Dynatrace) 00:03:55 most recently released in 2013. I mean, at what point is it old enough to just….
Daniel Dyla (Dynatrace) 00:04:00 I don't know.
Trent Mick 00:04:02 we've.
Daniel Dyla (Dynatrace) 00:04:02 Maybe there's browser files.
Trent Mick 00:04:03 I've already decided to move beyond that for the JSS to KV2 anyway, right?
Daniel Dyla (Dynatrace) 00:04:11 ….
Marc Pichler (Dynatrace) 00:04:13 Yeah, that… so what we changed there is, actually the ECMAScript version, and that, doesn't include any, like, Fetch or XHR, stuff.
But technically, we've moved, beyond that already.
No.
Yeah, it's, mostly IE, and, there's also… this here, I think that also includes this timeout thing, and onTimeout, which we're using.
So I think that is somewhat accurate here. … Yes, look.
some partial support for Internet Explorer.
Whereas with Fetch, we don't.
We don't have that at all.
Daniel Dyla (Dynatrace) 00:05:27 Yeah, I mean, personally, I don't think it's a big problem, but, … I can ask in the browser sig on Thursday.
I can bring this up.
Marc Pichler (Dynatrace) 00:05:38 Awesome, I'd appreciate that. … Yeah, if there's any strong opinions, please feel free to comment on the… CR that I had linked here, … Yup.
generally, I'd like to avoid having, like, this exporter grow and grow, supporting, like, basically everything under the sun. I would like to pick one and stick with that one that has the most, Like, supports the most… uses, which… XHR is doing right now on the browser, but there's other runtimes that, call for fetch, and supporting these would be, Britain move forward, I guess, for, … Yeah, also getting rid of a few old PRs, because the oldest one that we have open right now in the core repo is actually doing this. So… Been something that has been requested quite a bit.
Daniel Dyla (Dynatrace) 00:06:48 Yeah, I mean, if people really complain about it, or it's a big problem, then maybe… Maybe we can publish… An exporter that just does, like, … XHR and… … JSON, or something like that.
like, a minimal… … legacy browser, you know, it works.
Type of exporter.
But I would… I would hesitate to… to do that as a step, like, step one or step 0. I would wait until… we get feedback from the browser folks if XHR is really that important, and if it's important. Is it important for a… Like, how small is the minority?
And… is it okay? My guess is that anybody that's targeting Internet Explorer still is probably used to the idea that they have to do… Suboptimal workarounds.
… In almost every… place, and having to have a separate… JS exporter that doesn't even necessarily support all of the same features might just be one of those places as well.
Marc Pichler (Dynatrace) 00:08:09 Yes, I agree.
Yeah. … be out of office tomorrow, but, yeah, I… Probably watch the recording of the processing, or if there's any, … any outcome right away from that, I would appreciate a comment on the PR, and then I guess we can move ahead with whatever we decide there.
Daniel Dyla (Dynatrace) 00:08:33 Yep, I'll bring it up tomorrow.
Marc Pichler (Dynatrace) 00:08:35 Okay, thank you.
… Alright.
Does anybody have any immediate thoughts about this?
If not, then, I guess tomorrow's processing is the place to continue discussing this.
… Alright, the next topic is, Marilla.
MG Marylia Gutierrez 00:08:58 Yeah, so this one I just bring, because I brought this a couple of weeks ago about, like.
the GC talking about, like, new ways to organize projects and stuff, and now they're doing a little more formal discussion, so just sharing here, because I know it's gonna affect the maintainer job, so just sharing here, in case you guys miss it, too.
To give opinions.
Marc Pichler (Dynatrace) 00:09:25 Awesome, that's, … I don't know, I will have a look at that one.
MG Marylia Gutierrez 00:09:30 Yeah, the gist is pretty much the… like, each repo should have, like, kind of like a roadmap or, like, a project, but they wanna… if any, like, would the equivalent of working groups get created for each SIG to focus on a project?
they want to have, someone from the GC and DC to approve that, and have the, like, as a sponsor, and has their own, like, project board, but if there are also just regular projects that are big inside the SIG, Those should also be projects, kind of, like, similar to what I did for the cart config that I created a project, so that would show up on the main one. So, that is kind of, like, the gist of it, yeah.
Marc Pichler (Dynatrace) 00:10:21 It sounds, … Sounds really good, actually. I will have a look at this, … And… Yes.
It would be interesting to see how… how it will affect, the things that we are already doing. So, yeah.
Alright, does anybody have any additional… Things they would like to… Ask or, talk about, for this topic?
If not, then, … We can move on to the next one, which is also my next topic.
MG Marylia Gutierrez 00:11:10 Yeah, so this is regarding the, like, config provider. So you added the comment saying, like, that you should think you should have, like, an interface and then a function.
So I have, like, more clarifying questions. So one is that I was looking if there is any precedence like, other things that we're doing this, and I saw that we have, like, the meta provider, that the interface is on the API package, and then the actual class implementation is on the SDK metrics. Is that the pattern that we want to follow, or can I still have, like, the interface On the same config package?
Marc Pichler (Dynatrace) 00:11:49 Yes, so what I meant was actually on the same, package. I just didn't specify, there's not too many places where we do that yet. There is… like, one of the examples is here in this webcommon package. There is, like, a create session span processor.
Oh.
That's actually a bad example, because it uses an interface from another package, but … Roughly, the idea is to have, like.
the interface of the thing that you're creating just in the same package for now. I guess there's no need to split it out into a different package. It's just mainly to hide the class type, because the class type will also include the, Like, the private properties were… Like, start fighting each other if you, use different versions of the same package.
And, then you won't be able to assign one back to the old one, and that causes some trouble, usually.
MG Marylia Gutierrez 00:12:55 Yeah, because that was the part that I think I was having a little hard time to understand what is the actual issue, because I was like, okay, now I can't create, like.
the… gonna create an interface one, but my class implementation is gonna pretty much be the file that I already created, but instead, I'm just saying, like, actually implements this interface. But when I actually start using My idea was to then use this class implementation.
Is that still… is that the correct thing that you're telling me to do?
Marc Pichler (Dynatrace) 00:13:24 So, it's kind of difficult to, explain, in… like, words, but I think I had some example here.
… Looks like I didn't.
I seem to remember creating a bunch of examples somewhere.
… So… Essentially, what I, was trying to say here is, like, this getEnvironmentconfigProvider would just return, like, this config provider class that you already created.
But instead of returning the… like, actually using this class type as a return type, it would just use the interface, … As a return type.
So that, any… private properties that you have here. … like this.
our… They don't end up on the actual type that's exported.
MG Marylia Gutierrez 00:14:37 I see, so you want me to return the interface itself there.
Marc Pichler (Dynatrace) 00:14:42 Yes, exactly. So, … Because what's happening right now, if we go to… against PM, and, goal… SDK trace base, for example.
What we have here is, like, these end up on the type, … That, is being exported then, like, on the class type.
And… If you try to assign a basic tracer provider from one version.
two basic tracer providers from another version, then it will say that it doesn't have these, because they are private and, like, they were kind of break to build.
MG Marylia Gutierrez 00:15:39 So, with the other one.
Marc Pichler (Dynatrace) 00:15:42 Like, you can define it in a way that, like, the private properties won't fight each other in that way, and then you don't run into a bunch of version incompatibilities.
Where you might be using, like, a newer version of the config provider, somewhere, and trying to assign it back to an older version. And it technically has more stuff in it, but, the private properties, Can't be guaranteed that they're there, so it, like, breaks the build.
MG Marylia Gutierrez 00:16:13 Hmm, okay, I hear it.
Marc Pichler (Dynatrace) 00:16:15 Yeah, and we didn't do that yet for, most of the other places, because it would be quite a big change to have, like, everything that's a class right now, suddenly have, like, a function that returns, the… actual object there.
That's, like, specified by this interface.
We would have to, like, basically change every… piece of, like, where we have a constructor for some class, and that would just be a huge change for everybody and our users. But if we can get it right.
right at the start, then we will never run into that trouble that we need to migrate later on, so that's why I'm suggesting this here.
MG Marylia Gutierrez 00:17:00 Okay.
Marc Pichler (Dynatrace) 00:17:08 Oh, wait.
Yeah, if you have any further questions, please feel free to reach out. I will see if I can find the example that I made back when I wrote this, so….
MG Marylia Gutierrez 00:17:23 There they go.
Marc Pichler (Dynatrace) 00:17:23 Oh my god.
Yeah, then you can also try it out yourself, and see the problems that it produces. There's… there's been quite a few issues opened in the past with interfaces like the What was it?
I think it was the metric reader or something, where that was actually an abstract class, and it had some private properties, and these Always cause conflicts when something was updated.
And I guess with the conflict provider that's supposed to be used in the public interface somewhere, it would also, cause similar issues.
MG Marylia Gutierrez 00:18:03 Okay.
Okay, cool.
Marc Pichler (Dynatrace) 00:18:09 Okay.
Any other questions, comments?
Concerns.
If not, then, … I guess we can move on to… triage.
It's always, … If… there's another topic that you would like to discuss, please feel free to just let me know while I'm going through the issues here, and then we can go back and discuss the topic.
Alright, the first one is, lazy loading of the create service client constructor, which we do because, … we need to lazy load TRPC.
So that it can get instrumented.
by the instrumentation gRPC package. Otherwise, if you set up the SDK, you will end up with gRPC that's already loaded, and then you, set up the instrumentation, and then you don't get any telemetry from it, so that's why this is there.
I looked into this issue earlier today, … That's kind of… … Sparse on details, but it seems that they are having some trouble with, the bundle itself.
Complaining that this is… Aww.
Doing something that it shouldn't.
And I just asked them if I can have, … somewhat minimal example that I can run myself, so that I can, reproduce and give them some guidance on, what… could be done to change this. So I'll leave that at the triage for now.
And I'll circle back on that one, once the person gets back to me.
Then, the next one is, … Same thing that is already assigned to somebody.
Trent Mick 00:20:38 Yeah, I looked a little bit, … Dan said you'd look, but I don't think you do at this point. He's using something called Temporal Platform.
Which, I gave some ideas there.
It also looks like it's… a mix of, though I didn't mention that here, the… he's using at the top level.
JS SDK version 2.
And then a resource from that gets passed down to… This temporal thing, which creates its own… … exporter? No, I can't remember what little thing, but it's using JS SDK version 1.
So it's… there's mixing stuff in there. There's also worker threads going on.
Which will pick up the dash dash import.
command line… in those threads to create the SDK, and so, I don't know, I gave them some leads to try to… work on it, but I couldn't reproduce the exact issue.
Marc Pichler (Dynatrace) 00:21:42 We're actually wondering if we should, on that warning, attach a stack trace, so that people can see where it's actually coming from.
Trent Mick 00:21:55 Yeah, that's not a bad… I mean, that's what I suggested he do, but that's kind of hard for people to dig in sometimes. It's maybe not a bad idea.
Marc Pichler (Dynatrace) 00:22:03 And we have done that with, … What was it? The span and, like… Doing operations on a span after end, so that people can see where this is actually happening, because before that, it was just, very… Very difficult to figure out where that was being caught.
So, I guess that's something that we could do to… Guide people in the correct direction, because if we can see the stack trace them as well, we will know If it's somewhere in our, code that it's happening, or if it's happening somewhere else.
I were suggested on the issue here. … And then… I guess we can… Go ahead and make the change, it should be fairly straightforward.
… 11.
I'll also add me as an SIE there, and I guess we can still leave that at triage.
But, yeah, right now it seems that it's just incompatible packages, then, … As you said.
And… There's nothing that we can… do here immediately.
to leave.
Daniel Dyla (Dynatrace) 00:24:11 won't.
Marc Pichler (Dynatrace) 00:24:11 issue.
Daniel Dyla (Dynatrace) 00:24:13 Only just now realizing that I was muted. I think this is not a bug.
If we're correct about the… I mean, it's fine to leave it as triage for now, but I'm leaning towards this is not a bug.
Marc Pichler (Dynatrace) 00:24:28 Yeah, I would, … still keep the label on it for now, waiting for the… waiting for the person to get back. We also need an author response on it, I think.
Yeah. ….
Daniel Dyla (Dynatrace) 00:24:45 Sorry, I assigned this to myself, and then promptly went on vacation, and have essentially not been around since, so… Thanks for looking into it, Trent, I appreciate that.
Marc Pichler (Dynatrace) 00:24:59 Yes, thank you for looking into that one. It's a good find with the, temporarily… temporal Leo thing.
… Alright, I guess that's it for the core repo, and then we can move on to Contrip.
Alright.
… This seems to be for… Instrumentation user interaction.
I'll change the title of this so that it… … It's a bit easier to figure out what it's about.
… There seems to be listeners added, and… You're removing evangelism is using signals.
No.
… I guess this component is owned by Opeckney, if I recall correctly.
Yes.
I was actually meaning to, create the PR to sort out some of the ownership, here.
But didn't get around to it yet, so I'm gonna do that in the following… weak.
I'll just write down a note real quick for myself.
Nope.
There's nothing that we can immediately do to resolve the issue. I just know that this user interaction instrumentation has had its fair share of problems in the past, and I'm not sure if it's something that, Would be kept around now that, … There's some work going on in, adding other instrumentations.
Or web things.
Daniel Dyla (Dynatrace) 00:28:24 Stop.
Marc Pichler (Dynatrace) 00:28:30 … Having a hard time prioritizing this as well.
Recess functionality silently breaks.
Do you want to make this.
….
Daniel Dyla (Dynatrace) 00:28:58 Alright.
Marc Pichler (Dynatrace) 00:29:00 That is it, for… contribute backtriage, and then we can move on to… Oh, I'm actually on the wrong… We can move on to country PR triage.
Alright.
Oops, that sorted correctly? No.
That was actually correctly sorted.
So, first one… Jonathan, the… being pinked… … Yeah, looks like I'll have to have a look at that one.
Myself, or actually reach out to them.
the illness.
….
Trent Mick 00:30:21 Poor Jonathan.
Marc Pichler (Dynatrace) 00:30:23 Yeah.
Seems to be… Also changing some… SEMConf things?
Yeah, I'm not sure if that's… Something we would want to do in that way, or if there's this opt-in thing that we would like to do.
Trent Mick 00:30:48 I don't think there is an opt-in for messaging yet.
Sir?
Marc Pichler (Dynatrace) 00:30:53 It's messaging stuff, yeah.
versus URL.
Spring?
You're a fool.
… But it's just this one.
Singing.
I'm not sure what the handling actually is for attributes that are shared, like this.
I guess URL full wouldn't be just a messaging thing, it would also be HTTP, right?
….
Daniel Dyla (Dynatrace) 00:31:22 And other stuff.
Marc Pichler (Dynatrace) 00:31:27 If there's snow… So… Anything that, … we need extra, things that interact with each other, or if the messaging SAMConf thing is only supposed to be upgraded to the latest if … The messaging thing becomes stable.
… Yeah, I will, reach out to the owners here. There's actually multiple owners for this package.
So, … Somebody… Oh, I should take a look here.
Trent Mick 00:32:14 I think we have a number of pings, Tim, over the weeks, but this is a hard one to review, so….
Marc Pichler (Dynatrace) 00:32:22 Yeah, and it doesn't help that I, myself, am not too, familiar with AWS stuff.
I don't have anything ready to test, so it's… Sometimes difficult to read beauties.
… How does React Native stuff, … So, I guess that's something to skip for now. Here seems to have been some activity.
Minding tests… 19 hours calls ago.
… Let's see, what do we have… I've almost added… There is… Bunch of stuff seems to be using the… Logs SDK… … two approvers on it already, so I'd be inclined to, get this merged if Martin Moss assessed it.
… Using fade off already. You think this is experimental.
I'm just… Ping the author, ….
Daniel Dyla (Dynatrace) 00:34:15 I think as long as we're clear about it, there's no disadvantage to releasing it if we don't include it in auto instrumentations, and we're clear about what it is.
Marc Pichler (Dynatrace) 00:34:43 Yeah, just need the build to pass, and then we can merge this in.
… What is the instrumentation… … Yeah, has approvers by the owners, so, … Just needs one.
Final review by someone with right access.
Hmm.
It's… that's nothing that I can quickly do on the car here today, but I put it on the list again.
just going forward very slowly with the PR reviews, as there's a few in core that I have prioritized for myself for now.
There's another browser.
Thing, where there's… Changes requested from my site.
So I just… Write the comment here again.
It's mostly on component owners.
Alright, … That was web exception instrumentation, then this PR, I… Remember… Yeah.
One comment here, so nothing… - Report for this one.
Maybe I should actually, … Postal review with, … So I'll just request it so that it's clear that that's what it's waiting for.
… This one was, the….
Trent Mick 00:38:09 Related to the GCP detector one that we Closed… So, waiting on Aaron still to make a PR separate for that. I'm not sure if this one still would be useful to Aaron in the next PR or not, so I don't know.
Marc Pichler (Dynatrace) 00:38:26 Yeah, I guess, if… it is, just changing some of the assertions in the test user's package, so if that is the package that he wants to use to, test the code that he moves over, then I guess he could just… Changed a few lines here. … So I've been trying to close this one.
Certainly.
as it's fairly small, and was mainly there for the other PR, to move along.
….
Trent Mick 00:39:24 No.
Marc Pichler (Dynatrace) 00:39:37 Then we can move on to the next one. This is… … Bedroking local with response stream….
Trent Mick 00:39:49 We'd been waiting for updates from Eula, but it looks like she did in the last week, so it's on me to review.
I think.
Marc Pichler (Dynatrace) 00:40:00 Okay, thank you for looking into this one.
… So… Guess we can then also skip over that one, as there's quite a few changes that need to be revealed, nothing that's… can be addressed quickly. … Marketing, more IT… Looks like Jonathan reviewed this one.
Oh, nothing to do here as well.
Seems to be going along.
Still undraft. Is this draft? Yes.
Scrimination GraphQL….
Daniel Dyla (Dynatrace) 00:41:05 This is Opeckney again.
Marc Pichler (Dynatrace) 00:41:12 There's nothing to… I can look into right now… This one, I'd looked into that.
Trent Mick 00:41:29 Oh, I have a PR to actually drop that dip.
from… Mmm… one of those two, from Fastify.
Instrumentation.
I think I just got trespassing on that.
No, I didn't.
Marc Pichler (Dynatrace) 00:41:49 It is, actually… Likely related to this type stripping thing.
… duh, duh.
Trent Mick 00:41:57 Actually, it's something about the test build cache failing. I'll try to rerun it again.
Might be something funky with David's… Build cache stuff.
Fair.
Anyway, I'll follow up on that one, and then once that one's in, then it simplifies this.
round of APR so we can get it to regenerate.
Marc Pichler (Dynatrace) 00:42:21 Okay.
Then I will leave the renovate PR open for now.
… This one here is for types I already, painting the… Tests… So I will close this.
Just it's not actionable for now.
And this one we've been holding off for so long, because I always say I'm out of office on the next day, but we can't wait forever, so we will… Released it now.
Alright, … This one is, … Another renovate PR.
That is also failing the test, so it's not action number, so I'm also gonna close this here.
… And this one is in draft, the next one is… Adding instrumentation of OpenAI SDK.
Trent Mick 00:43:53 So this is upstreaming… an instrumentation that I wrote for work.
And that's a… Another co-worker that's doing the job of… Updating it a little bit, from our repo.
… We have to ask around and try to see if we can find another maintainer for this, because I'm not necessarily the best code owner for this one.
So I'll have to ask in the GenAI SIG to see if we can find people there.
Most of the traffic in the GenAI SIG has been about Python instrumentation, so this would be the first JIS one.
And then, I guess, after… Anna Rag and I've finished cycling on this one. I'll get review from any… one of the rest of you, because it probably shouldn't just be an all-elastic push.
Marc Pichler (Dynatrace) 00:44:42 Yeah, that makes sense. … I guess it's fairly up-to-date on the semantic conventions already, right?
Trent Mick 00:44:53 barely up-to-date. I have to… that's kind of one of the reasons I'm not going to be the best person to be the code owner for this, because the GenAI SimConf is moving pretty fast.
Oh.
And it may be a bit behind at this point, I don't know.
The state of the PR is basically reviewable, if anyone wants to jump in and take a look at it. That'd be great.
And hey, if anyone is… has any… I'm there and be interested in being a code owner, please.
Marc Pichler (Dynatrace) 00:45:28 Yes, I think having this instrumentation is, would be really good, because there have been quite a few requests for this already. I've seen, issues being opened, and I think there was one attempt already to try this, right?
Trent Mick 00:45:46 There was that old one, yeah, yeah, which we closed a couple of weeks ago.
Marc Pichler (Dynatrace) 00:45:53 I also put it on… my least, it's just getting longer and longer. But, yeah.
If there's time over, so… Look into that one.
And I encourage everybody who is, interested in… That to also have a look at this.
appear here.
… This type's restify, making quite a large jump, and it is unmaintained, so I'm also going to close this.
Here, as it's not actionable right now.
The next one is… -oh.
Yeah, just PR, … This person needs to be looked at a bit closer here.
… In fact, it's the default disabled instrumentations.
That aren't configurable always.
But the way that we merge these together is kind of a pain, as with most, most config things.
So… It's an in-depth review there. … … Nothing that we can merge right now, because… Pipeline's still running.
… Then we have here, support for Redis V5.
… It looks like they….
Daniel Dyla (Dynatrace) 00:48:18 I think they added it, yeah. So they added the environment variable opt-in. I tried to remove my… requested change, but was unable to last week. So it looks like you have the… I was missing that box. Hold on, before you do that.
I want to see if I have the box right now. This is 29D.
Marc Pichler (Dynatrace) 00:48:37 Because I want to see if somehow I lost a permission or something like that.
Trent Mick 00:48:42 Well, they couldn' is you don't have a block on it if you go to the top.
Marc Pichler (Dynatrace) 00:48:49 Oh, yeah.
Trent Mick 00:48:51 So I don't know what's going on there.
Daniel Dyla (Dynatrace) 00:48:53 So, the top right is, like, requested reviewers.
But the block, it is actually, like, at the bottom.
… because I requested changes, but have not, like… it doesn't dismiss it, it's just re-requesting a new one. That's why I show not blocking at the top.
But it looks like I can dismiss it now, so I wasn't able to last week, so hopefully this was just a….
Trent Mick 00:49:25 GitHub blip.
Daniel Dyla (Dynatrace) 00:49:28 Yep.
Marc Pichler (Dynatrace) 00:49:28 Cool.
Daniel Dyla (Dynatrace) 00:49:35 Yeah, I was able to dismiss it.
I just didn't even have that, ….
Trent Mick 00:49:40 And look at the build filler.
Daniel Dyla (Dynatrace) 00:49:42 I left for last week.
Trent Mick 00:49:43 22, unit test 22. That's the same one that I just mentioned earlier in that earlier PR we were talking about.
But they are in fact, so I wonder what's going on there.
Something we potentially have to look into.
Marc Pichler (Dynatrace) 00:49:59 It could be that there's too many things going on in this… at the same time, … I know that the cache at some point runs out, so if there's too many builds running at the same time, I would assume that… … Artifacts get pushed out before they… So they expire before… It can be downloaded again, maybe?
I'm not sure if that's a setting that we could change.
I'll rerun this and see if… Huh.
Let's see if that serves it.
Seems also to be a, like, code coverage thing, I guess. There's… … I'm not sure Does the merging now already… work with Tesla versions, or is that, still working?
Trent Mick 00:51:04 The CodeCap thing, I… no, I think that's still working progress.
Marc Pichler (Dynatrace) 00:51:07 Okay.
And I guess that's the reason why the codec, thing is failing here.
….
Trent Mick 00:51:17 Yeah, I wouldn't expect anything from CodeCo stuff, yeah. David's out.
This week, so….
Marc Pichler (Dynatrace) 00:51:26 Alright, … Yeah, this also needs, like, probably more in-depth, review now that this opt-in mechanism is in there.
But it seems to be going ahead, so, guess we can move on.
… There is… these two… Yeah, ours that are changing the way that, … ESM output, looks like… be valid ESM, actually. So… One of these is approved now, whereas the other isn't.
Yeah.
Trent Mick 00:52:26 We still wanted to discuss, right, before merging.
Marc Pichler (Dynatrace) 00:52:30 Yeah.
I guess, we can give that some more time, and, David is out right now already, so, … we'll just wait until he's back. I also wanted to put a comment here, because this one is actually… doing it with TSUp, or just ask… … If it is possible to use… because TSUP uses Rollup and is built.
If there's any way to use the underlying tools directly instead of having this extra dependency there.
Right, … Nice. Then, we can move on to the next one.
Which is Instrumentation core.
… Professing… Post to the column here… Seems to be… Somewhat recent activities, so, … Guess we can still wait for the, … Also, to come back here… … I suffered myself.
Surface, I guess if it's so… Unless we have seen.
Hello?
I didn't do it. … So… Have a look at that one later. I still wanted to get a grasp of what exactly has changed in this, thing here.
The next one is in draft.
Then… There is… spread here… Sport streaming handlers… … It's only one big old, so, … I guess I'll leave some time to… … I'm going to have a look at that one.
… This is actually approved by component owners, so… I'll apply the labor here.
Duke squeezing the brush.
This will now parse the labors and rerun test our versions again, so let FP.
… And there's two Renovate PRs, which… Probably can't do anything about it right now.
… And there's one PR for, instrumentation AMQP.
… Adding steeper semantic conventions.
Obsessed into the… That's okay.
Is messaging already stable now?
Daniel Dyla (Dynatrace) 00:58:05 I don't think so. Yeah, no, it's not. It says development.
Trent Mick 00:58:09 Oh, it does have opt-in there for messaging.
Daniel Dyla (Dynatrace) 00:58:13 It does have the opt-in.
Marc Pichler (Dynatrace) 00:58:14 toes.
Daniel Dyla (Dynatrace) 00:58:16 I thought there… there's, like, a PR to make it release candidate, but it's been open for a really long time.
I'm not sure exactly what the blockers are there, but it's coming soon.
Marc Pichler (Dynatrace) 00:58:33 Alright, then I guess this is… Ready for review, but we won't be able to merge this until, the spec is actually Staper.
Oh, move….
MG Marylia Gutierrez 00:59:26 Do you know if maybe this is some of the, like, proof of concepts that they are creating?
Marc Pichler (Dynatrace) 00:59:32 Hmm.
MG Marylia Gutierrez 00:59:33 I don't know, I didn't see any mention, but just in case.
Marc Pichler (Dynatrace) 00:59:36 No.
MG Marylia Gutierrez 00:59:37 Because that would be, like, the case when I was doing, like, for example, the database ones. We were merging before it was a stable, because those were, like, proof of concepts. I don't know if they are depending on that.
Marc Pichler (Dynatrace) 00:59:51 I would, actually right here, unless… This is part of an effort to… -oh.
books.
Bye.
Effort to create prototypes.
Mark, the… Inca searching sent both.
Fast saver.
That is the case.
Please link the corresponding, … issue, wrong.
Alright.
Looks like we're out of time, … Thank you, everybody, for joining.
Have a nice… Week, and see you next week.
Trent Mick 01:01:11 Excellent.
Marc Pichler (Dynatrace) 01:01:14 Thank you, bye.
