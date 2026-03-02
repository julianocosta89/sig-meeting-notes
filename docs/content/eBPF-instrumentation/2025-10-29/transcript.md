SIG: eBPF instrumentation
Date: 2025-10-29
Duration: 22 minutes
Zoom Recording URL: https://zoom.us/rec/share/P0JJgY4sNxSY1SfIYwkSwov_f-YMCjFJp3QVoU56Yu1mdEGHMYNoiRJR75KjwEA6.u8T7QC2_okZU9Iz8
============================================================

## Zoom Recording Transcript

**Tyler** 01:21 Hey.
**Mario Macias** 01:23 Hello?
**Florian Lehner** 01:25 Okay.
**Tyler** 01:25 How's it going?
**Mario Macias** 01:27 Pretty good, and you.
**Tyler** 01:29 Good, good.
Raphael, good to see you.
**Rafael Roquetto** 01:35 Yeah, good to see you too.
I'll be away next week again, and the week after, but so far, good to see you.
**Tyler** 01:44 Does that mean you're not joining at, KubeCon?
**Rafael Roquetto** 01:47 Yeah, I'm not joining KingCon, no.
**Tyler** 01:51 Are you… are you thinking of going to the Europe one?
**Rafael Roquetto** 01:54 I haven't thought of it, but yes, maybe? That would be cool, yeah? .
**Tyler** 01:58 Yeah.
**Rafael Roquetto** 02:01 What is it again?
**Tyler** 02:02 I think it's, like, sometime in March? It's in Amsterdam.
**Mario Macias** 02:07 Yeah, in March.
**Tyler** 02:09 Yeah.
**Rafael Roquetto** 02:10 Okay, gotta see. My brother's getting married in March, so we'll see.
Maybe I'll go to KubeCon.
**Mario Macias** 02:18 There's another in Asia in June.
But I've never been… I wish to.
**Tyler** 02:26 Yeah, that flight has to be pretty, pretty long.
Hmm.
Yeah.
Be cool, though.
Well, cool, it looks like we have quite a few people here, so maybe we can just, jump off in just a little bit. If you haven't yet, please go ahead and add your name to the attendees list.
If you have agenda items you want to talk about, please go ahead and add them there as well. It's, pretty light so far, but we can…
We can jump in here.
Cool. Alright, so, to start us off, that's kind of, like, the main point that I want to talk about as well, is this releasing the 1.0, the milestone that's left, and so…
We talked about this last week, the only outstanding issue is from Mario, you've been working on a lot of refactoring. I've seen a lot of refactoring happening this week, and last week, so I'm wondering where we are at on this milestone here.
**Mario Macias** 03:26 I think there's nothing else to do.
We reduced as much as we could.
Yeah.
**Stephen Lang** 03:43 Tyler, I added the test package to PKG.
**Tyler** 03:48 Okay.
**Stephen Lang** 03:49 So, I guess new public API, I don't know if that… Affects this or not.
**Tyler** 03:57 Yeah, it would. So,
Sorry, you added a test package to… here?
**Stephen Lang** 04:07 Yeah, so this is based off of last week, so if you go to Test…
**Tyler** 04:13 Integration right here?
**Stephen Lang** 04:14 Yeah.
So this is the shared testing library we spoke about last week.
**Mario Macias** 04:20 Yeah, then it's fine if it's public, right? It should be public, I guess, or…
**Tyler** 04:27 Yeah, exactly, that's kind of the intention. Yeah, no, there's nothing wrong with that, yeah, that sounds… that sounds good.
**Stephen Lang** 04:32 Cool.
**Tyler** 04:32 It's.
**Stephen Lang** 04:33 Because it's new compared to whenever the report was run on the issue you were looking at.
**Tyler** 04:39 Oh, oh, I gotcha. Yeah, no, that's fine.
This is still here, huh?
Did… did we look at moving this, or was there a reason…
We ended up not moving this.
This is, huh.
Does this have any Go code? Yeah, okay.
**Stephen Lang** 05:10 Mario, I don't think this has been moved, has it? This is just where it's always been?
**Mario Macias** 05:15 Which one? Which… this…
**Stephen Lang** 05:17 Top, top-level test directory?
**Mario Macias** 05:20 Oh, I don't remember.
Yes, the top-level test is just for… for… yes, it's… it's always been there, yeah. Yeah, it's always been there.
**Tyler** 05:36 Yeah, I thought we… In here, there was a talk to move it into internal.
It's unused by the OB.
**Mario Macias** 05:47 Test package.
Okay, is it publicly visible? Okay, okay, let's move it to.
**Tyler** 05:54 Yeah.
**Mario Macias** 05:54 Okay, I will… I will move it then and see.
I think we need to fix some… some paths, some paths in the… some relative paths in the internal Docker files.
But, yeah, okay, okay.
**Tyler** 06:13 Yeah, so the only thing that was… was used from there was this, externally, was this collector, and we had talked about just duplicating that process upstream.
**Mario Macias** 06:23 Okay.
**Tyler** 06:25 Do you think that's possible.
**Mario Macias** 06:28 Yes, yes.
**Tyler** 06:29 Okay.
Yeah, I think if we can move this test package internal, then I think this should be done.
Cause otherwise there's nothing used there. That was kind of, like, the big one that, like, there's just… all of… all of these packages were not used.
And so moving those internal was kind of the goal.
Okay, well, let's plan on doing that.
**Mario Macias** 06:52 Okay.
**Tyler** 07:09 Okay, I think with that, though, once that PR is merged, the…
the milestone should be… it's done, so I think we're ready to make a published release for the,
0.1, so hopefully… I'm guessing, Mario, is that something you can look at today?
**Mario Macias** 07:28 Yes, yes, yes, right after, right after this, I'll move it, yeah, hopefully.
**Tyler** 07:34 Yeah.
No, no worries, yeah, that sounds good. I just want to make sure we're all clear on timeline, so if that's good, then I think we can start working on the, release, after that, so today or tomorrow, we can probably get that out.
**Aviad Hahami** 07:46 Amigos.
**Tyler** 07:46 And then…
Someone's microphone is unmuted, I don't know who it is. But yeah, so I think once that's done, we can…
then work on the Helm chart after that. So yeah, this is… I'm super excited. I think we're… I think we're right in time.
And then with that, we should be ready for KubeCon.
In 2 weeks. So, yeah.
Yeah, that's… that's exciting. There's also the blog post.
That I think has been started.
So yeah, we could work on that as well. So yeah, there's a lot happening in the next two weeks, so yeah, this is all clicking it off.
Well, cool. That sounds like a great plan to me. Any other comments on this?
**Mario Macias** 08:32 Not from my side.
**Tyler** 08:33 Okay, cool.
Okay, cool, then I think the only other thing left is to talk about any open PRs. I did see a few, so we can go through these.
Cool. So, looking at new ones, there's,
There's an update PR here, I think this is something we talked about last time. Oh yeah, this is just the tempo one. This just needs some… some eyes on it. The CI was failing for some…
weird reason. But, yeah, we talked about that last time, so let's talk about,
DNS tracing, this is something that I think was pretty cool. Nicholas has been showing me this, offline, so I think this is a pretty awesome feature.
It has, reviews on it, so, looks like, Mattia, you've asked for some changes, and Nicola looks like he's come back, and yeah, there's some, some great suggestions,
So, I think… this is just looking for iteration. There's definitely some feedback, I think,
to the feedback, but there's also feedback that Nichol's looking to incorporate. It's pretty, recent, this comment, so yeah, still a work in progress here. I didn't see Nickel on yet.
**Mattia Meleleo** 09:45 minor stuff, but I think Nicola is in it already.
**Tyler** 09:49 Yeah, right, exactly. So, yeah, this doesn't look, like, too,
consequential, like, I think it… I think the overall design, is solid, it's just the implementation we gotta clean up. So, yeah.
But yeah, otherwise, I don't know, if you haven't taken a look at this, please take a look, it's pretty, pretty, snazzy, and it's gonna be pretty helpful.
Collector contributor image, I thought I took a look at this as well,
I thought this was actually passing, for a second.
Not even close. I'm guessing this actually probably has something to do with the same reason that the, Grafana Tempo…
Docker image upgrade is failing, so there's probably something related here that we probably need to take a look.
**Mario Macias** 10:35 Yeah.
**Tyler** 10:35 So, yeah.
okay.
It just takes some eyes. I haven't got around to it. If others can take a look, that'd be great too.
Although, last time I did take a look at the tempo on it was pretty, obscure, but…
Okay, and then the last one is this improve this, gibberish detection?
Nikola has definitely found that there's been some issues with, I think, route,
Route processing? It's not technical. Sorry. Generated.
Yeah, and so I think he's taking a look at trying to fix this. This is an interesting one. I was kind of hoping Nicola was on to talk about this,
Double checking he's not here. Yeah, so I don't know…
Oh, you know, yeah, so the thing is, is that…
**Mario Macias** 11:25 Yeah, this comes from an issue we have. We found
That there… there are some… some… users, setting,
As identifier, for example, the, the product name.
And then it's not detected as… as giverish, because, for example, this example, bar attached, generic product, whatever, so this… this has a very high cardinality, but it's not detected as giverish, so the cardinality grows a lot.
So, what Nikola did is try to identify in… in… in this long…
products, some parts that could be identified as giver is. So, if a subset of this path is detected as giver is, then the whole path… so the whole folder of the path is…
is… is marked as giver is.
**Tyler** 12:30 So, yeah, can I just… maybe I can ask you then, just a naive question.
but it's not doing the detection based on the fact that there's a hyphen, or an underscore or something like that. There's gotta be more, right? Because, like, if there's a hyphen or an underscore in the path, like, that shouldn't be replaced, right?
**Mario Macias** 12:49 No, what it does is it splits this… the complete sentence.
and then looks, by… between the hyphens, or the underscores. In that case, it will look word by word, it will look for bar, attack, generic, product, then in this, AP, J, K, whatever, it will detect the gibberish there, and then will mark everything as gibberish.
**Tyler** 13:14 Oh, okay, alright, I think I see what you're saying then. Yeah, that makes sense. And then, yeah, so then this whole thing, gets… collapsed into this star, so that, that makes sense. Yes, exactly.
Cool. Yeah, awesome. Awesome. Alright.
**Stephen Lang** 13:26 There's a unit test example if you want to see.
**Tyler** 13:30 Thanks, that would be helpful, maybe, to understand it.
**Stephen Lang** 13:37 Yeah, the cluster test.
So there's the new ones around line 56 to 59.
So the, the output is… is first?
And then the input is on the, on the right.
So it's kind of showing that the whole thing gets collapsed.
**Tyler** 13:54 Yeah, but it also handles things like this, where…
like, TestPlus has not collapsed, right? Like, that was kind of my… my concern.
**Stephen Lang** 14:01 Yep.
**Tyler** 14:04 This… Looks like… yeah, okay.
Yeah, okay, cool. Yeah, thanks for pointing that out.
Yeah, it looks like it has the… their reviews. I did see… so there's this comment, but then I think…
Steven also had one other note here.
**Stephen Lang** 14:25 Yes.
**Tyler** 14:26 It could probably get cleaned up, is what you're saying, right?
**Stephen Lang** 14:28 Yeah, it's… I mean, it works fine with it, it's just a duplicate code, so it's…
**Tyler** 14:34 Yeah.
**Stephen Lang** 14:35 I can go.
**Tyler** 14:36 Well, cool. Alright, then I think that's a… that's a quick cleanup. We'll wait on that cleanup before we, merge this, because otherwise it looks like it's ready to go.
But, yeah.
Okay, cool. And then, outside of that, Nimrod, you had this protocol support, it's still draft. Did we want to talk about it, or are you still working on this one?
**Nimrod Avni** 14:58 I am still working on it, but I would love to, like, talk about it a bit. Also open, an issue, which I think mentions another issue from the, someone opened on, like, the auto, repository. It's basically…
both for, like, internal and external use, I think it would be good to have, like, some kind of support… I don't know if it's gonna be a support matrix, or some, like, clear docu… like, internal documentation of…
I said… I listed it, like, in our… the protocols that we support, but it can be other features, like, I don't know, like, context propagation and spend metrics, service graph connector metrics, all that stuff. Basically, have some sort of way to list
the stuff that we support with the limitations of, like, for example, in each protocol, I did something in the draft that, like, from my, like, the way I remember the code or whatever.
lists all the protocols that we support and their limitations. And I think it would be good if people want to have a look, add stuff, maybe think other stuff that we might be able to document.
And also, I thought, like, having… adding some sort of, like, PR template to make sure, like, to remind us to update this thing, like, continuously as we continue developing.
And by the way, like, if this, like, format of a table doesn't completely fit, or, like, needs other columns or whatever.
I'm, like, open for, suggestions, and, and, like, adding more information that I don't know.
I think that's, like, the main gist of what I did.
**Tyler** 16:39 Yeah, this looks great.
**Mario Macias** 16:41 Yeah.
**Tyler** 16:43 Yeah, I, I mean, I… I don't…
I don't know if there's a better format, but I think that even if there is, this is a great way to start. So, yeah, I think this is worth just…
Appro- yeah, this looks great.
**Nimrod Avni** 16:57 Yeah, so if anyone, if the… if you can, like, if anyone thinks I missed something, or, like, some edge cases, like, I thought also, like, describing, the current limitations we have with context propagation is, like, you know, the kernel, like, a kernel version limitation, the cgroup thing limitations.
And yeah, all the stuff here that have, like, some supports only in Go, some supports only non-Go, so, like, it's more for, like, for us to know and to be able to communicate it with, like, people who use this.
**Tyler** 17:33 Yeah, I think that maybe the only suggestion I have is, like, this is good, but I think that it also probably needs to exist on, like, the OpenTelemetry.io, website, just for end users, right? Because that's where they're going to be looking at the docs.
**Nimrod Avni** 17:45 Yeah, definitely. I think that can be, like…
I think it… I don't know if it can be, like, automatically updated there, or…
we can do some, like, you know, whenever people update the docs, they can, like, refer to here. But I, like, I think this is really good for us, like, to kind of maintain and make sure we also update it as we develop, especially, like, now we added a bunch of different.
protocols like, like, OpenSearch and S3 and, like, all that stuff, and I think it's good to have it, like, documented somewhere and, like, make sure we remember to document it.
**Tyler** 18:18 Yeah, the syncing thing was tried in a few different places before for the docs team, and they…
moved away from it, they don't… they don't like doing that anymore.
I think, ultimately, this should probably live on the OpenTelemetry.io, but I think
For now, we could probably just start curating it here, like you're saying, and maybe, like you're saying, also build out maybe more policies around…
you know, I think maybe, like, a good time… what we do at a lot of other repos is we have, like, a release checklist, and in that release checklist, you have, you know, like, update docs or something like that, and that is to just verify that, like, you've updated any new features, you've updated
versionings is usually what it is for us in other projects, so, yeah, I think that that's something we could live with, but I think…
For this, I would probably say we could just start here.
And then if we wanted to move it at a later point, like, that's something we could do as well.
**Nimrod Avni** 19:11 Okay.
**Tyler** 19:12 Is there a reason this is still, in draft form?
**Nimrod Avni** 19:16 It can be a PR, I just thought that, mainly I wanted to get your feedback on, like, both the format, and if I am missing anything. And also if we want to kind of…
want to document stuff that, like, other stuff that are not, like, protocols, stuff like, you know, like, like I said, like, context propagation and other features that we have.
But we can open it as PR and have people comment already.
**Tyler** 19:45 Yeah, I think that's a great way to go. I think it's ready. I think you're right, we could add more sections. There's definitely some more sections I think we could add, but I think this is a great place to start, at least. So, yeah, I think it's… I'm ready to review this. This looks great, yeah.
**Nimrod Avni** 19:57 I'll move it to, to, PR.
**Tyler** 20:02 Cool. Anybody else on the call have feedback on this one? Things that are missing, that are obvious to them?
**Mario Macias** 20:11 Well, cool.
**Tyler** 20:15 I think Mario's still reviewing it, so… maybe, maybe expect some comments. Yeah.
Okay, cool. Alright, that's the end of the pull request. Going back to the agenda, there's nothing else here, so I can stop sharing my screen.
Any other topics people wanted to discuss? Talk about? Maybe issues they've opened? Things they're working on, locally?
**Mario Macias** 20:48 Hmm.
**Tyler** 20:50 Mario, last week, I think we talked, you had, given an interview, right?
Did that ever get published, or is that still coming out?
**Mario Macias** 20:57 Yes, I think I shared in the… unless I forget it… yeah, in the hotel EVPF instrumentation, there is the link.
**Tyler** 21:08 Oh, cool. Awesome.
**Mario Macias** 21:10 Yeah.
**Tyler** 21:11 I'm gonna have to go check it out after this, then.
Yeah, it looks like I missed that. Okay.
Well, cool, yeah, so if anybody also missed that, please, yeah, go take a look, it's in the Slack channel. Mario's, full, full hour, I think is what you said, right? And, talking about EVPF, yeah.
**Mario Macias** 21:29 Yeah, full hour.
**Tyler** 21:31 And, if you're super popular on social media, if you want to share it for us, that'd be great. We'd love to get more, visibility into this. So, yeah.
Cool.
Well, I think if that's the case, we could probably end it here.
Thanks everyone for joining. We'll see you all in a week's time. If you have some time, please take a look at those PRs. Otherwise, yeah, good to see you. I'll talk to you later. Bye.
**Stephen Lang** 21:59 Right.
**Mario Macias** 22:00 Bye-bye.
**Giuseppe Ognibene | Coralogix** 22:00 Bye, buddy.
