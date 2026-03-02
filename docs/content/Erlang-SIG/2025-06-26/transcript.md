SIG: Erlang SIG
Date: 2025-06-26
Duration: 15 minutes
Zoom Recording URL: https://zoom.us/rec/share/97hfZaNiN-Zv7aEfpfLm6h6gh98OtQP39Klygbr9pB-dIIWhrXnMSVowH6EKUzx_.3JMq5sV2explCDcv
============================================================

## Zoom Recording Transcript

**Greg Mefford** 04:15 Hey! There!
**Tristan Sloughter** 04:20 They!
**Greg Mefford** 04:24 I joined the other meeting, and there was nobody there. So found you.
There's a there's a different link in the observability group document.
**Tristan Sloughter** 04:36 Oh, great!
To get that fixed.
**Greg Mefford** 04:45 I mean, I guess it's fine, because this is
I guess this is the Hotel Erlang Sig. One.
**Tristan Sloughter** 04:51 Oh, you mean you went to the observability.
**Greg Mefford** 04:54 Yeah, I just joined the other meeting.
**Tristan Sloughter** 04:55 Oh, got you? I thought you meant like in the observability cause. I think we mentioned this group in there somewhere. So I thought maybe we had a link there. Never mind.
you're gonna do something with the top half of that wall.
**Greg Mefford** 05:09 I know I have a plan. It's just been years in the making, because, I just have so many other projects.
**Tristan Sloughter** 05:15 Yep, it looks like you got a lot of projects back there. But yeah.
**Greg Mefford** 05:21 Yeah, our house is currently under construction or consistently under construction.
**Tristan Sloughter** 05:27 It is.
**Greg Mefford** 05:27 Permanently.
**Tristan Sloughter** 05:32 So yeah, yeah. 8. After not sure anybody else is gonna join hoping Brian would, because I have a
trying to clean up Admins and Maintainers groups on Github. So I wanted to check with him on something.
**Greg Mefford** 05:48 Yeah, that's probably a good topic for discussion, because I think last time he mentioned that he just can't do this time slot anymore, because or something.
**Tristan Sloughter** 05:56 Yeah, I think you did.
**Greg Mefford** 05:58 Figure out like what time like. I don't mind changing the time, either, but we need to figure out what time works for him.
**Tristan Sloughter** 06:03 Yep, yep, yeah, I'll ping him a
I can't remember if he said, this whole day is messed up, or let's just move to a different time in this day.
**Greg Mefford** 06:16 I don't remember. I'd have to go look back to, but.
**Tristan Sloughter** 06:18 Oh, yeah, follow up.
Actually, I'll ping him right now.
Find out later.
Eastern time zone there so, and moving it whenever is fine with me.
Let's see, yeah. And I'm main thing I'm working on is, aside from, I gotta start pinging people again about metrics is configuration, which
will be nice once it works. But right now it's a bit of a pain to try to
backwards compatibility layer for our existing configuration and the new configuration, because I can't.
**Greg Mefford** 07:17 Paint all on our side as maintainers, though right like we don't
like users don't have to care. They could just keep using whichever one right.
**Tristan Sloughter** 07:24 Yeah, except I think so. Yeah, it depends on couple of things. One. So yeah, they won't have to change, because it would be backwards compatible like. I won't break what works now.
But there's a few oddities, I think, in our existing configuration that make me wonder if
we shouldn't only support the Json model or the exist well, Yaml model, or the existing configuration, but also in
Erlang elixir config, support, one that looks like the Jason. One cause, then.
**Greg Mefford** 07:57 Could move to that if they want to, just because the current one's kind of weird in some ways.
**Tristan Sloughter** 08:01 Yeah, and it would match without having to use Yaml or Json. It would match what they see elsewhere. So they'd be like.
oh, in these examples. For this go application. It uses a configuration file and defines trace, tracer, provider batch processor.
This size buffer.
Oh, I can translate that exactly as is into elixir terms, and it works.
So I kind of want to do that
unless it becomes too daunting. So yeah, I decided to start with
changing the internal configuration structure to match that one, because I like it better.
**Greg Mefford** 08:45 Like it.
**Tristan Sloughter** 08:46 It's segments right now. We don't segment like tracer provider on its own thing
and then meter provider and then logger provider. We just have all their configurations in the top level
like it just has that span processor
or processors at the top level. And
that's assumed to be tracers processors. But now there'll be
under tracer providers. So you'll know these are tracer processors. This is the batch under there, and this is the limits for the tracers attribute value length.
So it's a little more structured.
**Greg Mefford** 09:31 Yeah, I think that makes more sense to me.
**Tristan Sloughter** 09:33 Okay.
**Greg Mefford** 09:33 And I think also, I think I understand more now what you're asking in the chat, and I think it it does make sense to like, probably
move to a new thing, but still support the old format by just like converting the old one into the new one internally like, if people continue using their existing configs, it'll still work.
But it's basically like you're introducing a new way to configure things that makes more sense potentially.
**Tristan Sloughter** 09:58 Right.
**Greg Mefford** 10:00 Yeah, I think that makes sense to me like you wouldn't actually use a Json file. It would just match the structure of the Json. Spec. I mean, you could.
**Tristan Sloughter** 10:08 You could. But yeah.
**Greg Mefford** 10:09 The difference.
**Tristan Sloughter** 10:10 I think the initial thing the second thing. So I'd change the internal, then I'd support it as
Erling or elixir config terms, and then I'd support the Json last
cause I think it's still nice to be able to say
what works in every other language works for us. So.
**Greg Mefford** 10:31 Because there's gonna be. There's always gonna be some people that are like they want to configure their hotel configurations via helm chart or something like that.
They don't want to put it in a config dot excess file in their elixir project.
**Tristan Sloughter** 10:43 They have an sre team in the company. They want their hotel configured by them, and
they can do that.
**Greg Mefford** 10:51 Makes sense. I mean, it's kind of weird to somebody who doesn't have that like. They don't understand why you would want that. But.
**Tristan Sloughter** 10:56 Why would I ever want this in Jason? You wouldn't, you wouldn't! But.
**Greg Mefford** 11:02 And also, I think if you make the internal configuration match the Json, then it's easier to just parse the Json into the config. Probably.
**Tristan Sloughter** 11:10 It'll be basically be just of
yeah. Cause there's a few things that are more verbose in it that I don't think we need. Like
attributes are
name value maps like with the key name and the value value, and then are then point to the
actual keys and values. But we don't need to do that in.
That's something you might need to do in Json for some reason, but
maybe it's so they can have.
**Greg Mefford** 11:42 I think it's literally so that you can specify with what's the thing.
Json? Schema? I think Jason Schema itself doesn't support dynamic key names.
**Tristan Sloughter** 11:53 Oh, that's true. That is probably why.
**Greg Mefford** 11:55 Can't specify it, even though you can do it.
**Tristan Sloughter** 11:59 Yeah, that's probably, why, yeah.
**Greg Mefford** 12:01 Technically, Jason Schema does do it, but only in the most recent version which most tooling doesn't support.
**Tristan Sloughter** 12:07 Oh, really.
**Greg Mefford** 12:08 Going through this, this like struggle with that at a previous job.
**Tristan Sloughter** 12:11 Oh, really, yeah. I remember, we yeah. We struggled with which Jason Schema to support cause. I was part of this Sig in the beginning for configuration file, and we're trying to.
**Greg Mefford** 12:21 Yeah, figure out.
it's been really frustrating. Where, like Jason Schema, 3.1 does support these dynamic keys that people want to use. But, like none of the tooling for creating and validating, it supports that version. Yet.
**Tristan Sloughter** 12:34 On, the the.
**Greg Mefford** 12:35 That was like 3 years ago, or 5 years ago, or something.
**Tristan Sloughter** 12:38 Some of the the versioning is also really bad, cause it like went by years at 1 point, but not always.
**Greg Mefford** 12:48 Sweet.
**Tristan Sloughter** 12:48 So it's like Jason, 2021. But there's also Jason, 3, Jason Schema, 3.
**Greg Mefford** 12:55 Oh, I might even be talking about open Api actually.
**Tristan Sloughter** 12:58 Oh, yeah, you probably are.
**Greg Mefford** 13:00 But still, it's probably the same problem. Yeah.
just something that they didn't think about, or whatever.
**Tristan Sloughter** 13:08 Yeah, they went. It was draft oh, 9.
And then it became (190) 920-1909.
**Greg Mefford** 13:20 Makes sense.
**Tristan Sloughter** 13:21 But there's like no tooling in Erling, or even elixir, it seems, that are up to date. So
we have to use this go program.
**Greg Mefford** 13:32 Yeah, we used Jason Schema somewhere that I worked before, but now I don't remember what we used, as far as I think we might have had an internal library to do it. It's I mean, it's not that complicated.
**Tristan Sloughter** 13:42 And it still might have been dated.
Yeah, I didn't want to deal with that, and I didn't want to introduce it as a dependency that
I would then have to maintain, and when there's features used in the.
**Greg Mefford** 13:56 Like a business.
**Tristan Sloughter** 13:56 Email, yeah.
**Greg Mefford** 13:58 It's probably easier, anyway, to just manually check it. And like like manually support whatever
config options we want to support, because ultimately, like, you're gonna have to actually build support for them, anyway. Right? Like.
**Tristan Sloughter** 14:11 That's true.
**Greg Mefford** 14:12 You can't really code. Gen, the actual implementation that uses the config.
**Tristan Sloughter** 14:17 Right.
**Greg Mefford** 14:18 So I think it's gonna end up being hard coded, anyway.
**Tristan Sloughter** 14:22 Yeah, probably.
Cool. Well.
**Greg Mefford** 14:29 I think on my end the up. Only update is I'm still cranking away whenever I have time on the profiling stuff. But I'll be on vacation for a couple of weeks, and I don't know whether I'll be able to work on it or not. During that.
**Tristan Sloughter** 14:41 All right.
**Greg Mefford** 14:42 Probably another longer pause. But
I'm planning to bring my laptop, but I don't know if I'll have access to actually like I have a Linux machine that I ssh into to work on it, so I don't know if I'll be.
**Tristan Sloughter** 14:54 Pale scale.
**Greg Mefford** 14:55 Yeah, I might set up tail scale before I go.
**Tristan Sloughter** 14:59 Stuff's magic.
**Greg Mefford** 15:00 Yep.
**Tristan Sloughter** 15:03 Cool.
**Greg Mefford** 15:06 Maybe I'll finally get around to trying it on my apple silicon
code, mostly written. I should be able to just run it in a Vm.
On Linux.
**Tristan Sloughter** 15:16 Yeah.
**Greg Mefford** 15:17 I need to probably make sure it works on arm, anyway.
**Tristan Sloughter** 15:20 That's true.
**Greg Mefford** 15:21 So.
**Tristan Sloughter** 15:23 It's true.
**Greg Mefford** 15:25 It was just harder to develop it on that, because, like using a Vm is a lot slower to manipulate files and update stuff.
**Tristan Sloughter** 15:32 Oh, yeah.
**Greg Mefford** 15:36 Cool.
but now then.
**Tristan Sloughter** 15:42 I've got little ones. You're yo running at me right now.
**Greg Mefford** 15:48 Cool, all right.
See you later.
