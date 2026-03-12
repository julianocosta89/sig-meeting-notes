SIG: Python SIG
Date: 2025-12-04
Duration: 78 minutes
Zoom Recording URL: https://zoom.us/rec/share/9nnTzCFHwXxPm3nZ8cKRPZ2bOqMB6Rc7x7O_LtZ4rMWtL3_omhi4GyKzq_powPTQ.rR3qYFOfXUcY17FI
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 02:29 Hello, everyone.
Welcome, everyone, to the Sweet Python SIG weekly call.
And I shared, on the chat a link to the… to the notes. In the meantime, but we're waiting a few more minutes for more people to join.
Please add yourself as an attendee, and also, if you have, anything you want to discuss, please add it as a… the list of topics. Thank you.
**Aaron Abbott** 04:02 Hello?
**Riccardo Magliocchetti** 05:23 Okay, I think we're gonna start, so welcome again to this week, Python SIG, call?
Okay.
We have a bunch of topics, mostly for me, but… okay, let's start.
Some updates on the log stabilization process, Well, like, yesterday, we released the… analyze, with most of the… Breaking changes and deprecation, We did want to have.
And… Yeah, like, I don't remember.
What's this one? Okay, summary names.
And… yeah, I think, Aaron merged yesterday also the other day, the… Event CP deprecation.
And… and because of this, like, I think last week, I released a new release for the OpenAI instrumentation we have.
Some random fixes. Also, like, Tressloop, some weeks ago, already released, A version of what, was not using the events anymore.
And so, hopefully… Even the percussion didn't break.
Many downstream users.
So, I think on the API SDK side, we are… fully fine.
And… yeah, next step, I think we need to sort out, the logging under part of the issue.
I think we want to move the current logging end out of the… SDK module.
I still haven't looked at it in detail.
But, like, now, like, we have a bit more time, I think, I guess, Next at least would be… Next year, so at least we have a month or so to think about that.
But, like, yesterday's release, bring?
some regression.
The first one is this one, but it's a trivial one, but now, in our test, UTIS package.
We have some warnings, because we have a function that is resetting the… The events, logged events provider.
Yeah.
Event logger provider, sorry. Should be easier to fix.
what?
So, okay, this is a duplicate.
And so, yeah, if anyone wants to take, hello?
Don't wake up.
I don't?
**Aaron Abbott** 08:35 Yeah, I was just gonna say, I was a little surprised that people are using the test utils.
But… no, that's okay. It's just… it just prints a warning, though, right? Like, in their test case.
**Riccardo Magliocchetti** 08:47 Yep.
Yeah, I think… The reporter is suggesting to just move the import inside the function that requires the thing, because… I guess that is not using the function.
I saw, like… We could probably save the deprecation just by moving the imports.
**Aaron Abbott** 09:13 Yeah, I think we could do that, yeah. It's also, like.
Once we remove it, because we're going to remove… delete the actual event stuff at some point to just remove this code.
Great.
**Riccardo Magliocchetti** 09:31 Yep.
**Aaron Abbott** 09:33 Yeah, I mean, it should be a small thing. I don't think it's a big deal either way, so…
**Riccardo Magliocchetti** 09:37 No, no, right? It's just, like, probably just annoying for people that looks at best, That's my childhood, yeah.
**Aaron Abbott** 09:47 Okay.
**Riccardo Magliocchetti** 09:50 And then we had a brief… Issue?
That was reported and been closed.
about the… I think it's, the Azure Monitor.
What, is importing log data?
Like, maybe someone from Microsoft can…
**guptaradhika** 10:13 PH, Ricardo, like, we're already taking care of it and fixing, the breaking changes in the SDK, and we're planning to do what it used to do. So, this, a copy of this issue is already there in the SDK issue, so we'll kind of, resolve it from there.
**Riccardo Magliocchetti** 10:35 Okay.
**Hector Hernandez** 10:35 Yeah, problem with this one is that we were prepared for this change, but we were on a release freeze that… Just finished today, so we were… it was, like, the timing was a little bit off, but, yeah, we'll take care of this right away.
**Riccardo Magliocchetti** 10:53 Okay, so you can release again? Thank you, okay.
**guptaradhika** 10:56 We can use today only, that's why we weren't able to push the chambers yesterday.
**Riccardo Magliocchetti** 11:01 Oh, okay.
**guptaradhika** 11:02 Maybe.
**Riccardo Magliocchetti** 11:03 Okay, thank you.
Sorry for the break, actually.
Dila, you added the note, like, do eventually remove the underscore from the logs package.
I guess, yes, but, like, probably, like.
Why don't we have checked it again with… We are fine, we just probably just… Move the module, and… Keep the underscore logs prefixed 1 as duplicated.
And then remove it.
**Aaron Abbott** 11:43 Okay, yeah, that makes sense.
And then we bump up the version number, or… How do we mark it stable?
**Riccardo Magliocchetti** 11:55 Good question.
Erin, do you have an opinion?
**Aaron Abbott** 12:04 I mean, what was the question? Just getting rid of the underscore? No, the version… Like, do we change the version number?
like, incre… What does it know? It's like… It's just, like, in the API and SDK, right, so the… The versions are already, like, 1.
Right.
So there's nothing… to do… Other than, like, remove the underscore and just say it's stable.
Yeah.
We should… we should probably keep, I don't know if there's a good way to keep the underscore around.
Just so that people don't, like.
You know, upgrade to the stable one, and then it breaks because it's stable.
So maybe we could keep the underscore one.
Around, but then expose the import without the underscore.
I don't know, what do you think?
Yep, I agree that… Keeping it around makes sense.
**Riccardo Magliocchetti** 13:24 Yeah.
I agree.
**Aaron Abbott** 13:33 Cool. Did you have anything else in mind, Ricardo? Like, you know, blog post or something, I don't know.
**Riccardo Magliocchetti** 13:40 No, I probably just… you know.
Wait a few more days for more people to… You know, to have a shot to play with the brackages, and we'll see.
If, like… We'll probably, like, we'll see if we miss it.
some more uses, or some more use cases, I don't know, yeah.
But select… but I have to select.
Pretty happy, but we just got just a bunch of issues in more than 24 hours.
Looks nice, yeah.
**Aaron Abbott** 14:26 We did get new issues, or… Just those 3.
**Riccardo Magliocchetti** 14:32 I've only seen this… Shu reported.
**Aaron Abbott** 14:36 Okay, okay. Yeah.
Cool.
**Riccardo Magliocchetti** 14:44 Okay, speaking of the latest release… We have another, regression that is coming from the synthetic sources. We added to the HTTP… Client and server, instrumentation, And this is, like, assuming that… Something is a string when it may be, by bytes.
So… so we should be easy to fix. I pinged the… the author of the changes.
**Hector Hernandez** 15:22 You can assign this to me, this is Hector. I work with Jackson, I will take care of this.
**Riccardo Magliocchetti** 15:28 Okay, thank you.
Okay… And then… Next topic, while looking at, randomly, at, issues we have in, In the contributor repo, I've seen that we have a bunch of long-chain PRs.
But does not have, like, reviews, or… Or, like… Like, mostly reviews from content owners.
Component hours? Owners?
And was wondering… like… well, more than one day, but I also noticed that sometimes The competent owners, supposed, owners are not, added as reviewers on PRs.
But, like.
only sometimes. For example, like, I see the… you have Lib-free PRs, always have a reviewer, or an CNE.
But, for example, I… The Bottocort ones don't.
As I was wondering if… You already seen this of component owners not working, or maybe there's another reason?
I don't know.
**Aaron Abbott** 17:11 Are the code owners also in the approvers?
Or, like, URL lib versus Photocore.
**Riccardo Magliocchetti** 17:20 I don't know, we can check…
**Liudmila Molkova** 17:25 It's actually not the code owners, but the com…
**Riccardo Magliocchetti** 17:28 Ponant owners, right?
Yeah, sorry, it's component holds, yeah.
**Liudmila Molkova** 17:33 And I think what happened, at least, was one of the long-chain PRs that I've seen, there are… there is an owner for instrumentation GenAI, I'm the owner for… Length chain.
But Lankchain is under Gen AI.
**Riccardo Magliocchetti** 17:54 Yes?
**Liudmila Molkova** 17:56 But who is notified is the general, the instrumentation gen AI.
Not the… Link cheat sheet.
**Riccardo Magliocchetti** 18:08 what, I think?
Okay, where's…
**Liudmila Molkova** 18:13 And I should take some blame for not paying attention, sorry.
**Riccardo Magliocchetti** 18:18 No, yeah, yeah. These are the GenAI approvals, yeah.
**Liudmila Molkova** 18:22 So maybe we can, what I can do, I can ping the current component owners.
For GenAI, the generic one.
And ask them which individual components they feel comfortable being.
Owners on, and we kill the general group, but we'll reassign people to own specific packages instead.
Do you think it's… is it a good solution?
**Riccardo Magliocchetti** 18:53 Click.
I see it as a positive change, but they don't know if it's a solution for the specific issues, because, like, I'm seeing the same issues with Bartacore.
**Liudmila Molkova** 19:04 Oh, I see.
**Riccardo Magliocchetti** 19:05 And we don't have, like, the parent directory… But yeah, this is, like, another issue I would like to get resolved, because… We have a lot of people here.
And I'm sure we're getting a lot of reviews from this list.
**Liudmila Molkova** 19:25 Yeah.
**Riccardo Magliocchetti** 19:28 Let's you.
**Liudmila Molkova** 19:29 Yeah, I'll follow up on this, this week.
**Riccardo Magliocchetti** 19:34 Thank you very much.
**Liudmila Molkova** 19:58 So the component owners is, task developed by Dylan… by Dan Dylan.
Sorry, the… Dandela.
And yeah, I probably can.
Provide more details on why it might not.
**Riccardo Magliocchetti** 20:20 Pick up some PRs.
Okay.
Okay, not to ask, then.
Thank you.
So… I think this was the last topic for today.
Anyone else have something to discuss?
**Yazdankhah, Mani** 20:54 Yeah, sorry, I raised an issue on the open source repo, and I was told to attend these meetings to maybe get it prioritized.
**Riccardo Magliocchetti** 21:04 Yeah, can you share the issue, or in the doc, or… In the Zoom chat?
**Yazdankhah, Mani** 21:13 One second, I can probably share it in the chat.
**Aaron Abbott** 21:31 You should be able to, edit the doc as well. It should just be publicly accessible, so…
**Yazdankhah, Mani** 21:40 I don't have the dock open just yet. I'm from my work right now.
Yeah, basically what we want to do, maybe this issue isn't a good description, but for metrics, we don't have a way to add or remove metric readers at runtime, whereas with log records and with tracers.
We can add the synchronous multi-whatever processor that have the ability to add or remove further processors.
And we like to have this ability because we use it in JPMorgan for a bunch of different applications, and we can't know ahead of time.
It's basically like a generic library, and ahead of time, we don't know which exact set of The metric readers we need.
The proof of concept that we've done is using, multi-measurement consumer, similar to… The multi-locked record processor, or the multi-spam processor.
But the problem is we don't have any public APIs for that. Now, another solution might be to add the public API to the meter provider itself.
where we can have two functions to add or remove metric readers, similar to, I think, the other, like, tracer provider and logger provider, add the ability to… At new processors?
Directly to the provider itself, but again, the meter doesn't have that ability either.
If that makes sense.
**Aaron Abbott** 23:24 Yeah.
I'm… I didn't completely understand, like, the use case. I know you mentioned it's for some internal code.
Yep.
I don't know if, like, we haven't heard a lot of ask for this, and it's not something that's generally part of the spec.
And, like, for a little background, if I remember correctly, the reason that we don't have the same APIs we have for, like, tracing and logs was… To avoid… Like, a global lock on new… New stuff is… new stuff's added for the, For new providers, or sorry, for new metric readers, so… I was wondering, in your implementation.
Was it something that you were able to do without… Adding a global lock, basically.
**Yazdankhah, Mani** 24:15 It's not a global look, it is per… Measurement consumer.
Like, it's contained in the same object. We still need a lock, but it's in the same object.
**Aaron Abbott** 24:27 But, like, when you add a new measurement consumer, Is it just… Like, is it…
**Yazdankhah, Mani** 24:33 It's, it's not a new… so… In terms of implementation, it's a new measurement consumer, but the meter provider has that one measurement consumer, and that measurement consumer just has two APIs to register new metric readers.
I understand it's a bit of a niche issue, because… Most projects know their setup ahead of time, but because we're using it as a general library, the way that the metric provider works right now, it assumes you know ahead of time all the metric readers you're going to need.
But that's not the case for us, unfortunately.
**Aaron Abbott** 25:11 Okay.
So yeah, two other… I mean, I guess if you could add more context To the bug like that, it would be… it would also be a little bit helpful.
**Yazdankhah, Mani** 25:22 It's not a bug, it is a feature request, because there is no bug, but we need to, at runtime, add or remove metric readers. For example, your application is running fine, but at some point, you want to capture stuff as in-memory objects, or write them to the console. Right now, you can't. You need to specify that ahead of time.
**Aaron Abbott** 25:45 Okay, Sorry, another question. Did you, by any chance, have a look at the spec and see if there are any spec issues around this?
**Yazdankhah, Mani** 25:54 No, I have not looked at this spec.
**Aaron Abbott** 25:57 Okay, I feel like it's come up, maybe once before, that we kind of discussed this, so it would be a good, Good thing just to track down the context.
So, one, I know you mentioned remove, too, which is pretty interesting.
So, like, In terms of adding them later, you can always… use the API, and then it will give out proxy instruments, and then if you set the, meter provider later on. Like, if you need to wait until you have some you call an API, there's some control plane that configures the, The metric setup reviews or something like that.
You can totally do it later once, but yeah, the general adding and removing, I hear the feature request.
**Yazdankhah, Mani** 26:43 Yeah.
No, again, unfortunately, we can't do it. We need to do the setup at the start, but we don't know which exact set of processors or readers we need. That depends on the application.
Specifics?
So, yeah, we basically need that mechanism, and with traces and logs, there is public APIs for it.
extend it to the remove. The remove was a very easy addition, but for metrics specifically, there's no public API or again, we've gotten it to work by hacking the internals, but we didn't feel comfortable doing that. Yeah. And if there isn't issues with the spec, I'll double-check the spec, but if there's an issue around that, I think it's a fairly easy addition.
**Aaron Abbott** 27:30 Okay, so one last question would be… Instead of, like, just exposing this measurement consumer thing.
What do you think about contributing, like, an add-remove?
metric reader into OTELPython itself, so you don't need to, kind of.
make a hack on a public… on a new public API, but we could just support the use case directly.
**Yazdankhah, Mani** 27:54 That sounds good, but… So, do you mean… having, proximetric reader, basically.
**Aaron Abbott** 28:05 No, I mean, like, basically having, like, an add… add metric reader, remove metric reader on the meter provider.
**Yazdankhah, Mani** 28:12 Okay, yeah, yeah, that can work as well. That'd probably be easier, honestly.
**Aaron Abbott** 28:16 Okay.
Yeah, I mean, I think, like I was saying, I think it boils down mostly to the implementation.
Obviously, like, if you add and remove meter providers, like, the points that were made before will be missed. I think that's kind of just… And you'd be willing to send a PR for this?
**Yazdankhah, Mani** 28:36 Yes, yes.
Okay. I actually have the code ready, I need to check with corporate, but… I think I should be able to raise a PR fairly quickly for this.
**Aaron Abbott** 28:47 Okay, I'll take a look at the issue. And by the way, we have a CLA, I don't know, it's just the CNCF CLA.
**Yazdankhah, Mani** 28:53 Yeah, JFE already has that with OpenTelemetry.
**Aaron Abbott** 28:56 Okay, cool.
**Yazdankhah, Mani** 28:57 I believe so.
**Aaron Abbott** 28:59 Okay, cool. Yeah, I'll take a look at the issue, and then maybe we can, discuss there before you, Send a PR, just make sure we're on the same page.
**Yazdankhah, Mani** 29:08 Sure. Thank you very much.
**Aaron Abbott** 29:11 Okay, thank you.
**Riccardo Magliocchetti** 29:19 Okay, any more topic?
So… Thank you, everyone.
Have a nice rest of the day.
And see you!
**Aaron Abbott** 29:37 Yep.
Hey, girl.
**Liudmila Molkova** 29:38 Thank you.
**shuwpan** 29:40 Thank you.
