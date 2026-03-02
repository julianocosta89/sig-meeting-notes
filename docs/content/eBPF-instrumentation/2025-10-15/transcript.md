SIG: eBPF instrumentation
Date: 2025-10-15
Duration: 27 minutes
============================================================

## Zoom Recording Transcript

**Giuseppe Ognibene | Coralogix** 01:09 Good one.
**Tyler Yahn** 01:10 Hey.
**Mattia Meleleo** 01:12 Oh…
**Tyler Yahn** 01:12 going.
How y'all doing?
**Mattia Meleleo** 01:17 Pretty good. What about you?
**Tyler Yahn** 01:21 Yeah, pretty good as well.
Making it through the week? Yeah.
Giuseppe, I didn't catch, are you based in Italy as well?
**Giuseppe Ognibene | Coralogix** 01:32 Yes.
**Tyler Yahn** 01:32 Oh, okay. Are you near Matea, or is it pretty far?
**Giuseppe Ognibene | Coralogix** 01:37 let's say Britain area, I mean, Sicily.
**Tyler Yahn** 01:41 Oh.
**Giuseppe Ognibene | Coralogix** 01:41 I can pull your.
**Tyler Yahn** 01:42 Yeah.
Cool.
**Giuseppe Ognibene | Coralogix** 01:45 Where are you based?
**Tyler Yahn** 01:46 Portland, Oregon.
So, in the US, yeah.
So, a little cooler than where you guys are at.
**Giuseppe Ognibene | Coralogix** 01:53 Yeah, definitely.
**Tyler Yahn** 01:55 Yeah.
Yeah, a nice, nice warm Italian beach sounds pretty great right now.
**Giuseppe Ognibene | Coralogix** 02:05 Unless… We should, we should do something, altogether in Italy.
Yeah.
**Tyler Yahn** 02:13 I'll tell EVPF, like, off-site, I'm all down.
We, I wonder, like, has there been a KubeCon in Italy?
**Giuseppe Ognibene | Coralogix** 02:24 Not in Italy, there is the Europe one is in Amsterdam, I think.
**Tyler Yahn** 02:29 Yeah, yeah.
Yeah, it was London before that, and then,
I think Paris before that, so yeah, I think… I think they're overdue for Italy.
I think Sicily sounds great.
**Giuseppe Ognibene | Coralogix** 02:40 Never in Italy, yeah. But I think they will do… if they will do something, they will do something, like, in Milan.
**Tyler Yahn** 02:47 Yeah, yeah, yeah.
That would make sense.
**Mattia Meleleo** 02:52 the infrastructure in the South in general is terrible, so I don't think they will make such a big event in
That'll be perfect.
**Tyler Yahn** 02:59 Oh, okay. We'll be having the talks in tents or something like that, or…
Maybe not that bad, but… Yeah.
That makes sense.
Well, cool. Alright, so we're 3 minutes in. I don't think the Grafana folks are gonna make it today,
I think they're all at an off-site based on talking with some of them, so we could probably jump in here. I don't have too much on the agenda. If you haven't yet, please go ahead and add your name to the attendees list.
And if you have agenda items you wanted to talk about, go ahead and add them there as well. Otherwise, we can just jump in. I just wanted to do a quick recap,
On where we're at, but if you have specifics, we can talk about those as well.
Cool. Alright, so I did see that there's a few more open PRs, so I wanted to just kind of go through this really quick. Obviously we talked about this, this replaced the internal GoTools, tool mod directive, don't need to talk about that.
Still a work in progress, for Mario.
Nicola had opened up this one recently. I don't know the status of it, I took a quick look at it. It looks like it still hasn't had much eyes on it.
Yeah, looks like the CI is failing. It's only 300 lines. Okay, so, yeah, this one is open. It doesn't look like anyone's taken a look at it yet, or reviewed it yet. I've definitely…
expect people have taken a look at it, maybe. So, yeah, I think this is just looking for a review. This is opened 2 days ago, so yeah, still actively looking for a review on this one.
**Mattia Meleleo** 04:41 I didn't review this yet, because I saw that CI was failing, and there were some follow-up commits to try to fix it, so I'm not sure if it's reviewable.
Or we should wait, or…
**Tyler Yahn** 04:58 Yeah. For the CR to be fully green, I don't know.
That's a good question.
Yeah, okay, I'll post that question, that's a good question.
Yeah, I did notice that as well. This test…
Can be flaky, so it may just be…
Why don't we actually just kick this off again?
But, okay. Yeah, so maybe it needs to be a little bit worked, but I know that this is still open… this is an interesting…
One, it looks like, both Mattia and Nimrod have taken a look at this. It looks like it's trying to add some sort of, validation?
Yeah. Tooling around our configuration.
**Giuseppe Ognibene | Coralogix** 06:10 Yeah.
This is just, let's say, a standard way to validate things in a declarative way.
I just, thinking to split in multiple progress, because it's… Should be a big one.
And also, for some validations, I'm not so sure. We had an internal discussion, maybe we need to change something to…
Be more user-friendly.
**Tyler Yahn** 06:43 How is the… sorry, can you expand on the user-friendliness? How does this address that?
**Giuseppe Ognibene | Coralogix** 06:50 Sorry?
**Tyler Yahn** 06:51 You're saying that this makes it more user-friendly?
**Giuseppe Ognibene | Coralogix** 06:54 Yeah, no, I mean, there are, let's say, some… I implemented some validations that, from my point of view, they are, let's say, correct, but we had an internal discussion, maybe I can
Remove it, and just validate,
how can I say? In a way that people who are using OB right now with the default configuration, they don't have any problems.
But at the same time, we have a way, a declarative way, to validate all the fields. For example, as you can see, this validate Boolean, or this one, requiredIF, the enable field is true, we just check if it is greater than equal to 0.
**Tyler Yahn** 07:45 Okay.
So…
How does this get used, though? So it looks like it's setting a bunch of tags, I guess is kind of my question, but is there already tooling with this?
**Giuseppe Ognibene | Coralogix** 07:58 Yeah, if you go down… In the config, yeah, a bit down.
Download here, in the validate.
In the validate function, I adjust a number.
here in the validate function, I just,
Use the validator, actually, and then align 300, 300, 300, 350,
Just pass it the entire struct, the configuration.
And it will check all the tags that we put in all the fields. That's all. If you don't have any…
particular stuff, usually use the default tags, otherwise you just implement some custom validations. For example, I implemented this 4.
for, to validate the agent type interface and the rest of it, but I think it's a, let's say, declarative and standard way to do validation.
As you can see, I removed a lot of code, instead of, like, trying to catch everything, you just use a standard way.
But this is just a proposal, I mean.
**Tyler Yahn** 09:11 Okay, yeah, I gotcha.
And so, what about next steps on this one? Are you looking for more review? Are you looking to split it up still, or is this already the split-up version?
**Giuseppe Ognibene | Coralogix** 09:22 No, no, this is not the split-up version. I mean, yeah, this is the, let's say, the small one. I just, validate the eBBF tracer and the network config. Then, if,
the community wants to do that, I need to validate all the other structs, because, you know, the configuration is really, really long, so instead of doing all the work in one time, I just,
Decided to do a smaller version.
**Tyler Yahn** 09:50 Yeah, that makes sense.
Okay.
So what do you need, Giuseppe, to move this forward?
**Giuseppe Ognibene | Coralogix** 10:00 I… if, I mean, we had an internal discussion, I just need to…
remove some stuff, and then I request again the review. I think it's good for me. I don't know if Nimrod or Mattia, they have something else in mind.
**Nimrod Avni** 10:18 I think that the… I can just share a bit what we…
talked about is mainly, if you wanna go… I think one of my comments, if you wanna go a bit down, was about something that, yeah, Pino, commented out.
I can think… this one, yeah. Basically, we can say that, like, the default config…
let's say, in this situation here, you have, like, listen interface watch, and then you can also specify the listen poll period, but theoretically, like, it doesn't make sense because the listen poll period is not used if
listen interfaces, watch, it needs to be pull. So basically, you have, like, a dependency between two,
two fields.
But we do want still to have, like, the… the behavior of if a user changes, the listen interface to be what, to be pull, then we have a default
listen pull period. Basically, we can have, like, the default config can have fields that are, like, redundant, basically, that are not used, but if the user changes one field, they will be used. So I think we decide, like, we discussed…
If that should, like…
Like, the main discussion was if, for example, if we decide to make the poll period be dependent on the listener interface, we can break…
customer config, I think, which would decide it's probably not good. I guess it's, like, some niche cases, but I think it's not gonna be good. The opposite… the opposite is good. I mean, if we say, like.
I don't know, you have, like, some field that, if you enable it, then another config needs to be in, like, bigger than zero or something? That makes sense.
But the other way around of having a config that is, like, not used, I think it's still good, because the default config makes it kind of easy to, like, oh, I can turn this feature on, and some of its config is already, like, pre-configured, even though that, by default, it's not being used.
I think maybe it was kind of confusing, hoping I said it right.
I mean, we can, like, discuss if we think it's… what's the correct case here, but…
I think mainly we wanted to change that, and then we can…
Merge this, and then do, like, all the other config, do it with this, like, validation approach.
**Giuseppe Ognibene | Coralogix** 13:03 let's say that, from a user point of view, the validation that I introduce is really… maybe it could be a problem, because if there is a user deployment of Obi, where they are using the default configuration, so, for example, in this case, with the listing interfaces.
watch, and at the same time, at least simple period of 10.
Doesn't have any, meaning, actually, because if it's, listener interface is, watch, the poll period is not used.
But in my validation, I just say, no, you can do that.
And… but as Nimrod said, maybe we can just, like, relax this validation, and just don't use the list pull period in that case. And as in this case, there are, like, other 2-1, two gazes.
For the reverse, reverse DNS.
**Nimrod Avni** 13:59 Mmm.
**Tyler Yahn** 14:01 Yeah, I think… I think this is kind of highlighting that this is not really ideal configuration.
I kind of wonder if it is… Promoting, trying to change this.
So instead of, it having two different fields that are related, one of which is required when another isn't, set or is set a particular way, I think that it'd be better if… man, what is going on?
Yeah, I think it'd be better if we actually defined this in a way that, like, didn't have this redundancy.
So, we had maybe, like, a listener, or a listen…
Fields here that you could put in something that is watch, and it wouldn't have this, and you could put in something that is pole, and it would have a period as well.
**Nimrod Avni** 14:57 I mean, ideally, yes, like, you want to have it so that, you know, the…
Type system doesn't allow you to have this, like, illogical state.
But the issue is, like, you know, I think customers are rely… unless we can, like, save both the YAML configuration and the environment configuration to be the exact same.
then it's gonna be, then we can't, like, change the full structure of it. I mean, maybe we can, like, if we… I don't know, if we do some refactor. I think it will also… it will make it easier in the future to…
Like, if we have this type of validation, we can, like, kind of avoid this pattern of, like…
like, dependent fields that are, like, you know, maybe we can do it all in one struct, I don't know.
Yeah, I don't know how in Go, we… they have, like, some kind of un… I don't know, not, like, union types, more, like.
enum or, like, algebraic data types, like, that you can do, like, one of this, this, or that. I mean, you could do it with, like, interfaces, I guess, but…
**Tyler Yahn** 16:09 Yeah, you'd have to do it with an interface.
Just because the types underlying would be different, so you'd have to understand
like, I think an enum would work for things like this.
Which I would probably recommend, instead of having just strings here, but then when you wanted this type to be either some sort of string or a, you know, some sort of field that has a… or a struct that has a field.
You would need to have an interface here.
Which is not, impossible. It's… it's pretty…
Pretty straightforward, we've done this in other places.
I do think, though, that, like, it's worth addressing these at this point in time, because it's also one of those things where we aren't a stable
package yet. Obviously, we have users with this, and so backwards compatibility, I think, is something that we can look into, in trying to provide some forward-facing, migration path, but…
I do think that, like, Moving forward with a config like this is definitely something we want to address.
It's… it's not…
it's not a good idea, I think, to just keep adding to this when we could better structure this, yeah.
**Nimrod Avni** 17:21 Yeah, just, yeah, just to think…
I think, like, backwards compatibility gotta be something we consider, because…
I don't… I'm guessing, I don't know, I don't think we have a lot of,
a Grafana guy's here, but I guess Bayla is, like, used for a while now, and if they depend on these types of fields, then you gotta consider it.
But, I don't know, like, I agree with you, we want to have, like, a more neat structure of, like, config, but…
Maybe we can, like, consult with some of the Grafana guys, if we can… maybe we can change it in a way that, like, from the config side, it's, like, clear.
But, I mean, still, like, when you configure it with, like, environment variables, it's still gonna be different environment variables.
No, no.
**Tyler Yahn** 18:13 Yeah, I mean, there's always translations I think you can do. It depends on how this is integrated. We have changed the config in this process going forward. Like, moving to Obi, we've actually changed quite a few different configs, so I do think that the Grafana folks have already handled, these sort of configs.
Changes, so I don't think it's out of the question.
what that looks like, though, I think, like, is probably pretty important. I mean, we haven't had a release yet, but, like.
we also haven't had a stable release, but I think as this becomes more stable, like, those kinds of questions are needed an answer of how this, like, evolves, but… yeah, I do think that this is a good question to maybe tackle.
In, like, an issue or something.
Yeah, probably an issue is probably the best place for this.
**Nimrod Avni** 18:59 Yeah, I think, you know, maybe we can… I think we can, like, continue…
Maybe, like, merge this, and then open an issue on some…
Specific, like, configs that are not, like,
A fully type constraint, I don't know how to call it.
And we can tackle it.
**Tyler Yahn** 19:18 Yeah, I think it's just the structuring, right? Like, we want something structured where there's not, information is not spread across fields, is kind of the key here.
I do think we also probably want to look at things like this, where…
we have, like, magic strings that exist, where you just need to know them. That's also a pretty…
frustrating, approach for your users trying to use the configuration. So I think that, like,
We probably want to take a look at some of these things.
Okay. So maybe as an action item, I'll open up an issue to take a look at this, and we can move forward.
Cool.
Alright, so that is…
all of the open PRs, giuseppe, I think we're gonna wait for, like you're saying, some updates, and then, well, more reviews on this one.
I don't think it's blocked by what we discussed, so yeah.
**Giuseppe Ognibene | Coralogix** 20:18 Yep.
Thank you.
**Tyler Yahn** 20:21 Cool. So then the only other thing is the milestone. I was taking a look at this. This is still waiting on some of the Grafana folks, which, I was coordinating with them last time on it, like, I think that this is just something…
we need to wait for them to, I think, get back to it. So, yeah, no update there as well.
Okay, cool. I think with that, it's the end of my agenda. I can stop sharing here.
I'll ask, any other questions, or topics, or things you all are working on.
**Giuseppe Ognibene | Coralogix** 21:00 I don't have any wisdom, but I'm working on the Elasticsearch spun support.
**Tyler Yahn** 21:08 Oh, cool.
Yeah.
Yeah, that'd be a cool one to add.
**Nimrod Avni** 21:16 Yeah, many doing quite a lot of,
Doing a lot of stuff based on… after Mattia merged the GraphQL stuff.
So we're working mainly on… we're also doing some AWS stuff, like, S3, SQF, all that stuff.
A lot of stuff we can… It'll be cool.
**Tyler Yahn** 21:36 Yeah, no, sounds great, yeah.
Well, cool. I think if it's… that's it, we could probably end the meeting early here.
It was good seeing you all. Enjoyed seeing ya. I don't know,
Yeah, I'm guessing the Grafana folks are gonna be back, based on my understanding, so yeah, we'll plan on talking more with them next week.
Well, until then, I'll, see you asyncously, or in a week.
But…
**Giuseppe Ognibene | Coralogix** 22:03 How about you guys?
**Mattia Meleleo** 22:04 Goodbye.
**Giuseppe Ognibene | Coralogix** 22:06 Thank you.
