SIG: OpenTelemetry C/C++ SIG
Date: 2025-09-08
Duration: 40 minutes
============================================================

## Zoom Recording Transcript

**Tom Tan** 02:28 Hi, Mark.
**malff** 02:30 Hi, Tom.
**Tom Tan** 02:32 Good evening.
**malff** 02:35 Yeah, good, good afternoon, I guess.
**Tom Tan** 02:38 Yep.
Lalit is joining the meeting.
**malff** 03:10 Okay.
**Tom Tan** 04:16 I love it.
**malff** 04:19 Hi, Lalit.
**Lalit Kumar Bhasin** 04:22 Yeah, hi. Hi, Mark.
Boom.
**malff** 04:39 Okay, I don't have a lot of things for the agenda today. The only thing I noticed was, A new issue… About VAT… Which I would like to discuss if, if you have time.
Otherwise I don't have any specific topics. Do you have any… anything in particular you want to discuss?
**Tom Tan** 05:05 So do we have a new issue tracking already, or… Still…
**malff** 05:12 For the new reason, we don't have an issue yet, I can create one.
**Tom Tan** 05:18 Okay.
Yeah, I think I want to include the PR I'm picking up to the new release.
**malff** 05:34 Okay.
So, let me make a note of that.
Okay, so on this thing, So, there seems to be a general question in the specs, which is affecting every, every language.
Which is to decide whether it's okay or not to add new attributes.
I don't know the full extent of that, But I think for C++, That would be a breaking change, because of the way we have an attributes class with all the variants of things that we can store in an attribute today.
So, if we can do that, but if we do that, it will be an EBI change.
So we'll have to be, to do that only in ABIV2 then.
So it's, technically possible, but we need to be only… In the next API, because it's a breaking change.
And the next part to that is, I don't quite get the full extent of the change, but I think it might also involve some changes in the OpenTelemetry portal.
messages, so that will, in my understanding, also affect the OTLP protocol.
I don't know if you had time to look at it, or if you have any… comments on that. I just found that today. It's very recent.
**Lalit Kumar Bhasin** 07:34 Yeah, I think, I agree with you. I mean, this is a breaking change from EVI perspective at the API level, so… And, you know, it will need the changes in… OTLP also. The Proto also, Protob also, I mean, OTLP.
**malff** 07:49 Okay.
Are you looking at doing the same thing in Rust, or…
**Lalit Kumar Bhasin** 07:58 No, I think we have to… we have to look into that.
There are also similar changes would be required, but… Haven't started discussing yet.
**malff** 08:08 Okay.
So, I'm assuming that we can do it, but first with OTLP changes in the proto… Which, opened the imagery prototy first.
And then, if we send new type of attributes, I'm expecting also that the OpenTeametry collector will need to be upgraded at some point to To speak the new OTLP flavor.
So… It's, I don't know the technical change itself for the new type of attributes, but it will most likely take some coordination to have all the different bits and pieces in a line so that everything works together.
**Lalit Kumar Bhasin** 08:57 I mean, it's going to be a bit… bit… Complicated in the sense that we don't have any type Like, right now, I think the change is basically to adding the heterogeneous types in the list.
And that's something going to be a bit complicated in C++.
Right now, we only support, A list of string, list of integer.
**malff** 09:21 Yeah. But now it's… Yeah, we have all the basic types and the span of them, I think.
**Lalit Kumar Bhasin** 09:26 Miram this one.
But yeah, I think, yeah.
So… but yeah, doable, very breaking change, so yeah.
**malff** 09:35 Okay.
Okay, so, if it's okay with you, I will reply to that issue with explaining the details.
Basically, the summary is that, yes, we can do it, but it will be only in a new API.
**Lalit Kumar Bhasin** 09:50 Yep.
**malff** 10:26 Bum.
Anything else you want to discuss in particular, also? Let's see…
**Lalit Kumar Bhasin** 10:36 Not for my site.
**Tom Tan** 10:38 Oh, my son.
**malff** 10:39 One thing I noticed, so Nikhil made some changes recently to the resource detectors.
And a part of that discussion was to have some scrubbing, so that we don't expose everything which is in the process command line, which makes sense.
So I saw that, There is a new issue, and it most likely will be working on a new BR for For that part specifically, so… That looks okay, I guess, it's making some progress.
And… Well, we can go to the usual with issues and pull requests, but just so you know… I've… I'm finally, ready to move to the very last parts of the file configuration.
And one part in particular, which is now ready, is all the BazelMake files.
Oh… So, there is… Apart from the PR, which is to be reviewed, everything which is left is basically Bazel and CMake all over the place.
plus a couple of files, but it's getting there. The next major thing would be Or we make files with Bezel and CMake?
Okay. Just so you know.
**Lalit Kumar Bhasin** 12:08 Thanks.
**malff** 12:13 Want to over the issues quickly, then?
So that we just discussed, so this one, it's the next step for, resource detectors.
**Lalit Kumar Bhasin** 12:31 Yep.
**malff** 12:42 So, we need to see exactly the syntax, but yeah, I'm assuming that there would be a way to specify that some… Some parameters are to be ignored, typically when we have a password or a key or whatever.
So that's, that makes sense.
This one, it was from last week. I don't exactly know the… know all the details. The initial complaint was that somehow we changed behavior between two releases.
Due to the changes in Makefile.
But, later, I think… maybe it was Owens, yeah, he commented that it could also be because, the way gRPC was installed was either only built with shared libraries, or only built with statics, or both, and that would have some impact also on the… on the way things are built. So, not sure what the… What the result of that is, yet.
**Lalit Kumar Bhasin** 14:00 I think Ovent suggests that we should keep the existing functionality, but to add a warning, right?
**malff** 14:07 Yeah, it looks like it.
**Lalit Kumar Bhasin** 14:08 Hmm.
**Tom Tan** 14:11 Probably wait for the… User's confirmation.
**malff** 14:21 So, basically, having the make file more explicit about if it finds something which is not expected.
Say exactly what's… what's going on.
So, I guess, yeah, we can accept it.
**Tom Tan** 14:35 Yeah.
**malff** 14:42 I think Laditu had a comment a long time ago about that, pointing to, unit tests.
Yes.
**Lalit Kumar Bhasin** 14:54 Oh, boots.
with the GCC version, which does not support regex.
**malff** 15:03 Yeah, but, I mean…
**Lalit Kumar Bhasin** 15:05 Yeah, I'm not sure if we should support that older version, or… we can do that, I mean, we can ask him if we want to really add the support, we can… Definitely.
**malff** 15:16 Quite frankly, I don't see the point. I mean, there is no way we can… Check that in CI.
Because we'll have to build that version itself, and… I'm… That seems to be pretty old.
**Lalit Kumar Bhasin** 15:31 Hmm.
It's wonderful.
**malff** 15:48 So… My question is, I mean, either this is going in production somewhere, and why on earth would be… Would someone take that in production today?
Or, I mean, why is it that they cannot upgrade to, A component of that works.
**Lalit Kumar Bhasin** 16:10 Yeah, I mean…
**malff** 16:11 So… Unless there's a really, really… compelling reason to actually support that. I don't see how we can.
**Lalit Kumar Bhasin** 16:22 Yeah, fine.
do we mention in our, in our, README, I mean, what all GCC version? We don't really mention anything, right?
the supported.
**malff** 16:39 Supported versions? I don't… I don't remember.
**Tom Tan** 16:46 I think we specified the language version, not in the… I know.
**Lalit Kumar Bhasin** 16:51 You can give headphones.
Oh, that's a CI pipeline, so… but we don't really…
**Tom Tan** 16:56 Minimal version, something like this.
**malff** 16:59 And, and even Vought, I mean, Vat… the day Ubuntu is upgraded, this will change as well. It will go to something more recent.
**Tom Tan** 17:09 But we require C++ 14, right? Is that Russian support C++14?
**Lalit Kumar Bhasin** 17:14 Supporting? It supports you.
**malff** 17:16 Yes.
**Lalit Kumar Bhasin** 17:16 I was checking that it supports…
**Tom Tan** 17:18 Oh, okay.
**malff** 17:29 Because realistically, I mean, if a compiler doesn't support regex, it will mean… to implement some custom regex code as a workaround for that.
Only for that version.
**Lalit Kumar Bhasin** 17:47 I mean, the only thing is that, as of now, we do have support for compiler which does not support regex. Either we should remove that, or probably we should allow him to add, if he wants to add.
**malff** 18:01 So you mean removing that workaround, then?
**Lalit Kumar Bhasin** 18:03 Yeah, this one… I had a conditional macro for this, and… Are more of a string comparison kind of…
**malff** 18:14 Yeah.
Oh, by the way, one thing, though, I… I didn't get why… Instagram as kneedrug expert. I didn't get that.
**Lalit Kumar Bhasin** 18:28 Sorry?
**malff** 18:30 So, why is it that the histogram code depends on regexp?
**Lalit Kumar Bhasin** 18:35 It's, that's a good point. I think it's not just specific to histogram, it's basically for, For views. I think in views we use it, so…
**malff** 18:49 Or in views, like, to find instrument by name, or something like that?
**Lalit Kumar Bhasin** 18:52 Probably the custom… with the custom buckets, I think somehow that's coming into the picture.
**malff** 18:57 Okay.
**Lalit Kumar Bhasin** 18:57 Because we have to set it using views.
But, yeah, ugh.
Yeah, so he has to specify, I think.
custom buckets with a given view… with a given view conditions, and yeah, so I think it probably… it will come into the picture, because for view comparison, we use regex.
**malff** 19:28 Like, if you specify a star for to mean all instrument, or things like that.
Yeah, okay.
And likewise, I mean.
value's pretty old, too. I mean, we have fixed plenty of bugs since then. It's very surprising to me to see people Using old versions of that.
I mean… if it was packaged on a platform, then, okay, this is whatever goes with the platform, but it's not the case. People have to take the code exclusively and build it themselves today, so… It's, it's interesting to, to, to see why they keep all versions on instead of, Making something more recent.
**Lalit Kumar Bhasin** 20:23 would be that, they are still on C++11, and I think they just want to stick with the version which probably was C++11. I don't know.
**malff** 20:31 Yeah, could be, yeah, it could be part of it.
Okay, so… to clarify and investigate, I guess, but it's, it's unlikely we will support that version of GCC just for, I guess.
realistically.
**Lalit Kumar Bhasin** 20:55 then probably we can mention that, I think.
we won't be supporting this GCC version, or at least, at least we need a GCC version with the GX support.
**malff** 21:03 Nice.
**Lalit Kumar Bhasin** 21:04 To use it.
**malff** 21:06 So maybe there is a warning when this is… When we don't have that.
**Lalit Kumar Bhasin** 21:11 Yeah, there was a time when we supported it, and probably we didn't really… Ideally, we should be removing it. In that case, all these…
**malff** 21:19 Yeah.
Okay, I will probably follow Nishu, then, too.
Deprecate this and remove it in the long term.
And just to enforce that we… we use a platform with, working regular expression, VIN.
**Lalit Kumar Bhasin** 21:41 Yeah.
**malff** 21:42 Okay.
We take it because we need to clarify it and reply to that.
And this one, which was from 2 weeks ago.
So, this guy is actually filing the same issue on every single repo.
We basically have an… Slightly different way to export things, with regard to sampling.
So, the change itself looks, looks easy to do. The part that worries me is that, let's see… Well, basically, I've seen the same issue filed on every different repo to do that, but what is missing, in my opinion, is to update the specs to say in the spec that we should do that.
Otherwise, we end up with the same… exactly the same feature in all the repo, and yet not introspect, which is somewhat weird.
Oh, that's fine.
**Lalit Kumar Bhasin** 24:23 Go through the specs, or not right now?
Alright.
**malff** 24:29 Let's see… No, this was something which I added.
**Lalit Kumar Bhasin** 24:32 Google Playbook.
**malff** 24:39 Management… I don't remember how I felt that, but… It was… Maybe you should look at the stagnant sense.
Okay, I can't seem to find it now, but… Once I have that, I will add it to, in comments.
**Lalit Kumar Bhasin** 25:31 Okay.
**malff** 25:31 I don't think there is a PR for that, it was only an issue if I… If I remember all.
Yeah, the question is to have a PR.
**Lalit Kumar Bhasin** 25:42 Yeah, I think we should… then we should not add it if it's not in these specs.
**malff** 25:46 Yes.
And the minimum, just to have the same parameter name in the configuration file.
That's what we agree on each.
Where did I find that?
**Lalit Kumar Bhasin** 26:12 What's the, sorry, the first issue, issue 4990, is it?
Is it Java? Okay, it's a JavaScript, okay, yeah, click it.
**malff** 26:23 Did I have this one?
**Lalit Kumar Bhasin** 26:25 Yeah, that's on the…
**malff** 26:26 It could be.
**Lalit Kumar Bhasin** 26:34 Oh, there's a pixels also, yeah.
Understood.
**malff** 26:45 Okay, here we go. This is the one with… with plenty of… Maybe not.
Okay, well, I will find the details, but From my understanding, right, is to just slightly change the logic around sampling to decide what we export and when.
And the shoe itself, I mean, the… Very quickly made sense. The only question is to have a respect for that.
**Lalit Kumar Bhasin** 27:19 Nope.
Yeah, I think you can reply to that. I mean, I just created… I mean, I was testing Copilot, so I just created in PR for that, not to include it, but just to test if Copilot works fine after that AZC Olympics or not.
So…
**malff** 27:41 Is it this one, or…
**Lalit Kumar Bhasin** 27:43 Yeah, I was just checking EZCLD whether it works fine or not. Oh, it was working fine, yeah, and that's…
**malff** 27:48 Okay.
**Lalit Kumar Bhasin** 27:54 But we found another issue with our existing codebase while doing this.
But yeah, that's… that can be done separately, not… not a…
**malff** 28:08 Okay, well, to discuss, I think we can do it, and we should do it, just a matter of process.
**Lalit Kumar Bhasin** 28:13 Hmm.
**malff** 28:56 So, I think this is it for, new issues, I haven't seen any… anything else.
So, out of curiosity, how is it going with Copilot? I saw that you…
**Lalit Kumar Bhasin** 29:25 Not, not very.
**malff** 29:25 you would.
**Lalit Kumar Bhasin** 29:26 Not very smooth, I'll say that it's still notable to, For the PRs, it's still not able to run the CI test and ensure that they are successful.
I mean, you have to tell it again and again.
**malff** 29:42 So…
**Lalit Kumar Bhasin** 29:44 I mean, it's… I've seen it's much better than Rust as… as compared to C++.
Not very smooth right now in CTR.
**malff** 29:54 Yes.
From what I've seen, so there is a… well, there's an issue with EZCLA, first of all.
But, who went bumped into…
**Lalit Kumar Bhasin** 30:04 Yo.
**malff** 30:05 Basically, the… if Copilot generates a PR, it's fine, and EZCA check passes.
However, if Copilot suggests the changes, and if you take it.
then Copilot is not, is filed as co-author for the suggested change.
And then, EGCRE fails on that.
And then the PI is fried because you cannot go back, so you have to… take the… take the patch, find a different PR, and start over again, which is annoying.
**Lalit Kumar Bhasin** 30:39 So that was… I haven't seen this issue in Rust.
So, kind of, I was surprised to see that this behavior in C++ I don't know, probably.
if he has taken the changes from… I mean, like, normally in Rust also, if we take some changes from Copilot, we never face the issue in… Merging it, but yeah, it's… Kind of strange.
**malff** 31:17 I think it was with SPR.
So, yeah, when Copilot does a suggestion like that.
Oh, and took it, took it, and it broke, is this area.
So we had to revert it back to be able to pass.
Yeah, this one.
**Lalit Kumar Bhasin** 31:36 Hmm.
**malff** 31:41 So, apart from that.
I've not tried to use Copilot, but from what I can see on all the comments written in my PR, It sounds like, you have to… basically to do some spoon-feeding to Copilot, to tell him, do this, do that, no, you've… you missed that, fix this, and it's, Seems like a long process.
**Lalit Kumar Bhasin** 32:07 Yeah, and even… it's not taking that, that markdown file which it creates as instructions, it's not using it Properly also, which is kind of… Another issue I found.
**malff** 32:20 Okay.
**Lalit Kumar Bhasin** 32:29 Yeah, let's see if, I mean, if we don't see much of the success with it, probably we… can decide.
How… how and for what, what you think we should be using it, or whether we should use it or not.
**malff** 32:44 No.
**Lalit Kumar Bhasin** 32:45 Or it may happen that it gets better over the course of time.
**malff** 32:51 It probably can be useful to… To generate a big draft of something.
But then, if you have to tell it to fix it, to fix something, or if you… You spend less time fixing it yourself.
Then we probably can use it only to draft something and then take it from there.
**Lalit Kumar Bhasin** 33:11 Didn't take it out.
**Tom Tan** 33:13 I'm just wondering, I'm also using it locally, or clouded, do you know if it works very different, like, if I run… Num… Copilot vest code extension in age and model locally.
Or maybe I expect those will be similar, or very different?
**Lalit Kumar Bhasin** 33:37 It works, I mean, in the… if we are using it in Visual Studio VS Code, right?
It works better, because there we… we can give you… give it an instruction to, like, as part of the code changes, we can give it an instruction to always run the tests With those, and it works fine, it does run the test when it will fix them.
But it's not doing these things in the… as part of the GitHub.
**Tom Tan** 34:04 Let's a more interaction with the local extensions.
**Lalit Kumar Bhasin** 34:07 It's more interactive.
**Tom Tan** 34:10 Don'.
**Lalit Kumar Bhasin** 34:10 The same agent probably used across both, but probably the… One in VS Code is… looks like much better.
**Tom Tan** 34:18 Yeah, so maybe for, like.
kind of more big or complex feature, we do that locally with competitors and for some, like, middle-level or trivial thing, maybe just do it on the web, maybe suggest it for now.
**Lalit Kumar Bhasin** 34:33 Yeah, that's one we can think, I mean.
**Tom Tan** 34:36 like, implement a big feature, like, just the, like, with, Copilot on the website, maybe, need a lot of, like, interaction, right?
The back and forth.
**Lalit Kumar Bhasin** 34:51 Yeah, we can do that. I mean… My only thought was that if maybe it gets smoother and better over the course of time if we are giving instructions at GitHub level.
So continue using it for some time and see if it gets better.
**Tom Tan** 35:07 Okay, yeah, that's true.
Okay.
**malff** 35:21 Tom, just so you know, I saw your PR, so… My understanding is that, yes, you took the code from this old thing to get it up to date again.
I have a couple of questions, I don't know if you saw them.
Yeah, I'm Canada.
Okay, and one area where maybe we can simplify a lot of things is to always take an aggregation config.
So that we don't have to test, all over the place if we have one or not.
Because what, what could was.
**Tom Tan** 35:57 Yeah, cool.
**malff** 35:57 And pasted in a lot of places, so…
**Tom Tan** 36:00 Yeah, I'm looking to this, and then we'll address the feedback.
**malff** 36:04 Okay.
And yeah, it looks like Doug took a look as well.
**Tom Tan** 36:10 Yeah.
**Lalit Kumar Bhasin** 36:15 Hey, Tom, I'll be reviewing it as well today.
Sorry.
**Tom Tan** 36:19 Okay, thanks.
**malff** 36:36 A lot of things there are very old, so no… Noisome changes.
So this one from, from Nikhil, so this is the follow-up on, well, cleaning up… Argument from the command line.
Sorry, no, this is something different.
This is… so also for… for processors, there's, let's see… Maybe you find, willing to respect.
Yes, sorry, different context. So, when I did all the… all the YAML spec parsing.
One thing I noticed from the YAML schema is that there's a feature in the spec that we don't support directly.
Which is some fancy… Way to filter attributes by providing both an include and an exclude list with Logic which is described in this place. And the part which is missing is, you know, defining… An attribute processor with a proper behavior.
I've not looked at the PR yet, but this is some part what was missing.
Boom.
Yes, this one.
So… Long story short, the… The spec defined a very specific way to filter metrics.
And we need to subclass satellite processor to just implement that behavior, which is to have both an include and exclude list.
So it's good that Nikki is, Looking at that and picking it up.
And the other thing, which is, filtering of attributes in the… no, what was it? Yes.
in the… in the process command line, there's an issue for it, and I'm assuming it will… it will also look at that.
And this is pretty much it for recent changes.
any… PR, any other things you would like to discuss in general?
**Lalit Kumar Bhasin** 39:14 Not from my site.
**malff** 39:28 Okay, so… Yeah, I will… I will update that, so that we… especially for the next release, that we have an issue.
At least where we can track things, We'll start to put some comments in, Endings to issues that we need.
**Lalit Kumar Bhasin** 39:47 Okay, thanks.
**Tom Tan** 39:49 Thank you.
**malff** 39:54 Follow it. Well, thanks everyone, Vince, Getting a bit light here, as you can see.
**Lalit Kumar Bhasin** 40:03 Excellent.
**Tom Tan** 40:03 Okay.
Thank you.
**malff** 40:05 Thanks, everyone.
Right.
