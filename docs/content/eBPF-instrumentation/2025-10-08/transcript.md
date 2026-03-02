SIG: eBPF instrumentation
Date: 2025-10-08
Duration: 13 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 01:05 8.
**Mike Dame** 01:07 Hello?
**Tyler Yahn** 01:08 How's it going?
**Mike Dame** 01:10 Good, how about you?
**Florian Lehner** 01:11 Hello.
**Tyler Yahn** 01:12 Wait, Lauren.
Good. Hey, Giuseppe.
**giuseppe.ognibene@coralogix.com** 01:31 Can you hear me?
**Tyler Yahn** 01:34 Yeah.
**giuseppe.ognibene@coralogix.com** 01:34 Okay, thank you.
I enjoyed my comment.
**Tyler Yahn** 01:39 Yeah, no worries.
I'm not sure if we're gonna get a full attendance today. I think, some people might be at, like, conferences or something like that. I think Nicholas said something like that, so…
We can wait a little bit, and see.
If you haven't yet, go ahead and add your name to the attendees list, and if you have agenda items you want to talk about, please go ahead and add those there as well, and then we can jump in here in just a little bit.
Cool. Alright, yeah, let's, let's just jump in here. So, yeah, welcome, everyone.
I think to start us off, I just wanted to go through and take a look at the open PRs, see what's, in progress, and if anything's being blocked, and
Wow, okay, alright, this is even better than what I looked at last night. Alright, so yeah, there's really nothing…
open right now. There's just this one, that Mario's been working on. I don't think we need to jump in here. It's still probably a work in progress, right, Mario? Yeah.
**MM Mario Macias** 03:16 Yeah.
**Tyler Yahn** 03:18 Well, cool. Yeah, I think with that, then, that was a quick action item. The only other thing I had was this idea of the 1.0. I know we are waiting on this,
issue here, so I just wanted to maybe check in on this. And Omar, you had been looking at this one as well.
**MM Mario Macias** 03:36 Yeah, but no… no progress since the… since the last week.
**Tyler Yahn** 03:41 Okay, cool.
Alright, yeah, then I think, we'll still wait on that. Otherwise, yeah, that's, I think, the remaining. I don't think there's been any open issues either, in the past…
I guess we got one yesterday, so… cleanup per service and routing config.
Oh, I think this has to do with the collector definitions. This is very similar, I think, to what we did for, other portions. So, yeah, I think this may be worth something we need to take a look at. I don't think it needs to be done in this milestone, for sure, though.
Yeah.
**MM Mario Macias** 04:18 Yeah.
**Tyler Yahn** 04:20 Okay, well…
Cool, that was way shorter than I thought it was gonna be for the action items I had.
Okay, well, I guess I can pause here.
Are there any other things that people are actually, working on that aren't PRs yet?
**MM Mario Macias** 04:41 We are… we are working in a… in a back fix.
It's… it's a bit complex. A user reported that sometimes
We are providing traces, with our wrong
with a… with a wrong, ports, and even wrong, trace type. For example, it's an ATTP call, and it is reported as… as Redis.
It seems to be a… I know Nikola is working on it. It's… it's a bit complex, because it's in… in some… in some servers that reduce the same thread for multiple connections.
It seems sometimes we… we are merging information and providing… Providing incorrect data.
**Tyler Yahn** 05:36 Probably, Nikola, when it…
**MM Mario Macias** 05:39 Provides a pull request.
We'll… we'll provide more… more information about the cause, but this is where our… we're working on.
**Tyler Yahn** 05:49 Okay, yeah. Is this something that you see only at really high loads or something like that? Or is it just really random?
**MM Mario Macias** 05:55 I think this… this is very, with a very concrete…
With a very concrete, solution, from a customer, yeah. It's not…
**Tyler Yahn** 06:07 Okay.
**MM Mario Macias** 06:08 It's not frequent.
**Tyler Yahn** 06:10 Yeah, I gotcha.
Well, cool, alright, well, we'll keep an eye on, PRZ then. That sounds good. Thanks for the update on that one.
Also, I guess, Steven, thanks for all the work you've been doing on the CI stuff, too. I think that that's been really beneficial, so, yeah, the past week, I've seen a lot of great stuff, so appreciate that.
**MM Mario Macias** 06:28 Yeah.
**Stephen Lang** 06:29 You're welcome, yeah, I did the oats as well, which is probably the last one that I'll do as a priority, because I think everything now should be done within
Sort of 18, 19 minutes.
But yeah, the biggest one was,
A kernel 515 that used to take an hour and a half.
Yeah. Now less than 20 minutes.
So everything is less than 20 minutes now.
So I think, yeah.
It should be a lot better, DevEx.
**Tyler Yahn** 06:57 Yeah, yeah.
Absolutely, yeah, definitely. Again, thanks, yep.
**Stephen Lang** 07:01 Welcome.
**Tyler Yahn** 07:04 Okay, cool. Any other cool, maybe, side projects besides Mario? Or bugs, or, interesting demos that maybe people are doing?
**Nimrod Avni** 07:15 Pino, you wanna mention the… what we talked about, the, like, documenting the configuration? Maybe some people there.
Maybe…
**giuseppe.ognibene@coralogix.com** 07:26 Yeah, so…
I don't know if anyone knows, but I joined, like, one week ago, so I'm new, and I started to, like, build Obi, start to create stuff, and I noticed that there is no getting started documentation, because my getting started was, like, the README of Villa.
So, I am creating a new… getting started with how you can build the binary, how you can test it with Dogger, Kubernetes, and so on.
I'm working on that. So, then, obviously, we'll create our pull request, and then everybody can, just…
Give me some advice.
**Tyler Yahn** 08:09 Yeah, that sounds great.
**Nimrod Avni** 08:11 No, but we… I think you told me something that's really cool about the…
I think… I think Nicola mentioned it a while back, that some of the configs are not, like, not all the config is, like, documented, because we keep, basically, we add documentation, like, config flags for everything.
like, either, like, on the YAML or, like, environment variables, and that's… I mean, that's good and important, but if you don't know the code, it's kind of hard to know that. So, we thought maybe… maybe if you know anything,
If there are maybe some, like, static, like, code analysis, code generation tools that can maybe
I don't know, they can take the top-level, like, config struct of Obi, kinda scan it, and for each, thing that is in, like, a config option that has any, like, an env or a YAML
annotation, I don't know what's the name of it in Go, I forgot. Maybe it can… I don't know, maybe it can take, like, the…
Most of them have, like, one row, like, comment above that explains about it a bit. Maybe we can take all this somehow with CI, create, like, a Markdown file, even attach it to the OB docs.
It can be an idea, I don't know. I don't really… I never did something like that.
But maybe it can be, interesting.
Just to have every config option, like, properly documented.
**giuseppe.ognibene@coralogix.com** 09:50 Another thing that I was working on is,
Not every, environment variable are recommended.
And I would try to create, like, a separate documentation, but as Nimrod said, maybe there is some tool that, like, from the comments of a fields of a struct, can generate some Markdown file. I check it, and there is, like, Godoc, but I think it's really, like.
small, and there is another one called GoMarkDoc, maybe this could be, like, the… the good one, but I need to check.
**Stephen Lang** 10:27 You can also use the Go AST directly, as well, on the standard library, if you wanted to make
Absolutely.
**giuseppe.ognibene@coralogix.com** 10:35 about Kodak.
**Stephen Lang** 10:37 Sorry?
**giuseppe.ognibene@coralogix.com** 10:38 you're talking about GoDoc, I mean, the doc command of the Go CLI?
**Stephen Lang** 10:43 No, no, I mean… I mean, like, create a new, GO program in the OBU.
**giuseppe.ognibene@coralogix.com** 10:48 Okay, yeah, yeah, yeah. Users. I can handle it.
Yeah.
**Stephen Lang** 10:51 can use the AST there, to do, like, introspection on the source code.
And you could maybe target it to pick up specifically on…
The annotations, or, you know, the variables.
I don't know how well it works with dot blocks and things, but I mean, it must do, because
That's how GoDoc is built, right? With the same tool. So…
**giuseppe.ognibene@coralogix.com** 11:16 Okay.
**Stephen Lang** 11:16 If you can't find something that already exists, you could do that, and then maybe you could tie it into the Go Generate step.
Or add it as, like, a… I don't know.
**giuseppe.ognibene@coralogix.com** 11:30 Okay.
**Stephen Lang** 11:31 Because the other option would be to add it as some kind of, like, Git commit hook.
But we already use the…
the Go Generate stuff quite significantly, so…
That could just be, like, another tool that gets,
executed. I wondered about doing something similar when I was doing the sharding for the integration tests.
To look for, you know, all the tests that have the integration.
build tag.
Or, you know, to try and split up the tests in… in some way, but I ended up just using
Shell scripting It's great.
is, incredibly fast.
That's the only downside of using GoAST, is it's… you've got some overheads with…
Compiling the binary and then running the scan.
But that's just another option.
**Tyler Yahn** 12:23 Yeah, I think another one is… you could try to look at Weaver, but I think that would be a very different approach, where you would have to define the configuration in a different format, which would be JSON, and then it would render both the Go and the docs, using Weaver, but…
Yeah, I think Steven's option as well is a good one, if there's not already something pre-built that would do this.
**giuseppe.ognibene@coralogix.com** 12:47 Okay, thank you.
**Tyler Yahn** 12:49 Yeah.
Well, cool.
Any other topics? Otherwise you'll probably end the meeting early, don't wanna…
Have a meeting just for the meeting's sake, obviously.
Well, awesome. It's good to see you all. A lot of great work is, done, so yeah, I'm happy to see us making a lot of progress. Almost there. So yeah.
Cool, we can edit here. I will see you all in a week's time, or, asyncously.
Bye, everyone.
**giuseppe.ognibene@coralogix.com** 13:20 Thank you.
**MM Mario Macias** 13:20 Bye-bye!
**giuseppe.ognibene@coralogix.com** 13:21 Bye-bye.
