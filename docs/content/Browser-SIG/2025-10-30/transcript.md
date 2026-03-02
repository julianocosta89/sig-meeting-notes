SIG: Browser SIG
Date: 2025-10-30
Duration: 32 minutes
Zoom Recording URL: https://zoom.us/rec/share/dUNsehfkq9hzvvvda3kIrO_pbepFC2k7ik3axkdZgiW5EoaYllCm_qdjZsr063CN.nrkBT3aJwKyEUFTR
============================================================

## Zoom Recording Transcript

**Ted Young** 00:11 Yo.
**Jared Freeze (embrace)** 00:16 Hello, what's up?
**Ted Young** 00:21 Nothing…
Too much. I had a total delay of game yesterday. I walked down into my basement for the first time in forever and discovered it flooded the last.
**Jared Freeze (embrace)** 00:33 That's true.
**Martin Kuba** 00:35 Excuse me.
**Ted Young** 00:36 So…
**Jared Freeze (embrace)** 00:37 Terrible.
**Ted Young** 00:38 Yesterday. I know it didn't happen yesterday, so…
**Jared Freeze (embrace)** 00:45 It's the worst.
**Ted Young** 00:47 Dealing with that nonsense.
Never.
**Martin Kuba** 00:54 So you have to, you have to get a pump or something, too.
**Ted Young** 00:58 I ended up just mopping it out.
Which took forever. But it was, like…
the amount of time it would take to, like, go to Home Depot and get something like a sump pump.
and get it back, and set it all up. I was like, I bet if I just start mopping now…
I have one gun.
Before all of that.
And it still took forever.
Yeah.
People were suggesting, oh, use your shop vac as a wet vac, and I was like, whose shop vac is in a state where putting a bunch of water into it would be, like, a good idea?
It's like, are we trying to make glue, like, intentionally? Is that the goal?
**Jared Freeze (embrace)** 02:17 I'm just gonna copy and paste the entire list, because it's everybody except Elliot, so…
**Ted Young** 02:22 Great.
**Jared Freeze (embrace)** 02:22 You don't have to add your name.
Oh, and Benoitz, Benoit?
**Ted Young** 02:31 Yeah.
**Jared Freeze (embrace)** 02:32 My gun.
**Ted Young** 02:42 But… There's David Luna.
**Jared Freeze (embrace)** 02:53 Cool.
**Ted Young** 02:54 Definitely, add things to the agenda if you got them, but otherwise, we've… we've got a list, and we've got people, so…
Let's, maybe kick it off. Joaquin?
**Joaquín Díaz** 03:09 Hey, how are you? Yeah, first of all, I… we created the PR for the semantic conventions for the user action.
I ended up changing it to just being click. One of the suggestions during the PR was that if we have a
like, a… just a user action generic event, it will be hard to understand which attributes you will get based on, like, it will be whatever event.
And it now makes sense, so I just changed it to user click, this case, and so the instrumentation is also about clicks.
Then we can iterate over, like, more events and more instrumentation, or maybe it's the same instrumentation that just handles all the user actions, but in different events.
So that… I got the idea, I think that makes sense. Then they ask if we can add the triage accepted label, which…
I couldn't do it. I don't know how to do it.
**Ted Young** 04:11 They asked you to set that?
**Joaquín Díaz** 04:14 No, they say if a maintainer can do that,
I don't know if it means maintaining of the semantic conventions repo, or what.
**Ted Young** 04:23 Yeah, I think that's what they mean.
**Joaquín Díaz** 04:27 Okay, so if anyone here can do that, because I need to do a change, but he said that I couldn't do it until that label is there, otherwise the PR gets closed.
I… yeah, I don't know why.
**Ted Young** 04:42 That's a little strange, though. That should be the semantic convention SIG adding that as part of their triage process.
**Joaquín Díaz** 04:49 Okay.
**Ted Young** 04:50 In their main… at least, that's my understanding, is they're, like, the spec SIG, so in their main SIG, they… they have, like, a triage process, and they mark that. They use that label.
To know that they actually processed it.
And then they're only looking at the unprocessed things. I'm a little surprised they would ask you to do that, so maybe they'll.
**Joaquín Díaz** 05:10 Yeah, they didn't ask me, they asked, is this someone from the roster segue or maintainer at the triage asset label?
So I don't know. Anyways, that's that, so if you can take a look, if I can get someone to add a label, so I can do another update.
And then, another comment there was to use an existing event, which is called AppWidget Click.
I think it's used for…
Like, more adapts right now?
I know my concern is that some of the attributes
Name, they don't make sense to me, in a browser perspective.
One of the suggestions was to update their description, so we can say, like, if you are in a browser environment, you can fill this in by using this or that.
I'm okay with that, but I… I wanted to bring this here.
like, I think it's going to happen for more events, where we'll have this thing where we want to share things with the other clients, and I think that makes sense. I mean, the most we share with the other clients is better, because then the end user don't… they don't need to think about
The client itself, they have to… they only get the event.
So, I don't know. I think…
If we can have a better description that feels…
the gaps between that name and the browser, I'm fine with that, but I wanted to bring that here.
**Ted Young** 06:47 Yeah, so this has, of course, come up before. Specifically, I think Clicks is, like.
the classic example of, like, this is, like, a cross-platform concept, but you do actually get different data out of the different platforms for a click event, right? Like, the browser is going to give you back a different object to describe that.
Android will. And the question is, like, are they all giving us the same data, and can we just translate all of that into the same…
Generic set.
Of, like, XY coordinates and stuff like that.
Or… Is it the case that… They're totally different.
Or is it more like a middle ground?
Where there's, like, a couple of fields that are common, and then we still want to have, like, for each language, an attribute that describes, like, the original source event.
So maybe it's, like, you have a click event, but then you have an attribute that's, like, browser click data, or something, and that's where we put the browser specific…
**Joaquín Díaz** 07:53 Yes.
**Ted Young** 07:54 Blob of stuff.
like, Android click data or something, and the Android-specific blog that they got from the system goes there.
kind of freewheeling it here, but maybe… I feel like we haven't actually explored that as a middle ground.
Because we were thinking about only having one body field the last time we talked about this.
**Dan Gomez Blanco** 08:16 Just one comment on the… the app events.
They were initially, I think, thought to be, representing both web apps and mobile apps.
I think that was the original idea, so I guess that's where that app.screen.click.
M… Yeah, I don't know if that matches the current…
my expectation for browser, that doesn't really…
Or if we need something else for browser-specific.
**Joaquín Díaz** 08:44 I think it works, like, the attributes that are defined for the event, they work. They have a, like, a coordinate… coordinates that we have on browser.
I suggest the naming is weird, but again, like, I'm open to just on the description of… description of the attributes, say.
how they can be filled for browsers. In that way, we can use the same attributes and same events.
**Wolfgang Therrien** 09:07 Yeah. I think we will need some sort of middle ground there to
capture information that is not part of that lowest common denominator, right? Because there are also events that exist on mobile that do not exist in the browser, right? Or they have different characterizations. Like, a click, a tap, and a long press are all different, like, all expressed differently in mobile, and they don't necessarily exist at all in the browser in that way. And so…
That sort of, like, will lose that fidelity across clients if we try to, meet this lowest common denominator without an additional place to capture that data.
**Joaquín Díaz** 09:47 Yeah, I think I like the idea of…
grouping all the extra attributes together, so, you know, if I…
The coval denominator, as you say, that you have the coordination, you have…
What, what, like, what, what's click?
And then you had, like, another attitude that says, these are all the browser stuff, and you only care about them if you're in a browser environment.
**Ted Young** 10:08 Or maybe not even just browser, right? Like…
Even in these different environments, there's different kinds of clicks.
So, even there, you have a question of, like, do we have a click event, and then a payload area where you've got all the…
Specific details about this event, and then some generic attributes.
I feel like we even ran into problems of, like, different…
Environments don't even agree on the coordinate system.
Being anchored in the same spot.
**Joaquín Díaz** 10:42 Yeah, that's for sure it's going to happen, but it's still… we have an X and Y value, but you know what that means if you know where you are being captured, you capture the event.
But…
**Ted Young** 10:55 I'm just wondering if… where… if anyone has memories for where we left this when we last talked about it in the client SIG, because we may have flipped all the way back around to… there isn't really a point in having a generic click event, because they're all just so different from each other.
**Joaquín Díaz** 11:12 So, in the previous PR, there was a comment
About agreeing or not using the click event.
the app does click event, but then, like, the same person asked the same question on the PR.
So, they are pushing really hard on this,
Anyways, I think, again, like, I'm not opposed to sharing events with
with other clients, I think it makes sense.
hubs.
But I think, yeah.
Should I… Think I'll… Like, common… sorry, yeah, Martin?
**Martin Kuba** 11:54 No, I was just gonna respond to what Ted was saying about, like, if anyone recalled what we talked about, I just remember there being, like, a lengthy discussion about the coordinates.
And, you know, part of the discussion was, like, the namespacing, which is not, obviously.
the main issue here, but I remember that, like, browser has, like, 3 different types of coordinates.
So… so, like, if you just say, like, you know, X or Y, then, like, which one is it? So…
**Ted Young** 12:26 Yeah.
we identified, you don't want to ever have X or Y, you need to actually name these coordinate systems. It needs to be screen X or screen Y or something.
To let you know what it's registered against.
we were still in the phase where we were mixing in, preemptively mixing in, like, optimization stuff into the conversation, so I remember it went sideways.
for that reason as well? Like, do we store this as, like, a comma-separated tuple, was like…
you know, versus, like, an X attribute versus a Y attribute. I think we're, like, past all of that now, and we're fine with just…
having a separate X and Y attribute, and we're not trying to optimize things right now.
But… I don't know.
**Joaquín Díaz** 13:16 Yes.
**Ted Young** 13:16 It'd be good to go to our android brethren and…
and double-check with them, like, are they using this event right now? Or is this just some old stuff that got in there, and now we collectively want to rethink what we're doing?
**Dan Gomez Blanco** 13:31 Yeah. I think this is the sort of stuff that… why we're still keeping the client-side SIG for that.
You know, cross.
Device, discussion.
**Ted Young** 13:41 Yeah.
I mean, I would suggest what we… I would suggest going ahead…
And trying to get as much detailed information as we have about browser click events.
maybe that's what we should do, is, like, let's just go forward with the browser-specific version. Try to figure out all the information we want.
and then talk to the Android people, and just compare notes, and just see how much…
Similarity there is when we get into all of those actual details.
**Joaquín Díaz** 14:16 Max.
Yes, so if you like showing the next tenancy, just bring that up there.
**Ted Young** 14:23 Yeah. When do we have our next client meeting?
**Dan Gomez Blanco** 14:27 There was one on Tuesday, and… well, we're now thinking if we want to restart the weekly… we moved to bi-weekly at some point when we started this SIG, but because now we're trying to focus on, like, this sort of thing specifically, like, you know, in the… on Tuesday, in the client side.
So we said, okay, let's try to put together a proposal for a project, or for an initiative.
that we could, you know, what things do we want to focus on? Session ID, you know, interaction, blah, blah, you know, things that are cross-cutting.
And so this would be an interesting one. And we said that we would talk about it at KubeCon more in detail, because we've got the bi-weekly one, so it's now, basically, it was Tuesday, in two weeks we'll have KubeCon, so we'll have another chat there about this specific thing. What does the client-side SIG want to focus on for cross-cutting aspects?
**Ted Young** 15:21 Okay. Yeah, so KubeCon's in 2 weeks.
I'm out next week for a leadership thing.
**Dan Gomez Blanco** 15:29 You know, async on Slack is probably the…
**Ted Young** 15:32 Yeah, yeah.
**Joaquín Díaz** 15:33 Yes.
**Ted Young** 15:35 let's aim if… for a meeting in 2 weeks, and if it has to be, like, in person at KubeCon, it's great, but maybe let's ask the different SIGs to…
by… not next Tuesday, but two Tuesdays from now, have…
Or maybe by next Tuesday, have a write-up, at least, for what you need.
With the idea that two weeks from now, we're gonna come together and… And sort it all out.
Maybe we can put iOS involved as well. This would be… we don't see much of them, but…
This would be a good thing to reach out and encourage them to… Come to the client SIG.
**Joaquín Díaz** 16:11 Yeah, that makes sense. Cool. So…
We will handle that. I will just flag them and see how we can continue, but ideally.
**Ted Young** 16:22 Yep.
**Joaquín Díaz** 16:23 By the meeting in two weeks, have something right up.
**Ted Young** 16:26 Great.
**Joaquín Díaz** 16:27 Just…
**Ted Young** 16:27 Find all the details about, like, all the platform-specific stuff around clicks, because that's…
That's what we want to hash out.
**Joaquín Díaz** 16:36 Yiff.
Cool. So the other question around that was, so…
On the original PR, they were suggesting to use XPath to identify the element in the browser.
There was a suggestion if you've seen… CSS selectors instead?
I think that works.
to me, but I just wanna…
Bring it here in case there is some concern around that.
I wasn't around when you decided to use XPath, or if you use XPath for other stuff, I don't know.
But to me, yes, CSS selectors are easier to read, and they also say that it's faster, so I… I wouldn't know any other reason to not use them.
Cool. So that's… I can update that.
yeah, that was it for that PR, but I think it's…
Good, we are moving forward.
On the next topic, I also did the instrumentation for this.
There is a PR, I got a review already, but if anyone else want to take a look, that's good.
Separately from the actual code, I am setting up Unitest for the first time on the repo. I'm using byte test with GSTOM.
I think he was enough for this, for the…
Based on the type of thing that I'm testing.
But I'm wondering if you have another opinion on which, like, unit test framework to use?
And, if you think that we should be doing, like, headless browser unit testing before…
Just, like, for every instrumentation, or just wait until we have end-to-end tests and do that on the end-to-end test?
Separately.
**Ted Young** 18:40 I'm wondering what the existing Node.js stuff uses for unit testing.
Can we use the same stuff?
**Joaquín Díaz** 18:50 I took a look, they use,
Mocha and Chai, which is, like, another framework, but it also uses a virtual DOM, like JSDOM. I'm not an actual browser.
I found a few, instrumentations using Web TestRunner to run the tests.
Which is a headless browser, where you can, you know, run the test on an actual browser.
So… I, yeah.
I think it's always faster to use a…
First of all, to run the tests, when they test, like, when you're testing something that you know.
It's just JavaScript or JavaScript, but it's not really… it doesn't really matter which browser runs it.
But I don't know, like…
if you have any other opinions, I also saw that Byteest are… they have an experimental browser mobile Which…
It also… that also runs on the browsers, and supposedly really fast, but it's an experimental.
So I don't know…
If you have any thoughts on that, or do you think we should just set up a web test runner, which is a more…
Standard way of running these tests on the browsers,
I don't know if you have any opinions on that.
**Jared Freeze (embrace)** 20:12 I would say no to Web Test Runner, only because of its age and interests. It doesn't seem…
Let's involved, still not my directives.
not that it's, like, super buggy, but, like, if VTest has a browser, I think we should try it. I think it was a great place to be experimental. And I don't even think it's that experimental, it's, like, baseline.
same structures co-wrote, so I'm all for new stuff, as you all probably know.
**Ted Young** 20:45 Anyone else have feels?
This is the kind of thing I don't want to have a feel about, because I'm not reading the…
I mean, I'm not writing, because I don't want, you know…
**Joaquín Díaz** 20:53 I… I'm open to death.
I, like, bike test works really well for unit testing.
And I'm open to testing for browser mode. Like, it's not something that is going to be…
Clients are not going to consume our unit tests, so if something breaks down, we can change it in the future, just use another test runner.
So it's an internal API that, you know, if it doesn't work, we can change it.
**Ted Young** 21:22 Yeah. But I think I'll later give you the trial list myself.
**Joaquín Díaz** 21:33 I can't set that up. Then… Given that…
I think my other question was whether we want to run
all unit tests against, hand-est browsers, or just use CSTOM, and be like,
knowing where… when we want to run… have this browser know when to run JSTOM, or should we just say, have this browser all the way for unit tests?
And that's it. Or, yeah, I don't know if you have any thoughts on that.
**Jared Freeze (embrace)** 22:06 I think it depends on how fast V-Test is, let's just try it and see. Because if it's a lot faster than the other stuff, that'd be great.
Are the runners free inside?
The Cloud Pond is there.
Like, per time.
Really, I mean, that was a big concern, like, in a lot of places.
**Joaquín Díaz** 22:27 Take these top runners.
**Ted Young** 22:31 I don't know, I mean, like, I think there's some generic GitHub action budget that we have as, like, an organization rate.
I don't know where we're at with that.
I wouldn't worry about that.
**Jared Freeze (embrace)** 22:41 Okay.
**Ted Young** 22:42 For sure.
**Jared Freeze (embrace)** 22:43 Yeah, I think the JS stuff takes 2 hours, so we're probably good.
**Joaquín Díaz** 22:50 Okay.
Then, yeah, I'll set up All unit tests are run.
in browser mode, provide test, and we can see if it is too slow. I mean, we don't have any… almost no go-to test, so it's not going to be slow, but…
In the future, we can see how it goes, but I think it gives us some extra confidence that even unit tests are running against brosters.
Instead of 5 years old lumps, so I think… I think it makes sense for me.
That was slow, I got.
**Ted Young** 23:26 Nice.
In the interest of time, Martin, I moved your item up.
I think that's more important, what I want to talk about.
**Martin Kuba** 23:35 Yeah, I mean, this is really quick. We talked in previous meetings about documenting use cases for the data model, and for the different types of signals we want to collect.
So I opened a PR to start with,
Documenting use cases for the navigation.
event, which we have in progress with both semantic conventions and instrumentation, I would like to… I would like to drive those to completion. So, like, with this, my intent with this PR is just to…
kind of solidify our thinking about the use cases that we're trying to address with this… with this event.
Yeah, I just want to make sure that we're all on the same page here, so please take a look at this, and we can comment on the PR, yeah.
**Ted Young** 24:25 Nice.
Yeah, I think this is super important, for us, in particular, to start getting feedback from people who are not in the SIG, but who are maybe in the client side of the industry.
like… this model, I think, is going to be very helpful for us, so…
So please have a look at this.
My last thing… Is just looking at, dupe…
just looking at things that are in the semantic conventions repo that are labeled Area Browser,
I feel like… Some of this stuff is, like, super old.
Resort by last updated.
I was just wondering about… are there's… do people see stuff on this that's just, like… like…
Totally out of date.
like…
Browser page view effect. I know we're still working on this, right?
**Martin Kuba** 25:48 So, this one's… This one is being replaced by the navigation event, yeah.
**Ted Young** 25:54 Okay, so do we want to close this one?
**Martin Kuba** 25:58 I think so. I think we can close this one. I can add a comment there, or you can do it.
**Ted Young** 26:03 Do you mind, yeah, since you opened it, if you mind adding a comment at closing?
**Martin Kuba** 26:06 That's right.
**Ted Young** 26:11 Defined a standard way to identify a synthetics request.
**Martin Kuba** 26:20 That's a very, very old issue.
**Ted Young** 26:22 Super-duper old, right? I think this is… by synthetics, they mean, I'm guessing, pulling out span metrics?
Is my… I'm just literally guessing.
What that would be in reference to.
If we're talking about… Labeling this thing as a browser thing.
I'm wondering if we can go ahead and close this.
**Joaquín Díaz** 26:47 Yeah, I… I don't think anything from 4 years ago with…
For comments is going to be useful.
**Ted Young** 26:55 this… labeled as… Browser… But… the…
Okay.
Kill that one.
Resource timing event… I know, again, I believe we're… we're still…
Interested in this, so this is still…
something we want to keep open, right? This hasn't been replaced by something new.
For resource timing.
**Martin Kuba** 27:46 We still want this, yeah.
Yep.
And in fact, someone yesterday was… Asking if they could take… Be assigned to the instrumentation.
**Ted Young** 27:57 Oh.
Do we know who?
Because I feel like Carly was taking this on, but I haven't seen Carly around as much.
**Martin Kuba** 28:07 Yeah, it was a person who I don't think has been in this… in this… in the meetings yet.
**Ted Young** 28:13 Have them just ping on Slack if you remember who they are.
To say that they're interested in it, or if you remember where they were interested.
**Martin Kuba** 28:23 Yep.
**Ted Young** 28:27 Reduce overlap between UA and browser namespace. This is something…
I think that's still in flight, right?
Right.
**Martin Kuba** 28:46 Yeah.
**Ted Young** 28:47 Browser versus user agent.
**Martin Kuba** 28:50 That's still in flight, yeah.
**Ted Young** 28:53 Yeah.
Okay.
I'll leave that open…
Document how consumers should identify browser telemetry.
this is, like… having some…
You know, single key people can look at.
To know that something's in the browser.
That's interesting.
I don't think we've thought about this very much.
I can keep it open.
**Wolfgang Therrien** 29:38 Yeah.
**Ted Young** 29:39 But… doesn't seem…
**Martin Kuba** 29:44 Yeah, I think, I think we,
Yeah. I think, if I remember correctly, the outcome was to just look for the presence of some attributes. I think, I don't know if it was, like, presence of the… some browser namespace attributes, or…
Like, a device… device versus…
**Ted Young** 30:04 Yeah. We have, like, device platform operating system kind of things, and that is… we should make sure that… figure out the best way for that to get filled out with browser. I wouldn't be shocked if, for some reason, it's an awkward fit.
**Martin Kuba** 30:21 Undocumented.
**Ted Young** 30:24 Yeah.
Okay.
I think this is good.
Record is available.
And then, user action event, Navigation event, click event.
I think these are all in flight.
Right.
**Joaquín Díaz** 30:46 So, the user action event is,
PR that I took over, I couldn't push the same branch, so I had to make a new PR.
**Ted Young** 30:54 I think we can…
**Joaquín Díaz** 30:56 close this one in favor of the other one that I created.
**Ted Young** 31:00 Okay, do you mind responding to this?
**Joaquín Díaz** 31:04 Yeah.
just say that we are going to close it. I cannot close it, but, I can say that.
**Ted Young** 31:11 Yeah, oh, I see you mentioned it here. Add browser click.
Okay.
Alright, I can just… I'm gonna label it that way, then.
Thanks.
And then Browser Click Events, your new one.
So good.
**Joaquín Díaz** 31:55 Yes.
**Ted Young** 31:56 Great.
Alright, thank you all.
That's all the time we got.
Okay.
**David Luna Bistuer** 32:03 Bye.
