SIG: Resources and Entities SIG
Date: 2026-11-23
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Nathan Smith (Elasticsearch, Inc.)** 03:19 So it looks like… Josh said in Slack that he's out sick today.
Yeah, so I don't know if anyone else is joining.
I just joined to listen in, so… Did… did you have… where… is this your item on the agenda about the, disabled Entities?
**Jan Korona (Splunk)** 04:30 Yeah, that's, my item, I added it, just wanted to… Discuss it with, with you guys.
So, basically, it's a… related to OpenTelemetry Collector, we have the tool Call them data gender.
And this tool allows to… Create some interfaces, both for the configuration and for the… Go.
To create the entities?
And currently, I'm working on some changes to that interface, and there are two issues that I spotted.
One is related to… Disabling entities, because every… NTT depends on a number of resource attributes, and currently those resource attributes can be Enabled, disabled, individually.
But, the question is, what if, there's identity attribute disabled.
But, it's Entities enabled, how we should handle that.
So I was thinking about, For example, doing the validation on the config load, so if there is such Use case spotted, we can just throw an error.
That obviously would be a breaking change for the… For any existing, definitions.
But, probably the most accurate, I would say, just for me.
We can also, like, Take precedence of the entity settings over the resource attribute.
Settings.
And eventually logs a warning to the user, so it's not like… Dropped silently.
And yeah, these are the two ideas that I have for this one.
I'm interested if you have any, any thoughts about it.
**Nathan Smith (Elasticsearch, Inc.)** 06:53 Yeah, I don't… I don't know if there's any,
**Jan Korona (Splunk)** 06:58 Right, I can, I can maybe…
**Nathan Smith (Elasticsearch, Inc.)** 07:00 If there's any, like, testing.
**Jan Korona (Splunk)** 07:03 I can maybe share the screen to show you how that looks like.
Because if you didn't play with it.
Previously, it might be not so clear.
Yeah, so basically, this is how it works.
So in the… every… every component in the collector has own metadata YAML file that, Provides some information about the… Telemetry that this particular component produces.
And that includes also resource attributes and entities.
So, yeah, as you see, there are some resource attributes.
And there are entities, those entities have references to Results attributes.
And I can enable, disable, particular entities, but I can also enable, disable.
the resource attributes. So the issue is when there is this identity Attribute, which is mandatory, because it's, like, a uniquely identifies given entity.
But I… but the user disabled this identifying attribute.
So the question is what we should do in that case.
**Nathan Smith (Elasticsearch, Inc.)** 08:33 Yeah, your… your suggestions… seem reasonable. I don't know if there's alternatives. I mean, I suppose, but…
**Jan Korona (Splunk)** 08:43 Yeah, bye.
**Nathan Smith (Elasticsearch, Inc.)** 08:43 I was thinking that.
**Jan Korona (Splunk)** 08:44 I mean, eventually we can, like, even… This, like, remove possibility to enable, disable, Attributes and control it only on the entity level.
But this is, like, a next step, I would say.
Okay, maybe I should rise this question once again, next SIG. Maybe we'll have, like, more folks.
But there's one more question, related to the topic.
Which is about the relationships, because we can have… A relationship between entities defined.
So also the question is about… what if… what if… we… Disable the entity that another entity depends on.
Should we, like, disable both, or just remove the relationship, or, again, the… Throw the validation error.
So this is another concern that I have.
**Nathan Smith (Elasticsearch, Inc.)** 10:34 Yeah, I don't think we're gonna have a lively discussion about this one either, so I put on the meeting notes that we should discuss in the next meeting when more people.
**Jan Korona (Splunk)** 10:44 Yeah, I know that, I know that Josh has some more… Opinions about this stuff, so maybe… And he'll be able to join, we could, like… Give it more space.
**Nathan Smith (Elasticsearch, Inc.)** 11:00 Yeah, and if he catches up on the recording, we'll probably end the notes, so…
**Jan Korona (Splunk)** 11:04 Yeah, yeah, yeah.
clip.
**Nathan Smith (Elasticsearch, Inc.)** 11:07 So, and yeah, maybe the rest of us can think about it, because I…
**Jan Korona (Splunk)** 11:13 Sure.
Any other topics, guys?
**Nathan Smith (Elasticsearch, Inc.)** 11:39 No, thanks for, thanks for bringing those, hopefully you can get some… We'll have some more discussion next time.
Thank you.
**Jan Korona (Splunk)** 11:48 Yeah, looking forward to that. Maybe I will also rise it on, some, some GitHub issue.
So we can handle it offline as well.
Okay, I'm dropping by.
