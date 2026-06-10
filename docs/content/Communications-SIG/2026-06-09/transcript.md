SIG: Communications SIG
Date: 2026-06-09
Duration: 15 minutes
============================================================

## Zoom Recording Transcript

**Mike Blum** 01:09 Yep.
I work with, Jay DeLuca on the, the Hotel Explorer projects.
**Patrice C (CNCF)** 01:19 Got it.
**Mike Blum** 01:20 And I was coming by today to… sorry, Pete, is there too much background noise?
**Patrice C (CNCF)** 01:26 No, it's fine, actually. I think your buds are filtering part of it.
**Mike Blum** 01:30 Excellent. Excellent. So… Jay's already… seen part of this, but it's in relation to this issue here, and this PR…
**Patrice C (CNCF)** 01:51 Hey, Andromed.
**leandrocaracciolo** 01:54 Whoa.
**Marylia Gutierrez** 01:57 Hello.
**Patrice C (CNCF)** 01:58 Hello, hello!
Thank you, hi, Jay.
And, hello, Mike. Nice to you.
**Mike Blum** 02:06 Thank you.
**Jay DeLuca** 02:09 Oh…
**Marylia Gutierrez** 02:13 So, Patrice, somebody just opened a PR for, like, a Portuguese translation, so I already messaged, like, Viter saying, like, do not do anything on this PR, let me just be the only one interacting, so I can test it out, the workflow. I was like, do not even look at this PR.
**Patrice C (CNCF)** 02:29 Yeah, I've been doing that as well. Some people say, don't touch this.
**Marylia Gutierrez** 02:34 See, hopefully I can… yeah, they just opened, so I'm gonna do a review by the end of the day and test it out, and I can share on the Slack channel, whatever happens.
**Patrice C (CNCF)** 02:45 Super. Awesome.
Yeah, I hope this approach works.
it all.
**Marylia Gutierrez** 02:53 Yeah, so…
**Patrice C (CNCF)** 02:53 Teams some autonomy.
**Marylia Gutierrez** 02:56 Yeah, because, like, if it fails, like, okay, we know that there is something to fix. If it works, I'm not sure if it is… because I'm an admin, or if it is actually work, so it's like, at least it's some signal, but yeah.
**Patrice C (CNCF)** 03:10 At least having somebody other than me try it out.
**Marylia Gutierrez** 03:14 Yeah, cheers.
**Patrice C (CNCF)** 03:14 It's good, so it's very much appreciated.
Hello, everybody! I don't know, somebody started… An entry in the notes… Yes, thank you. Whoever the anonymous mink is.
**Jay DeLuca** 03:40 It's me.
Don't tell anybody, though.
**Patrice C (CNCF)** 03:47 We didn't have any topics, Mike jumped in and shared some… Links… an issue and a PR.
I would say you were first, so… Go ahead.
Mike?
**Mike Blum** 04:04 Well, yeah, let me just pull up. Man, I didn't want to go through, like, kind of line by line what this is doing, or… because, Jay, I know we've already talked about this needs to be broken up into… smaller components. What I more wanted to talk about was the somewhat existential thing I've got going on where the watchers currently in the Ecosystem Explorer are all Python, and all require UV.
this… I wrote this in Go just because that's what the previous stuff was on, and I was able to take advantage of some… libraries of… to, like, kind of work a little more effectively with the Go ecosystem, things like GoMod and GoSum.
But the crux of it is none of the CI passes.
And one thought I wanted to run by you all is, like.
if we wanted to go the route where ecosystem explorer watchers are all, like, in their language of the ecosystem that they're watching, so, like.NET as in .NET, Go as in Go, Ruby's in Ruby, etc.
Do we have, like, do we want to make, like, make files for each of the different watchers, and it's just, like, a set of make commands that we call, that CI hits, like, every watcher implements, like, a make file, or something to that effect?
Because right now, it's all just assuming it's all UVPython across the board.
Where do we want to go.
**Jay DeLuca** 05:27 Awesome.
**Mike Blum** 05:27 route.
**Jay DeLuca** 05:29 Yeah, so I don't… I don't think that, we necessarily need them to be written in their respective languages. I think having them in Python Is, probably should be the default, just because we have some existing Stuff there, and in theory, the watcher should just be scraping something that has been pretty much already… all the logic and language-specific stuff can hopefully live upstream. I know we have a different situation here while we're kind of working things out.
**Mike Blum** 06:02 Right.
**Jay DeLuca** 06:03 So, I would say, just to more concretely answer your question, we should be able to get around this… this UV stuff, like… I didn't look too deeply into it, but we could probably, if it's… if it's just, like, I think it's saying, like, it's missing a pipe.
**Mike Blum** 06:18 Yeah, it's missing just, like, the Python-ness.
**Jay DeLuca** 06:20 Right.
**Mike Blum** 06:21 I'm not opposed to, like, having it read, like, we can have the LLM rewrite this in Python, if that's what this needs to be, that's fine.
**Jay DeLuca** 06:28 Well, I think the… so, your watcher is a little bit different because we're implementing some of the… like, in the Java agent, we do a lot of what you're doing in terms of, like, inferring the, the attributes and the telemetry. We're doing that all upstream in Java.
**Mike Blum** 06:46 Yeah, I haven't talked to the SIG yet about what they want to do yet.
**Jay DeLuca** 06:50 Right, and that's fine. So what I was getting at is, I think what you're doing is perfectly reasonable, like, we should work through how it would look and work in this repo, and then once we have a working prototype that, we know the end interface works with what we need, and we've kind of worked out the kinks, then I think we can move that upstream if they're amenable to that.
But so… so yeah, so we can keep this in the project as is. I imagine we can configure UV to not blow up when we add a Golang, or we move it if that… if needed, like, if we have to put this in the root.
That's perfectly fine, because this one is a little bit different from the other watchers, but… Yeah, so that's kind of my thought. Like, I think what you're doing makes sense. Let's break it up into smaller pieces, just so it's easier for us to work through and review. Right. And I can look into the UV stuff and see if we just need to configure something to tell it to ignore this particular directory, otherwise we can just move it to the root of the directory. And then you asked another question about using make. I think make probably makes sense for us at this point, because we have A lot of different sub-projects that use different technologies, so it might be a nice consolidation feature.
But, we should just start small. Like, let's… if we want to put a make file in the root of this directory that's just for this particular project, I think that… that sounds like a.
**Mike Blum** 08:20 Yeah, that's what I'm thinking. Yeah, then just wire… I can, like, modify the GitHub action to use the makefile, and then otherwise just go to the UV approach, But yeah, that sounds good. Okay, yeah.
**Jay DeLuca** 08:31 So, I don't.
**Mike Blum** 08:32 Yeah.
**Jay DeLuca** 08:33 Yeah, I was gonna say, so you don't need to rewrite this in Python, just keep doing whatever you're doing if it… it'll make it easier to upstream it.
**Mike Blum** 08:40 It's mainly because of the Go mod, so there's some pretty… not to bore you with the implementation details of Go, but similar to, like.
JavaScript has the same problem, where each of the repositories pinned to their own specific modules, and this spec here for how this Go mod is laid out is part of the standard library.
like, you could, in theory, write some Python code that does the same thing, but this was just a, like, the standard library plugs and chugs this as its normal part of its build chain already.
**Jay DeLuca** 09:12 Cool.
**Mike Blum** 09:12 Yeah, if you want.
**Jay DeLuca** 09:13 Yeah, if you want to write it in Python, that works too, but I wouldn't say it's a requirement.
**Mike Blum** 09:19 Okay, yeah, I'll go… I'll definitely go the other route. I kind of treat that as a nuclear option, slash somewhat facetious, because, you know, only in the LLM era would I ever say, like, let's just rewrite the whole project in a different language, just for fun.
Yeah, that sounds like a good plan.
**Jay DeLuca** 09:36 Cool.
**Patrice C (CNCF)** 09:44 And anybody else? Other topics they want to bring up?
I think everybody's been busy in their own way, both personally and on the project.
I've been trying to help alleviate Some of the main site maintainer burdened by, for example, working on this new feature, which, if it… Hmm… works will allow locale maintainers to request that approved PRs Be sent to the merge queue.
So that way, we, as main site maintainers, won't have to triage and deal with all that.
And the Japanese locale has been super, super busy. I don't know if you've noticed, but they're pushing at least, on average, I had to get some stats, 17 PRs per day in the last couple of weeks. That's per day.
But they are following our guidelines to a T, which is… we said small PR as well. They're doing one PR per page, which makes sense.
And but they're really pushing through with the translation. And this is where, in particular for them, I don't want us to have to be a bottleneck in terms of Us being the, docs maintainers.
a bottleneck for their PR merging.
So yeah, so that's what I've been busy with, and…
**Marylia Gutierrez** 11:29 Yeah, I think, like, Yoshi's gonna keep creating a lot more. He actually joined Grafana, like, last month or so. So he's, like, a dev route here, so this is why, like, he's focusing a lot on the Japanese. We have, like, some ideas on also how to bring more of the Japanese community, maybe helping out with the Ruby SIG.
And to that, we want to make sure that it's, like, welcoming. So, he's been focusing a lot on the translations and stuff, so this is why you see this huge.
Yeah, like a monofiar.
**Patrice C (CNCF)** 11:59 Like, yeah.
**Marylia Gutierrez** 12:00 Yeah, there's a… there's a reason.
**Patrice C (CNCF)** 12:02 guide it.
Thanks, thanks for the… the background.
**Vitor Vasconcellos dos Santos** 12:06 I'm curious to see the update numbers for them, by the way.
**Patrice C (CNCF)** 12:17 I think at some point we, we, as you know, we collect the stats for… or locales.
See how those come Jay, you wanted to talk about… Mentorship?
**Jay DeLuca** 12:36 Oh yeah, it's mentorship, not internship.
Yeah, just, just given us, just a inform, nothing needed here, but we have, we submitted an LFX mentorship.
around, the information architecture, and usability of the information in the Ecosystem Explorer. So we… we kicked it off this morning, actually. We have, someone from Nigeria who's… who's gonna be working on it, her name's Karamat, and she's gonna be doing some user research, so if any of you know of people who might be good Who might be interested in being interviewed around, kind of, how they approach finding different, information around different components of OpenTelemetry. We'd love to kind of point her at them, but yeah, just giving an informed that we just kicked that off, and over the next 3 months, she's going to be, just trying to help us improve the, the architecture and user experience of the Explorer project.
**Patrice C (CNCF)** 13:39 Great.
Glad that you were able to find a candidate, and The thought that comes to mind, maybe reach out to the, SIG end user group.
**Jay DeLuca** 13:55 Yeah, we have, one of the maintainers of that SIG is another mentor in our group, so yeah, so we're already clued in with them.
**Patrice C (CNCF)** 14:02 Got it. You're all hooked up there.
Anything on the, admin maintainer side that… I… Should know about, from the main website.
If not, any other topics?
Might be a very short meeting, which is okay.
Going once.
Going twice.
Thank you, everybody, for joining, and… Might be one of the shortest meetings on record. Have a great day. Thank you.
**Jay DeLuca** 14:57 See you, Mike. Bye.
**Mike Blum** 15:00 DJ.
