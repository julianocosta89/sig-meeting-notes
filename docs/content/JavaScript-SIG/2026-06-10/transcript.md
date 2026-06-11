SIG: JavaScript SIG
Date: 2026-06-10
Duration: 59 minutes
============================================================

## Zoom Recording Transcript

**Marc Pichler (Dynatrace)** 01:36 Hello?
**Matt Wear** 01:40 Whoa.
**Marylia Gutierrez** 01:41 No.
**Raphaël Thériault** 01:45 Hello.
**Marc Pichler (Dynatrace)** 02:03 One night.
Let's get started. The first topic on here is… I don't know.
**Pranav Sharma** 02:23 Ace.
**Marc Pichler (Dynatrace)** 02:25 Hey.
I just had a look at this PR earlier, actually.
**Pranav Sharma** 02:34 I see.
**Marc Pichler (Dynatrace)** 02:35 It does look good. From, like, a, from the perspective that, of what we talked about last week, I will give it another pass, and I think then it should be good to merge. I haven't seen any obvious, problems, so I think I probably won't find anything anymore.
But I just wanna, like, get a bit more into detail of what the code doesn't, and I think we should be good to go.
**Pranav Sharma** 03:12 Okay, thank you, appreciate the reviews. Thank you.
**Marc Pichler (Dynatrace)** 03:16 Thanks for working on it.
Alright.
Does anybody have any other topics you would like to discuss?
Looks like no topics. As always, if there's something you would like to discuss and we're doing triage, then please feel free to… Just interrupt me, and then we can go back to discussing your topics.
We haven't done bug triage in a while, so, Now is probably a good time to do it anyway.
this is, something about… Timing code in… Trace SDK… So, sophisticated release space… It looks like… The log entry… It seems that this is actually also affecting logs, so I'm also putting… SDK logs on here.
Usually, these things only pop up in, in the trace SDK, but looks like logs is also affected this time around.
They were put on… Nope.
be too labeled, because, it's incorrect telemetry, and it looks like somebody has worked on a PR for this already, so, Would be good to also have a look at that one.
There's a bunch of comments here as well.
Just approve the workflows so that we can see if the tests are passing with this.
Hopefully, it should be an easy fix.
Alright, I think that was it for the core repo.
Let's see if there's anything that obvious, sticks out that was reported just as a plain issue.
This looks like a bug report from the title.
- It looks like more of a feature request, I think. The way to figure out whether band processor export failed is usually through the global error, and And they have already founded… This might be more of a feature request, actually.
And I'm not sure if we can implement that feature request and still be spec compliant on that, but we'll have to… Figure it out.
I type something up later to let them know, what to look into before we can go ahead on that one.
Alright, let's head on to… The country people, here we have express instrumentation.
Looks like, Way that we display the… or the way that we put the paths into… The attributes isn't… isn't fully reflecting anymore what's… what's going on, so… I'm gonna also put the P2 label on there, because the telemetry is… Probably wrong, or not what they'd expect.
And you can continue on from there. It looks like there's actually two pull requests already.
Looks like this person here came first, so… Sure, we should probably look into this.
So that's, Instrumentation Express.
Buck, then we can move on.
Oh, that also seems to be… Express-related… Looks like, that's actually something that we run into fairly often, these warnings.
pop up.
sometimes… Due to, And actually can sometimes, just because we, push that over the limit with installing, any event handlers.
that we need for generating telemetry, so this is always a bit difficult to figure out what's actually going on.
Seems like it's either Instrumentation Router or Instrumentation Express, so I will put these two labels on there, and then… this is… E3, because it's either a performance issue, or it is… just, annoying log spam, so… We need to figure out which one it is there.
Moving on to user interaction instrumentation. I'm not sure if this one actually is still here in this repo, but we could check that fairly easily.
Yes, it's still here.
Let's see if there's actually stuff in there, yes.
Actually… Don't really know exactly how the user interaction instrumentation works.
Looks like there's two normal maps inside the weak map, and… It should be all weak clips.
According to… What this person is saying.
it's very likely that this is an issue. I think the user interaction instrumentation was fairly neglected over the past few years, so… There's a lot of… weird stuff going on there.
This sounds like a P1 issue to me, so I put the P1 label on there, because if that, just keeps… Growing, then, that's obviously not a good experience.
Alright.
Looks like… That was it for the country preval.
**Matt Wear** 13:42 Hey, Mark. I was slow, but I dug up some documentation for force flush. I dropped it.
**Marc Pichler (Dynatrace)** 13:48 Huh.
**Matt Wear** 13:49 puppets.
It does say it should provide a way to let the caller know whether it succeeded, failed, or timed out.
So it seems like rejecting would probably be… be a way to do that. I gave you logs first, because that's what I first found, but trace is the second link, because I think it was actually a simple span processor. But same… Basically, same verbiage, just replaced, like, Span with log.
So my read is that maybe it's a bug, and maybe we can accommodate them.
**Marc Pichler (Dynatrace)** 14:30 So this is, Tracer provider spec, and then the other one… Was the logs back right?
**Matt Wear** 14:46 Yeah, logs, I probably should not have pasted in, it was just, like, the first one I found.
**Pranav Sharma** 14:53 Does this exist… does this exist for meters as well?
**Matt Wear** 14:59 See, meters are a little different.
Possibly.
I'm not gonna say yes or no until I can actually find anything.
Sit.
**Marc Pichler (Dynatrace)** 15:21 Yeah, I think, so this is in context of, this issue that we talked about earlier, right? One that I labored feature request.
For the simple spam processor, it's kind of a weird edge case, where… every, Every export happens immediately after you end the span, and it happens synchronously, or at least it's triggered synchronously.
Oh… In the context of this specification here… oh, that's the logar one, So, for the trace SDK here, I'm actually wondering if… This even applies here, because this says, for the provider to immediately export RSPANs that have not been exported.
or the internal processes. So there's a bunch of processes going on, and if it's a simple span processor, immediately once it ended… once the span is ended, then this is the one that hasn't been exported yet, and it gets immediately exported.
So, whenever somebody calls force flush on On a simple span processor, the only way for them to get the information Is… the only information that they would get is for something that is currently in progress.
Which I guess this is what they're asking for here, right?
**Matt Wear** 17:30 Yeah, I don't know, as we talk this through, it's kind of like… It's kind of weird calling force flush on a processor yourself, maybe? I feel like… that's really there for, like, the SDK to call when you call it on the… Oh.
Tracer provider?
Is that…
**Marc Pichler (Dynatrace)** 17:52 Yeah, I think it usually goes through the tracer provider, because… That just does it for all of them. I think I've seen some people use it just for… A singular processor, if they wanna, trigger export to just one destination. I think you've seen that before, but it's not the most common way of doing that.
And then doing it on a simpler span processor is… I wonder what the use case for it is.
**Matt Wear** 18:27 Yeah, use case aside, it does seem like it should still notify a failure, just so that, like, you know, if a tracer provider was calling it, that it.
**Marc Pichler (Dynatrace)** 18:35 Bye.
**Matt Wear** 18:36 By its color of, A failure on one of the processors, but… Yeah, I don't know.
Boom.
If this is not useful, we don't have to keep talking about it, I just found some documentation that seemed to say that Failure should be reported.
**Marc Pichler (Dynatrace)** 18:55 Thanks for… yeah, thanks for looking it up.
**Matt Wear** 19:01 No problem.
**Marc Pichler (Dynatrace)** 19:04 This is an intriguing issue, because I kind of want to know what Or, like, how to… Get into a state where… The force flush on a simple span processor would actually… do anything.
Because the Emory export is already the… it already includes the forest flush.
Bing.
I will type up my thoughts on that, on the issue, and ask them.
what it is… About, and what they're trying to accomplish with it, because it could also be… Then I'm just completely misunderstanding what they're trying to do here.
But yeah, if… if it would trigger an export, then I think… Parse Flash should, of course, recheck in that sense, and just let… Let the user know that it's, that it has failed.
Right.
There's no other topics, I guess we could move on to… The Art Cognache.
So we have 59 PRs in Core Ripple, and 44 in Contrape, so I guess we're gonna go with court this time.
The first one is a long-standing, PR to add the logs package to the API.
Package, and… I can check our milestone here.
How far along we are to make that happen.
I think the only thing that's missing right now is, Figuring out what we're gonna do with the log attributes type, And then also there's this one here, which is to double-check that everything that's logger configurator related is marked as experimental.
So, yeah, if anybody has time to look into that, that would move things forward a bit, and then… Yeah, it's really just… Just renaming or widening of, the… attributes type.
Which… We have been talking about here.
And once that's done, we can request the TC to have a look to review, and then nothing should be in the way anymore for promoting the logs API to Stable.
**Carlos Alberto Cortez** 22:45 There was… part, by the way, that I wanted to review, which was regarding the processors, which actually kind of touches with what you were discussing now. So I will do that before the end of the week, and then, yeah, after that, yeah, should be done. Because I already reviewed part of the SDK and the API, if you remember… if you remember those parts.
**Marc Pichler (Dynatrace)** 23:06 Sorry, I didn't get the last few words that you said. I think the.
**Carlos Alberto Cortez** 23:11 that I already did some, initial, paths on the API, and part of the.
**Marc Pichler (Dynatrace)** 23:17 J.
**Carlos Alberto Cortez** 23:17 So yeah.
Yeah. This will be, of course, yeah, it will be… we need also somebody else from the TC to come and do a formal review, but hopefully this helps, yeah.
**Marc Pichler (Dynatrace)** 23:30 Yeah, thanks for, Starting out with the… with the review already, that was very helpful, really good to… Cross some things off the list early, so that, There will be, hopefully, less stuff to work through later on.
So yeah, I think the main, main thing that we're looking at right now is just these, attribute, like, what we're gonna do with the attribute type, and once we've sorted that out, I think we should be good to go.
Alright, continuing on.
With the triage thing, I… did.
make a few changes to the renovate config lately. This was one of the things that… We're still missing here.
Yeah, I think the reason for that was to make sure that minor bumps… or anything other that's not JS will be… still opened without a dependency dashboard approver, I think this makes sense, so I just… Merge this in real quick.
And I think I did merge all the other PRs that this person had opened, so, I think this should be the last one here.
If anybody has time, I also have another PR for Renovate, here, which… We recently set the minimum release age to 7 days to avoid, pulling in dependencies that, Might be compromised by some supply chain attack and stuff like that, but turns out that, like, the schedule is also set to 7 days, so, it always gets updated before we can actually merge it, so if anybody has time to put a review on that one would appreciate it. Then we can actually… Continue, with the log file maintenance PRs, which, They are good to do, quickly before, It gets so large that when we run into an issue, we don't know what's going on anymore.
Right. So… That's this one, I'm not sure if I now clicked the merge button, yes. So that's queued. We should be good to go with this, and then we can move on to the next one.
We talked about this one quite often, so… We're gonna assign this to myself… Looks like there were a bunch of comments here already.
And it looks like the person is not working on this anymore. We can still leave this open for a bit, and if the person doesn't come back to it, we can close it.
Gonna check the… Agenda again. Seems like no, no new topics here. As always, if you have something that you would like to talk about during the Sikh meeting, please feel free to just interrupt.
**Marylia Gutierrez** 27:35 Somebody posted on the…
**Marc Pichler (Dynatrace)** 27:36 Oh my gosh.
**Marylia Gutierrez** 27:37 Somebody posted on the JS dev channel about, like, 3 PRs that they want to review.
**Marc Pichler (Dynatrace)** 27:43 Yeah, we can look at those.
Let's see… Oh… Oh, this is the first one.
I think this was… this is the fix for one of the issues we looked at earlier.
There's dynamic path fragments.
Here, it looks like the coverage reports.
Failing.
It's odd.
Don't block the PR, though. We might have to look into that. I think I saw that on main somewhere.
Expect the same thing's happening here.
We'll have to look into that.
So yeah, this is the first PR here.
These are always really difficult to figure out, without actually running them.
And seeing what's going on.
Looks like all the tests for this are passing.
I do remember that, the way that we generate the route or, instrumentation Express is kind of fragile, There were quite a few issues reported in the past, which were then fixed, but it's one of these things… That, don't like to, Change a lot, because a lot of stuff can go wrong, and it impacts usually a bunch of people.
That would also be interesting to see how often this runs.
If that's cached somehow, or if that runs every time a request comes in.
is… This actually looks fairly straightforward.
I mean, the tests are passing, I think we should be okay.
marching to see… I still have another look at, where this is called, actually.
architecture match route… Let's see here… It's probably used somewhere in here.
And it looks like this is… Card, essentially, every time we… Get the request.
I think there might be a way to… Look into if the performance can be somehow improved for this.
I'm not exactly sure if the overhead will be… that much.
Probably not. Probably would be fine.
Might still be worth benchmarking this.
Looking at what they wrote in Slack.
I also have a bunch of other PRs that are somewhat loosely related to this.
Looks like there's… One thing that just adds a test… I'm tested, cool.
path, according to function without a video.
Oops.
Okay, so I guess we can merge that one in.
It's a bit easier to review that one.
And there's also a parted request test on Windows, which apparently happened. I have no way of verifying this right now.
If this is actually what's happening, looks like, I fire had a look at this…
**Raphaël Thériault** 36:00 Yeah, I don't really have a way to test it either, so…
**Marc Pichler (Dynatrace)** 36:10 It's always a bit difficult to figure out with these things that just happen on Windows, it seems.
Like, this is just a smaller issue that affects the developer experience.
So it doesn't really warrant spinning up, whole VM, just to check it out.
This not seems necessary to give enough time for the client's events to fire.
Where did assertion runs on Windows?
This is really weird.
I wonder if we run into something like that?
There's Will already.
I seem to remember some instance in the past where I, also had a similar problem.
Because in the core repo, we actually have tests that are also run on Windows, And this… Horror thing kind of feels very familiar.
will probably also be something to dig into later. At least we got one of these PRs merged.
Ideally, I would like to… Avoid having, any timing-related stuff in there.
Even if this one just is a Windows-related thing, it can be annoying if it fails.
Every… every once in a while, so it would be good to have that.
That must not be flaky.
Because that would be even harder to detect if we have a flaky test on Windows, which, almost nobody, can… Easily.
Try out locally, then, detecting that will be kind of… Painful.
Yeah, looking into if there's any other… Things in the… Cheers, children.
Looks like this here is… Another take on the same issue, where these… Oh, white coat.
syntax things… Are being introduced.
This also looks… Looks okay to just, Approve the workflow run for now, and then we can also re-look into that later.
Follow me.
I'm just going through the pull requests now that are in the AutoJS channel, so, Just in case you're wondering where I'm getting these from.
This is one I was actually looking at earlier, and I was wondering, if that is actually the… Way that we're supposed to do.
are to handle these sorts of things. So essentially, what is happening here is… We have, This issue, where there's this, auto event name.
Bing.
And… what Trent mentioned here is that the… if he understands correctly, that the log bridge, would translate an attribute or something that's, like, utterly bent name.
2… Actually be present on the top-level, event name property.
But looking at what is being… what has been added to the hotel event name, spec… it says here, this attribute should be used by non-OTRP exporters, When the destination does not support, Event name or equivalent field.
It actually says here. Maybe I've been just misreading that then. So it looks like this… is actually the way to go, for it. So, we should… Probably map anything that has this auto event name thing on there, to actually, the event name property on the log record, and then… People can define events.
Just with a peanut onion.
or Winston, whatever they're using, so… Looks like Hector already reviewed this PR here.
the change itself should be fairly straightforward, I think.
Also, what they're doing here is the… Import the event name.
Which… is stable already.
And then they just, where did they actually get that from?
That looks okay.
I did a bunch of tests… Sports are good.
Move this to dependencies… They did plant the version, which… Shouldn't be an issue for us.
And they also have… Same thing happening here in… No.
And here, DHF… Also, this event name attribute… Did they get… Let me make sure that they don't add anything that's not a string.
And a bunch of tests again.
Just get the block named there.
Our abstet, which is good, and then we have the same thing for winds and transport.
Which, I wonder if there's a better way of doing that.
But it all our sort of looks… Gee… That actually looks fine to me, so… I'm gonna prove that.
Oh, looks like there's some pending checks.
I'm gonna have those run before… And then, once these are finished running them.
Can approve that one as well.
Reassigning myself so I don't forget.
look over everything, and then, not approve it, that'd be a shame.
Alright, we can go back to… a user, or at least I don't think there's anything… Where's… did somebody ask for? There's one more, that somebody asked for.
About a week ago, so I guess we can also look into that. This is for instrumentation runtime node, which, That's an active resource.
gauge.
Discussion about community conventions, It's actually already merged.
You're independent of each other, and then… Let's see here… looks like there's actually, nothing left on… some comf to look into, and it.
**Marylia Gutierrez** 49:07 Yeah, I'm trying to remember, I think, like, all the cement convention stuff got merged, but because, Daniel had put some comments there, but he never got back after we made the changes. So yeah, you can see, like, the latest comments are just, like, the person tagging Again, saying, like, anything else, anything else? Because I think he addressed all the things.
**Marc Pichler (Dynatrace)** 49:35 I'm actually not familiar too much with, what was added there in SEMConf.
Oh no, that's not the right repo.
really need a shortcut for some comf there.
Now, this is resource active, right?
So…
**Marylia Gutierrez** 50:17 Yeah, so that was the new thing that he added.
**Marc Pichler (Dynatrace)** 50:29 No good resource active here, Age of active resources that are currently keeping diabetic alive.
Alright, so… Great, I think it's the data… I'm gonna check some… No chairs documentation on it, because I actually don't know exactly what we get back from that.
Oh… see here… I have strings containing the types of active resources that are keeping it alive currently, so… What I'm mostly interested in right now is figuring out If these known types are a finite set of… things which… I suppose they are, but it's good to double-check that.
To make sure we don't get cardinality issues.
Imagination on this is actually fairly… Minimer, so… as opposed… If this is, something that is… a finite set of keys, then I think we should be fine with this approach.
It's fairly simple.
I guess this is one of the things that Dan mentioned.
Where it should record zero now.
Instead of disappearing… Which I'm actually not sure if it would be the right way to think about it.
I don't want to walk back the decision that was already made, but I'm just curious what the discussion was here.
It means if you have some resources, like, immediate keeping the value and that drops to zero, that drop will never be reported.
Yeah, I think that makes sense, actually, now thinking about it.
Just trying to… Like, there's probably no good way to, Remove it, then, once it is zero.
Actually, we could just remove the key, from there, then we are currently iterating over it, that's also kind of odd.
It's annoying to do. It's probably better to just keep a meeting zero for it.
It would just mean that metric streams are showing up, and once they've shown up, once.
And… They'll just continue being there.
Which I guess would be fine. One could derive some, information from that behavior.
This is just generated, so the tutorials will be fine.
And we have a bunch of tests.
okay to me. Also, I'd be inclined to… Approve.pR.
underneath the open, in case, anybody wants to have another look at this.
Also… Put a note here.
Oh, I've seen my… Local notes to… reach out to Dan if he has it.
another comment on this. Otherwise, I'll just merge this in, during this week, and then… I'm also hoping to have a release this week, so, then we can… Get this out to people… soonish.
Alright, looks like time is up already.
So, I guess we can… Commit a meeting here. Thank you, everybody, for joining.
Have a nice week, and see you next week.
**Marylia Gutierrez** 57:46 Thank you, thank you for driving.
**Hector Hernandez** 57:48 Thank you very much.
**Raphaël Thériault** 57:50 Thanks.
**Marc Pichler (Dynatrace)** 57:52 Great.
