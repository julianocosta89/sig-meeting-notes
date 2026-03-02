SIG: Java SIG
Date: 2025-06-19
Duration: 54 minutes
============================================================

## Zoom Recording Transcript

**GZ Gregor Zeitlinger** 01:00 Hello!
**Jack Shirazi** 01:03 Hi.
**Trask Stalnaker** 01:15 Hey folks.
**GZ Gregor Zeitlinger** 01:20 Morning.
**Trask Stalnaker** 01:22 Good evening.
I think we're going to have a bit limited attendance from some of the Jack
Jason, John. At least I know our out today.
**GZ Gregor Zeitlinger** 01:58 What's the reason?
**Trask Stalnaker** 02:01 It's a Us. Holiday for a bunch of companies Juneteenth.
Unfortunately, not for Microsoft, though, so I'm here.
**GZ Gregor Zeitlinger** 02:18 What is juneteenth?
**Peter Findeisen** 02:21 That's anniversary related to abolishing slavery in United States.
**GZ Gregor Zeitlinger** 02:33 So it's not an official holiday, but.
**Peter Findeisen** 02:36 It. It is kind of official, but it looks like it's not mandatory. So it's yeah.
especially with the current administration. Many companies do not feel it's necessary to
to obey that. Well, I don't want to go into politics, of course. But yeah, that's
that's how it works.
That's why some companies have it off, and some don't, so.
**GZ Gregor Zeitlinger** 03:01 I see.
**Trask Stalnaker** 03:10 So I will.
**GZ Gregor Zeitlinger** 03:12 And chart.
**Trask Stalnaker** 03:16 What's that?
**GZ Gregor Zeitlinger** 03:17 Ending of slavery. That's the day.
**Peter Findeisen** 03:20 Yes. Well, not. Well, yeah, it's complicated.
**Trask Stalnaker** 03:26 Everything about slavery in the Us. Is complicated.
So we'll probably bump some topics to next week
when we have those folks. Sorry, Peter.
Just creating a slot for me to bump
agenda topics over as we need
But let's start I think we can start with this one, Jack.
**Jack Shirazi** 04:11 Yeah. So I'm looking at the methods instrumentation, which is the one where you can specify arbitrary methods to be instrumented.
You just use a there's a there's a
code or environment variable that you can set, and you can give it a list of methods, and it will start tracing them.
I need to make it dynamic. Well, I don't need to, but we want to make it dynamic. And so I'm I'm the question here is
because I don't know how extensive the changes are, although when I I 1st looked at this.
and I think it might just be
dynamic in in the easiest way would be to just add
add instances for new method, for new methods that are declared, and just
tell any old ones that are no longer required to, obviously not to remove the instrumentation, although we could do that, but actually just to set it so that they don't generate any spans the same ways. It's like instrumentation scope works.
So that might not be that difficult if that works
So I guess the question is, if it's if it's straightforward.
I I probably would just keep it in the instrumentation method and add some capability there in the in the existing instrumentation.
But if it's not, if it's more extensive, do we?
Do? We want me to try and make a copy of instrumentation and have a different instrumentation method?
A different name. A different tree, if you like.
which kind of duplicates it but is is dynamic?
So the question I'm asking is, if if it's extend. If it requires extensive changes.
Shall I just do a new instrumentation.
**Peter Findeisen** 06:15 Can you? Can you explain a little bit more about what you mean by dynamic in this context?
**Jack Shirazi** 06:21 So you essentially, if you, you can add methods later.
That should be great.
**Peter Findeisen** 06:28 During during runtime.
**Jack Shirazi** 06:29 During Runtime. You can add methods to be traced, and you can also remove methods that are being traced from the list.
And
I suspect, adding, shouldn't be that difficult and removing shouldn't be that difficult. But I'm I'm not, really. I haven't really dived into it, removing being like I said the just setting to to not generate spans rather than actually removing the instrumentation.
**Peter Findeisen** 06:58 So if you have capability to add instrumentation dynamically, you can also remove instrumentation dynamically. This is there's. This is not different.
**Jack Shirazi** 07:08 You you can do, but I'm but we don't do that anywhere, and and so I I think probably I won't go that route. But I'll look at it.
I mean that that's what we do in our in our
old elastic agent, is we? Just? We dynamically instrument and uninstrument methods, and it works fine but the
the instrumentation in in the open telemetry agent.
It's not so dynamic in terms of bytecode instrumentation. So
I'll I'll I'll see if that works. But regardless, I guess more. My question here is, if it requires extensive changes.
Should I do a new instrumentation.
**Trask Stalnaker** 08:06 So have you seen Gregor's? Gregor's been doing some work on that same instrumentation lately?
And making it support declarative config.
**Jack Shirazi** 08:20 I haven't seen that, but I don't think that would change.
**GZ Gregor Zeitlinger** 08:24 Sounds unrelated, I'd say.
**Jack Shirazi** 08:27 Yeah.
**Trask Stalnaker** 08:27 It's yeah. So the reason I mentioned it is
It's more motivation to me to have a single instrumentation.
Because there's more features that you would need to copy, paste over
as we with declarative, I I think, by moving to declarative config and adding this feature well, by moving to declarative config, we could also start adding more features to it.
We kind of put a stop on adding features to this, because we didn't wanna try to encode more and more things into the
environment variable.
So definitely, my preference is a single instrumentation.
But, as you say, like, if you get into the weeds, and it's just doesn't look good. Then it is what it is, sort of.
**Lauri Tulmin** 09:27 My quest would be that what you're trying to do? Isn't that involved in the instrumentation side?
To add the methods you you need to figure out how to do the class redefinition. I assume
that's outside of the instrumentation.
**Jack Shirazi** 09:45 Yeah.
**Lauri Tulmin** 09:47 And if you figure out how to add methods via the instrument like via the red definition, you're probably going. Just remove them the same way, too.
although, like, as you probably are aware, like closer definition comes with certain risks.
**Jack Shirazi** 10:02 Yeah, that's that's why I'll probably not go for uninstrumenting.
And just because there it already has the the capability to just say, this span
don't don't generate something for for this this particular method.
So I think it's fairly easy to extend that that part of the this instrumentation.
So the the
I'll look at an instrumenting. But probably I'll just go with the don't generate a span.
**Lauri Tulmin** 10:43 Well, yeah, if you figure out how to do that.
there definitely are some like concerns on
on doing it, be like one of the issues. Is that
that you have to somehow handle correctly the case where, like on the method entry.
the method was traced, and on the exit. It isn't traced anymore.
**Peter Findeisen** 11:13 No, that that's not going to happen. So class 3. Transformation in Jvm.
**Lauri Tulmin** 11:18 If you are not using retransformation, I'm talking.
**Jack Shirazi** 11:23 Yeah, he's saying that if I if I have a switch in there with.
**Peter Findeisen** 11:26 First, st which? Okay, yeah. Got it? Yep.
**Trask Stalnaker** 11:37 Cool. So I does that sound good, Jack, just to start
in, which I think sounded like what you were planning to do anyway, at least start with the current one and then see where it goes. And if it ends up being problematic to do in the same one, then if you can
bring that back, and we can kind of evaluate
the cost benefit of duplicate it, duplicating it versus making the existing one more complicated.
**Jack Shirazi** 12:12 Yeah, that's great. And thanks for the the thing, Laurie, about pointing that out.
**Trask Stalnaker** 12:22 Well, I'm gonna bump these 2 till next week when we have actually, this one
this one, we need Jack, this one. We could
chat about in the context of the Java instrumentation repo, at least.
So there's been a push to use. Github projects more to track things across open telemetry. What's this
So like collector v, 1 browser sig phase one. And then, like you can add the status
updates here as kind of a way of
Then sharing what is happening? More broadly
but more scoped, less less
in the idea of like sampling Sig, which is just like a backlog, and and people can still.
of course, have a backlog, a general backlog in projects we haven't used projects for our backlog
before, and we don't need to
But there's some
If we did use github projects for, say something like our 3 0 release or
stable database, some com declarative config.
We could group.
We've kind of been using milestones and tags. I think the advantage of using projects.
if kind of the open telemetry community and as a whole is kind of folks in the Gc. Are kind of trying to move proposing to move in that direction so that
we can have a better overview.
And then also one thing I like about it potentially for is.
then people can kind of see
kind of a couple of big initiatives that they could help out with and participate in and pick up
issues from, and it might be a little bit more visible if we
start advertising. Github projects a little bit more.
So just kind of wanted to give. Get people's thoughts on that.
If you care, you don't care think there's some pros, some cons.
**GZ Gregor Zeitlinger** 15:41 No, I don't care.
**Trask Stalnaker** 15:47 I kind of figure that's gonna be the general
feeling. I think we'll have to prove out. So probably what I'll do is, I'll probably create a couple and just kind of maintain the
just so we can start rolling them up, and we can start seeing if we
seeing what we can do with that at the overall, open telemetry level. And if we start seeing
advantages of doing that versus it just being, you know, overhead, for example.
**Jack Shirazi** 16:30 How, how long is it?
How long have projects been created for this initiative?
**Trask Stalnaker** 16:41 What do you mean?
**Jack Shirazi** 16:43 Where it's cause I'm I'm just looking at the the projects. There's there's already 20 there.
I'm just thinking.
This. This sounds like it's gonna sprawl to to be a very large number of projects.
**Trask Stalnaker** 16:57 Yeah, so there's if you look
at, there's actually 77 projects in open telemetry.
But that's because anybody can create a project, and any Sig can create one and use it.
These are the ones that are pinned
or linked to the community repo.
which I think are the ones that the Gc wants to sort of track and
share more broadly with the community.
And users and sort of
show. You know what the progress is on some key initiatives, for example.
But yes, it.
Yeah. If we continue going down this road right? We've got like 70 plus repositories.
I forget how many sigs, maybe like 30 sigs.
It's there's gonna be work on the Gc. To make something good out of it
something useful. Out of this information.
**Jack Shirazi** 18:15 These, these look like Meta issues.
And yeah, I I mean it. I I guess I'm neither for nor against. But I just wonder what.
how much better this is than a Meta issue.
**Trask Stalnaker** 18:35 Then a Meta. Oh, an issue that tracks other issues.
**Jack Shirazi** 18:40 Yeah.
**Trask Stalnaker** 18:42 Yeah, I think. It's a little bit from you can
as far as rolling them up here as
projects. You mean versus like adding them in the community repo, or each repo having kind of their own Meta issues.
**Jack Shirazi** 19:07 Yeah, I mean, we you already have, you know, Meta issues, people, open issues
saying, these are the things that the the scope of
it's kind of already a project, right? But it's just in an issue rather than as a project.
And this seems like another way to have that capability. And does it add that much more?
I guess. I guess if you're looking at across repos, then this is beneficial. But if you're looking at a particular repo. This doesn't help anything.
**GZ Gregor Zeitlinger** 19:42 Well, I'll admit.
**Trask Stalnaker** 19:43 Yeah.
**GZ Gregor Zeitlinger** 19:43 Easier to to see the status. How many items are completed. You can move them around. You can have
different lanes.
**Trask Stalnaker** 19:56 Yeah, I mean, I've gotten a little more
as I've used. The github projects a little more and they've definitely added, Github has added a lot of features to Github projects
in the last couple of years to make it more usable.
So I mean it. There's some nice things there.
but I tend to agree. My personal experience.
Jack, has been similar. Like the Meta issues have been.
My, go to and I.
**Jack Shirazi** 20:36 Yeah, especially since what you're looking at is a, it's a project board. I mean, it's a classic project board that that teams use right. But that's for
an an ongoing project that's on in development under control of the team
and the open telemetry projects are.
They're they're much more that I don't think they fall into this kind of project scenario very nicely.
because because of the number of people involved and the way they develop. Anyway, I
I I don't think it matters what I think to be honest, so get on and do it.
**Trask Stalnaker** 21:17 Yeah, I mean, kind of my my take is I'll
I'll I'll try it out with a couple of our projects. And then, so that the Gc. Has some data to pull together. Because I think you're right, Jack, about there's
or at least I
that aligns with my thinking on. It doesn't matter locally. It's more whether we do something good with this data globally. Because the projects having projects
the big advantage here is that it's yeah, a centralized something. The question is, can the Gc do something
good with this data and
share it with, you know, end users and put together roadmaps based on this and things.
Gregor, declarative config.
**GZ Gregor Zeitlinger** 22:24 Right.
**Trask Stalnaker** 22:25 Some of this. Some of this will want Jack
Bird, but for the for some of it we can chat through.
**GZ Gregor Zeitlinger** 22:35 And also a bump it. But we don't have a lot.
Seems yeah, so generally I tried out using declarative configuration
and it worked well for me as a contributor.
but I think it's quite hard to use for end users, and that is because there's only a section
and the SDK and there's not a complete
guide how to use it. That's also why I wasn't sure if it's even usable until last week.
the link that I that I put there. I think it's quite hard to figure out what to do with it.
**Trask Stalnaker** 23:28 Yeah, we would definitely. I mean, I think, we would want something under the Java agent.
Talking about declarative configuration if and when we're, you know, ready to really push that
**GZ Gregor Zeitlinger** 23:53 We are not.
**Lauri Tulmin** 23:57 Think,
didn't this come up a few weeks ago? I think there was suspicion that since the agent includes some programmatic customization for the SDK. Some functionality will be missing when using declarative config.
**Trask Stalnaker** 24:16 Did you run into that Gregor? Cause? Yeah, that's kind of a that was one of my.
**GZ Gregor Zeitlinger** 24:23 Can you elaborate? I didn't understand that.
**Lauri Tulmin** 24:28 I think one sample was that
There is something that adds a trade name and trade id attributes to the spans.
I did not pay attention.
**GZ Gregor Zeitlinger** 24:42 Attention to that, so I can.
**Lauri Tulmin** 24:43 That that is achieved through programmatic configuration.
and that probably wouldn't work when you are using decorative config probably doesn't also work with the spring starter. I guess.
**GZ Gregor Zeitlinger** 24:59 I don't know.
**Lauri Tulmin** 25:01 I think there were a couple of more other, more things that
that use programmatic configuration. I think we need to track down all of those, and figure out how to make them work with the declarative config.
**GZ Gregor Zeitlinger** 25:17 So some people apparently use it because I saw that there are some issues filed.
So, having some feedback, General would be great to see what is missing.
**Trask Stalnaker** 25:36 Yeah, it may just be some like, and maybe some things.
**Lauri Tulmin** 25:42 That definitely isn't something critical that's missing, I would assume.
But
we still would need to like somehow figure out how to test this, to ensure that we are like feature complete when using the decorative config.
**Trask Stalnaker** 25:59 I mean, it's not yeah. It was just our seed, though.
Yesterday, I think.
The Gregor what do you think of trying, seeing if you can. Hook make
the tests.
The instrumentation tests run with optionally, with declarative configuration.
**GZ Gregor Zeitlinger** 26:32 I have done something similar today. Actually, I have adapted the spring starter to use declarative configuration.
and I ran into an issue that's not affecting the Java agent, which is that you cannot.
that you require the global instance. And I,
I'll create a ticket and maybe also fix that.
But other than that the tests are running. Well, it's 1 test. It's running.
**Trask Stalnaker** 27:05 Or the methods I mean the methods, instrumentation only.
**GZ Gregor Zeitlinger** 27:11 No, the methods was running before, but it was not
maybe not as comprehensive as the smoke tests that I did today.
**Trask Stalnaker** 27:22 I see? Yeah.
**Lauri Tulmin** 27:24 There will definitely be some obscure issues like, as far as I know, like we have one
feature for logging that somehow adds, I think resource attributes or like exposes resource attributes
to the through the Mdc. Or something like that.
The problem is like that. The supposedly, the way that we get the resource from the SDK.
It doesn't work when declarative config is used it, I believe it returns an empty resource.
So so like that functionality wouldn't currently work with decorative config.
So definitely, there is like
there should be something failing when you try running all the tests with the creative config, that that was what I wanted to say.
**GZ Gregor Zeitlinger** 28:10 Yeah, got it? Yeah, cool that this is coming up. So it sounds like.
just need to spend some more brain cycles
and dump all the memory, so that we can make a plan.
**Lauri Tulmin** 28:25 I know that.
**GZ Gregor Zeitlinger** 28:26 That that is like a hard stop that really cannot work? Or is it all just not implemented yet?
**Lauri Tulmin** 28:35 I I think there's a ton of stuff that just requires a lot of hard work, especially to figure out how to make extensions work. And
I don't know if Grafon also has a custom agent distribution. And if you have a custom agent distribution that
does some customization, then that's definitely
like going to be a problem with the declarative config.
**GZ Gregor Zeitlinger** 29:00 Oh, yeah, this is actually on my list
for next week. If I'm as fast as I hope I am.
**Lauri Tulmin** 29:09 Or if you, if you manage to solve that with a week, then that would be awesome.
**Jack Shirazi** 29:15 Yeah, definitely, we want to know about that.
**GZ Gregor Zeitlinger** 29:20 I think I can get this part with the distribution to run, because it has similar challenges as the spring starter, and that required a lot of thought, but
I figured it out this week.
Well, I hope I'm not. There's nothing coming up new, but all the things that I have identified are working now.
**Lauri Tulmin** 29:45 Because, like one of the concerns for the custom distributions is that
ideally, we wouldn't want to duplicate the logic between the
current auto configure, and the the way that declarative configuration uses
somehow share the code that does the customization.
**GZ Gregor Zeitlinger** 30:04 Yep, I think
the the main logic. Maybe there is some glue layer, and I don't know how how much glue layer there will be in the end.
Maybe there's even
possibility to use some library that the instrumentation repo publishes. I don't know. Instrumentation api incubator, or something like that.
I don't know yet.
**Trask Stalnaker** 30:38 I feel like this is a really good one to focus on. Just because we, this will uncover the list of the things that are
problematic, that we don't know, at least in the base Java agent.
And we can create a list.
**GZ Gregor Zeitlinger** 31:04 What kind of setup do you have in mind? Run every test with declarative configuration, or or some or.
**Trask Stalnaker** 31:14 Yeah, kind of like how we run like tests with, I think,
there's a current pr example we run tests with and without certain setups.
**GZ Gregor Zeitlinger** 31:40 Like stable semantic conventions, for example.
**Trask Stalnaker** 31:44 Yeah, we'll run it with the stable or not.
I don't know if we did that.
Okay, so we kind of
so that that's 1 option is to have a test declarative config for each thing.
I don't know, Laurie, do you have better ideas there? How to test that.
**Lauri Tulmin** 32:18 Not really sure whether, like I think that many tests is reasonable, that.
**GZ Gregor Zeitlinger** 32:26 Seems quite heavy, because you cannot
just run in a different mode, because declarative configuration requires that you have a file.
Maybe you, I don't know. Generate the file so that you don't have 100 copies of a very similar file.
**Trask Stalnaker** 32:50 Do we want to do something like? So if somebody's using, say, we did have, hey?
An option, maybe not even here, but just in the central test config
that sets that declarative config file
to just something pretty much empty ish, or something like basic the basic settings.
Are these in the bridge. Are these going to be completely ignored?
**GZ Gregor Zeitlinger** 33:33 Yes, but we could. We can build some magic code that turns that into the file content because
the translation is deterministic, and it's not difficult to figure out.
**Trask Stalnaker** 33:54 Yeah, I'm wondering. I know the
general direction of declarative config, and the SDK settings will get ignored.
I'm just trying to think how we like. How will we roll this out to users? Users of the Java agent
are
heavily using these properties. I mean, not this one in particular, obviously, but like various all our
**GZ Gregor Zeitlinger** 34:34 Maybe you're looking for this config example, this migration config example. Let me look that up
because Jack created that particularly for users who already have a working setup.
**Trask Stalnaker** 34:52 Yeah, it's just it's very focused on the SDK, right now.
**Lauri Tulmin** 34:58 Another place that this will pop up is that
In most of our library instrumentations we pass all the configuration to the telemetry class.
But we have some of those like auto-configured libraries.
They're loaded through some Sbi don't have like this telemetry class.
When those need configuration. They usually read the system properties and the environment variables directly.
**GZ Gregor Zeitlinger** 35:32 Yeah, that is true. While working on the spring starter. I also discovered that, and
I already like improved those that were used by the spring starter, so those
can take advantage of declarative conflict. But that was only what I touched back then, and
**Lauri Tulmin** 35:55 I don't even know whether whether there is anything to be done with those, because
it's quite possible that those libraries are initialized, maybe even before the open telemetry setup or no.
**GZ Gregor Zeitlinger** 36:10 You mean you are saying that it's not possible to fix.
**Lauri Tulmin** 36:14 I don't know.
**GZ Gregor Zeitlinger** 36:15 I think it's possible. The key is that there is a global state, which is the agent config
which is starting a
static field, and that has a bridge to the config file. So that is working.
**Lauri Tulmin** 36:34 Yeah, but that that probably works if we're using the spring starter. But if you're just using the
libraries as standalone.
**GZ Gregor Zeitlinger** 36:42 Oh, you mean not the agent.
**Lauri Tulmin** 36:44 Yeah.
**GZ Gregor Zeitlinger** 36:52 I have to look into that. I don't know how that is working.
**Lauri Tulmin** 36:57 Me, neither.
**GZ Gregor Zeitlinger** 36:59 But that's a good point to write down. How do we have to evolve existing Apis like for
service and clients that we already stabilized? Or did we actually.
**Trask Stalnaker** 37:15 We haven't but I don't think the the public Apis at least
are all programmatically driven. I don't think the library instrumentation reads config in general, because we don't didn't have a way for them to.
**GZ Gregor Zeitlinger** 37:33 Okay.
**Trask Stalnaker** 37:34 We require people to programmatically set all of those options.
**GZ Gregor Zeitlinger** 37:40 That saves us in this case.
**Trask Stalnaker** 37:46 Right? Right?
Speaking of Meta issues Gregor, do you have a do you want to create a Meta issue for sort of
tracking declarative config for the Java agent.
**GZ Gregor Zeitlinger** 38:10 Yeah, okay, maybe Meta, issue or project your choice.
**Trask Stalnaker** 38:15 Oh, right, I was going to create. Yeah, I think I will create a project that I think this is
large enough.
I mean. I do think it's a fairly.
and it's a big, deliverable cool. I will do that.
**GZ Gregor Zeitlinger** 38:35 So for the spring starter I did a project, and it had more than 100 issues. So it was definitely worth
having that.
**Trask Stalnaker** 38:45 Nice.
**GZ Gregor Zeitlinger** 38:49 And, Laurie, can you help with
your inside knowledge about the things that you know are not working.
**Lauri Tulmin** 39:00 I I think I already mentioned those.
**GZ Gregor Zeitlinger** 39:04 Right, but writing it more down in detail, because that is not enough.
If I find the time to work on that.
**Lauri Tulmin** 39:15 I know that Robert is already looking into this.
but I think I can paste you the link in slack.
**GZ Gregor Zeitlinger** 39:24 Okay. Thanks.
**Trask Stalnaker** 39:29 Yeah. And I, I feel like we, we will need to figure this out at some point. Because the tests are the only thing that give me
confidence in the Java agent is so big and widespread.
I guess I'll have to think about that more
cool.
**GZ Gregor Zeitlinger** 40:00 Yeah, I'm wondering
if you're looking for tests for the SDK, or for the instrumentation. That is what I'm wondering.
**Trask Stalnaker** 40:09 The Java agent.
So the all the instrumentations.
That
just to catch like edge cases like the thread span processor, although I honestly don't even know if we test this in the instrumentations themselves.
**Lauri Tulmin** 40:31 I think that is disabled for the instrumentation to reduce the number.
**Trask Stalnaker** 40:36 Yeah.
**Lauri Tulmin** 40:37 Notes.
**Trask Stalnaker** 40:40 This one it would catch. So maybe there's yeah.
It could be argued that there's not enough there to be worth that.
or possibly we wait, and at some point, if there's a way to move all our tests to declarative config
in a way that we maintain confidence that we didn't break the existing stuff.
**Lauri Tulmin** 41:12 Well, what we could do is we could just like,
try to track down all the places where we know that we use programmatic configuration and have a smoke test
that runs with declarative config and verify that those programmatically added things are present.
**Jack Shirazi** 41:35 So if if we if we run all the integration tests with declarative config using a standard
agent, declarative config, then that would be like a 1st step.
**Trask Stalnaker** 41:59 That's kind of what I was
thinking, so that the the entire battery of tests.
**Jack Shirazi** 42:11 Just I mean the integration ones, because obviously the unit ones don't matter for this. This scenario.
**Trask Stalnaker** 42:18 Right?
Yeah, if we can find a way to sort of centrally enable declarative config or not.
then we could matrix it out fairly easily in the Github action
as opposed to having to add one of these
test new cradle test configuration for all of them which I agree is.
**GZ Gregor Zeitlinger** 42:50 That scares the hell out of me.
Oh.
**Trask Stalnaker** 42:55 Yeah, all, all 200, all 200 gradle modules.
**GZ Gregor Zeitlinger** 43:03 Yeah, I'll think about if if we can make it an environment variable and then do some magic.
**Trask Stalnaker** 43:21 I mean, what's what? Let's see how many jobs we have today.
**GZ Gregor Zeitlinger** 43:31 And you don't probably need to run it for every person.
Huh!
But you don't want to duplicate that right.
**Trask Stalnaker** 43:42 We don't do. What do we do here? Common? Oh, we do against all the yes, yes.
**Lauri Tulmin** 43:51 Well, if you if you want, we could like run it only for one Java version.
**GZ Gregor Zeitlinger** 43:57 Yeah, that's a good idea.
It's fine.
**Trask Stalnaker** 44:19 Or Java eights.
I don't know what's does probably doesn't matter
cool. Alright, yeah, thanks, Gregor, for continuing to plug away on that.
**GZ Gregor Zeitlinger** 44:38 My pleasure.
Let's let's bump the resource question until next week.
**Trask Stalnaker** 44:46 Yeah, yeah.
Gotten really bad at filling these out
to the extent that one of the meetings I go to. We looked back at the last week, and nobody had filled it out or like where there were all these topics. And it's like, well, a lot was discussed by nobody.
I like what they do in the spec meeting, I think, where they put the number
of attendees also.
Jack.
**Jack Shirazi** 45:51 Yeah. So someone's working on this jamx,
is actually the he's working on that
that Pr that he's linked there. And what he's found while he's working on it is that they've got all these
metrics that are generated which are useless.
So he's given a full description in this, in this issue of
exactly what he's seeing and why they're not any good.
What he really wants is some feedback or ideas on how best to eliminate the the problem. So
useless metrics or high cardinality ones that are following this pattern.
And how how to best get rid of them. He's he's suggesting metric views. But maybe there's
other ideas, or maybe that's perfect. And and it works. Or maybe it doesn't quite work. So
yeah.
**Trask Stalnaker** 46:58 And so so I think I basically, I understand that.
You, we really, we want to aggregate over all of these.
**Jack Shirazi** 47:14 Yeah.
**Trask Stalnaker** 47:15 And so the question is whether we need to do that aggregation in the Jmx insights component.
or if we can leverage metric views to do that aggregation in the SDK.
**Jack Shirazi** 47:31 Yeah.
and then there's also I mean, it's a little bit more complex in that. It's not just aggregation. But I think there's also some
elimination. Because the like, he's saying that the context key value is like a high cardinality value.
And that would be part of what the metric generates, and you'd want to eliminate that.
So it's
yeah, it's a little bit more complex. But I think that's I mean, that's that's essentially it.
**Trask Stalnaker** 48:01 Okay, yeah. Cause, I'm thinking that the for context key is just another thing that you want to aggregate over and not capture individual context key values.
**Jack Shirazi** 48:13 Yeah.
**Trask Stalnaker** 48:18 So I forget, if can you add in metric views programmatically.
**GZ Gregor Zeitlinger** 48:35 Dimensional.
**Trask Stalnaker** 48:47 Set advice attributes
this might work. This is what we call from the Java agent.
For because we, when we record
metric, say, for, like Http. Server.
we pass all the attributes from that Http span to the metric
but when we're constructing the
instrument, we set the advice attributes we set the list of attributes we actually want stamped onto the metric
and that has to be a subset of everything that we're passing in.
And that will then basically, it will drop all the other attributes and only aggregate over those.
Let's see if we're missing any.
The technical.
Oh, I see the 10 distinct with the same, unless we map id key, as I see.
**Jack Shirazi** 50:57 Yeah. So it's not just elimination of it's like
the combining elimination and aggregation at the same time. I guess.
**Trask Stalnaker** 51:14 So let's look at a a
should not contain.
Let's look at this jetty.
That configuration for that should be
Markdown.
Peter, can you help me find the
jetty? Oh, no, not not Markdown. I wanted Yaml.
**Peter Findeisen** 52:15 Yeah, that's it.
**Trask Stalnaker** 52:17 Cool.
So we've got.
Yes. So the problem is that
So we wanna capture these.
So what I think would work is, I think if you call set, attribute advice with these 4,
and then when you're recording the metric
you would pass in context equal something id equals something every time.
Then you're passing in all 6 of these attributes
where you're recording to the metric api. You're recording all 6 of these attributes. And then the metric SDK
via that attribute advice will restrict that down to just those 4
essentially dropping these 2 that you passed in and aggregating over them.
**Jack Shirazi** 53:36 Oh, nice!
**Trask Stalnaker** 53:43 I can. I'll I'll comment on here, and we'll see if that aligns with what Sylvain is
thinking. But I think that I think that attributes advice actually is perfect. For this.
**Jack Shirazi** 54:01 Thank you.
**Trask Stalnaker** 54:02 Yeah.
cool.
Alright. I think we hit end of our agenda and nearly end of our time. Slot.
Thanks all.
**Peter Findeisen** 54:19 See you next week.
**GZ Gregor Zeitlinger** 54:20 See you.
