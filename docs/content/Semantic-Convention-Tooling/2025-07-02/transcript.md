SIG: Semantic Convention Tooling
Date: 2025-07-02
Duration: 65 minutes
============================================================

## Zoom Recording Transcript

Josh Suereth 00:00:26 Hey? How's it going.
Jeremy Blythe 00:00:28 Good! How are you?
Josh Suereth 00:00:29 Not bad.
Jeremy Blythe 00:00:30 You managed to get out of the line. Then.
Josh Suereth 00:00:33 Yeah, I it turns out the Dmv splits you by what you have to get done.
And so, while there were 50 people in front of me. There were only 2 in front of me, for the thing I had to do, and the thing I had to do was considered fast, and so they put us through right away. They like fragment out the line.
Jeremy Blythe 00:00:50 Cool.
Josh Suereth 00:00:51 Yeah, it was I felt bad for everyone else. I'll just say that.
Laurent Quérel 00:00:57 Hey, guys.
Jeremy Blythe 00:00:58 Hey!
Josh Suereth 00:01:03 Alright! I might have a a hard stop here, where I have to leave a little bit early for the meeting, so I want to try to get through some of our important discussions quickly, at least the ones that you need me for, and then and then go to other discussions. So
I do think the most important thing is this needs more eyes
the enum thing. I think Ludmilla has a fix for it.
which is what she's linking to.
to move forward with an implementation who
I thought she had a fix for this.
Jeremy Blythe 00:01:49 Yeah. There's a group.
Josh Suereth 00:01:50 Oh, no! It's this one here.
Jeremy Blythe 00:01:55 Oh, that one,
Josh Suereth 00:01:56 Yeah.
Jeremy Blythe 00:01:57 Yeah, we talked about that last week.
Josh Suereth 00:02:03 I see was that copied from last week. Then.
Jeremy Blythe 00:02:06 I'm guessing. That's been Kobe from last week.
Yeah.
Josh Suereth 00:02:12 Okay.
Let's let's real quick. Then go through.
Jeremy Blythe 00:02:19 Alexandra said that she wouldn't make it today, anyway, so I'm not sure we can
move forwards on that one.
Josh Suereth 00:02:26 Yeah.
I want to go through weaver triage, because I think the most important thing I want to sort out is a release.
Laurent Quérel 00:02:33 Yeah.
Josh Suereth 00:02:35 So Weaver should resolve full. URL, generate Json Schema from us models. That was when I was looking for document exact. That's yeah. Weaver diff template extension weirdness.
updating new values and referencing attribute that one. We still need to actually get something implemented. I think let's move to the Prs for Weaver, because I think what I want to sort out there is
what we'll do.
We were, by the way, finally managed to update
dependencies. So we have 2 breaking dependency updates to sort out. But we finally got approval on June 25th
for that license, the permissive license for the web pki roots. So I think we're in good shape there.
Alright annotations for new members. This was one I was actually thinking is critical. This is a a bug fix for
for simcov. I think you saw my comment here about changing these around.
And then.
yeah, this one looked good to me to merge. I don't know if you guys want to take a look at this quick, but this one I we should get this out so we can fix the break and on on enum collisions and semcom. We're also looking at backing out the change in semcom and cutting a patch fix. But if we can fix it in Weaver. I think that's
that's important. So we can re-roll forward. For context. This is another issue where I can show you the the change.
Where's an example?
Is this?
Nope.
so basically, if you have a
is this the one second stable?
Maybe maybe it's better just to read the description.
all right, we'll go to the actual bug that was open. So basically, we renamed from azure underscore to azure dot
the ids of enums, and it breaks cogen.
And what we did in the past for attributes was, we have hints where we can suppress cogen for the underscore version and switch to the dot version.
Laurent Quérel 00:05:04 Okay.
Josh Suereth 00:05:05 These are unstable enums, to begin with. So that's that's a
still an acceptable breakage from a simcom perspective. But yeah, we weren't enforcing the namespace of the enum for dots versus underscores previously. There's work in somecom to fix that. I think Lyudmila has some options here of what we want to do, and she has this patch to weaver. So we can actually have an annotation. So we can make these changes going forward
with Cogen. So she has Cogen hints and all that stuff. If you look what she has is, she has Jq. Expressions that will leverage hints, and then she has annotations on enums is the big thing that that is added before annotations only touched attributes and groups, but not enum values. And so now they will be on enum values. So I looked at I looked at Pr. It looks well tested. It looks good. I think we can merge that and get that in for
for this release.
Laurent Quérel 00:06:01 Sounds good.
Josh Suereth 00:06:04 Any concerns. Or do you guys want to take a look at that before we okay.
Laurent Quérel 00:06:09 I'm looking in parallel, but.
Josh Suereth 00:06:12 Yeah, let me let me put this in our discussion board.
Laurent Quérel 00:06:21 Here's Prs, so this one
we will include. So if everything is well aligned, we will include 812 for the release.
If everything's in line, we'll do what?
Because we have the intend to create a release either today or tomorrow.
Yeah, I was seeing just that this release will include 812. Once it's once it's approved and.
Josh Suereth 00:06:51 Yep.
Laurent Quérel 00:06:53 What else is there any other
part of this request not merged yet that we need to include.
Josh Suereth 00:07:04 That's the discussion I wanted to have next, which was on. Let me put this in next release the next discussion. I wanted to have was a bit of the follow up on the discussion we had around metric type field.
What do we want to do around metric type, field going forward here.
Jeremy Blythe 00:07:22 So the the value type thing is that what.
Josh Suereth 00:07:25 Value type. That's what's called.
Jeremy Blythe 00:07:27 I. Last night I did a Pr. Which was approved and merged.
and that backs it all out.
Josh Suereth 00:07:35 Okay, okay. I didn't even notice great.
Jeremy Blythe 00:07:37 And then I made an issue which is
actually, it's gonna be really nice. Actually, I think is that we'll make the. We'll make the annotations, part of the model
visible to the live track rego policies.
So if you want to have a custom policy and we we could build custom policies as part of the
like the hotel. One.
Josh Suereth 00:08:04 See.
Jeremy Blythe 00:08:05 Oh, given this annotation.
But the Weaver code base itself doesn't care. It's kind of just passing this annotation through full model
to Eureka.
Josh Suereth 00:08:14 That's beautiful. It gives us a full open extension. So if you have annotations, you want to enforce some policies you get live check. Yeah, I love it.
Jeremy Blythe 00:08:21 Yeah, it's really nice. Actually, yeah. So sometimes deleting things is is a really nice thing to do.
Laurent Quérel 00:08:29 No.
Josh Suereth 00:08:29 We, we added the value type in a point release. This is kind of removing it is, isn't that? Would that be a breaking change or
right.
I. I'm fine doing it in the fact that we're doing it quickly. But we should warn people. We should just tell people, hey, we released this we didn't mean to.
I don't know.
Laurent Quérel 00:08:55 Yeah, I will add in the in the change log
during the preparation for the release, I will add
opponent on the fact that it's a breaking change was something that happened just for between one in one release
shortly. So I will add a small message about that.
Josh Suereth 00:09:16 Okay.
Cool.
Laurent Quérel 00:09:18 So no, no need to create a new Pr, I think I will just create that into the
the release. Yeah.
Josh Suereth 00:09:25 All right. So I think our release is sorted. Then.
Are you going to give it a minor version like we did before. Are you gonna give it a sorry, a patch version like we did before? Are you gonna give it a minor version?
So another.
Laurent Quérel 00:09:38 A minor version right? Because we.
So we have this breaking change. And we have the
the 812, which is a kind of new feature.
Josh Suereth 00:09:53 Yeah, that's what I was asking. Yeah, I would like to see this be 0 16. And yeah, okay.
yeah, cool. That's what they will do awesome
to me. That was the urgent thing I might need to drop in like 5 or 10 min for I'm double booked, apparently today, and I just noticed 5 min before this meeting, so I couldn't fix it.
Laurent Quérel 00:10:17 Okay.
Josh Suereth 00:10:18 And I need, anyway, getting people to respect your calendar is always fun when you you can open schedule meetings right?
Alright. So if we can move on to major discussions, I do want to call out that I
we need after the the 4th of July holiday. I think we need to make a more concerted effort around getting the telemetry schema 2.0 out.
which means we need to start making some hard decisions. So hard decision. Number one is what will diffs look like in telemetry schema. 2.0. Are we going to keep the current model of, you know? Manually.
you know, defining things. Anyway, you saw the tracking bug. We have the tracking bug. But I would like next week to start actually making decisions on that
and moving forward because I want to get that
proposal fleshed out. And I want to get us to a state where we
can publish the thing we want to publish and start working on
prototypes of weaver generating the entire. You know, Simcov URL, of stuff
in semcom. So like when we publish the Semcom Directory for a version. We can put all of the files we want in it that we have a prototype in semcom that does that
and generates the thing we want it to generate, and then we can start pushing spec work for this right?
So I'd like to kick that off. I don't think this is the right week, because some of us are possibly.
Laurent Quérel 00:11:53 Yeah.
Josh Suereth 00:11:53 Working for the rest of the week or longer. Some people might be. That's fine. But
yeah, I'd like to kick.
Laurent Quérel 00:12:00 I'm in vacation for the I'm in vacation, beginning next week for 2 weeks.
Josh Suereth 00:12:05 Exactly.
Laurent Quérel 00:12:06 Throughout.
Maybe we can start the discussion this week.
If you have any availability. I mean, we can find a can block 1 h and and try to
to make some progress, at least on the on the rational.
Josh Suereth 00:12:24 Technically, I have off tomorrow. But I'm going to be doing the entity sig in the morning.
So yeah, I I
I can probably do an hour discussion tomorrow just to to kind of get through some things.
Laurent Quérel 00:12:39 Okay, that that works for me.
Yeah, tomorrow morning I'm available.
Okay.
so yeah, let me know when you want exactly. And and I will make sure that I'm available.
Josh Suereth 00:12:55 Okay, that sounds good. We can.
If you guys want to talk, I do have to drop soon. So if you want to talk about it now.
Feel free coming for schema.
So next us, specification pushes. We we have. We have the tracking issue.
What? What I what I want to do
now is basically figure out what kind of prototyping we can do
to demonstrate that this works, Ludmilla. You already have schema. Next generation from Weaver diff
as a prototype. I'd like to take that and refresh that. So the schema diff is generated. I was also going to take that Pr. And I don't know if you want me to open Prs against your Pr. But I was going to add, publishing the current resolve, schema from Weaver, right beside the diff.
Liudmila Molkova 00:13:53 I can do this.
Laurent Quérel 00:13:54 Yeah.
Josh Suereth 00:13:55 If if you have time, feel free. I would. I was hoping we could divide and conquer. But if one person has time totally fine. I just wanna try to move quickly to the point where we are comfortable with the prototype. We all understand the the problems, and we can make this back if you have time to do that, please do. Yeah.
Liudmila Molkova 00:14:14 I'd rather not do this as a as a part of this Pr. But something on top of this, because I think once we see the result. Schema.
we will not.
We'll have some comments and improvements. But yeah, yeah.
Josh Suereth 00:14:31 Well, okay, I was. Gonna I was gonna take your Pr as the foundation and make a new branch that has this in it, and and basically start fleshing out. Okay.
if we take the new vision of application telemetry schema and what we want to publish from weaver.
let's start actually implementing that for semcom with what weaver does today.
Figure out where we have problems.
figure out those problems with weaver and then use that to write the spec. Does that sound reasonable to everybody?
Okay, and.
Laurent Quérel 00:15:04 I think I am regarding the the previous schema. There is a description
not not perfect, but at least the concept of we've always repackage.
Josh Suereth 00:15:17 Yep.
Laurent Quérel 00:15:17 Something like that in this document, just to be passed it
that could be useful for the
when. We will think about that, it's
and we need also to put the.
Josh Suereth 00:15:32 And I think you should follow that document. We also have a bug specifically about what the multi registry
thing looks like from a schema. URL standpoint.
So I think between those 2, like, yeah, we we should be using what we've written to make this template. I just wanna actually get like, let's actually
implement it for simcop right?
And let's make sure it works for Semkov, and then and then move on from there. So, Ludmill, if if you have time to refresh schema next, I can branch what you have to do this, or if you want to do this work too, feel free. I don't need to do it.
Liudmila Molkova 00:16:09 I I wanted to play with that for a long time. I should have time today.
Josh Suereth 00:16:13 Awesome. Okay? Then, let's if you want to take a crack at making a prototype of that that we can then talk about it next week and try to work, start working through issues. Because I expect that just this Doc, and what we have today, we'll have a lot of things to work through. And so let's let's get them started by like, actually implemented. But I think we're in terms of being able to implement it. We have the features. We just need to make sure that we have the
bugs, and you know rough edges patched cool. I do need to drop, so I apologize.
if you need me, for any of the other discussions like feel free to ping me offline. But yeah.
Laurent Quérel 00:16:45 Yeah, don't. Don't forget to send the invite for the meeting tomorrow.
Josh Suereth 00:16:50 Yeah, I will follow up on chat with like options. There.
Laurent Quérel 00:16:53 Cool. Okay.
Perfect.
Josh Suereth 00:16:55 Alright. I'll see you.
Laurent Quérel 00:16:56 Thank you.
Jeremy Blythe 00:17:09 So they're on great work on the blog posts.
That's really.
Laurent Quérel 00:17:12 Thank you.
Jeremy Blythe 00:17:14 I did. I put a note in slack
You were saying. Oh, we could, or, Josh was saying, to use
like a lot of that for the readme.
I'm kind of feeling now that
the readme should refer to that blog post. Actually, I think, like
we could put some snippets of
the really important things. But my feeling now on the blog on the readme
is, let's not just copy all of that in there, because
that blog post is written really nicely and reads really nicely. And so now we can just go like, Oh, here's like the elevator pitch for weaver. Here's the thing. And now it's like, Hey, if you want to know more about this, this, this here's a great blog post about it. And then the readme becomes more of a
getting started.
You know, links out to here are presentations. Here's a blog post. Here's another one. Here's an example.
You know, some of those full examples we did like.
Here are all the main commands, just like briefly.
where each command has a link to the how to or like the crate, Doc, that we have. So we've got some of those docs, for the crates are really, really descriptive.
And so it becomes. The meeting becomes more like a.
It's the front door.
Laurent Quérel 00:18:30 Yes.
Jeremy Blythe 00:18:30 Load of documents. That's.
Laurent Quérel 00:18:32 I. I totally agree when when I said that maybe we we can use some element of the the blog post, I was mostly thinking about taking some very small part of it.
Jeremy Blythe 00:18:44 Yeah.
Laurent Quérel 00:18:45 So an example of that. I think the the custom registry example
is, is more consistent in into the blog post. I I use your your example first, st and then I started to to improve it, to make it more realistic for someone.
I think we can reuse that.
and probably a few other things. But I agree we we don't need to copy past the the past directly into the windy. I think the really could be much more.
Yeah, I'll become the the how to use them. It's more more direct.
Jeremy Blythe 00:19:23 Okay, I'll rework it that way. Then, if we're happy with that.
Laurent Quérel 00:19:29 Yeah.
So the Severin told me that.
so there are some ptos here and there here in us. So I think Josh will approve the the blog post, because we need one at least one person from the seed.
the Turing series
to to approve it, and then it could be any of you, or so obviously, and
Jeremy Blythe 00:19:57 I saw an approval on it already from Josh.
Laurent Quérel 00:19:59 Oh, okay, okay, perfect. And he told me that hopefully, Friday, we, we'll be able to look again at the breakfast.
so we can expect to have this blog post maybe published beginning of next week.
So that means that if we can have a 1st version of the renew
ideally beginning of next next week. That that would be perfect.
Jeremy Blythe 00:20:31 Yeah.
Okay.
I will give it my best shot.
Laurent Quérel 00:20:38 Nice.
Liudmila Molkova 00:20:40 Is, is, the.
Laurent Quérel 00:20:40 And like I said, sorry.
Yes, there is.
Liudmila Molkova 00:20:46 Oh, okay. Wonderful.
Laurent Quérel 00:20:48 Yeah, and I, it's like a back and forth because Jamie created the this pr, then I use it as a source of inspiration for the blog post.
Jeremy Blythe 00:21:02 That's it.
Laurent Quérel 00:21:03 And even before that it was the slide deck that we did.
Jeremy Blythe 00:21:06 Exactly.
Laurent Quérel 00:21:07 For, for.
Jeremy Blythe 00:21:09 Yeah, exactly.
Laurent Quérel 00:21:11 Keep going.
Jeremy Blythe 00:21:12 It's a feedback loop.
Laurent Quérel 00:21:14 Yeah.
Okay, yeah. I think with with that we will have more visibility. And
that should also develop some awareness around the weaver and semantic conventions, which is great because people, I think people a lot of people are
now interested by the concept. That we introduced. To be Frank. We just need to be more visible.
Jeremy Blythe 00:21:47 I actually have a hopefully, a whole new, somewhat Greenfield project at at my work.
which I'm hoping to get the whole team to use
the sort of model the model driven approach from from the beginning. So yeah.
because, yeah, I totally agree that it, especially especially when you go down to the sort of the the low. When you get down into the lower level components, the libraries, the things like that
where there's
being model driven all the way down there definitely like pays pays off as you go higher up the stack. There's way more change going on like the application there. And it's like I'm
I'm not sure I'm still like. Is this.
is this being too strict? It's some some layer in the stack, but certainly, when you're all the way when you're like further down the stack. That's kind of approach, I'm thinking. Anyway.
Laurent Quérel 00:22:44 Yeah. And and similarly, at a 5, we also have engine mix, that is more and more.
adopting the this approach.
I'm sure some other project will will take inspiration of what ingenux did.
It's relatively common, you know the fact that teams are competing, the others and
and also the what we are doing with the hotel, our project that the the rest base data from Gene, that
on which I'm working now much more. We will not only use semantic convention and weaver.
but we will also, if no one is developing one specific type, safe client instrumentation. Api.
Try to remember the the right terminology. Now, thank you for that. So the we will use this approach
in order to and and it will take times, because the for us the the goal is not only to have a type safe Api.
directly into this new pipeline engine that could be integrated into the Go connector, but also
to create a massively better
in terms of performance client, so that the code should be generated to be fully optimized just for the this semantic convention that we decide to use for this specific application.
So we want, we want to bypass every abstraction layer that currently exists into any client. Dynamic client. Sdks?
No, no, hashtag, no, nothing like that.
We. In fact, we should be able to to derive directly the
the binary representation of the the Otp Otlp stream directly from your segmentation.
So that's the reason why we we want to go so into this direction.
Jeremy Blythe 00:25:02 We're good.
Laurent Quérel 00:25:05 I saw a link about the the I think it was config, the the 761. Maybe we can discuss that because we
we already put that in the last
meeting the same meeting, but we had no time to talk about it. I know that it's a
a topic that we like together, Emilia. So
I think we can. We can maybe, hopefully take some decision.
I can share my screen.
Liudmila Molkova 00:25:42 Yeah, that would be wonderful.
Laurent Quérel 00:25:46 I notice also that we have
a new person in the meeting. Could colleen.
Cullin 00:25:52 Hello!
Laurent Quérel 00:25:54 At all nice to meet you.
Cullin 00:25:59 Nice to meet you all too.
Laurent Quérel 00:26:03 So so you are. You have in front of you 3% of the
70 convention Slash Hotel weaver project
2 Matner for the the Weaver project and one Matner for 17.
So are you looking for some specific topic regarding the tooling for semantic convention.
Cullin 00:26:33 So you're asking if I'm looking for any to discuss anything.
Laurent Quérel 00:26:37 Yeah.
Cullin 00:26:38 No, I I I kinda I signed up for most of the open telemetry sigs.
and so I've.
Laurent Quérel 00:26:46 Oh, wait!
Cullin 00:26:47 Making the rounds. And here we are today, except.
Laurent Quérel 00:26:51 Okay.
Cullin 00:26:53 Thanks for having.
Laurent Quérel 00:26:54 Okay, okay, so no problem.
Jeremy Blythe 00:26:57 Fly on the.
Laurent Quérel 00:26:57 Okay, so I will share my screen regarding what we just discussed.
I think that's this, when
and then I will go to the to the Github issue.
So it was about just a reminder. Inconsistencies in the command line.
That's
Ramilla mentioned
multiple time not only in this Github issue, but also in some other conversation. So then from there. I
I try to to propose something that is a mix between minimizing breaking changes.
minimizing the effort inside river.
because we don't necessarily have a lot of time. And still improving significantly the the user experience in order to, and also definitely remove all the
inconsistencies.
And I think this proposal is following those principles.
And so from there came a conversation where Mia was
still thinking of a different approach.
and I will let you, Remilia, expose it.
But I'm I'm not fully on board, because
because for me it's it's more work, and I don't. I don't. I don't see the
that as a real problem, and I would prefer to favor the the values principle. I just enumerated minimizing breaking changes, minimizing effort and still removing inconsistencies
and and provide a good user experience.
Liudmila Molkova 00:29:06 Yes.
Laurent Quérel 00:29:06 So that's why we have some kind of looking situation there.
Sorry. Go ahead.
Liudmila Molkova 00:29:11 Yeah, my proposal, what's the
the user experience? First, st I agree, I'm not. I was not considering the minimizing breaking changes, because I think we can make them still.
We are experimental, we are version 0. There are a handful of users. We can
do this in non-breaking manner.
And second the
the work. Of course I don't have a good estimate on how much work it would take, but I thought that it would be useful to car kind of build, the
awesome user experience.
And then we can see how much
we can invest into, endorse him.
Laurent Quérel 00:30:06 Yeah. So let's talk about user experience. Then, because even without all your consideration, I still think that
I don't see the problem if we do those correction that are mentioned into this into this summary.
So I think that the main point of disagreement between the 2 of us is
you want to consider the the configuration file?
The 1st element. And personally, I want to consider like we do today.
the collection of templates and the the configuration file as the minimum treatment.
So right now we we use
dash, dash templates, and and we
we direct that to a pass
which is hard to understand, because,
there is a required organization where we have this pass. So that's the the with templates. And then we have subdirectories representing target. And then we have inside those target directory. We have template files or any kind of file. In fact, that will be used by the the template engine plus the the configuration file with.
So the 1st simplification is to make this intermediary target directories fully optional.
and in most of the time that will not exist now for future at least in my proposal for future
development of
A new set of templates. We will just direct, dash, dash, template, to
the the effective pass containing all the templates, plus without the Ml.
Liudmila Molkova 00:32:06 Yeah, so.
Laurent Quérel 00:32:09 If you stop here for a sec.
Okay.
Liudmila Molkova 00:32:12 I I understand.
Still.
for example, I we have cases and semantic conventions, and of course we don't need to cater for that. But we have cases where I I would like to put
the this multiple variables in the same
pulled there because it feels natural. But they they will be executed as part of different commands for absolutely different scenarios.
or essentially my my key point is that most of the
command line tools you take. They take a config, and config is the source of truth for all the config. It's not that you, and if you need to reference something.
you just use the relative or absolute pass in this config, and this feels super common.
Now you return it around. They are saying there is a directory, and there is a
actually an unknown set of things inside this directory
that are the source of the config, and I, I.
Laurent Quérel 00:33:25 Yeah, so.
Liudmila Molkova 00:33:27 Yeah.
Laurent Quérel 00:33:28 So I I don't disagree that some command use config. I mean, it's a common pattern, I agree.
What I'm seeing is, I don't think that where's the proposal I made?
We are overcomplifying, even complexifying the user experience. To be honest. And I see, I mean.
I don't see the huge. I mean even even a minimal problem with the the current experience. But with this experience that they expose. So, for example, I like to go in this direction we regenerate Java we generate go, once we have the template that.
Liudmila Molkova 00:34:08 Nothing stops us from doing this right. It's just if you specify.
Laurent Quérel 00:34:11 And.
Liudmila Molkova 00:34:11 Bye, it's I think our debate is between templates and config.
Laurent Quérel 00:34:19 Yeah. But so if you consider that the config is not in that case not useful. So why? Why do you think that it's it's so important to have when you specify the templates. So that what I'm saying is you, you have that.
And and in implicitly, it's saying, Okay, please use the template for Java.
Liudmila Molkova 00:34:41 That's what this government is saying, right.
and all default and default with our yaml.
Right.
Laurent Quérel 00:34:48 Yeah.
Liudmila Molkova 00:34:49 So there are 2 things actually.
Laurent Quérel 00:34:52 But part of those templates.
It's not, it's not any. It's not like
a default, it's it's not a weaver or yammer default.
It's a. It's the river that is present into the template containing the Java templates.
Liudmila Molkova 00:35:10 This this coupling? Right? So we have templates, and they implicitly have config
Laurent Quérel 00:35:18 But who is not liking this, this coupling.
Liudmila Molkova 00:35:22 Huh!
Laurent Quérel 00:35:24 You. You are saying that's what people don't like. But I I never got anyone saying except you, that the config should not be part
of the the Directory, where the templates are.
Liudmila Molkova 00:35:38 Oh, I think it's it's currently hidden behind the feedback that there is an implicit directory structure, and it has implicitly a fever that.
Laurent Quérel 00:35:48 No, I don't. I don't understand it this way. For me the the problem is more
the fact that people expect to have directly the template inside the the pass, where, when we specify, dash, dash, template, a pass people expect to put.
There are templates directly there, and unfortunately that was not the case, because we have this
additional subdirectory representing the target. That's the conversation, for example, we had with Martin was about that
he was not complaining about the fact that the weaver, the chairman, was
at the same level than the top lights.
He was complaining about this intermediary pass, which is, I agree.
Liudmila Molkova 00:36:33 I'm not saying that Weaver Yaml should be at some level against templates. I'm saying that it should be explicit.
Yeah, I would like to be able to explicitly give you the river Yamo
and I don't like that. It's part of the templates. It's not a template right.
Laurent Quérel 00:36:57 Yeah. But I like to see evidence of that. Because personally, I disagree. It looks like
I'm not the only one. If I read in that
I don't want to make any big change like that, because there are many implication in the existing code source.
and I don't see where the the user experience is so great that justified all of this effort.
So that's not.
Liudmila Molkova 00:37:28 So I don't. I don't. Honestly, I don't think there is any effort either. So there is currently you already support config. We can say, okay, we currently only support the templates that are in certain locations.
Laurent Quérel 00:37:39 The the way
I mean, I I implemented this stuff. I can. I can tell you that there is a huge fault
if you want to do it, feel free to do it. But yeah, I'm saying
TV, there is a huge effort to do.
Liudmila Molkova 00:37:53 To fully support it, to fully support different locations for templates and config. Yes.
but if you want to limit the 2 days, the support is limited to. I can keep limiting the support until we feel comfortable. Honestly, what I'd like to
here
is forget about the effort for a sec. Maybe we decide. Maybe the effort is huge. Maybe it's not justified. But this is the last chance for us to make the proper user experience.
I mean.
Laurent Quérel 00:38:28 Hopefully, you will. But I spent all this time to create this proposal just for that.
I mean, if you read carefully this proposal. It's really taking into account the user experience.
Liudmila Molkova 00:38:41 Yeah, but we we.
Laurent Quérel 00:38:42 So.
Liudmila Molkova 00:38:43 About user experience. We both are subjective and don't pretend to be the source of truth.
I, yeah, that's why I like to get additional feedback.
Laurent Quérel 00:38:53 Because, like, I said, you have your point of view. I have a different point of view.
I don't see why the the user experience is so different between the 2.
What I see. So that's my point of view. I don't see the the huge difference in terms of user experience. What I see
is the the breaking change and the the additional effort to do if we go in your direction. So knowing that for me there is no difference in terms of user experience.
I can't go into the into your direction because of the breaking change, and because of the the effort, the additional effort.
So that's why I can't separate the fact that there is additional default on the decision, because.
on my side, the the user experience is similar.
Liudmila Molkova 00:39:52 So how do we get additional feedback? We have a couple of folks here. I don't know if you
Laurent Quérel 00:39:58 I think we're getting Jeremiah because Jeremiah has some, I mean, has definitely experience with this stuff. So it would be interesting. We already get the
the feedback from Josh.
I want to let that ear, because I think it's for me clear. But
Jeremy Blythe 00:40:17 I feel like.
Laurent Quérel 00:40:18 I think we already have one feedback. Here, press your your feedback.
Jeremy Blythe 00:40:23 Yeah, I think I think
I think for me to properly comment on this. I need to properly read this and understand.
I can see the I can definitely see the the point of view that
do we want to take a step back and go like, okay, if we could, if we could do all of this configuration again. Another way that feels like it's like, you know, all the all the cli interface likes some other way. Would that be better like, I guess like, is that what we're talking about? I need to read it properly, digest it properly
and then comment. I think,
are there people who do? We have other users who are not us.
that we can get some feedback.
Laurent Quérel 00:41:08 We have not seen.
Jeremy Blythe 00:41:09 Make sure.
Laurent Quérel 00:41:09 Yeah, we have plenty.
Yeah, we have plenty of people, I think. Now, plenty
Liudmila Molkova 00:41:15 Everybody stumbled upon the current problem, which I think boils down to the implicit config.
If conflict was explicit.
Laurent Quérel 00:41:25 Yeah, with, with the with the yeah.
Liudmila Molkova 00:41:28 Problem.
Jeremy Blythe 00:41:29 I do. I must say that.
Laurent Quérel 00:41:30 Again, we have a different interpretation of the feedback of people.
You are saying that. It's about the implicit configuration file. I'm saying, it's about the implicit subdirectory. That's I mean, I can retrieve the the feedback from Martin, and I'm pretty sure of what I'm saying. It was because I remember a conversation I had with him explicitly. It was.
Liudmila Molkova 00:41:58 Yeah.
Laurent Quérel 00:41:59 Complaining about the the subdirectory. That is
not well explained and and confusing, and he was asking for dash, dash, template, directly to the the Directory containing the template plus the configuration file.
Liudmila Molkova 00:42:19 If he provided. If we, we ask to provide pass to the River Yarmo.
First, st you would never run into this problem.
Second, we would not design it in the way that there is any anything implicit.
Laurent Quérel 00:42:38 I agree, but I agree that it, it will not run into this problem. But what I'm saying the other way will not also run into the problem. And what I'm saying is in term of user experience. I don't see the difference. So when you have to select between 2 approaches that have more or less similar experience.
And and one is closer to what we have today. I think that for me the choice is
just abuse. But I think that's the the main. The main disagreement between us is about that. Just what I just explained
is about the fact that for me there is no real difference
with the the final proposal. I did what you are proposing
in terms of user experience. Then.
Liudmila Molkova 00:43:26 The key. The key difference, the key difference for me is implicitness. I think we were going to hit.
Laurent Quérel 00:43:33 There is no increase in this. In my case.
Liudmila Molkova 00:43:35 No, the the fact that the weaver Dot Yaml, should be present in this directory is implicitness. It turns config the other way around. You provide the file, the temp, the director of this templates. Why is there a config there? And why does it do 90% of the work.
Jeremy Blythe 00:43:58 Is it possible to have?
So we've we've we've got
We've got conventions, and we've got configuration.
Is it possible to keep the conventions for people who like conventions.
but to provide a way of specifying explicitly if you so wish.
So if you follow the convention, things will happen magically like they like they do now. I shouldn't say magically. Things will happen.
Laurent Quérel 00:44:26 She's a.
Jeremy Blythe 00:44:26 If I don't.
Laurent Quérel 00:44:27 To be funky.
Jeremy Blythe 00:44:28 And if we
and if you want to go no, I don't want my weaver file, my weaver file there. I'm going to provide.
I'm gonna explicitly provide a location is that, and maybe that's it.
Laurent Quérel 00:44:40 You should tell.
Liudmila Molkova 00:44:40 And we're.
Laurent Quérel 00:44:44 It's not exactly that. That's this stuff.
the override config. And that's another reason why
I don't want to choose that, because right now, so we
we are, I think, at the the right terminology. That's what you said. We are relying on a convention from the organization of this side, anyway.
And.
Liudmila Molkova 00:45:09 I don't think.
Laurent Quérel 00:45:10 And so I mean the We. We are relying on the fact that we have
template file and we also have. We respect the organization of those templates if they are into sub territories. They are also
we follow those subdirectories. There are some organization that are based on some convention right?
Liudmila Molkova 00:45:36 I don't think there should be. You should be able to use arbitrary location. I eventually arbitrary location in your config, saying, Oh, I have one template from there.
Laurent Quérel 00:45:47 But the problem is, if you if you So
one thing that I mentioned
Martin was okay. What I like to do is to use the dash, dash, template, to direct to a remote, detailed repo. That was the his main concern. In fact.
in order to do that, explain me how you will be able to direct to a config file
that will make references to something that is not, I mean, that could be if I follow what you are seeing everywhere into this repo it? I mean, it's not basic to for remote repository.
It's much easier to to get the content of a directory and every subdirectories that try to pick and choose everything that could be, even outside this directory.
because technically based on what you are saying. It's it's possible.
Liudmila Molkova 00:46:45 So.
Laurent Quérel 00:46:45 And for remote template system. I I'm not a big fan of that personally.
Liudmila Molkova 00:46:50 So if I take, let's say I don't know any config file I would normally 1st should be able to provide the absolute directory to something. The fact that we cannot is is a problem
to me. The other part is okay. You want your the URL provide the URL
it's hard to implement. But it's hard to implement, anyway.
The 3rd point, okay, if you want to take some specific location for the templates.
Well, we can have an argument templates that would, I don't know.
Get them from some specific repo, and then you can
or refer to the things inside the templates.
Otherwise we are having this.
The convention right? And the convention is nobody knows about.
And now video Call is going to read the documentation. Well, they will complain 1st and read the documentation.
Laurent Quérel 00:47:58 The the fact that we have a weaver dot channel is is a is a problem for you. I mean, if the only convention is okay. You need a weaver dot channel into a directory as templates
the presence of a weaver. The channel is, is that
The main concern that you have in terms of convention.
Do you agree that this kind of pattern exists everywhere? The fact that you have convention in many framework.
Liudmila Molkova 00:48:31 Now what I don't agree with that. It's common for cli tools
to have mixed source of configuration, and that you don't provide the explicit file risk config.
Laurent Quérel 00:48:53 What we provide is something like that if you want.
So let's say you have a remote another example.
So let's let's let's say that we have dash, dash, template, directing to a remote repository with the notation that we already have, and we already have the code to download an entire Directory only
for new people.
That's very nice, because it's self-contained.
So we we we don't have to do back and forth to to go to a remote report just because we have to read 1st the river and discover that inside we have other references that are not necessarily into the the subdirectory that we just download, which completely, which.
Liudmila Molkova 00:49:41 Oh!
Laurent Quérel 00:49:41 And that that complexifies a lot. So
that's 1 point. So 1 point is
in this specific context. Now, as a user of these remote templates.
You want to override the configuration.
What I'm proposing is, and and what is already there with the dash, dash config. But the dash dash config was like you said confusing.
So I written it. Dash, dash, override, config, to explicitly mention that if you want to override the Weaver Channel that is implicitly part of this remote template system.
You can, by using the dash, dash, override, dash, config.
So that's the.
Liudmila Molkova 00:50:28 The option
so maybe I can present, and they can make us. it's it's not the 10
pushing. It's more like, I want to show the idea that should I think, work
give me a sec, I'll open something to present.
Okay, so imagine if we did
this. So we're doing right today. We're registering generate minus minus template template something.
I don't know something for output, anyway.
and if I want to be explicit in how I provide config. I will do something like.
Laurent Quérel 00:51:23 This config is what.
Liudmila Molkova 00:51:29 This is my override.
Laurent Quérel 00:51:32 Oh, that's another one. Okay.
Liudmila Molkova 00:51:35 Okay.
Laurent Quérel 00:51:36 Which is not what I'm proposing. I'm proposing, I know.
Gosh!
Liudmila Molkova 00:51:39 I know.
Laurent Quérel 00:51:40 Right? There's no fee. Okay?
Liudmila Molkova 00:51:41 I know. I'm trying to.
Laurent Quérel 00:51:44 Because for me it's even more confusing. There.
Liudmila Molkova 00:51:47 Okay. So imagine if it was less confusing. So what we have in the river Yaml today?
Let's copy over something.
Let's see, let's look here.
So we have this.
Let's just keep a few.
Maybe we have some params.
So what if we did this
oops? Sorry what I meant?
It's just I want to demonstrate the full proposal.
Then this becomes this. You can override this with Bram, whatever.
It can be. The top level property
that can be made differently. It could be nice.
There are all the benefits, all the scenarios that you want to work.
There is single source lose.
Laurent Quérel 00:53:29 Can. Can I? Just explain why? No, because,
you are transforming a basic solution where
we have a URL targeting a list of templates
to a solution where for each individual template
the top place location. But it's it's not something that we we have right now. I mean, it's
Liudmila Molkova 00:53:55 It. It's just.
Laurent Quérel 00:53:56 Oh, okay, okay, okay. I didn't see the I. Okay. Okay. Okay.
Which
don't you think that it's more complicated? You you are. You are coming from just a basic parameter, pointing to a remote location, to something where you are forced to create
artificially, you first, st you have to enumerate all the internal
gija file that are into the the template that you are for the template directory that you are targeting. What happened if there is a modification you have to change this this weaver weaver file. Because, someone added remotely into the the list of template part of this the the weaver Yaml file that was present.
Oh, so so for me!
Liudmila Molkova 00:54:50 So we are not. I'm not about the templates at all with. The only thing I'm changing is that there are 2 ways to provide the config and templates today.
And I'm saying that the config
is the only source of truth for all the config stuff.
It's actually a config.
Laurent Quérel 00:55:14 I understand, but what I'm seeing is.
Liudmila Molkova 00:55:16 The config, but you can override it still.
Laurent Quérel 00:55:21 Cool.
Let let. So let's take this example. But with something more.
with the big, very complex picture.
we have 1 1 person responsible for, for example, creating templates for Java, a client SDK for Java
this person is in his own world, creating templates and doing that into a Github Repo right.
And now the another, another person wants to
to create, to to use these remote templates.
and we know that maybe the the repository will be updated, some ginger file will be updated. So, in fact, the list of templates will evolve over the time
and what you are saying. If I understand. Well, your proposal is
the the person that want to import, that
we'll do what? What will be the, the the exact, but the
the exact user experience for the person that is using this work that someone else did regarding the the code generation for Java.
I guess not what we have on the screen, right.
Liudmila Molkova 00:56:35 So I would imagine that the somebody who did call generation for Java actually
owns both the templates and weaver Yaml. In the most cases.
Laurent Quérel 00:56:45 Yeah, definitely.
Liudmila Molkova 00:56:48 So then they they write this Webraham, and you run it.
It can be.
Laurent Quérel 00:56:53 Why?
Okay? But why you have this URL. In that case,
and and this complication in the pattern where you have this variable? Because for for this person
the the that doesn't exist. Yeah, already have locally the the attributes, the underscore in me.md. Dot g.
Liudmila Molkova 00:57:15 Fine. If if it's not defined, you just use to to just what what you have in there.
Laurent Quérel 00:57:22 Yeah, I found it so
perfect. And then for the for the user that is now not this author of the Java stuff. What this user will do on on his side.
Liudmila Molkova 00:57:38 You are leading to that, that it should be a remote location for the weaver gamble.
Laurent Quérel 00:57:44 So you will. Okay, okay, so what is the fundamental difference between dash, dash, template, and the remote repo
and the dash, dash config, and the the weaver email that is inside this paper.
Knowing that if we go in this direction nothing prevalent to have to have this, I mean.
Liudmila Molkova 00:58:08 The, the explicit.
Laurent Quérel 00:58:09 This is different.
Yeah. But
is it possible to? Yeah. But is it possible to have this weaver not present into the location where the templates are. If that's the case.
Liudmila Molkova 00:58:22 Good.
Laurent Quérel 00:58:23 Yeah, but that's where one of my concern is, because then it's
it's it's adding even more complication. Which are, in my opinion, not.
Web, version.
Liudmila Molkova 00:58:42 To whom?
Laurent Quérel 00:58:43 Justified to me. For example, think.
Liudmila Molkova 00:58:47 The user or the to the somebody who writes weaver code.
Laurent Quérel 00:58:52 Somebody to write the code because for me, my, my.
I understand. For me I don't see to be honest. The the difference! Dash, dash, template, and and saying that we have a convention with inside. I don't see a so big difference that justify all this effort.
Liudmila Molkova 00:59:15 Yeah, I still don't get the effort part. I think we need to figure out how to make progress. My, the reason I'm arguing is because I'm arguing against the idea of implicitness until you do something like favor. Register generate Java.
So this I love.
Laurent Quérel 00:59:40 Okay, so that's we agree with that.
Liudmila Molkova 00:59:42 Yeah.
This as the almost mo, the most, the common scenarios the common scenario.
This I this is a big deal for me.
So I.
Laurent Quérel 01:00:00 That that, to be honest, it looks for me like a very I mean.
Liudmila Molkova 01:00:08 Yeah, these are templates.
These are templates. The weaver. Yaml is not the template, it's not the template, it's a config.
Laurent Quérel 01:00:22 Yeah, you will have a very hard time to convince me on that, to be honest. But I will be very frank. Except if I saw multiple person saying, Oh, it's so much, so, so big deal. Then. Okay, I I will do it. But if I have only one person that complaining on that so much.
and where I don't see the the real, the real. I will not do this work definitely, not
oh.
Liudmila Molkova 01:00:51 It. It makes me sad. That I'm I think the first.st
Laurent Quérel 01:00:56 Because the career session main adopter
was not going into this direction.
Liudmila Molkova 01:01:02 And and read the feedback. That's.
Laurent Quérel 01:01:05 You okay?
You know. I mean.
Liudmila Molkova 01:01:06 I I need to leave. I I am already 2 min late for my other meeting.
Do your thing. You're the Maintainer. You decide. I also hear your like that. You, my! My feedback, is not valuable, that that's the hard thing I I should take.
Laurent Quérel 01:01:24 Oh, no, no, no, that's not. I'm saying. I'm saying that when when there is a disagreement, why, one will be better than the other one you are. I'm saying that I will not change something existing
just because you disagree with it. I like to have another
feedback going in the same direction, at least
because what you are saying, your your opinion is more important than mine. That's how I see it right now, and you are seeing the opposite. I disagree with that, because the many films is we have something already there
with the dash dash templates, and you want to move from there to some different places just because of your personal preference. What I'm saying. I'm not saying that I I don't take into account your
your opinion. I'm taking it into account. I don't want to change something that already exists to something else.
just because of one opinion.
Liudmila Molkova 01:02:29 Yeah. So I I understand. I don't want to. My opinion to be the the more important than yours. I don't think that I think I have some basis behind my my opinion, which is that it's the typical pattern we by by improving user experience, we agree that we need to make it easier to use. Yet when we try to think about how to make it easier to use.
we put the breaking change and the amount of effort higher than the user experience. See? So we, we have a goal to make it easy. But we are not going to.
Laurent Quérel 01:03:03 Yeah, just, I'll let you go. But
you you we are on an open source project. Okay? We all have other works to do. You can't put aside
the fact that if there is no such difference into 2 alternatives, if there is more work to do and more implication in one of these alternatives you have to take that into account. To be honest.
Liudmila Molkova 01:03:30 Yeah.
Laurent Quérel 01:03:30 About the breaking change that also exists in your alternative.
So that's why I don't want to make this change.
because this values consideration and I can't accept that. You put that on the side, because you consider that in an ideal world we just need to take into account what you consider the
the best results, you know. So.
Liudmila Molkova 01:03:52 We've started it as the ease of use. The ease of use means.
Laurent Quérel 01:03:57 Yeah, but it's super easy to use in that that way.
The with the dash, dash, template. I don't think it's it's more complicated.
In fact.
Liudmila Molkova 01:04:06 Okay, you're the Maintainer. You have the ultimate decision. I'm glad we talked. I I'm sorry about the
if I give you any hard feelings. I it wasn't my attention. I appreciate working with you.
Laurent Quérel 01:04:20 Yeah, I know.
Yeah, I know that it's a. It's a. It's a complicated topic for for both of us. We have strong opinion on that, and I don't want to. I agree so what I will do I will add an additional.
Oh, you can add additional, and I will add additional feedback
from other people. To determine if it's so fundamental to have this dash dash, config stuff.
Liudmila Molkova 01:04:58 Let's just do your thing and hear to what people say. Let's not specifically poke people around it. It's not the the point.
Laurent Quérel 01:05:08 Okay.
Liudmila Molkova 01:05:11 Cool. Thank you. Have a good day.
Laurent Quérel 01:05:13 Sorry for this discussion. That is, it's twice one.
Liudmila Molkova 01:05:17 Yeah, yeah, I'm I'm I appreciate the we've done it.
Laurent Quérel 01:05:23 Okay. Great.
Liudmila Molkova 01:05:23 Thanks.
Laurent Quérel 01:05:24 Thank you. Have a good day.
Liudmila Molkova 01:05:25 Bye.
