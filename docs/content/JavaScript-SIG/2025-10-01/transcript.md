SIG: JavaScript SIG
Date: 2025-10-01
Duration: 58 minutes
============================================================

## Zoom Recording Transcript

**Marc Pichler (Dynatrace)** 00:19 Hello?
**David Luna Bistuer** 00:35 Hello?
**Marc Pichler (Dynatrace)** 01:13 Alright, let's get started.
The first topic here is David with a call for reviews on the user HPR.
**David Luna Bistuer** 01:30 Yeah, you want me to add?
Some context on that.
**Marc Pichler (Dynatrace)** 01:34 I… Already have a context, but if anybody else wants to…
Talk about it a bit more.
**David Luna Bistuer** 01:44 So, yeah, just the sense is, basically this PR, first, what it does is fixes a problem that…
CRPC exporter was not setting the user agent, header.
So if you… if you have a collector and debug… enable debugging, you see that the headers, they don't… they have the gRPCGS,
Header as the user agent.
But not anything else, so, it turns out that instead of sending metadata, you have to… when you're creating the client, you have to… you need to pass specific options for the user agent.
Also, what it does is this PR, also what it does is adding a new option in exporters, which is the, an extra user agent to depend.
to the current one, to the default one, okay? So, it's adding this property, it's leaking, because it's, it's adding on the legacy options.
So, also, it adds the same property to the actual HTTP options and gRPC options.
And then… Well, it resolves the userism, finally.
In the exporter, I think.
Have a look.
So…
It's not a big change, I would say, but since it's moving parts of the logic to other places.
I would like to have your attention on that.
**Marc Pichler (Dynatrace)** 03:10 Okay.
We're, review that one for sure.
Sorry for not getting to it earlier, the.
**David Luna Bistuer** 03:19 Oh, no, no.
**Marc Pichler (Dynatrace)** 03:20 Things were kind of keeping me busy, but, hoping for that to be done soon, and then we can…
Get this merged, hopefully soon.
**David Luna Bistuer** 03:29 Okay.
**Marc Pichler (Dynatrace)** 03:31 Alright, doesn't anybody… Sorry.
**David Luna Bistuer** 03:35 But basically, this, PR is because the spec has been updated, so now it allows to have a… if you want to pass an extra user agent.
for the fiat exporters. So that's the reason of having this PR.
Feel free to challenge it and… question.
these questions or whatever, okay?
**Marc Pichler (Dynatrace)** 03:58 Alright, thank you. Does anybody have any questions about this?
If not, then I for sure have a look. I encourage others to do the same.
Alright.
**David Luna Bistuer** 04:20 Okay.
Yeah.
Sounds like a lot of days, don't be afraid of that, so I'm going to be short. So, just some highlights of the changes on the CI.
Basically, if we are taking more or less time than before.
So, basically, when it comes to compilation, we do… because of
How NX works, it's like, whenever you touch a package.
This package is affected, and also, we have out-instrumentations, which depends on all the… on the rest of the packages, so at the end, we are ending up compiling everything.
well, not everything, well, everything that is related to Node.
We see that here we are not gaining or losing any time on the CI.
On the testing, if we are only touching the code.
Yeah, we have, faster CI, because we are actually only compiling and testing the packets in question, and then the autoimmmentation mode.
Okay, so here we have again.
The problem comes when… whenever we have, something that Trent, highlighted, in a conversation. It was, like, okay, whenever we talk to the packages on…
okay, we need to test everything, because maybe something is affected, okay? This is correct, I'd say, but it's slower than it was before, because, what we had before was a task that was adding… well, we still have the task that adds label
labels to the… for the packages that are, involved in that PR.
And actually, that testing were using those labels. Actually, it was getting the… reading the labels, and then transforming to package names to test that.
So, for example, there is an example here, so your data dependency on one instrumentation, maybe the types, maybe a new version of the package to be instrumented. This modifies the packages and of that instrumentation, but also the package log.
Previously, we were only testing that specific package because there was a label for that package.
Okay, now what we're doing, because NX says that, okay, everything… we need to test everything, because everything could be affected, because of the packets lock.
We test all the packages. We do test and test all versions for all the packages, which…
Means that we have a really, really slower.
PRs, okay?
So, maybe for discussion, or maybe for,
I don't know, to give, have a conversation. So, specific possible improvements we can do is, like, okay, we're still
can apply cache on the compilation, because some of… most of the times.
We modify just only one package, but we compile everything, so if we have maybe, what was, you know, the last commit, then…
the build of the last committee main, we can just leverage that to…
speed up the compilation step. That's, a first.
And then, maybe we can just revert the testing to actually check on labels.
We still have a specific portfolk, which is test-out versions.
That led us to run the test manually if we… if we need to. So…
that's kind of a… yeah, at least two things that, we can do for speed up the CI.
So, there is no… I'll work on that, maybe I'll create a PR.
Maybe for next week?
So we can… you can have a look. But if you have any ideas on what can be improved, or if you are…
Any… any concerns or whatever, just let me know, and…
I'll try to work with that.
Good.
**Trent Mick** 08:18 Hey, David, we had been discussing a little bit briefly, and I think batting around some ideas of things that we want to do. I'm not… I'm not sure we want to go as far as
not running TAV by default. I think we liked the idea of doing that, but we were talking about.
maybe… well, various ideas, I'm not sure we need to lay them all out here, but.
**David Luna Bistuer** 08:40 I think before…
**Trent Mick** 08:44 Maybe to save you time on implementing stuff, we should have an issue that discusses and agree on how we want
The various use cases, and how we want it to work by default, and what's…
required checks, and what's skippable, and that kind of thing. If we nail that down, then we can implement it afterwards. I don't want you to waste your time on…
**David Luna Bistuer** 09:04 Damn.
**Trent Mick** 09:05 Something that we don't want to be a certain way.
Thanks for spending all the time looking at it.
**David Luna Bistuer** 09:15 Okay, so that is, I'll create an issue, and then we can just move the conversation there, and if anyone is interested, it can,
Give some feedback.
**Marc Pichler (Dynatrace)** 09:26 I have one immediate question, maybe, on the,
on how we could handle the test or versions things when package log JSON has changed. I wonder if it would be possible to exclude package log JSON from this affected
computation thing.
And then just, have a label for, please run all tester versions things that we can put on, let's say, renovate what PRs and stuff like that.
So regular PRs would still…
Get the normal treatment of, using this automatic effective computation thing to, run tester versions and the normal tests.
But if anything changes package log JSON, we would just have to go in manually and add that label to trigger a full run. If we're interested in that, if we see it and we say.
It's probably fine, we can merge it in, then we just don't add the labor and merge it as is.
Might be one of the ways.
to do it, if that's possible, somehow. I haven't checked, if that's even feasible.
**David Luna Bistuer** 10:41 I think it's a good idea. Let me have a look at the NX implementation and see what we can do.
Okay, so I'll put, whatever I find, I'll put it in that issue, and then we can discuss on that.
**Marc Pichler (Dynatrace)** 10:54 Yeah, that sounds good.
**David Luna Bistuer** 10:57 Thank you.
**Marc Pichler (Dynatrace)** 10:57 Thanks for, looking into all that stuff, the, build…
thing in the country prevail is, ginormous, so, thanks for, taking the time to, sort out the things there.
**David Luna Bistuer** 11:14 Happy to do it, don't worry.
Okay, so that's it.
Thanks.
**Marc Pichler (Dynatrace)** 11:20 Thank you.
Alright, looks like we're at the end of the agenda here. Does anybody have any other topics?
I would like to discuss…
If there's no other topics, then I guess we can move on to the… oh.
Ian, you have a topic to discuss.
**Ian Ferrier** 11:49 Yes, hello, everybody. This is my first time here, by the way.
**Marc Pichler (Dynatrace)** 11:55 Nice to meet you.
**Ian Ferrier** 11:56 Is it alright if I share screen, by any chance?
And… Is that, is that a possibility?
**Marc Pichler (Dynatrace)** 12:04 Usually we, just briefly talk about what's, what the topic we're,
We're talking about this, and then, if you wanna, share your screen, we can… we can do that.
**Ian Ferrier** 12:17 Absolutely.
**Marc Pichler (Dynatrace)** 12:17 So, yeah.
**Ian Ferrier** 12:19 Thank you, by the way. I definitely want to learn the flow of things here.
**Marc Pichler (Dynatrace)** 12:24 Yeah, sure, sorry, we don't have, like, any guide for these SIG meetings, it's just, kind of ad hoc, but usually, yeah, if you, just write down anything you would like to discuss on the agenda, we can…
And… look into it, but yeah.
**Ian Ferrier** 12:44 But really quick, I don't know, if… I'm on the browser front-end side of things when it comes to OpenTelemetry. I have been noticing that…
My spans kind of get stuck in a pending state in the network tab section.
of my browser, it'll just… I can… I could pull up a screenshot if needed, or share a screen, but I've got many payloads coming out of the SDK, trying to make it out. I don't think it's reaching the limit of the beacon, payload size.
I think it's still well within that limit.
So I'm just trying to figure out where y'all might suggest, debugging on our end. We have an OpenTelemetry collector that we reach out to first.
Which then goes into, I think I see somebody familiar from Honeycomb, goes in a honeycomb refinery, but that's another… a whole other technology, I think.
Just trying to see if anybody has any suggestions.
For how to handle this situation, because…
I'm looking at, right now, my current network tab, there's about 90% of my payloads going out, or just, like, not going… they're not making it at all, according to the network tab.
**Marc Pichler (Dynatrace)** 14:03 Did you have it running before, by any chance? Did it work before, and broke recently, or.
**Ian Ferrier** 14:13 It's… it's been…
I would say it was, like, about 50% of them were… were… were coming out, or were, like, actually going, and I was just kind of dealing with that, but now it's slowly starting to get…
Less and less.
Going out, and that might be that we're adding a bunch of attributes, and…
maybe we're reaching a size limit or something on our end. I'm not entirely sure. I just… I wasn't sure if anyone's experienced this issue first, if that's something that's come up at any point for folks.
On the browser or client side.
**Marc Pichler (Dynatrace)** 14:44 I'm not aware of anything like that, happening. One thing that we changed recently, though, is that we, added this, fetch-based transport
And that one, actually has, what is it, keep alive set to true.
And if you define headers in your exporter config.
Then it previously used XHR to export, and Keep Alive has the same, so if Keep Alive is set to true on the…
fetch card, that would mean that it's subject to the same limit as send beacon was.
Yeah. So it might be that you're running now into a problem where, you previously had XHR,
making the request, and now Fetch is doing it, but you're running into that limit.
Yeah, I'm not sure, though, if that is what you're actually running into.
**Ian Ferrier** 15:50 I'm not entirely sure. Would it be good if I just opened up a GitHub issue on this topic, probably?
**Marc Pichler (Dynatrace)** 15:56 Sure, yeah, okay. That's ideal. Yeah. We, usually also do a little triage session, at the end of each, each meeting to make sure that bugs, get triaged properly, and we try to help out folks there.
Thank you very much. Yeah, but… yeah, thanks for, bringing that up.
Yeah, maybe we can troubleshoot it a bit more. If you want, you can also share your screen, and we can have a look at it here on the car. Maybe we can see something that sticks out immediately, if you're comfortable with that.
**Ian Ferrier** 16:35 Yeah, I'm okay with sharing if y'all want to right now. That's up to y'all.
I don't want to commandeer.
Yeah, it seems like I kind of broke order here. I'm sorry, this is the first time I'm getting into open source as well, so this is a…
**Marc Pichler (Dynatrace)** 16:49 No, this is great. Thanks for joining the meeting. We usually don't get many end users here, so it's actually great to have somebody who's using it on the car with us.
**Ian Ferrier** 17:02 And also, like…
**Marc Pichler (Dynatrace)** 17:04 usually at the end of the SIG meeting, there's just, bug triage and stuff like that. It's also something that we can do, async. So, yeah, if you want to share your screen, please, go ahead.
**Ian Ferrier** 17:16 Okay. I have… I'm hitting the button finally, I think.
Okay, so I think we're… I think I'm sharing now at this point. Does that everybody see network tab, browser? Okay, hopefully I'm being secure, hopefully I'm not showing anything secret from my company.
Shiff, I am, though.
But as you can see here, I… just from… Moving around my, my page.
we're collecting all of our HTTP requests and all that that we're sending out, all of our Vue error handling, we're Vue.js, we have a custom error handler that we put in, and a bunch of other things get swallowed into our,
Spam processing, and then out through the…
OTLP exporter, I think is what it is. And then we…
send that out. We don't really configure it to do anything, or we haven't configured anything like batch size, although at the very bottom here, I kind of demoed switching up to, like, a smaller batch size, and then, a more frequent export.
That was right after the successful trace, payload going out. But as you can see, we're still stuck in pending, like, I would say.
This is probably about… I'll go ahead and say 90-95% of these are stuck in a pending state, so…
That's kind of what I'm facing right now. Not even sure where to even begin, and I was just looking to see, hey, come out to y'all and maybe get a…
Or test the water, see if this has ever been experienced before.
**Marc Pichler (Dynatrace)** 18:52 Yeah, so this I definitely have not seen before. Would be interesting to have some example to try out.
And you said you're sending that to a collector, right? So… Collector should also be… fine, that case. Also…
Hmm.
Export. It's usually rather quick, so it wouldn't run into any timeouts or anything like that.
Hmm.
That's a weird case. So it obviously gets to a place where it…
It tries to export, but then gets stuck in pending.
**Ian Ferrier** 19:43 Yep.
**Marc Pichler (Dynatrace)** 19:44 Hmm.
I think, Jamie, you found an issue here, right?
**Jamie Danielson** 19:51 Yeah, it looks…
similar. I don't know if you can hear me or not, I'm in a coffee shop right now.
But it kind of matches a little bit of what you were talking about, Mark, and what I'm curious about is if this also gives us a repro to…
Try it out, because this old, issue does have
At least a little bit of something talking about different, you know, settings on the bash span processor.
**Ian Ferrier** 20:19 Yeah, I should actually mention, Jamie, you're from Honeycomb, right? If I… or potentially.
**Jamie Danielson** 20:25 Yeah.
**Ian Ferrier** 20:25 Yeah. I should also note that we are currently using the Honeycomb Web SDK that wraps around OTEL, but we kind of also…
We've hybrided it back towards OpenTelemetry a little bit, because that's where we started from, so we're slowly, like, seeing what all we can abstract back into Honeycomb. But I think this area, we are using our own exporter, but I think we are tied into y'all's batch span processor. I don't know if that would be something to make aware of here.
**Jamie Danielson** 20:54 Gotcha. It could be relevant. I haven't looked at the web SDK in a little bit, but depending on what other, you know.
things might be tied into the Honeycomb batch fan processor for the Web SDK could be.
Potentially relevant, but ideally, there's not a whole lot
Different when it comes to those main…
pieces. Even the batch pin processor, I think, is interchangeable if you wanted to replace it with the…
like, just regular vanilla hotel stand processor.
**Ian Ferrier** 21:23 Okay.
**Jamie Danielson** 21:24 but I feel like… It would be worth, like you said, opening an issue on
HotelJS, and, like, noting that.
**Ian Ferrier** 21:35 Yep.
**Jamie Danielson** 21:35 Let's see…
I don't think there should be something specific to the Web SDK that would cause it, but it's worth
Noting that.
**Ian Ferrier** 21:53 And I can also, I'll make note of, like, what our pipeline on the background looks, or on the back end looks like as well, in that issue as well.
maybe there might be something in between our, collector and our front end. I know we have Fastly, which could be rate-limiting by some means, or something along those lines, because we do have it guarded by the… our front-end endpoint guarded by Fastly, so…
I can take a look and kind of
Give some more clarity into that.
**Jamie Danielson** 22:23 Did you say if there's errors in the console?
**Ian Ferrier** 22:26 There, there are no errors.
Basically, just some… Other stuff. CSBA violation and some view errors that… We have, but nothing else.
Unfortunately.
**Trent Mick** 22:40 If you click on any of those traces, is there a flyout that shows more data on individual requests?
**Ian Ferrier** 22:46 Yeah.
**Trent Mick** 22:51 Is there any response?
**Ian Ferrier** 22:53 Oh, anyway.
**Trent Mick** 22:54 Is there a partial response, or any…
**Jamie Danielson** 22:57 Yeah, maybe there's nothing, hence.
**Trent Mick** 22:58 Hence the pending.
**Jamie Danielson** 23:00 Yeah.
**Ian Ferrier** 23:01 Hmm.
Not that I'm seeing.
It's kind of… kind of dead.
**Trent Mick** 23:11 Quest is not finished, it's stalled.
What's the initiator tab?
**Marc Pichler (Dynatrace)** 23:32 That's also… And that might be an older version of the export as well.
Seeing the, OTRP exporter browser pace, I think that version is…
Older now, because we don't have that class anymore.
**Ian Ferrier** 24:00 Oh, gotcha.
**Marc Pichler (Dynatrace)** 24:02 So,
I think likely an update won't help in that case, because it will just… like, most of the code in the background is still the same, so, something to try, maybe. I don't think it will really help a lot, but, it will just rule out a few other things.
**Trent Mick** 24:23 This is still version 1.x of the SDK, I think.
I think the browser base was removed before the 2.X.
I mean, yeah, the…
**Ian Ferrier** 24:35 Yeah.
**Trent Mick** 24:35 the browser… I mean, sorry, the exporter backend code's still gonna be mostly the same, but yeah.
**Jamie Danielson** 24:47 Do you know what version of the Web SDK you're using?
**Ian Ferrier** 24:51 Let me see here… Highly top secret things, don't take screenshots.
**Marc Pichler (Dynatrace)** 25:01 We are actually recording this card, so.
**Trent Mick** 25:05 If it's sensitive, you know.
**Marc Pichler (Dynatrace)** 25:06 go off, and… Yeah, you can…
**Ian Ferrier** 25:08 I'm not too worried. I'm just messing around. It's all good.
**Marc Pichler (Dynatrace)** 25:13 Yeah, you can also pause the share while you're going through stuff, if you, feel more comfortable that way.
**Ian Ferrier** 25:20 Smart idea. I will do that just for…
**Jamie Danielson** 25:23 Just a…
**Ian Ferrier** 25:24 just in case here. Yep. Let me go ahead and pull up…
**Jamie Danielson** 25:29 Yeah, looks like the Web SDK now has… there's, like, zero-dot versions and one-dot versions, and I think the one dots have the updated Hotel.js dependencies.
So, that could be relevant.
**Ian Ferrier** 25:47 Yeah, I'm kind of seeing some… I'm assuming this could theoretically be an issue here.
If you're saying the one dot… versions.
It looks like we might have an older exporter here.
**Jamie Danielson** 26:05 I guess, and so there's also the option, I guess, too, if you wanted to open an issue on the Web SDK repo, and then if, you know, looking at it, they say, actually, this is something we want to fix upstream, or that is off upstream, or whatever else, but I have a feeling it's probably a version mismatch.
**Ian Ferrier** 26:22 Yes.
**Jamie Danielson** 26:26 Yeah, so definitely an older version.
**Ian Ferrier** 26:29 Yep.
For sure.
**Marc Pichler (Dynatrace)** 26:37 Yeah, one thing to keep in mind when updating is the exporter got worse a bit for web use, and then got better again. So, if you go all the way to the latest version, it should be better than it was before, but stuff in between, there were few hiccups on the way.
**Ian Ferrier** 26:55 There were some hiccups.
**Marc Pichler (Dynatrace)** 26:56 Yes.
So… It's worse.
**Jamie Danielson** 26:59 it gets better. So yeah, probably the…
**Marc Pichler (Dynatrace)** 27:01 The first day.
**Jamie Danielson** 27:02 is update to the latest zero-dot web SDK, because there's definitely a few there, see what that does. And then if not, then it might be…
Yeah, might have to go to, like, the later one-dot, but that might require other changes, depending on what you have.
**Ian Ferrier** 27:19 Yeah, for sure.
Appreciate y'all. Thank you.
**Marc Pichler (Dynatrace)** 27:24 Thanks for, bringing it up, and coming on the call today.
Yep.
Yeah, as Jamie said, once you open an issue, we'll probably take some more time to look into it, offline, and then, yeah, if you…
want to join the call again sometime, feel free to also hop on. It's always great to have any people who are end users on the call, so first, I think.
**Ian Ferrier** 27:59 Glad to break the ice.
Thank you all.
**Marc Pichler (Dynatrace)** 28:03 Alright, thank you.
Alright, that would share again.
Alright.
The next topic here is… Mmm, Maria, about…
**MG Marylia Gutierrez** 28:30 I just added now, because I saw that we got tagged, is somebody updated the…
the example on the… basically, yeah, the documentation, because they were saying, oh, this is, like, not using the traces, so they removed all the beginning, but I think the idea of the example was, like.
set up your application, start adding, and, like, going step by step. But they were just trying to remove. I found it a little weird to, like, remove all of them, so yeah, I just added a comment to, like, saying, like.
No, we are doing this as a step-by-step, just to go over. But yeah, just in case anyone also wants to look, since they tag us on it.
Or anyone, yeah, maybe actually agrees with the removal of all of that, but yeah, I don't know.
**Marc Pichler (Dynatrace)** 29:21 I think we follow, like, the same pattern on all the language, examples, right?
**MG Marylia Gutierrez** 29:27 Yeah, yeah, as always, though, roll dice.
**Marc Pichler (Dynatrace)** 29:30 Yeah, so I'm wondering if the other language examples do something similar to what we do here, where, like, just the tracer is created and,
It isn't used yet.
**MG Marylia Gutierrez** 29:48 Yeah, maybe, like, adding in the extra step, like, for example, don't add any instrumentation. Then the next step, just add the traces, and then use… yeah, maybe that.
**Marc Pichler (Dynatrace)** 29:59 Yeah, so this one here is,
I see, but it, it just explains that, like, the scope,
In which a tracer should be created, but it's not actually using it yet, and then, down below, the scope changes a bit.
In the new example.
Yeah, I will definitely have a look at this one.
**Jamie Danielson** 30:31 To your point, it's definitely worth looking at what the other languages are like, because I'm pretty sure, right, that was the whole idea of the docs, was to be as consistent as possible in the different languages. So…
if they… also have a different… yeah, but… That's a good call-out.
**Marc Pichler (Dynatrace)** 30:49 And I think, signalin opened an issue… Some time ago now?
That he worked on…
**Jamie Danielson** 31:03 The reference application for getting started.
**Marc Pichler (Dynatrace)** 31:05 reference application, and I think the reference application is very similar to the one
Also has this dice roller… thing.
So…
Yeah, nope.
**Jamie Danielson** 31:25 It would be really nice. I didn't… I didn't actually read what's in there, but if it's, like, the suggestion of
making the application actually, like, available and runnable, I would be a huge fan of that, because anytime you're copy-pasting code into a Markdown file without running it first, you're kind of setting yourself up for
Issues, I feel like.
**Marc Pichler (Dynatrace)** 31:47 Yeah.
Hello.
Yeah, to get back to this,
to the question here is… I'm also not sure if that's the right way, but I guess some more digging into the other docs,
Should.
Give us some clarity.
Yeah, I will, definitely… Have to look at that one elsewhere.
Anything that sticks out to any of you on the call immediately that we should talk about here?
If not, then, yeah.
encourage everybody to have a look, with your comments on the PR.
And… Then we can go ahead there.
Next topic is also Marlia.
**MG Marylia Gutierrez** 32:57 Yeah, just one… just because it's not gonna… if we're going to triage, this one is not gonna show, because we triaged a couple weeks ago, but yeah, this person just added, like, can somebody look at… because I don't think we actually assigned somebody to look into this, because we just say, like, yep, it's an issue, but…
I don't remember if we actually assigned anyone to actually…
**Marc Pichler (Dynatrace)** 33:17 We… we did not, I think.
Yeah.
All of these that, are kind of,
And then there's some troubleshooting needed before actually being able to So if these things,
When looking at the… the,
pipes that are being used here. This is actually in the node,
in the node export, and I think the reason why this is happening is because…
So, when you import it, in TypeScript.
Oh, it's not an experiment, it's the core package.
Then you will get the types from…
Here, and that, by default, uses the Node.js types for everything.
So it ends up actually getting the types for this thing here, which was,
transpired with Node in mind, so, it's not that bad that these are in there, but, if you use it in a browser, then you'll get that
the Node.js types, where it then becomes bad.
So yeah, I were…
Assign myself, and we'll try to have a look at this one, unless anybody else wants to give it a shot.
**Trent Mick** 35:12 Would this magically get solved by one of David's…
build real ESM packages options. I can't remember if one of those had a package.json change where the types were actually a different…
Types exports were actually a different thing, so, like, maybe not magically solved, but a potential path where there's a different build file for the types? I don't know.
**Marc Pichler (Dynatrace)** 35:38 I think it… Probably won't?
Because there… there would still be… so I guess the types would also be rolled up into one file, and if that… these types are,
made with no JS in mind, then,
If you have a package that does.
export for Node.js and the web.
You still won't get the different types there.
Boom.
What it could be…
I guess the, we won't see it here, because the Undichi instrumentation is actually just for notes, so it doesn't run into that problem at all.
Yeah.
I will have a look at this one.
I'm not sure if it's possible to have, like, a conditional export, like,
Like, these four types as well.
That would be the ideal.
Bing.
So that… whatever, Node.js types we're, sending.
Their way, don't get sent away, and we just have the browser types here.
I've never tried it before, so… This is just me guessing.
Yeah, it's always kind of difficult with, prioritizing these bugs, because that's actually… it is…
a little bit of a problem, but, there's definitely other bugs that are, kind of higher priority for a reason, because they actually have, telemetry discussing problems and stuff like that. So,
Yeah.
-Oh.
But this one seems to be…
Important enough for the person to come back, so maybe…
there's something that I'm kind of… missing here…
That would make this higher priority, so I will have another look, and I will, reprioritize it if needed.
Figure out that it's costing.
more trouble than I initially thought.
Alright.
If there's no more topics…
And I guess we can move on to bug triage. As always, if you have anything that you would like to discuss, please feel free to just, write it here on the,
On the doc, and let me know that you would like to talk about it, and then, we can interrupt pack triage and talk about your topics.
Alright, so the first one here is… Something that…
is related to Webpack 4 support, which we have dropped. So ever… Put a comment here.
**Trent Mick** 40:00 Mark, are you able to set the width on your… Screen share.
I think I can… I don't know what the setting is, but…
**Marc Pichler (Dynatrace)** 40:08 Is it too smart?
**Trent Mick** 40:10 You have the full width thing going, so that you have, like, 3-point bond going on.
**Marc Pichler (Dynatrace)** 40:22 Fitbit.
Alright.
**Trent Mick** 40:26 Thanks.
**Marc Pichler (Dynatrace)** 40:28 Sure.
-Oh.
And so, what we would have to do to,
To solve this is we would have to introduce a bunch of new packages,
to break the different entry points out, and then introduce a bunch of new public API to share code across these packages, which could be,
would be difficult to deal with.
I think we now have,
We're also maintain this group.
I will just ping them here, and ask if they have any, Ideas, or any,
opinions on what bundler support should be for other packages, how far back we should support, and maybe we can shed some light on this.
And then continue making discussions based on what they come up with here.
**Trent Mick** 42:41 I don't know if it helps, the last Webpack 4 release was in 2023.
**Marc Pichler (Dynatrace)** 42:48 Yeah,
I think it's not that out of date, and also updating from Webpack 4 to Webpack 5 is kind of,
cumbersome, having… having done it in the… in the core repo, was a bit…
It wasn't the most fun thing to do, let's put it that way. So,
Yeah, I definitely feel the pain that the person is having here, because, like.
just having to update to Webpack 5 for using the library is, annoying, but the more time goes on, the more Webpack 5 is going to become the new, thing.
So… it's kind of difficult to figure out, but I would really like, to figure out what the,
Rosa maintainers, what ideas they have, or plans they have for, bundle support, so that we can align if necessary, on that side.
Alright, let's see if they come back with… Oh, and also… Error.
The next one is also a browser one, which is,
I think context gets lost after a second to wait. I was actually meaning who…
reach out to… Shang Tsung about this, so I'll put this again in my notes.
So the reason why this isn't working is,
Because we're kind of blocked on JavaScript language features, which is this TC39 async context proposal.
I can actually link that here as well.
Which we would need to, actually…
Do proper context management in the browser.
So… yeah.
I guess this more or less, either needs the proposal to go through, and then our browser to be updated, or a different approach be taken in the browser.
Which, I guess is happening with the, browser sig anyway.
**MG Marylia Gutierrez** 46:16 Yeah, kind of, like, related.
to the SIG? Is there a group for, like, the browser SIG, specifically, or label, that… to make sure that they are getting
Tag on those issues, just in case they don't miss.
**Marc Pichler (Dynatrace)** 46:31 I don't think there is right now.
**Trent Mick** 46:34 I doubt they're looking, but we have a target browser that I've been sometimes adding.
**Marc Pichler (Dynatrace)** 46:39 But…
**Trent Mick** 46:40 I'm not aware that the browser, SIG is actively looking at these.
**Marc Pichler (Dynatrace)** 46:48 Yeah, I was actually wondering,
Unfortunately, the browser sync meeting happened to land in an unconvenient time for me. I thought that I would be able to attend more often than I actually can.
But I was actually wondering if they would be interested to get, approval rights on the, browser.
relevant packages. So, since we now have this different publishing process where a maintainer has to approve,
packages being published to NPM.
We can add more approvers now, which is a side effect of… Like… not, perfect.
Previously, we didn't add a lot of approvers, because you get right access to the repo, and then you can technically run all the workflows and publish everything as you like. And now, we don't have
That limitation anymore, so you would still have write access, based on Whatever is in the…
In the code owner's file, but, yeah, you wouldn't have any access to published packages.
So, adding more folks, from…
other 6, to the, code owner's file, it becomes more feasible now.
Yeah.
David, I think you are, attending the BrowserSeq, quite frequently, right?
**David Luna Bistuer** 48:33 Yeah. Yeah, I'm digging it.
**Marc Pichler (Dynatrace)** 48:35 Would you be interested in bringing that up, with them, to…
Kind of test the waters a little bit.
**David Luna Bistuer** 48:45 Okay.
No.
**Marc Pichler (Dynatrace)** 48:47 So… We would basically just,
give them the same rights as an approver has on the… on the car repo, and then, they would be…
We would update the code owner's file.
For them, to, like, Get approval access on all the browser-related packages, so that would be…
**David Luna Bistuer** 49:10 Or so.
**Marc Pichler (Dynatrace)** 49:13 this, OpenTelemetry… That's the example. I wanted to go to the experimental packages here.
**David Luna Bistuer** 49:22 Are the Fed's instrumentation, and…
**Marc Pichler (Dynatrace)** 49:25 Yeah, there's this webcommon package here, stuff like that.
And also the shared packages, of course, would also be interesting to them, like OpenTelemetry Core and all the other ones.
And then we can make sure that we have, through the code owner's file, filtered out, or…
Node.js thinks that they are likely not interested in, like, the SDK node package and stuff like that.
**David Luna Bistuer** 49:53 Okay.
**Marc Pichler (Dynatrace)** 49:54 So that they don't get spammed with a bunch of things that aren't relevant.
**David Luna Bistuer** 50:01 Okay, good. So, yeah, I'll tell you, it's tomorrow, if I'm not mistaken.
So yeah, we can bring up the topic tomorrow.
**Marc Pichler (Dynatrace)** 50:10 Okay.
**David Luna Bistuer** 50:12 Yep.
**Marc Pichler (Dynatrace)** 50:14 Right.
then I guess we can… Move on to the next thing here.
This is… 100 people now, and, that is the I.O. Redis instrumentation, which…
Yeah, they are looking to have,
Mortyx expand somewhere in here, which is… Apparently not exported.
Let's see here… one is probably name.
DP connect, ready disconnect, ready, set, ready, get…
Ready, set, and ready to skit.
And… Yeah, so it seems that…
This here is not wrapped in another span.
Which, if I recall correctly…
Somantic conventions… There's probably some redis… singing.
It states that… should be there.
Individual operations are known to have the same command, and that command should be prepended by a multi-pipeline.
Right, so that then looks like,
E2.
Which means the telemetry is incomplete or missing.
And my link is here,
Alright, and I guess… It's true for both, ready single already, so…
Can leave both labors on here, and… Make it to an end.
I'll also update the title, too.
Alright.
So that's the first one here.
And we can move on to the next one, which is, SQS process hook. No longer available.
Yes, this was removed,
opium processing span. Yes, I think also that this is the case.
**Trent Mick** 56:20 So I'm not sure what the process is here. Do we just, like…
Unfortunately, just close it as designed.
Or…
**Marc Pichler (Dynatrace)** 56:28 I think so, yeah.
I guess we're,
there's this not planned, which I think would be the one to use for this. I will, just type up a quick comment that says,
It's really worth eating currently.
No, inconvenience, not the right word.
I take some time offline to think about the thing, so you don't have to watch me type stuff live on the car.
All right, looks like we are pretty much out of time for the meeting today anyway. So, I will type something up right after this, so don't forget.
Thank you, everybody, for joining today. Yeah.
Have a nice… Rest of your day, and see you next week.
**Trent Mick** 57:42 Hi, thanks.
**Jamie Danielson** 57:43 Michelle.
**Trent Mick** 57:43 Nice Friday.
**Jamie Danielson** 57:45 Thanks a lot.
**Jackson-iPhone15** 57:45 Yep. Bye.
