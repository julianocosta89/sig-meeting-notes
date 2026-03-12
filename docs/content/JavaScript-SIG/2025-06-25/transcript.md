SIG: JavaScript SIG
Date: 2025-06-25
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Marc Pichler (Dynatrace) 00:01:16 You.
Daniel Dyla (Dynatrace) 00:02:18 Hello! There!
Looks like we don't have a ton on the agenda today.
I guess we can just get started. Can everybody hear me?
Yes.
Marc Pichler (Dynatrace) 00:03:00 It's.
Daniel Dyla (Dynatrace) 00:03:00 Okay, cool.
So Mary Leah is not here asking for a review on instrumentation. Pg update to stable semantic conventions. Okay, yeah, that seems pretty straightforward.
Trent Mick 00:03:16 Yeah, that's me. I'll do it.
Daniel Dyla (Dynatrace) 00:03:18 Okay. Awesome. Thank you.
No other topics. Did I start too early, or I guess.
Trent Mick 00:03:30 You can take the time to save your Github recovery codes.
That's been 3 weeks at least, not yet done.
Daniel Dyla (Dynatrace) 00:03:39 Yes, it has been, I think, a while. I should probably save those, but not on a recorded call. Huh?
No, all right.
Untriaged bugs, lambda request hook, not working as expected.
configure, open telemetry, using the following setup request, hook logs of things, sets an attribute, logs, a thing again.
So it's not really doing much.
I don't think it's doing anything here that should screw anything up.
Looks like things are imported in the correct order import tracing first.st Yeah.
are they not?
They are starting the SDK.
Marc Pichler (Dynatrace) 00:04:56 And are suggested. If they manually create a span, it shows up.
Daniel Dyla (Dynatrace) 00:05:05 Okay.
I mean, it seems pretty likely this looks real to me.
Is the yeah. Okay?
Marc Pichler (Dynatrace) 00:05:32 As the lambda instrumentation create a root span.
Daniel Dyla (Dynatrace) 00:05:37 I was just gonna wonder that I was just gonna ask the same thing like if you don't have.
But I think these are he's using the get auto instrumentations.
And this is in like a yeah. Hmm.
I don't know how the handler is run router event. This seems to be in lamb. Oh, yeah, in lambda that makes sense. Aws. Lambda.
Yes, lambda should be creating a right span.
Okay? Do we know who the code owner is for the Aws lambda instrumentation.
Marc Pichler (Dynatrace) 00:06:38 It's Jonathan Lee that's I will signed in.
I always get their username incorrect. I can't find it right now.
Daniel Dyla (Dynatrace) 00:07:12 Oh, this is this should be in contrib, anyway.
So I will transfer this to contrib.
Marc Pichler (Dynatrace) 00:07:28 It's so the component owner is Jj. 2, 2, ee.
Daniel Dyla (Dynatrace) 00:07:59 For now I'm going to give this. P. 2.
Think that's okay, for now.
There was a second one in here.
Exponential histogram has invalid default parameter.
We got this bug report on the honeycomb web SDK. With a particularly strict compiler.
There is a reproduction repo.
Marc Pichler (Dynatrace) 00:09:16 I think it might just be not happy about the syntax we're using. There.
Daniel Dyla (Dynatrace) 00:09:36 Hmm!
I mean, I don't even know where I'm looking, or this might be it.
I don't even know what I'm looking at here, does any.
This is supposed to be the reproduction repo, but I don't see anything that actually like is using open telemetry in any way.
I guess this is.
I mean, it's not much of a I'm sure it reproduces the issue. But okay, So Mark, you think it's unhappy with this syntax, start time undefined here.
Marc Pichler (Dynatrace) 00:10:39 It like. If you look at the code, it can never be undefined.
but I think it's the the syntax that it's not happy with, because I don't think we do use that specific syntax in the other aggregators.
Oh, no.
Daniel Dyla (Dynatrace) 00:11:01 Where is start? Time?
Marc Pichler (Dynatrace) 00:11:02 We we actually do.
We actually do use the same syntax. So it's probably not that.
Daniel Dyla (Dynatrace) 00:11:09 Where's that? Start? Time to find a default?
You said it can't be undefined, but actually.
Trent Mick 00:11:15 Is that always undefined.
Daniel Dyla (Dynatrace) 00:11:17 Yeah.
Marc Pichler (Dynatrace) 00:11:17 I feel
Daniel Dyla (Dynatrace) 00:11:19 Oh, yeah.
Marc Pichler (Dynatrace) 00:11:24 Yeah, that's true.
Daniel Dyla (Dynatrace) 00:11:28 I think it is actually undefined.
Trent Mick 00:11:33 Ones don't have a default value for start time.
Daniel Dyla (Dynatrace) 00:11:35 I'm surprised that the default compiler doesn't complain about this.
Marc Pichler (Dynatrace) 00:11:43 SDK metrics, source, aggregator, exponential histogram.
Daniel Dyla (Dynatrace) 00:11:49 I know you probably can't see my editor, but I'm gonna just see what see what my editors like. Intellisense stuff has to say about that, and where it's defined.
exponential histogram. This is the aggregator we're looking at. Yes, source aggregator.
Let's see, start time.
It's it's self referencing. That's why it doesn't come. That's why the compiler doesn't complain.
Marc Pichler (Dynatrace) 00:12:33 It comes to type this Hr. Time, and it references itself so.
Daniel Dyla (Dynatrace) 00:12:39 It references itself. Yeah, so it is actually undefined.
I mean.
Marc Pichler (Dynatrace) 00:12:51 Should be an easy fix, though we can just do the same as we do with the other places.
and it should work.
Daniel Dyla (Dynatrace) 00:12:58 What do? What other places are you referring to?
Marc Pichler (Dynatrace) 00:13:01 If you go to any other aggregator.
Daniel Dyla (Dynatrace) 00:13:06 Oh, yeah, that construction doesn't have. It's not optional.
Marc Pichler (Dynatrace) 00:13:10 Yeah.
And this is an internal type, anyway. So if we make the change there, it won't be breaking to anybody.
Daniel Dyla (Dynatrace) 00:13:19 Yeah, okay.
Marc Pichler (Dynatrace) 00:13:21 Assign this to me, and I will have a look.
Daniel Dyla (Dynatrace) 00:13:27 Okay.
Thank you.
Jared Freeze (embrace) 00:13:31 I was. Gonna say, I just looked at the repo. It's a make shadow. I haven't seen that syntax like I haven't seen that kind of build system before, but make shadow apparently will start running. Whatever process you need to build.
Trent Mick 00:13:49 On the Repro.
Marc Pichler (Dynatrace) 00:13:50 Interesting.
Trent Mick 00:13:51 Repo you mean like.
Jared Freeze (embrace) 00:13:52 Yeah.
Trent Mick 00:13:53 So you're talking about, yeah, okay.
Daniel Dyla (Dynatrace) 00:14:18 Okay. So I guess this is p. 1, because it causes them not to compile, although it is a we probably don't have a Closure script label right
Marc Pichler (Dynatrace) 00:14:35 But I I've never seen any issue filed for it. So if we see 3 of them pop up at some point, we can create the labor, but I think it's fine without one, for now.
Daniel Dyla (Dynatrace) 00:14:48 Yeah.
I think it should actually just be literally a 1 line change removing that optional parameter should be fine.
Marc Pichler (Dynatrace) 00:14:57 Fingers crossed.
Daniel Dyla (Dynatrace) 00:14:58 Yeah.
Alright. So I think that was right should be it.
Yep, oops close the wrong contribute. Bugs opened on May 20. So this one's not exactly new.
Yeah.
Marc Pichler (Dynatrace) 00:15:26 They reacted with ice emoji. So maybe they are having a look. I would keep it open for 1 1 week. What? One more week, and then it's still there, we can close it.
I tried to reproduce this one, but couldn't find anything wrong with it.
so I asked them to have a look at the reproducer and see if they are doing anything different to what I was doing.
Daniel Dyla (Dynatrace) 00:16:07 Okay, that was it for Contrib bugs. So old Contrib Pr triage replace Karma with wpt runner end user interaction.
Marc Pichler (Dynatrace) 00:16:33 Yeah, Jamie said. She will have a look at this. And if there was another reason for her opening the Pr. On Shima, because we have now integrated it into open telemetry instrumentation. But she's out traveling right now, so Don't think there's any action to take at the moment.
Daniel Dyla (Dynatrace) 00:16:57 Okay.
Trent Mick 00:17:01 Then it's the Trent show sadness.
3 in a row.
Daniel Dyla (Dynatrace) 00:17:06 What? Oh, Trent, yeah.
3 in a row. Should we look at these, or are we.
Trent Mick 00:17:13 Okay. So the 1st one test services, David has a a, an alternative Pr that uses on the same concepts and is starting. Basically.
he's doing a good job. We should look at his Pr and people should review that if we want to.
not sure if it's linked there. But it's anyway, we can skip the 1st one many times should be spent on David's Pr, yeah.
Daniel Dyla (Dynatrace) 00:17:42 This plan.
I guess.
Trent Mick 00:17:44 I think not yet. Yeah, it's a draft. I think not yet. I'll close it when David's work moves along because David's done it for instrumentation. Pg, and my initial one had done it for. Sorry I had done it for a couple of different instrumentations, anyway. But yeah.
okay.
so Dave, David's working through it. The second one I'll come back to at some point when I don't know.
It feels like yeah. Us us breaking down these old Prs helps, because there won't be as much breakage when all the directories change names.
Daniel Dyla (Dynatrace) 00:18:13 Okay.
Trent Mick 00:18:14 But we can skip that for now.
Yes, build Plugin. That was a Poc thing that I did when someone else was proposing some espill plugin thing, and I think that person is then followed up with another newer Pr that I haven't had any time to look at.
Eventually this can get closed, and I guess if we could close it now, if people want, I don't expect to come back to this anytime soon.
Okay, I'll just.
Daniel Dyla (Dynatrace) 00:18:45 That decision on your own aws, SDK, Sqs. Receive, use span links instead of processing spans per the latest specification. I think. I remember we talked about this.
Yeah, I commented last week.
I guess no update. But what do we wanna do in these situations where the I guess Jonathan's usually responsive these days. He's probably just busy right now.
Winston attribute serialization.
Marc Pichler (Dynatrace) 00:19:27 Think I was meaning to get back to this one last week to close it followed followed up with creating an issue in the core repo investigative circular references are a problem during block record serialization. Because I think the type that we have right now would allow for such a thing.
Which is one of the things I gathered from the thread here.
Daniel Dyla (Dynatrace) 00:20:01 Okay, so should we close this in favor of the issue you created in the core repo.
Marc Pichler (Dynatrace) 00:20:07 That's just one offshoot of that.
I think everything that's in there should actually be handled in the SDK, and I think the type has also changed recently to allow for a lot of that.
So, in my opinion, we should close this here.
Daniel Dyla (Dynatrace) 00:20:35 When you say should be handled in the SDK, you mean it would properly be handled in the SDK. Or do you mean you think it is already handled by the SDK.
Marc Pichler (Dynatrace) 00:20:44 I think most of it is already handled by the SDK. The circular references is one problem that might not be
Daniel Dyla (Dynatrace) 00:20:54 Okay.
Marc Pichler (Dynatrace) 00:20:55 Handled yet. So there's an issue to look into that separately.
So ideally we wouldn't have to do all of that in each in each log bridge. We would just do it once in the SDK, and then I'll be done with it.
Daniel Dyla (Dynatrace) 00:22:04 React native navigation.
Yeah. So we discussed this last week, I'm not sure why it showed as still needs.
Marc Pichler (Dynatrace) 00:22:27 Oh, it's the Prs are just ranked by like which ones are the oldest.
Daniel Dyla (Dynatrace) 00:22:33 Yeah, but I thought I had. Oh, I the activity indicator. I thought, maybe not.
Should we create a label to remove issues? We've already.
or to remove Prs. We've already gone through from this list, or are we keeping them around so that we can eventually close them.
Marc Pichler (Dynatrace) 00:22:54 I would say, keeping them around. To eventually close them would be the way to go, otherwise we might put the label on there and then go through all of them, and then we will have to come back to them eventually, anyway, home.
Daniel Dyla (Dynatrace) 00:23:12 Yeah, so David commented here.
and the author has added changes since then, but did not respond to David's comment.
I am going to let's see, copy Link.
I'll add it as a review, I guess.
So that it's a little bit more obvious.
Let's see.
Okay.
Should be okay for now sequelize you. Calendar last. Please update Pr with owners. I think this is still.
how long do we want to let these go after commenting cause they're quite old.
Marc Pichler (Dynatrace) 00:24:39 I would say no more than a month.
Daniel Dyla (Dynatrace) 00:24:42 Okay.
Marc Pichler (Dynatrace) 00:24:44 We come back to it 4 times I guess it's safe to close them, and then a lot of them. They are outdated, anyway. So opening a new Pr would be the way to go.
Daniel Dyla (Dynatrace) 00:24:57 So it looks like Jonathan reviewed this about a month ago.
His review has not been addressed, but I guess this has been a month since.
Should we close this, or is it close enough to being approved that we keep it.
Marc Pichler (Dynatrace) 00:25:26 I will.
So this actually there! There was a thread in slack a while ago, where the person asked for reviews and said they would like to have a Maintainer review it.
Oh.
Daniel Dyla (Dynatrace) 00:25:41 Oh, I got you. Okay.
Marc Pichler (Dynatrace) 00:25:43 Before updating it, because they were taking care of conflicts all the time.
and they kind of get got annoyed by that which is understandable. So.
Daniel Dyla (Dynatrace) 00:25:54 That was why I added this comment, that that slack comment was before this.
Marc Pichler (Dynatrace) 00:26:02 Yeah, so I will actually right in that slack thread that there's a review now and if they want to get back to it where they can find it, and let's see if anything moves. Then.
Daniel Dyla (Dynatrace) 00:26:22 Okay.
open AI instrumentation fixes an issue. I think that's just asking for, you know, the same person instrument open. AI.
It looks like they have not added component owners or any tests.
Trent Mick 00:27:02 Oh, I'm sorry. It's just I was distracted.
Is this the yeah? This is the one that I said I'd follow up on 2 weeks ago, and then months before that.
Daniel Dyla (Dynatrace) 00:27:13 That's okay.
Let's see.
are we?
Trent Mick 00:27:20 Do you want to let me comment? I'll just comment right now let me do that.
Daniel Dyla (Dynatrace) 00:27:23 Okay?
Whoops!
I lost my position here at configuration helper for functions for web. This is a draft doesn't appear old. It is old current version creates an instance. In order to patch data, loader breaks usage where data loader classes extended.
Most recent thing here is a week ago. Please review. If you find time.
This person was actually active on this somewhat recently.
Trent Mick 00:29:20 Yeah, again. That's me. I've had it on my list from last week, and almost got to it yesterday.
Daniel Dyla (Dynatrace) 00:29:27 Should we ping Henry again or not?
Marc Pichler (Dynatrace) 00:29:30 I'm not sure if they actually receive the notifications. They are not part of the org.
They're they're the last component owner that I'm trying to contact to get on boarded into the organization and get triage permissions.
But I had no luck.
Daniel Dyla (Dynatrace) 00:29:50 Okay, I they're on. Have you pinged them on slack.
Marc Pichler (Dynatrace) 00:29:54 Yes, I have.
Daniel Dyla (Dynatrace) 00:29:56 Okay, but you're just not seeing them, I guess.
Marc Pichler (Dynatrace) 00:29:59 Yeah, they are offline. I'm not sure if they check slack recently, though, they they recently did review another Pr for that component. So they sometimes come around.
Daniel Dyla (Dynatrace) 00:30:13 Okay? Well, if you ping them on slack and you ping them here, there's not much more we can do, although if they are.
Trent Mick 00:30:21 Shit.
Daniel Dyla (Dynatrace) 00:30:21 Not responsive that potentially, they're not fulfilling the component owner contract. This may end up being an on maintained component.
Marc Pichler (Dynatrace) 00:30:38 Yes.
Daniel Dyla (Dynatrace) 00:30:41 Okay, I guess, for now there's not much more we can do if you already reached out to them.
Aws again, this is a draft.
What's the latest state here?
November?
I wonder if we should have like drafts that don't have any activity for more than a month just automatically closed.
Cause if somebody has something marked as draft, that's like a sign that it's not ready for reviews, and they're not looking for reviews.
and people often don't go. Just don't go back and close them.
Marc Pichler (Dynatrace) 00:31:29 Yeah, I think that would make sense.
Daniel Dyla (Dynatrace) 00:31:35 So should I just close it, or should I?
Yeah, I think, for now I'll comment. But we can add an automation that does that.
Marc Pichler (Dynatrace) 00:31:51 Yes, at the I'm not sure. I'm pretty sure this stale thingy has some way to config. Configure it to close drafts. After some time.
Daniel Dyla (Dynatrace) 00:32:03 It seems like a fairly obvious use case, I think.
add workflow to format using prettier trent, it looks like you opened a competing Pr with this one linting examples is this actually, Npm, run format is actually.
does it fail? Yeah, it probably does.
Okay.
I mean, it seems like a decent idea.
are we? I'm surprised we're not already running a winter in.
are we not?
Marc Pichler (Dynatrace) 00:33:25 It's the.
Trent Mick 00:33:26 Is this just about the examples folder.
Marc Pichler (Dynatrace) 00:33:29 Yeah.
Daniel Dyla (Dynatrace) 00:33:29 It must be even.
Trent Mick 00:33:32 So I had the competing thing with a Pr. That's next on the list here, which I have approval on. So I should just get that one merged which was part of I guess my alternative. It's a long time ago I have to look again, but.
Daniel Dyla (Dynatrace) 00:33:48 Yeah, I don't see anything here that's specific to the exam, to the examples.
The fact that it's like a separate workflow when we're already linting, I think.
I don't know what your Pr. Does, but I suspect that was probably your issue with it as well.
Trent Mick 00:34:08 Is this one adding a different base config, or something.
Daniel Dyla (Dynatrace) 00:34:12 Yeah.
Okay.
Trent Mick 00:34:32 Oh, I think I maybe I'm relearning. But I think I remember my issue with it instead. It's then gonna be using prettier for the examples when we're already using prettier indirectly, with possibly different config through es lint for everything else.
Which feels weird to have 2 different ways to do it. So my counter proposal was to just get the example stuff to be included in our regular linting and formatting, via es lint.
Daniel Dyla (Dynatrace) 00:35:01 Implementation, too, because all it's doing is like it does Npm run format. All Npm, run format is doing is
Trent Mick 00:35:11 Default.
Daniel Dyla (Dynatrace) 00:35:13 Yeah, it runs prettier just against, like all Ts files in the Directory.
with no config or anything like that.
It's like just running it with the default. I I think I don't like this implementation, anyways. So I'm just gonna comment and close.
Marc Pichler (Dynatrace) 00:35:44 It seems weird to workflow or sort of format stuff.
Daniel Dyla (Dynatrace) 00:35:53 So prettier formats and returns a non 0 status code. If it changed anything.
So that fails the workflow.
Yeah, prettier check, and then prettier. Right? Is like the auto format fix. But we already have lint and lint fix like, I think.
the fact that the examples aren't limited. Yes, is a problem. But adding a separate formatter is not the solution that I would prefer.
So I'm just gonna close it.
There we go. We actually closed one. It's only been 36 min.
Trent Mick 00:36:43 So the next one is.
Daniel Dyla (Dynatrace) 00:36:44 Nice one, is you?
Trent Mick 00:36:47 Well, the next one is me for this one. That was my counter proposal. So the reason it it doesn't do all the examples it does one of them, because mostly it was to show. Let's do this and get agreement and discussion. And so I have approval from Jamie. From a long time ago. I just haven't followed up cause there's the guilt factor that I then should start doing the same thing for all the other examples as well, but so yeah, I'll put it on my list.
Daniel Dyla (Dynatrace) 00:37:15 Okay.
January 30.th Jonathan reviewed this, even though it is a draft.
Okay.
my sequel to missing mask of queries this one is this year.
Looks like there's been a lot of conversation, including recently.
April.
yeah, not be on by default, and it's just waiting on.
I guess.
Should I comment here, or should we let the stale bot go ahead and handle this? Since this is in the authors.
Marc Pichler (Dynatrace) 00:38:54 Yeah. So the thing with this Pr is that it's almost like that. This just needs to be this one comment that needs to be addressed, and then this can get merged and will actually be useful.
Yeah.
Daniel Dyla (Dynatrace) 00:39:11 Would you like to? I mean, technically, we have permission to right to this branch, I think. Would you like to take it over and just make that change.
Marc Pichler (Dynatrace) 00:39:24 Oh, yeah, so.
Trent Mick 00:39:26 Would you like to nominate Marilia to do that?
Give? And she.
Daniel Dyla (Dynatrace) 00:39:30 Nominate anybody that's not here.
Marc Pichler (Dynatrace) 00:39:36 I'm.
Daniel Dyla (Dynatrace) 00:39:37 Merely because she's the Mysql To component owner.
Trent Mick 00:39:42 Oh, cause she's super active in the database instrumentation. And some kind of stuff is, yeah.
Daniel Dyla (Dynatrace) 00:39:48 Okay.
Marc Pichler (Dynatrace) 00:39:48 This, this would be part of it.
Daniel Dyla (Dynatrace) 00:39:50 It doesn't have permission. So the.
Marc Pichler (Dynatrace) 00:39:57 She is an approval, so she has permission to push to the branch.
Daniel Dyla (Dynatrace) 00:40:02 Oh, yeah, okay, so she should have permission. I think all you need is right. Access right?
Marc Pichler (Dynatrace) 00:40:09 Yes.
it. It seems that on this pr, there's just some disagreement on like, which path to take or some misunderstanding. Just.
Trent Mick 00:40:38 Talking past each other.
Marc Pichler (Dynatrace) 00:40:40 On what the next step should be.
Daniel Dyla (Dynatrace) 00:40:49 Okay.
I'm trying to think of a way to word this because I don't want it to just be like I'll reach out to her in slack. I don't wanna make it public comment necessarily, even though this is a recorded call.
I'll just ping the author here and I'll reach out to Marley and slack to let her know like, Hey, we have right permission on this. If you wanna just make the change and get this merged.
Okay.
Instrumentation for web exceptions.
no standardized way to capture and monitor unhandled exceptions and promise rejections. This has a couple of requests, changes.
Marc Pichler (Dynatrace) 00:42:04 Yes, I was just asking for
Daniel Dyla (Dynatrace) 00:42:07 2 component owners. Martin volunteered.
Marc Pichler (Dynatrace) 00:42:12 Okay has not been updated yet, I think suitable.
The changes requested still stands.
Daniel Dyla (Dynatrace) 00:42:23 Okay. Martin also requested changes, left a few comments. Yeah, a couple of things.
The fact that Martin volunteered to be a component owner. He's pretty active. I think this one and Pervy is also usually active as well.
I think that this one likely will end up going through a little ping never hurt anyone, though.
Add Github. Action to add, has approval.
Label for approved Prs automate label. Tagging. Jackson approved this mark. You added comments.
Marc Pichler (Dynatrace) 00:43:27 Yeah, I haven't. Haven't followed up on that one. I should have done that.
I will have another look.
I think I was having concerns about the the token that's provided, and it not having proper access. And if we provide access to modify the labors, then that's also not great.
I'll have to dig into that a bit more. I will have another. Look at this one.
Daniel Dyla (Dynatrace) 00:44:03 Okay.
here's all instrumented cause instrumented Lambda to fail.
Sounds like a bug report.
Errors thrown by shimmer cause the instrumented lambda to fail.
Most recent thought about it, not sure else uses underscore. Rat might depend on throwing errors.
Open a pull request to there, I assume, by there he means on Shimmer Shimmer's unmaintained, I think, though, isn't it.
Marc Pichler (Dynatrace) 00:44:53 There haven't been any commits to main in 8 years or so.
But we this is why we we vendor the code now
Daniel Dyla (Dynatrace) 00:45:05 Yeah.
Marc Pichler (Dynatrace) 00:45:05 In. So we can actually make the changes in Shima in open telemetry instrumentation. If that makes sense. So the the code that we took over.
We can change what they are asking for, though, would need to be added to the public Api of one of the packages. I'm wondering if there's anything that we can do here to.
Yeah, it means.
Daniel Dyla (Dynatrace) 00:46:18 It's also yeah. So actually, he already pointed that out.
he's suggesting adding a save wrap. If somebody depends on rap throwing errors, I think.
Well.
some people may consider throwing an error to be a part of the public Api. I think it's a not something I'm concerned about.
I'd rather it without reading too much into what this actually is.
I think this is just to adding a bunch of commented code. That's not my favorite. But wait, it's only adding, commented Code.
Am I missing something here?
Marc Pichler (Dynatrace) 00:47:35 Where's not, or what this is.
My bolt it just says like I tried to reproduce, but I don't really have an idea how to fix it in the title.
So I think they were just opening a Pr to show where stuff is going wrong.
It's like all the way at the bottom. There's a comment in German that says.
if you define a property that's not configurable, that's a problem for Shima.
and that's what's causing the error.
So.
Daniel Dyla (Dynatrace) 00:48:45 All the way at the bottom. Oh.
Marc Pichler (Dynatrace) 00:48:48 Of the diff, if you like the last file in the in the diff of the Pr.
just like to. Yeah, it says, if you if you set that, then Shima will fail.
So actually, this might be something that needs to be addressed in oh, well.
version of Shima, where we like, catch that somehow. Like if we try to wrap something that's that property, then we need to address it. So so maybe they actually need to go to the core repo and open a Pr. There to address it, and then it will automatically be addressed here.
Daniel Dyla (Dynatrace) 00:49:31 Yeah.
I'm just gonna close this.
Marc Pichler (Dynatrace) 00:50:06 Yeah, I think that's a good way forward, and if they have the they know where to go to open the Pr. That's good enough, I think.
Daniel Dyla (Dynatrace) 00:50:17 Yeah.
all right. 2 closed.
Make a progress. Now.
this is a bug fix fix instrumentation of Esm imported data. Loader.
Hmm.
Marc Pichler (Dynatrace) 00:51:04 This is mainly just missing a test.
Daniel Dyla (Dynatrace) 00:51:10 Yeah, it seems pretty straightforward. My only question is, is this something that we want to? Is this something that should be handled in all instrumentations, or is it like I? I don't know off the top of my head whether this is a good general solution, or whether it just works in this case.
Marc Pichler (Dynatrace) 00:51:31 It. So this is basically what we do in all the instrumentations that like, have an Esm export. There.
Daniel Dyla (Dynatrace) 00:51:45 So should we do this in the instrumentation package? Is there some reason that we don't.
Marc Pichler (Dynatrace) 00:51:51 It. Sometimes it's different. It depends on the way that the package export stuff.
Trent Mick 00:51:59 Awesome. Okay, being muted for a while. There's I've linked to 1942 is a Meta issue to work through all of the instrumentations to do the Csm thing.
And I guess I'd have to find the original discussion. But yeah, we did go through the discussion of whether we want to do this everywhere or do it in an instrument instrumentation class. But basically what Mark said.
Daniel Dyla (Dynatrace) 00:52:24 Okay.
Marc Pichler (Dynatrace) 00:52:27 So there's david linked Pr. Here in his comment that there was recently a Pr. That edit such a test, and they can take it as a reference should be fairly simple to do the same there.
And I think it's it's required to add a test for this, because sometimes it's different. It's not always the same thing.
And we've had Prs in the past that we merged that try to do the same thing, and then actually caused more trouble.
Daniel Dyla (Dynatrace) 00:53:12 Okay.
cloud run, support resource detector for Gcp. Did not previously support Cloud Run. Specific resource attributes supported in other sdks at support for setting fast and cloud platform resource attributes going to go ahead and assume that this is in semantic convention. I know that these namespaces, at least, are no longer working in this area is that that's 1 of the component owners. I think we already implemented it here. I would like to make sure that I'd like to make the cloud resource to just re expose the one from.
Oh, I got it.
Marc Pichler (Dynatrace) 00:54:13 Which is a different question. That we might need to answer at some point is, Do sort of thing.
Daniel Dyla (Dynatrace) 00:54:24 External implementations.
Marc Pichler (Dynatrace) 00:54:27 Yeah.
On one hand, it's just a small thing that we then have sitting there. On the other hand, if we need to make changes. We are reliant on them, fixing it upstream.
which might slow us down if we need to.
Do stuff like SDK 2. Dot, for example.
might have to remove the old, the the package that doesn't update that not publish a new major version because you need to do it upstream first.st
Daniel Dyla (Dynatrace) 00:55:03 Yeah, not to sound too cynical, but the idea of someone else slowing us down makes me laugh a little bit.
I would probably prefer to just remove it rather than proxying implementations. That's what the registry exists for.
Marc Pichler (Dynatrace) 00:55:21 All of it.
Daniel Dyla (Dynatrace) 00:55:22 Again, somewhat cynically. I don't know how many people actually look at the registry and if you want it in anything in auto instrumentations. Although this is a detector it needs to be in here.
I think this is not something we're going to address with 5 min left in the meeting. But I think we need to clarify the story on externally hosted things, how we handle them and how they can be better integrated without having to add proxy contrib modules in order to be discovered and included in stuff.
I think that's too big of a question, for here Aaron commented on this 3 weeks ago. He's the code. He's the code owner. He's aware of this.
I think this is sufficient for now.
Maybe we can talk about the strategy of this type of thing in general next week, though.
when we have more time.
Marc Pichler (Dynatrace) 00:56:36 Yeah, sounds like a good idea.
And then it will be 4 weeks since the last comment, too. So we can see if we want to close this or keep that up.
Daniel Dyla (Dynatrace) 00:57:50 Okay, think that's good enough for now on that one.
This is the same person.
Likely extending the same resource detector. Yeah.
Personally, I don't necessarily love like, I think one problem will be that if we just proxy and implementation over to someone else that's not gonna stop people from opening issues on our repo on stuff that just is, gonna we already have a hard enough time triaging the things we actually do control.
Marc Pichler (Dynatrace) 00:59:08 And where's the look? Spot?
Daniel Dyla (Dynatrace) 00:59:12 We have one.
Marc Pichler (Dynatrace) 00:59:12 I don't think it's the best approach to take.
Daniel Dyla (Dynatrace) 00:59:15 Yeah, Jonathan opened this May 13.th He is the component owner.
Looks like it's being actively reviewed, commented 2 weeks ago.
Okay.
Marc Pichler (Dynatrace) 00:59:48 This actually has an owner approver. So this actually just needs to get marched in. I think I'll update the branch and take care of merging it.
Daniel Dyla (Dynatrace) 01:00:01 Cool.
That's even better than closing stuff, I think.
Alright, we're out of time.
We almost got to page 2. How many things are on page 2.
A few.
Alright I am. I'm feeling good about this.
We only skipped 20 prs.
Alright. I guess that's it for this week. Thank you everybody for your time.
I'll see everybody next week. If you're here and not gone for the holiday, I'll be here.
Trent Mick 01:00:41 I.
Daniel Dyla (Dynatrace) 01:00:43 Alright! Have a good one.
Trent Mick 01:00:44 Thank you.
Marc Pichler (Dynatrace) 01:00:45 1, 5.
